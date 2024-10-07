import math

class Node:
    
    def __init__ (self, x, y):
        self.x = x;
        self.y = y;
        self.pheromone_level = 1.0;
        
    def update_pheromone(self, increase):
        self.pheromone_level *= increase
        
    def get_pheromone(self):
        return self.pheromone_level
        
    def evaporate(self, pheromone_evaporation):
        if self.pheromone_level/pheromone_evaporation > 1.0:
            self.pheromone_level = self.pheromone_level/pheromone_evaporation
        else:
            self.pheromone_level = 1.0
            
    def get_weigth(self):
        return self.weight
    
    def get_x (self):
        return self.x
    
    def get_y(self):
        return self.x
    
    def find_distance(self, other_node):
        return math.sqrt(pow((other_node.get_x()-self.x),2) + pow((other_node.get_y()-self.y),2))
