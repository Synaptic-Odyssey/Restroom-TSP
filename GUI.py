import pygame
from AntColonyOptimization import AntColonyOptimization
from Ant import Ant
from Node import Node
import random

class GUI:
    def __init__(self, colony):
        self.colony = colony
        self.width = colony.length
        self.height = colony.height

        pygame.init()
        self.screen = pygame.display.set_mode((self.width + 80, self.height + 60))
        pygame.display.set_caption("Ant Colony Optimization")
        self.clock = pygame.time.Clock()

        self.running = True
        self.generations_completed = 0

        # Generate a list of colors for each ant
        self.ant_colors = self.generate_ant_colors(colony.num_ants)
        self.shortest_path = None

    def generate_ant_colors(self, num_ants):
        colors = []
        for _ in range(num_ants):
            # Generate a random color
            color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            colors.append(color)
        return colors

    def draw_nodes(self):
        for node in self.colony.nodes:
            pygame.draw.circle(self.screen, (0, 0, 0), (int(node.get_x()), int(node.get_y())), 8)

        # Draw start node as a distinct point (e.g., a larger red circle)
        pygame.draw.circle(self.screen, (255, 0, 0), (int(self.colony.start_node.get_x()), int(self.colony.start_node.get_y())), 10)

    def draw_pheromone_trails(self):
        if self.generations_completed < self.colony.generations - 1:
            # Draw trails for all ants in previous generations
            for ant_index, trail in enumerate(self.colony.pheromone_trails):
                for i in range(len(trail) - 1):
                    start_pos = (trail[i].get_x(), trail[i].get_y())
                    end_pos = (trail[i + 1].get_x(), trail[i + 1].get_y())

                    # Get the color for the current ant
                    color = self.ant_colors[ant_index]

                    # Draw the pheromone trail for the current ant
                    pygame.draw.line(self.screen, color, start_pos, end_pos, 3)
        else:
            # Draw only the shortest path in the final generation
            if self.shortest_path:
                for i in range(len(self.shortest_path) - 1):
                    start_pos = (self.shortest_path[i].get_x(), self.shortest_path[i].get_y())
                    end_pos = (self.shortest_path[i + 1].get_x(), self.shortest_path[i + 1].get_y())
                    pygame.draw.line(self.screen, (255, 0, 0), start_pos, end_pos, 3)  # Red color for the shortest path

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.screen.fill((255, 255, 255))
            
            if self.generations_completed < self.colony.generations:
                # Run simulation for all ants
                self.colony.simulate()
                
                # Draw all paths after each ant's journey
                self.draw_nodes()
                self.draw_pheromone_trails()
                pygame.display.flip()

                # Update the shortest path for the final generation
                if self.generations_completed == self.colony.generations - 1:
                    self.shortest_path = self.get_shortest_path()

                # Pause for visibility after each generation
                self.display_frame(1000)  # Pause for 1 second to allow drawing

                self.generations_completed += 1

            else:
                self.draw_nodes()
                self.draw_pheromone_trails()
                pygame.display.flip()

            # Control the frame rate
            self.clock.tick(30)  # Limit to 30 frames per second

        pygame.quit()

    def display_frame(self, duration):
        # Store the start time
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < duration:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # Redraw nodes and trails for clarity
            self.draw_nodes()
            self.draw_pheromone_trails()
            pygame.display.flip()
            self.clock.tick(30)  # Control the frame rate

    def get_shortest_path(self):
        shortest_path = None
        shortest_distance = float('inf')

        for ant in self.colony.pheromone_trails:
            total_distance = 0
            prev_node = self.colony.start_node
            
            for node in ant:
                total_distance += prev_node.find_distance(node)
                prev_node = node
            
            if total_distance < shortest_distance:
                shortest_distance = total_distance
                shortest_path = ant

        return shortest_path


# Create an ant colony and visualize it
num_ants = 10
num_nodes = 30
length = 800
height = 600
start_node = Node(30, 30)
generations = 4

colony = AntColonyOptimization(num_ants, num_nodes, start_node, generations, length, height)
gui = GUI(colony)
gui.run()
