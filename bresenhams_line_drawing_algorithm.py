# An optimized implementation of bresenham's Line Drawing Algorithm using only integer incrementation

def draw_line(x1, y1, x2, y2, w):
    # Determine the starting point based on the x-coordinate comparison
    x, y = [(x1, y1), (x2, y2)][x1 > x2]

    # Calculate the absolute differences in x and y coordinates
    dx, dy = abs(x2 - x1), abs(y2 - y1)

    # Determine the slope direction (positive or negative)
    m = -1 if not dx or (y1 - y2) / (x1 - x2) <= 0 else 1

    # Calculate intermediate values for the algorithm
    d2min, dmax, d2max = min(dx, dy) * 2, max(dx, dy), max(dx, dy) * 2
    pk = d2min - dmax

    # Iterate over the longer distance (dmax) to draw the line
    for i in range(dmax):
        # Update the x and y coordinates based on the slope and decision parameter
        x, y, pk = x + (dx >= dy or pk > 0), y + m * (dx < dy or pk > 0), pk + d2min - d2max * (pk > 0)

        # Draw a point at the current (x, y) coordinate
        Point(x, y).draw(w)
