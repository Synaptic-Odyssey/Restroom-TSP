import pygame
from AntColonyOptimization import AntColonyOptimization
from Ant import Ant
from Node import Node
import random

class GUI:
    def __init__(self, colony, draw_enabled=True):
        self.colony = colony
        self.width = colony.length
        self.height = colony.height
        self.draw_enabled = draw_enabled  # Toggle for drawing each generation

        pygame.init()
        self.screen = pygame.display.set_mode((self.width + 80, self.height + 60))
        pygame.display.set_caption("Ant Colony Optimization")
        self.clock = pygame.time.Clock()

        self.generations_completed = 0
        self.shortest_path = None
        self.ant_colors = self.generate_ant_colors(colony.num_ants)

    def generate_ant_colors(self, num_ants):
        return [
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for _ in range(num_ants)
        ]

    def draw_nodes(self):
        for node in self.colony.nodes:
            pygame.draw.circle(self.screen, (0, 0, 0), (int(node.get_x()), int(node.get_y())), 8)
        pygame.draw.circle(self.screen, (255, 0, 0), (int(self.colony.start_node.get_x()), int(self.colony.start_node.get_y())), 10)

    def draw_pheromone_trails(self):
        if self.generations_completed < self.colony.generations - 1:
            for ant_index, trail in enumerate(self.colony.colony_pheromone_trails):
                for i in range(len(trail) - 1):
                    start_pos = (trail[i].get_x(), trail[i].get_y())
                    end_pos = (trail[i + 1].get_x(), trail[i + 1].get_y())
                    color = self.ant_colors[ant_index]
                    pygame.draw.line(self.screen, color, start_pos, end_pos, 3)
        else:
            if self.shortest_path:
                for i in range(len(self.shortest_path) - 1):
                    start_pos = (self.shortest_path[i].get_x(), self.shortest_path[i].get_y())
                    end_pos = (self.shortest_path[i + 1].get_x(), self.shortest_path[i + 1].get_y())
                    pygame.draw.line(self.screen, (255, 0, 0), start_pos, end_pos, 3)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            if self.generations_completed < self.colony.generations:
                self.colony.simulate()

                # Only draw the current generation if drawing is enabled
                if self.draw_enabled:
                    self.screen.fill((255, 255, 255))
                    self.draw_nodes()
                    self.draw_pheromone_trails()
                    pygame.display.flip()

                self.generations_completed += 1

                # After the final generation, calculate shortest path
                if self.generations_completed == self.colony.generations:
                    self.shortest_path = self.get_shortest_path()
                    # Print the total distance and coordinates of the shortest path
                    total_distance = 0
                    prev_node = self.colony.start_node
                    print("Final shortest path coordinates:")
                    for node in self.shortest_path:
                        total_distance += prev_node.find_distance(node)
                        print(f"Node at ({node.get_x()}, {node.get_y()})")
                        prev_node = node
                    print(f"Total distance of the shortest path: {total_distance}")

            else:
                if self.draw_enabled:
                    # Redraw the final shortest path
                    self.screen.fill((255, 255, 255))
                    self.draw_nodes()
                    self.draw_pheromone_trails()
                    pygame.display.flip()

            self.clock.tick(10) 

    def get_shortest_path(self):
        shortest_path = None
        shortest_distance = float('inf')

        for ant in self.colony.colony_pheromone_trails:
            total_distance = 0
            prev_node = self.colony.start_node
            for node in ant:
                total_distance += prev_node.find_distance(node)
                prev_node = node

            if total_distance < shortest_distance:
                shortest_distance = total_distance
                shortest_path = ant

        return shortest_path

num_ants = 10
num_nodes = 20
length = 800
height = 600
start_node = Node(30, 30, num_nodes + 1)
generations = 30

colony = AntColonyOptimization(num_ants, num_nodes, start_node, generations, length, height)

gui = GUI(colony, draw_enabled=True)
gui.run()