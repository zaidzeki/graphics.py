def draw_circle(xc, yc, r, win):
    # Initialize the starting values
    x, y, pk = 0, r, 1 - r

    # Iterate until the x-coordinate surpasses the y-coordinate
    while x < y:
        # Move the x-coordinate one step further
        x += 1

        # Update the decision parameter and y-coordinate based on the current state
        pk += 2 * x + 1 - (2 * y) * (pk >= 0)
        y -= pk >= 0

        # Draw the eight symmetric points around the circle
        for x_, y_ in [(x, y), (y, x), (-x, y), (-y, x), (x, -y), (y, -x), (-x, -y), (-y, -x)]:
            # Draw a point at the current (x, y) coordinate with the center offset
            Point(x_ + xc, y_ + yc).draw(win)
