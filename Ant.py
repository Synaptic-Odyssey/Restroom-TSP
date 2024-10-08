import math
import copy
import random
from Node import Node

class Ant:
    
    #class attribute, meaning this value will be the same for every ant
    distance_weight = 3
    pheromone_weight = 8
    
    #self is a parameter because it allows the class to access one specific instance of the class
    def __init__ (self, start_node, nodes):
        #current node
        self.node = start_node
        #pherome_trail of the ants is an instance attribute, meaning it is unique for each ant object
        self.start_node = start_node
        #This is the central list of nodes that keeps track of all the pheronomes
        self.nodes = nodes
        self.pheromone_trail = [self.start_node]
        
        self.nodes_not_visited = []
        for a_node in self.nodes:
            self.nodes_not_visited.append(a_node.get_indice())

    def update (self):
        next_node = self.calculate_next_node()
        self.node = next_node
        self.pheromone_trail.append(self.node)
        self.nodes_not_visited.remove(self.node.get_indice())

    #The ant chooses the next node that isn't in the nodes it has previously visited
    #It is based on the pherome left on the node and the inverse of the distance to that node
    #There will be a factor of randomness

    def calculate_next_node(self):
        weights = []
        on_node = self.node
        total_weight = 0

        # Calculate weights for all nodes not visited
        for node_indice in self.nodes_not_visited:
            # Find the actual node in the central list based on the indice
            for a_node in self.nodes:
                if a_node.get_indice() == node_indice:
                    after_node = a_node
                    break
            
            distance = on_node.find_distance(after_node)

            if distance < 0.00000001:
                print("Warning: Distance is zero. Skipping this node.")
                weights.append(1)
                continue
            
            # Calculate weight based on pheromone and distance
            weight = ((after_node.get_pheromone()**Ant.pheromone_weight) / (distance**Ant.distance_weight))**3
            weights.append(weight)
            total_weight += weight

        # Select the next node index based on the calculated weights
        next_node_indice = random.choices(self.nodes_not_visited, weights)[0]

        # Convert the selected index back to the actual Node object
        for a_node in self.nodes:
            if a_node.get_indice() == next_node_indice:
                return a_node
        
    def get_pheromone_trail(self):
        return self.pheromone_trail
    
    def reset(self):
        self.node = self.start_node
        self.pheromone_trail = [self.start_node]
        
        self.nodes_not_visited = []
        for a_node in self.nodes:
            self.nodes_not_visited.append(a_node.get_indice())