import pgzrun

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25


# Funktioner (def) här nedanför
def draw():
    screen.fill((255, 255, 255))

    for y in range(18):
        for x in range(10):
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

pgzrun.go()  # måste vara sista raden