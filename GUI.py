import pygame
from AntColonyOptimization import AntColonyOptimization
from Ant import Ant
from Node import Node

class GUI:
    def __init__(self, colony):
        self.colony = colony
        # for node in self.colony.nodes:
        #         print(f"Before Simulation: Node: {node.get_x()}, {node.get_y()}")
        self.width = colony.length
        print(f"colony length: {colony.length}")
        self.height = colony.height
        print(f"colony height: {colony.height}")

        pygame.init()
        self.screen = pygame.display.set_mode((self.width+80, self.height+60))
        pygame.display.set_caption("Ant Colony Optimization")
        self.clock = pygame.time.Clock()
        
        self.running = True
        self.generations_completed = 0

    def draw_nodes(self):
        for node in self.colony.nodes:
            pygame.draw.circle(self.screen, (0, 0, 0), (int(node.get_x()), int(node.get_y())), 8)

    def draw_pheromone_trails(self):
        for trail in self.colony.pheromone_trails:
            for i in range(len(trail) - 1):
                start_pos = (trail[i].get_x(), trail[i].get_y())
                end_pos = (trail[i + 1].get_x(), trail[i + 1].get_y())
                pheromone_intensity = trail[i].get_pheromone()
                # Adjust transparency based on pheromone intensity
                color = (0, 0, 0, int(pheromone_intensity * 255))
                # Draw pheromone trail  
                pygame.draw.line(self.screen, color, start_pos, end_pos, 3)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.screen.fill((255, 255, 255))
            
            if self.generations_completed < self.colony.generations:
                self.colony.simulate()
                self.generations_completed += 1
            
            self.draw_nodes()
            self.draw_pheromone_trails()
            pygame.display.flip()
            
            # for node in self.colony.nodes:
            #     print(f"After Simulation: Node: {node.get_x()}, {node.get_y()}")

        pygame.quit()


# Create an ant colony and visualize it
num_ants = 10
num_nodes = 10
length = 800
height = 600
start_node = Node(400, 20)  # Example start node
generations = 1

colony = AntColonyOptimization(num_ants, num_nodes, start_node, generations, length, height)
gui = GUI(colony)
gui.run()