import math

class Node:
    
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.pheromone_level = 1.0
        
    def update_pheromone(self, increase):
        self.pheromone_level = self.pheromone_level*increase
        
    def get_pheromone(self):
        return self.pheromone_level
        
    def evaporate(self, pheromone_evaporation):
        if self.pheromone_level/pheromone_evaporation > 1.0:
            self.pheromone_level = self.pheromone_level/pheromone_evaporation
        else:
            self.pheromone_level = 1.0
            
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
