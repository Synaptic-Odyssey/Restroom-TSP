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
        # for on_node in self.nodes_not_visited:
        #     print(f"nodes not visited: {on_node.get_x()}, {on_node.get_y()}")
        
        #this is not supposed to go from one node to the next; it is current node to all nodes
        on_node = self.node
        total_weight = 0
    
        #the issue is that I'm updating a copy of the nodes, not the actual nodes that exist within AntColony
        for node_indice in self.nodes_not_visited:
            # print(f"current node: {on_node.get_x()}, {on_node.get_y()}")
            # print(f"next node: {after_node.get_x()}, {after_node.get_y()}")
            
            for a_node in self.nodes:
                if a_node.get_indice() == node_indice:
                    after_node = a_node
            
            distance = on_node.find_distance(after_node)
            
            if distance < 0.00000001:
                print("Warning: Distance is zero. Skipping this node.")
                weights.append(1)
                continue
            
            #print(f"just to make sure it's not zero: {on_node.find_distance(after_node)}")
            
            #should have fixed retrieval issue, after_node now points to a node in the central system
            weight = (after_node.get_pheromone()**Ant.pheromone_weight)/(on_node.find_distance(after_node)**Ant.distance_weight)
            #print(f"weight: {weight}")
            weights.append(weight)
            total_weight += weight

    
        #print(f"total_weight: {total_weight}")
        #parameters: population, weights
        # print(f"len nodes: {len(self.nodes_not_visited)}")
        # print(f"len weights: {len(weights)}")
        
        #weights should be in the same order as the nodes not visited, so they should pair up
        
        next_node = random.choices(self.nodes_not_visited, weights)[0]
        return next_node
        
    def get_pheromone_trail(self):
        return self.pheromone_trail
    
    def reset(self):
        self.node = self.start_node
        self.pheromone_trail = [self.node]
        
        self.nodes_not_visited = []
        for a_node in self.nodes:
            self.nodes_not_visited.append(a_node.get_indice())
        
        #self.nodes_not_visited = self.nodes
        #deep copy is necessary
        
        #This copy should have the new and updated pheronome values
        #self.nodes_not_visited = copy.deepcopy(self.nodes)
