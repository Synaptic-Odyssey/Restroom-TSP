import math

class Node:
    
    def __init__ (self, x, y, indice):
        self.x = x
        self.y = y
        self.pheromone_level = 1.0
        self.indice = indice
    
    #p_level is increasing as it should here    
    def update_pheromone(self, increase):
        self.pheromone_level = self.pheromone_level*increase
        #print(f"x: {self.x}, y: {self.y}, p_level: {self.pheromone_level}")
        
    def get_pheromone(self):
        return self.pheromone_level
    
    def get_indice(self):
        return self.indice
        
    def evaporate(self, pheromone_evaporation):
        if self.pheromone_level*pheromone_evaporation > 1.0:
            self.pheromone_level = self.pheromone_level*pheromone_evaporation
        else:
            self.pheromone_level = 1.0
        #here p-level is always zero for some reason
        print(f"x: {self.x}, y: {self.y}, p_level: {self.pheromone_level}")    
            
    def get_weight(self):
        return self.weight
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def find_distance(self, other_node):
        # if self is other_node:
        #     print("Warning: self and other_node are the same!")
        #print(f"distance: {math.sqrt(pow((other_node.get_x()-self.x),2) + pow((other_node.get_y()-self.y),2))}")
        # print(f"this node x: {self.get_x()}")
        # print(f"other node x: {other_node.get_x()}")
        return math.sqrt(pow((other_node.get_x()-self.x),2) + pow((other_node.get_y()-self.y),2))
