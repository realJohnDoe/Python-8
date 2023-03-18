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
            colors = {
                ' ': (222, 222, 222),
                'i': (120, 195, 239),
                'j': (236, 231, 108),
                'l': (124, 218, 193),
                'o': (234, 177, 121),
                's': (211, 136, 236),
                't': (248, 147, 196),
                'z': (169, 221, 118),
            }
            block = inert[y][x]
            color = colors[block]
            block_size = 20
            block_draw_size = block_size - 1
            screen.draw.filled_rect(
                Rect(
                    x * block_size, y * block_size,
                    block_draw_size, block_draw_size
                ),
                color=color
            )


# Kod för att starta appen här nedanför
for y in range(grid_y_count):
    inert.append([])
    for x in range(grid_x_count):
        inert[y].append(' ')

# Tillfälligt
inert[17][0] = 'i'
inert[16][1] = 'j'
inert[15][2] = 'l'
inert[14][3] = 'o'
inert[13][4] = 's'
inert[12][5] = 't'
inert[11][6] = 'z'

pgzrun.go()  # måste vara sista raden
