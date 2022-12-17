import random
import copy
import os
import time
import math
import csv

try:
    from tkinter import *
    from tkinter.ttk import *
except Exception as e:
    print("[ERROR]: {0}".format(e))
    from Tkinter import *

list_of_cities =[]
k_mut_prob = 0.4
k_n_generations = 100
k_population_size = 100
tournament_size = 7
elitism = True

class City(object):
    def __init__(self, name, x, y, distance_to=None):
        self.name = name
        self.x = self.graph_x = x
        self.y = self.graph_y = y
        list_of_cities.append(self)
        self.distance_to = {self.name:0.0}
        if distance_to:
            self.distance_to = distance_to

    def calculate_distances(self): 
        for city in list_of_cities:
            tmp_dist = self.point_dist(self.x, self.y, city.x, city.y)
            self.distance_to[city.name] = tmp_dist

    def point_dist(self, x1,y1,x2,y2):
        return ((x1-x2)**2 + (y1-y2)**2)**(0.5)

class Route(object):
    def __init__(self):
        self.route = sorted(list_of_cities, key=lambda *args: random.random())
        self.recalc_rt_len()

    def recalc_rt_len(self):
        self.length = 0.0
        for city in self.route:
            next_city = self.route[self.route.index(city)-len(self.route)+1]
            dist_to_next = city.distance_to[next_city.name]
            self.length += dist_to_next

    def pr_cits_in_rt(self, print_route=False):
        cities_str = ''
        for city in self.route:
            cities_str += city.name + ','
        cities_str = cities_str[:-1] 
        if print_route:
            print('    ' + cities_str)

    def pr_vrb_cits_in_rt(self):
        cities_str = '|'
        for city in self.route:
            cities_str += str(city.x) + ',' + str(city.y) + '|'
        print(cities_str)

    def is_valid_route(self):
        for city in list_of_cities:
            if self.count_mult(self.route,lambda c: c.name == city.name) > 1:
                return False
        return True

    def count_mult(self, seq, pred):
        return sum(1 for v in seq if pred(v))


class RoutePop(object):
    def __init__(self, size, initialise):
        self.rt_pop = []
        self.size = size
        if initialise:
            for x in range(0,size):
                new_rt = Route()
                self.rt_pop.append(new_rt)
            self.get_fittest()

    def get_fittest(self):
        sorted_list = sorted(self.rt_pop, key=lambda x: x.length, reverse=False)
        self.fittest = sorted_list[0]
        return self.fittest

