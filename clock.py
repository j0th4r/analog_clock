import pygame
import math
from bresenham_line import LineDrawer
from bresenham_circle import CircleDrawer

class AnalogClock:
    def __init__(self, width=400, height=400):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Analog Clock")
        self.width = width
        self.height = height
        self.center = (width // 2, height // 2)
        self.radius = min(width, height) // 2 - 20

    def draw_line(self, start, end, color):
        line = LineDrawer(start[0], start[1], end[0], end[1])
        coordinates = line.draw_line_with_bresenham
        for coord in coordinates:
            pygame.draw.circle(self.screen, color, coord, 1)

    def draw_circle(self, center, radius, color):
        circle = CircleDrawer(center, radius)
        points = circle.get_full_circle()
        for point in points:
            pygame.draw.circle(self.screen, color, point, 1)

    def draw_clock_face(self):
        self.screen.fill((255, 255, 255))
        
        # Draw clock circle
        self.draw_circle(self.center, self.radius, (0, 0, 0))
        
        # Draw hour markers
        for angle in range(0, 360, 6):
            outer_x = self.center[0] + int(self.radius * math.cos(math.radians(angle)))
            outer_y = self.center[1] + int(self.radius * math.sin(math.radians(angle)))
            
            inner_radius = self.radius - 10 if angle % 30 == 0 else self.radius - 5
            inner_x = self.center[0] + int(inner_radius * math.cos(math.radians(angle)))
            inner_y = self.center[1] + int(inner_radius * math.sin(math.radians(angle)))
            
            self.draw_line((outer_x, outer_y), (inner_x, inner_y), (0, 0, 0))

    def draw_hands(self):
        # Placeholder test hand positions
        # Hour hand (red)
        hour_x = self.center[0] + int(self.radius * 0.5 * math.cos(math.radians(-90)))
        hour_y = self.center[1] + int(self.radius * 0.5 * math.sin(math.radians(-90)))
        self.draw_line(self.center, (hour_x, hour_y), (255, 0, 0))
        
        # Minute hand (blue)
        minute_x = self.center[0] + int(self.radius * 0.7 * math.cos(math.radians(0)))
        minute_y = self.center[1] + int(self.radius * 0.7 * math.sin(math.radians(0)))
        self.draw_line(self.center, (minute_x, minute_y), (0, 0, 255))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_clock_face()
            self.draw_hands()
            
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    clock = AnalogClock()
    clock.run()
