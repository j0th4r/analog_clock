class CircleDrawer:
    def __init__(self, center, radius):
        self.xc, self.yc = center
        self.radius = radius

    def get_full_circle(self):
        # Combine all octant coordinates to create full circle
        octants = [
            self.first_octant, self.second_octant, 
            self.third_octant, self.fourth_octant,
            self.fifth_octant, self.sixth_octant,
            self.seventh_octant, self.eighth_octant
        ]
        
        # Flatten and create symmetric points
        full_circle = []
        for octant in octants:
            full_circle.extend(octant)
        
        return full_circle

    @property
    def first_octant(self):
        x = 0
        y = self.radius
        p = 1 - self.radius
        octant = []

        while x <= y:
            octant.append((x + self.xc, y + self.yc))
            if p <= 0:
                x += 1
                y = y
                p = p + 2 * x + 3
            else:
                x += 1
                y -= 1
                p = p + 2 * x - 2 * y + 5
        return octant

    @property
    def second_octant(self):
        x = 0
        y = self.radius
        p = 1 - self.radius
        octant = []

        while x <= y:
            octant.append((-x + self.xc, y + self.yc))
            if p <= 0:
                x += 1
                y = y
                p = p + 2 * x + 3
            else:
                x += 1
                y -= 1
                p = p + 2 * x - 2 * y + 5
        return octant

    @property
    def third_octant(self):
        x = 0
        y = self.radius
        p = 1 - self.radius
        octant = []

        while x <= y:
            octant.append((-x + self.xc, -y + self.yc))
            if p <= 0:
                x += 1
                y = y
                p = p + 2 * x + 3
            else:
                x += 1
                y -= 1
                p = p + 2 * x - 2 * y + 5
        return octant

    @property
    def fourth_octant(self):
        x = 0
        y = self.radius
        p = 1 - self.radius
        octant = []

        while x <= y:
            octant.append((x + self.xc, -y + self.yc))
            if p <= 0:
                x += 1
                y = y
                p = p + 2 * x + 3
            else:
                x += 1
                y -= 1
                p = p + 2 * x - 2 * y + 5
        return octant

    @property
    def fifth_octant(self):
        x = 0
        y = self.radius
        p = 1 - self.radius
        octant = []

        while x <= y:
            octant.append((y + self.xc, x + self.yc))
            if p <= 0:
                x += 1
                y = y
                p = p + 2 * x + 3
            else:
                x += 1
                y -= 1
                p = p + 2 * x - 2 * y + 5
        return octant

    @property
    def sixth_octant(self):
        x = 0
        y = self.radius
        p = 1 - self.radius
        octant = []

        while x <= y:
            octant.append((-y + self.xc, x + self.yc))
            if p <= 0:
                x += 1
                y = y
                p = p + 2 * x + 3
            else:
                x += 1
                y -= 1
                p = p + 2 * x - 2 * y + 5
        return octant

    @property
    def seventh_octant(self):
        x = 0
        y = self.radius
        p = 1 - self.radius
        octant = []

        while x <= y:
            octant.append((-y + self.xc, -x + self.yc))
            if p <= 0:
                x += 1
                y = y
                p = p + 2 * x + 3
            else:
                x += 1
                y -= 1
                p = p + 2 * x - 2 * y + 5
        return octant

    @property
    def eighth_octant(self):
        x = 0
        y = self.radius
        p = 1 - self.radius
        octant = []

        while x <= y:
            octant.append((y + self.xc, -x + self.yc))
            if p <= 0:
                x += 1
                y = y
                p = p + 2 * x + 3
            else:
                x += 1
                y -= 1
                p = p + 2 * x - 2 * y + 5
        return octant