class GA(object):
    def crossover_experimental(routeA,routeB):
        child_rt = Route()
        routeB_len = len(routeB.route)
        random_city = random.choice(list_of_cities)
        incrementing_a = True
        incrementing_b = True

        idx_a = routeA.route.index(random_city)
        idx_b = routeB.route.index(random_city)

        idx_a -= 1
        idx_b += 1

        if idx_a < 0:
            incrementing_a = False

        if idx_b >= routeB_len:
            incrementing_b = False

        child_rt.route = [random_city]

        while (incrementing_a and incrementing_b):

            if idx_a >= 0:
                if not (routeA.route[idx_a] in child_rt.route):
                    child_rt.route.insert(0, routeA.route[idx_a])

            idx_a -= 1

            if idx_a < 0:
                incrementing_a = False
                break

            if idx_b < routeB_len:
                if not (routeB.route[idx_b] in child_rt.route):
                    child_rt.route.append(routeB.route[idx_b])

            idx_b += 1

            if idx_b >= routeB_len:
                incrementing_b = False
                break

        shuffled_cities = sorted(routeA.route, key=lambda *args: random.random())
        for city in shuffled_cities:
            if not city in child_rt.route:
                child_rt.route.append(city)

        return child_rt

    def crossover(self, parent1, parent2):
        child_rt = Route()

        for x in range(0,len(child_rt.route)):
            child_rt.route[x] = None
        start_pos = random.randint(0,len(parent1.route))
        end_pos = random.randint(0,len(parent1.route))
        if start_pos < end_pos:
            for x in range(start_pos,end_pos):
                child_rt.route[x] = parent1.route[x] 
        elif start_pos > end_pos:
            for i in range(end_pos,start_pos):
                child_rt.route[i] = parent1.route[i]


        
        for i in range(len(parent2.route)):
            if not parent2.route[i] in child_rt.route:
                for x in range(len(child_rt.route)):
                    if child_rt.route[x] == None:
                        child_rt.route[x] = parent2.route[i]
                        break
        child_rt.recalc_rt_len()
        return child_rt

    def mutate(self, route_to_mut):
        if random.random() < k_mut_prob:
            mut_pos1 = random.randint(0,len(route_to_mut.route)-1)
            mut_pos2 = random.randint(0,len(route_to_mut.route)-1)

            if mut_pos1 == mut_pos2:
                return route_to_mut
            city1 = route_to_mut.route[mut_pos1]
            city2 = route_to_mut.route[mut_pos2]

            route_to_mut.route[mut_pos2] = city1
            route_to_mut.route[mut_pos1] = city2
        route_to_mut.recalc_rt_len()

        return route_to_mut

    def mutate_2opt(route_to_mut):
        if random.random() < k_mut_prob:

            for i in range(len(route_to_mut.route)):
                for ii in range(len(route_to_mut.route)): # i is a, i + 1 is b, ii is c, ii+1 is d
                    if (route_to_mut.route[i].distance_to[route_to_mut.route[i-len(route_to_mut.route)+1].name]
                     + route_to_mut.route[ii].distance_to[route_to_mut.route[ii-len(route_to_mut.route)+1].name]
                     > route_to_mut.route[i].distance_to[route_to_mut.route[ii].name]
                     + route_to_mut.route[i-len(route_to_mut.route)+1].distance_to[route_to_mut.route[ii-len(route_to_mut.route)+1].name]):

                        c_to_swap = route_to_mut.route[ii]
                        b_to_swap = route_to_mut.route[i-len(route_to_mut.route)+1]

                        route_to_mut.route[i-len(route_to_mut.route)+1] = c_to_swap
                        route_to_mut.route[ii] = b_to_swap 

            route_to_mut.recalc_rt_len()

        return route_to_mut

    def tournament_select(self, population):
        tournament_pop = RoutePop(size=tournament_size,initialise=False)

        for i in range(tournament_size-1):
            tournament_pop.rt_pop.append(random.choice(population.rt_pop))

        return tournament_pop.get_fittest()

    def evolve_population(self, init_pop):
        descendant_pop = RoutePop(size=init_pop.size, initialise=True)
        elitismOffset = 0
        if elitism:
            descendant_pop.rt_pop[0] = init_pop.fittest
            elitismOffset = 1
        for x in range(elitismOffset,descendant_pop.size):
            tournament_parent1 = self.tournament_select(init_pop)
            tournament_parent2 = self.tournament_select(init_pop)
            tournament_child = self.crossover(tournament_parent1, tournament_parent2)
            descendant_pop.rt_pop[x] = tournament_child
        for route in descendant_pop.rt_pop:
            if random.random() < 0.3:
                self.mutate(route)
        descendant_pop.get_fittest()

        return descendant_pop






