import pgzrun

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

inert = []


# Funktioner (def) här nedanför
def draw():
    screen.fill((255, 255, 255))

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            block_size = 20
            block_draw_size = block_size - 1
            screen.draw.filled_rect(
                Rect(
                    x * block_size, y * block_size,
                    block_draw_size, block_draw_size
                ),
                color=(222, 222, 222)
            )


# Kod för att starta appen här nedanför
for y in range(grid_y_count):
    inert.append([])
    for x in range(grid_x_count):
        inert[y].append(' ')

pgzrun.go()  # måste vara sista raden
