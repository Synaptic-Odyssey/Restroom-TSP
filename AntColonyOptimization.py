import Ant
import Node
import random

class AntColonyOptimization:

    pheromone_evaporation = 2
    pheromone_deposit = 100
    
    def __init__ (self, num_ants, num_nodes, start_node, generations, length, height):
        self.num_ants = num_ants
        self.start_node = start_node
        self.num_nodes = num_nodes
        self.generations = generations
        self.length = length
        self.height = height
        
        #initialize a set of random nodes
        self.nodes = []
        for _ in range(num_nodes):
            x = random.randint(0, length)
            y = random.randint(0, height)
            self.nodes.append(Node(x, y))
            
        self.ants = []
        for _ in range(num_ants):
            self.ants.append(Ant(self.start_node, self.nodes))
            
    def simulate(self):
        for gen in range(self.generations):
            print(f"generation: {gen}")
            
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
        
        for pheromone_trail in self.pheromone_trails:
            total_distance = 0
            prev_node = self.start_node
            
            for node in pheromone_trail:
                total_distance += node.find_distance(prev_node)
                prev_node = node
            
            for node in pheromone_trail:
                node.update_pheromone(1/(total_distance)*AntColonyOptimization.pheromone_deposit)    
        