class App(object):
    def __init__(self,n_generations,pop_size, graph=False):
        self.n_generations = n_generations
        self.pop_size = pop_size
        if graph:
            self.set_city_gcoords()
            self.window = Tk()
            self.window.wm_title("Generation 0")
            self.canvas_current = Canvas(self.window, height=300, width=300)
            self.canvas_best = Canvas(self.window, height=300, width=300)
            self.canvas_current_title = Label(self.window, text="Best route of current gen:")
            self.canvas_best_title = Label(self.window, text="Overall best so far:")
            self.stat_tk_txt = StringVar()
            self.status_label = Label(self.window, textvariable=self.stat_tk_txt, relief=SUNKEN, anchor=W)
            for city in list_of_cities:
                self.canvas_current.create_oval(city.graph_x-2, city.graph_y-2, city.graph_x + 2, city.graph_y + 2, fill='blue')
                self.canvas_best.create_oval(city.graph_x-2, city.graph_y-2, city.graph_x + 2, city.graph_y + 2, fill='blue')

            self.canvas_current_title.pack()
            self.canvas_current.pack()
            self.canvas_best_title.pack()
            self.canvas_best.pack()
            self.status_label.pack(side=BOTTOM, fill=X)
            self.window_loop(graph)
        else:
            print("Calculating GA_loop")
            self.GA_loop(n_generations,pop_size, graph=graph)

    def set_city_gcoords(self):
        min_x = 100000
        max_x = -100000
        min_y = 100000
        max_y = -100000
        for city in list_of_cities:

            if city.x < min_x:
                min_x = city.x
            if city.x > max_x:
                max_x = city.x

            if city.y < min_y:
                min_y = city.y
            if city.y > max_y:
                max_y = city.y

        for city in list_of_cities:
            city.graph_x = (city.graph_x + (-1*min_x))
            city.graph_y = (city.graph_y + (-1*min_y))

        min_x = 100000
        max_x = -100000
        min_y = 100000
        max_y = -100000

        for city in list_of_cities:

            if city.graph_x < min_x:
                min_x = city.graph_x
            if city.graph_x > max_x:
                max_x = city.graph_x

            if city.graph_y < min_y:
                min_y = city.graph_y
            if city.graph_y > max_y:
                max_y = city.graph_y

        if max_x > max_y:
            stretch = 300 / max_x
        else:
            stretch = 300 / max_y

        for city in list_of_cities:
            city.graph_x *= stretch
            city.graph_y = 300 - (city.graph_y * stretch)


    def update_canvas(self,the_canvas,the_route,color):
        the_canvas.delete('path')
        for i in range(len(the_route.route)):
            next_i = i-len(the_route.route)+1
            the_canvas.create_line(the_route.route[i].graph_x,
                                the_route.route[i].graph_y,
                                the_route.route[next_i].graph_x,
                                the_route.route[next_i].graph_y,
                                tags=("path"),
                                fill=color)
            the_canvas.pack()
            the_canvas.update_idletasks()

    def GA_loop(self,n_generations,pop_size, graph=False):
        start_time = time.time()
        print("Creates the population:")
        the_population = RoutePop(pop_size, True)
        if the_population.fittest.is_valid_route() == False:
            raise NameError('Multiple cities with same name. Check cities.')
            return 
        initial_length = the_population.fittest.length
        best_route = Route()

        if graph:
            self.update_canvas(self.canvas_current,the_population.fittest,'red')
            self.update_canvas(self.canvas_best,best_route,'green')

        for x in range(1,n_generations):
            if x % 8 == 0 and graph:
                self.update_canvas(self.canvas_current,the_population.fittest,'red')

            the_population = GA().evolve_population(the_population)
            if the_population.fittest.length < best_route.length:
                best_route = copy.deepcopy(the_population.fittest)
                if graph:
                    self.update_canvas(self.canvas_best,best_route,'green')
                    self.stat_tk_txt.set('Initial length {0:.2f} Best length = {1:.2f}'.format(initial_length,best_route.length))
                    self.status_label.pack()
                    self.status_label.update_idletasks()

            self.clear_term()
            print('Generation {0} of {1}'.format(x,n_generations))
            print(' ')
            print('Overall fittest has length {0:.2f}'.format(best_route.length))
            print('and goes via:')
            best_route.pr_cits_in_rt(True)
            print(' ')
            print('Current fittest has length {0:.2f}'.format(the_population.fittest.length))
            print('And goes via:')
            the_population.fittest.pr_cits_in_rt(True)
            print(' ')
            print('''The screen with the maps may become unresponsive if the population size is too large. It will refresh at the end.''')

            if graph:
                self.window.wm_title("Generation {0}".format(x))
        if graph:
            self.window.wm_title("Generation {0}".format(n_generations))
            self.update_canvas(self.canvas_best,best_route,'green')
        end_time = time.time()

        self.clear_term()
        print('Finished evolving {0} generations.'.format(n_generations))
        print("Elapsed time was {0:.1f} seconds.".format(end_time - start_time))
        print(' ')
        print('Initial best distance: {0:.2f}'.format(initial_length))
        print('Final best distance:   {0:.2f}'.format(best_route.length))
        print('The best route went via:')
        best_route.pr_cits_in_rt(print_route=True)

    def window_loop(self, graph):
        self.window.after(0,self.GA_loop(self.n_generations, self.pop_size, graph))
        self.window.mainloop()

    def clear_term(self):
        os.system('cls' if os.name=='nt' else 'clear')

def random_cities():
    with open('./data/iran.txt') as f:
        for line in f.readlines():
            cty = line.split(' ')
            x = City(str(cty[0]), float(cty[1]), float(cty[2]))

    for city in list_of_cities:
        city.calculate_distances()
    app = App(n_generations=k_n_generations,pop_size=k_population_size, graph=True)

if __name__ == '__main__':
    random_cities()

