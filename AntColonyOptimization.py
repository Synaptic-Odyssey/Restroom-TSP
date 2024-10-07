from Ant import Ant
from Node import Node
import random

class AntColonyOptimization:

    pheromone_evaporation = 1.1
    pheromone_deposit = 10000
    
    def __init__ (self, num_ants, num_nodes, start_node, generations, length, height):
        self.num_ants = num_ants
        self.start_node = start_node
        self.num_nodes = num_nodes
        self.generations = generations
        self.length = length
        self.height = height
        
        #initialize a set of random nodes
        self.nodes = []
        for _ in range(self.num_nodes):
            x = random.uniform(0, self.length)
            y = random.uniform(0, self.height)
            # x = random.randint(0, self.length)
            # y = random.randint(0, self.height)
            #print(f"node_before : {x}, {y}")
            
            new_node = Node(x, y)
            self.nodes.append(new_node)
            #print(f"node_after : {new_node.get_x()}, {new_node.get_y()}")
        
        #print(f" node number : {len(self.nodes)}")
            
        self.ants = []
        for _ in range(num_ants):
            self.ants.append(Ant(self.start_node, self.nodes))
            
    def simulate(self):
        for gen in range(self.generations):
            # print(f"generation: {gen}")
            
            self.pheromone_trails = []
            for ant in self.ants:
                for _ in range(self.num_nodes):
                    ant.update()
                self.pheromone_trails.append(ant.get_pheromone_trail())
                ant.reset()
            
            self.update_pheromones(self.pheromone_trails)

    #pheromones should only evaporate after each generation
    #pheromes will also be updated each generation
    #the shorter the total trail of the ant, the more pheromones are deposited
    def update_pheromones(self, pheromone_trails):
        for node in self.nodes:
            node.evaporate(AntColonyOptimization.pheromone_evaporation)
        
        #Debugging, have established that these values are consistent
        # print(f"evapo: {AntColonyOptimization.pheromone_evaporation}")
        # print(f"deposit: {AntColonyOptimization.pheromone_deposit}")
        
        for pheromone_trail in self.pheromone_trails:
            total_distance = 0
            prev_node = self.start_node
            
            for node in pheromone_trail:
                total_distance += node.find_distance(prev_node)
                prev_node = node
            
            for node in pheromone_trail:
                node.update_pheromone((1/(total_distance**2))*AntColonyOptimization.pheromone_deposit)    
        