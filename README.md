## Analog Clock Project

### Project Overview
The Analog Clock Project aims to develop a digital analog clock utilizing Pygame for visualization. The primary objective is to design a unique clock featuring custom drawing algorithms to enhance both its visual appeal and functionality. This project leverages the robust graphical features provided by Pygame to create an interactive and aesthetically pleasing clock interface.

### Requirements
- Python 3.8 or later
- Pygame library

### Installation
1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the required dependencies:**
    ```bash
    pip install pygame
    ```

### Project Structure
The project is structured as follows:
```
<repository-directory>
│
├── line_drawer.py          # Contains the LineDrawer class
├── circle_drawer.py        # Contains the CircleDrawer class
├── main.py                 # Main script to run the clock
├── README.md               # Project README file
```

### Running the Project
To run the analog clock application, execute the following command:
```bash
python main.py
```

### Code Explanation
#### `bresenham_line.py`
This file contains the `LineDrawer` class, which implements Bresenham's line drawing algorithm to ensure pixel-perfect line rendering.

```python
class LineDrawer:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @property
    def draw_line_with_bresenham(self):
        coordinates = []
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        sign_x = 1 if dx >= 0 else -1
        sign_y = 1 if dy >= 0 else -1
        dx, dy = abs(dx), abs(dy)
        x, y = self.x1, self.y1

        if dx == dy:
            for _ in range(dx + 1):
                coordinates.append((x, y))
                x += sign_x
                y += sign_y
        elif dy > dx:
            p = 2 * dx - dy
            for _ in range(dy + 1):
                coordinates.append((x, y))
                if p < 0:
                    p += 2 * dx
                else:
                    x += sign_x
                    p += 2 * (dx - dy)
                y += sign_y
        else:
            p = 2 * dy - dx
            for _ in range(dx + 1):
                coordinates.append((x, y))
                if p < 0:
                    p += 2 * dy
                else:
                    y += sign_y
                    p += 2 * (dy - dx)
                x += sign_x

        return coordinates
```

#### `bresenham_circle.py`
This file contains the `CircleDrawer` class, which implements a method based on Bresenham's algorithm for drawing circles.

```python
class CircleDrawer:
    def __init__(self, center, radius):
        self.xc, self.yc = center
        self.radius = radius

    def get_full_circle(self):
        octants = [
            self.first_octant, self.second_octant,
            self.third_octant, self.fourth_octant,
            self.fifth_octant, self.sixth_octant,
            self.seventh_octant, self.eighth_octant
        ]
        full_circle = []
        for octant in octants:
            full_circle.extend(octant)
        return full_circle

    @property
    def first_octant(self):
        x, y = 0, self.radius
        p = 1 - self.radius
        octant = []

        while x <= y:
            octant.append((x + self.xc, y + self.yc))
            if p <= 0:
                p += 2 * x + 3
            else:
                y -= 1
                p += 2 * x - 2 * y + 5
            x += 1
        return octant

    @property
    def second_octant(self):
        x, y = 0, self.radius
        p = 1 - self.radius
        octant = []

        while x <= y:
            octant.append((-x + self.xc, y + self.yc))
            if p <= 0:
                p += 2 * x + 3
            else:
                y -= 1
                p += 2 * x - 2 * y + 5
            x += 1
        return octant

    @property
    def third_octant(self):
        x, y = 0, self.radius
        p = 1 - self.radius
        octant = []

        while x <= y:
            octant.append((-x + self.xc, -y + self.yc))
            if p <= 0:
                p += 2 * x + 3
            else:
                y -= 1
                p += 2 * x - 2 * y + 5
            x += 1
        return octant

    @property
    def fourth_octant(self):
        x, y = 0, self.radius
        p = 1 - self.radius
        octant = []

        while x <= y:
            octant.append((x + self.xc, -y + self.yc))
            if p <= 0:
                p += 2 * x + 3
            else:
                y -= 1
                p += 2 * x - 2 * y + 5
            x += 1
        return octant

    @property
    def fifth_octant(self):
        x, y = 0, self.radius
        p = 1 - self.radius
        octant = []

        while x <= y:
            octant.append((y + self.xc, x + self.yc))
            if p <= 0:
                p += 2 * x + 3
            else:
                y -= 1
                p += 2 * x - 2 * y + 5
            x += 1
        return octant

    @property
    def sixth_octant(self):
        x, y = 0, self.radius
        p = 1 - self.radius
        octant = []

        while x <= y:
            octant.append((-y + self.xc, x + self.yc))
            if p <= 0:
                p += 2 * x + 3
            else:
                y -= 1
                p += 2 * x - 2 * y + 5
            x += 1
        return octant

    @property
    def seventh_octant(self):
        x, y = 0, self.radius
        p = 1 - self.radius
        octant = []

        while x <= y:
            octant.append((-y + self.xc, -x + self.yc))
            if p <= 0:
                p += 2 * x + 3
            else:
                y -= 1
                p += 2 * x - 2 * y + 5
            x += 1
        return octant

    @property
    def eighth_octant(self):
        x, y = 0, self.radius
        p = 1 - self.radius
        octant = []

        while x <= y:
            octant.append((y + self.xc, -x + self.yc))
            if p <= 0:
                p += 2 * x + 3
            else:
                y -= 1
                p += 2 * x - 2 * y + 5
            x += 1
        return octant
```

#### `clock.py`
This is the main script that initializes the Pygame environment, creates the clock, and runs the main loop to display the clock.

```python
import pygame
import math
from line_drawer import LineDrawer
from circle_drawer import CircleDrawer

class AnalogClockProgress:
    def __init__(self, width=400, height=400):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Analog Clock Progress")
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
        
