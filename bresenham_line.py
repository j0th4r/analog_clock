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

        if dx >= 0:
            sign_x = 1
        else:
            sign_x = -1

        if dy >= 0:
            sign_y = 1
        else:
            sign_y = -1

        dx = abs(dx)
        dy = abs(dy)

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
        elif dy < dx:
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
