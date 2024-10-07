import math
import copy
import random
from Node import Node

class Ant:
    
    #class attribute, meaning this value will be the same for every ant
    distance_weight = 1.5
    pheromone_weight = 0.9
    
    #self is a parameter because it allows the class to access one specific instance of the class
    def __init__ (self, start_node, nodes):
        #current node
        self.node = start_node
        #pherome_trail of the ants is an instance attribute, meaning it is unique for each ant object
        self.start_node = start_node
        self.nodes = nodes
        self.pheromone_trail = [self.start_node]
        self.nodes_not_visited = copy.deepcopy(self.nodes)

    def update (self):
        next_node = self.calculate_next_node()
        self.node = next_node
        self.pheromone_trail.append(self.node)
        self.nodes_not_visited.remove(self.node)

    #The ant chooses the next node that isn't in the nodes it has previously visited
    #It is based on the pherome left on the node and the inverse of the distance to that node
    #There will be a factor of randomness
    def calculate_next_node(self):
        weights = []
        current_node = self.node
        for on_node in self.nodes_not_visited:
            print(f"nodes not visited: {on_node.get_x()}, {on_node.get_y()}")
            
        for i in range(len(self.nodes_not_visited)):
            on_node = self.nodes_not_visited[i]
            print(f"current node: {current_node.get_x()}, {current_node.get_y()}")
            print(f"next node: {on_node.get_x()}, {on_node.get_y()}")
            
            weight = (on_node.get_pheromone()**Ant.pheromone_weight)/(current_node.find_distance(on_node)**Ant.distance_weight)
            weights.append(weight)
            
        #parameters: population, weights
        next_node = random.choices(self.nodes_not_visited, weights)[0]
        return next_node
        
    def get_pheromone_trail(self):
        return self.pheromone_trail
    
    def reset(self):
        self.node = self.start_node
        self.pheromone_trail = [self.node]
        self.nodes_not_visited = self.nodes[:]