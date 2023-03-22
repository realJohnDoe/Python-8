# Flowers ⭐⭐⭐
## En handledning för Python och Pygame Zero 1.2

Det här projektet använder bilder från [flowers.zip](https://simplegametutorials.github.io/pygamezero/flowers/flowers.zip). 
De filerna finns redan med i startprojektet på https://replit.com/@RobertStorlind/flowers-starter.

![image](https://user-images.githubusercontent.com/4598641/226450608-0fb4fbf9-c465-4d93-8acd-c3f38ac4225d.png)

# Regler
Spelet börjar med ett rutnät av täckta celler. Under några av cellerna finns blommor. Spelet är över när en blomma avslöjas.

Vänsterklick på en cell avslöjar den. Om ingen av de intilliggande cellerna innehåller blommor, avtäcks de också och för de avslöjade cellerna, om ingen av deras intilliggande celler innehåller blommor, avslöjas de också, och så vidare.

Att högerklicka på en cell växlar mellan en flagga, ett frågetecken eller ingenting. 
- Flaggor förhindrar att en cell avslöjas med ett vänsterklick. 
- Frågetecken är  markeringar som inte påverkar vad som händer när cellen klickas.

Spelet är slut när alla celler utan blommor har avslöjats.

## Kontroller

**Vänsterklick med musen**	Avslöja en cell

**Högerklick med musen** Växla en dold cell mellan att ha en flagga, ett frågetecken eller ingenting.

# Översikt

Cellerna representeras av ordböcker som innehåller ett booleskt värde som anger om den innehåller en blomma eller inte, och ett strängvärde som anger i vilket av fyra tillstånd cellen är: täckt, täckt med en flagga, täckt med ett frågetecken eller avslöjad.

De celler som har blommor är slumpmässigt valda. Den första cellen som klickas utesluts från de möjliga alternativen.

När en cell klickas läggs dess position till i listan "avtäck stack".

Medan det finns något kvar i avtäckningsstacken...

- En position tas bort från slutet av stapeln.
- Denna position är inställd på avslöjad .
- Om det inte finns några blommor som omger denna position läggs de omgivande täckta och frågemarkerade positionerna (dvs. inte de avtäckta och flaggade positionerna) till avtäckningsstacken.

Cellerna ritas genom att sätta ihop följande bilder:

![image](https://user-images.githubusercontent.com/4598641/226450949-d9e02014-22b1-4aac-84ed-d00dfe9f782b.png)

# Kodning
## Rita brickor
Den täckta cellbilden ritas för varje cell.

Du kan komma åt bildfilerna som används i den här handledningen genom att ladda ner och packa upp .zip-filen som länkas till högst upp på den här sidan.

Så här ser koden ut nu. Du hittar den i startprojektet https://replit.com/@RobertStorlind/flowers-starter

```python
import pgzrun

# Globala variabler här nedanför


# Funktioner här nedanför
def draw():
  screen.fill((0, 0, 0))
  cell_size = 18

  for y in range(14):
    for x in range(19):
      screen.blit('covered', (x * cell_size, y * cell_size))

# Kod för att starta appen

pgzrun.go()  # måste vara sista raden
```

![image](https://user-images.githubusercontent.com/4598641/226451206-410b436d-e044-4c2f-876e-f5109dc96310.png)

## Markera celler

Cellpositionen under musen uppdateras varje bildruta.

Detta behöver cellstorleken, så det flyttas till att vara globalt.

För närvarande är denna position ritad som text.

pygame &ndash; modulen importeras så att `pygame.mouse.get_pos` kan användas.

Matematikmodulen är importerad så att `math.floor` kan användas.

Så här ser koden ut nu:

```python
import pgzrun
import pygame
import math

# Globala variabler här nedanför
cell_size = 18

# Funktioner här nedanför
def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)


def draw():
    screen.fill((0, 0, 0))

    for y in range(14):
        for x in range(19):
            # Removed: cell_size = 18
            screen.blit('covered', (x * cell_size, y * cell_size))

    # Temporary
    screen.draw.text(
        f"selected x: {selected_x} selected y: {selected_y}",
        (0, 0), color=(0, 0, 0)
    )

# Kod för att starta appen
pgzrun.go()  # måste vara sista raden
```
![image](https://user-images.githubusercontent.com/4598641/226451267-d9515e88-2fc0-4a97-828d-6781174e029a.png)

## Bara celler inom rutnätet ska gå att välja

Om muspositionen är större än rutnätets storlek i X- eller Y-led, alltså om vi pekar utanför rutnätet, så ställs den valda positionen in på den sista cellen på den axeln.

Rutnätets storlek i X- och Y-led återanvänds från att rita cellerna. Vi gör därför variabler med storlekarna.

✏️ Uppdatera koden och testkör. Vad händer när du pekar innanför och utanför spelplanen med muspekaren?

📝 Så här ser koden ut nu:
```python
import pgzrun
import pygame
import math

# Globala variabler här nedanför
cell_size = 18

grid_x_count = 19 #nyrad
grid_y_count = 14 #nyrad

# Funktioner här nedanför

def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1: #nyrad
        selected_x = grid_x_count - 1 #nyrad
    if selected_y > grid_y_count - 1: #nyrad
        selected_y = grid_y_count - 1 #nyrad

def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count): #ändrad
        for x in range(grid_x_count): #ändrad
            screen.blit('covered', (x * cell_size, y * cell_size))

    # Tillfälligt
    screen.draw.text(
        f"selected x: {selected_x} selected y: {selected_y}",
        (0, 0), color=(0, 0, 0)
    )

# Kod för att starta appen

pgzrun.go()  # måste vara sista raden
```

![image](https://user-images.githubusercontent.com/4598641/226451363-15f4d3b2-c3f1-4187-9d11-949fd2691b7d.png)


## Markera celler
Den markerade cellen ritas med grafiken som heter 'covered_highlighted'. Du kan se hur den ser ut i mappen `images` i repl.it, till vänster i fönstret.

✏️ Uppdatera koden för `draw()` och testkör. Ritas markeringen rätt?

```python
def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            if x == selected_x and y == selected_y: #nytt
                image = 'covered_highlighted' #nytt
            else: #nytt
                image = 'covered' #nytt
            screen.blit(image, (x * cell_size, y * cell_size))
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun
import pygame
import math

# Globala variabler här nedanför
cell_size = 18

grid_x_count = 19
grid_y_count = 14

# Funktioner här nedanför


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            if x == selected_x and y == selected_y:
                image = 'covered_highlighted'
            else:
                image = 'covered'
            screen.blit(image, (x * cell_size, y * cell_size))

    # Tillfälligt
    screen.draw.text(
        f"selected x: {selected_x} selected y: {selected_y}",
        (0, 0), color=(0, 0, 0)
    )

# Kod för att starta appen

pgzrun.go()  # måste vara sista raden
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226451429-c6b5e111-f945-47a4-bfe6-5005c372f603.png)

## Ändra cellbild när vänster musknapp är nere
När vänster musknapp är nere, ritas den markerade cellen som en avslöjad cell. Bildfilen heter 'uncovered' och du hittar den i mappen 'images' i repl.it.

✏️ Uppdatera funktionen `draw()` och testkör. Fungerar det att klicka?

```python
def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            if x == selected_x and y == selected_y:
                if pygame.mouse.get_pressed()[0] == 1:
                    image = 'uncovered'
                else:
                    image = 'covered_highlighted'
            else:
                image = 'covered'
            screen.blit(image, (x * cell_size, y * cell_size))
    # etc.
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python
import pgzrun
import pygame
import math

# Globala variabler här nedanför
cell_size = 18

grid_x_count = 19
grid_y_count = 14

# Funktioner här nedanför


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            if x == selected_x and y == selected_y:
                if pygame.mouse.get_pressed()[0] == 1:
                    image = 'uncovered'
                else:
                    image = 'covered_highlighted'
            else:
                image = 'covered'
            screen.blit(image, (x * cell_size, y * cell_size))

    # Tillfälligt
    screen.draw.text(
        f"selected x: {selected_x} selected y: {selected_y}",
        (0, 0), color=(0, 0, 0)
    )

# Kod för att starta appen

pgzrun.go()  # måste vara sista raden
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226451476-56697739-2fbd-436c-8baa-06d9e22be4ad.png)


## Rita blommor
Ett rutnät skapas för att lagra tillståndet för cellerna.

Varje cell kommer att representeras av en ordbok som lagrar två värden: om den har en blomma och om den är avslöjad/flaggad/frågemarkerad/ingenting.

För närvarande kommer det bara att lagra blomvärdet.

Om en cells "blomma"-nyckel är sann, ritas just nu blombilden över cellbilden. Vi kommer att ändra det sen så klart 🙂

Uppdatera koden och testkör. Ritas blommorna rätt?

```python
grid = [] #nytt
grid_x_count = 19
grid_y_count = 14

# etc.
def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            if x == selected_x and y == selected_y:
                if pygame.mouse.get_pressed()[0] == 1:
                    image = 'uncovered'
                else:
                    image = 'covered_highlighted'
            else:
                image = 'covered'
            screen.blit(image, (x * cell_size, y * cell_size))

            if grid[y][x]['flower']: #nytt
                screen.blit('flower', (x * cell_size, y * cell_size)) #nytt

# Kod för att starta appen
for y in range(grid_y_count): #nytt
    grid.append([]) #nytt
    for x in range(grid_x_count): #nytt
        grid[y].append({ #nytt
            'flower': False #nytt
        }) #nytt

    # Tillälligt för att testa ritningen av blommor
    grid[0][0]['flower'] = True
    grid[0][1]['flower'] = True


pgzrun.go()  # måste vara sista raden

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python
import pgzrun
import pygame
import math

# Globala variabler här nedanför
cell_size = 18

grid = []
grid_x_count = 19
grid_y_count = 14

# Funktioner här nedanför


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            if x == selected_x and y == selected_y:
                if pygame.mouse.get_pressed()[0] == 1:
                    image = 'uncovered'
                else:
                    image = 'covered_highlighted'
            else:
                image = 'covered'
            screen.blit(image, (x * cell_size, y * cell_size))

            if grid[y][x]['flower']:
                screen.blit('flower', (x * cell_size, y * cell_size))


# Kod för att starta appen
for y in range(grid_y_count):
    grid.append([])
    for x in range(grid_x_count):
        grid[y].append({
            'flower': False
        })

    # Temporary
    grid[0][0]['flower'] = True
    grid[0][1]['flower'] = True


pgzrun.go()  # måste vara sista raden

```
  
</details>

![image](https://user-images.githubusercontent.com/4598641/226451517-df57e52b-abe0-4c91-b75c-fd350bc0ef44.png)

## Förenkla kod
Koden för att rita celler och rita blomman är densamma förutom bilden att rita, så en funktion skapas med bilden och X- och Y-värdena som parametrar.

```python
def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y): #nytt
                screen.blit(image, (x * cell_size, y * cell_size)) #nytt

            if x == selected_x and y == selected_y:
                if pygame.mouse.get_pressed()[0] == 1:
                    draw_cell('uncovered', x, y) #nytt
                else:
                    draw_cell('covered_highlighted', x, y) #nytt
            else:
                draw_cell('covered', x, y) #nytt

            if grid[y][x]['flower']:
                draw_cell('flower', x, y) #nytt
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python
import pgzrun
import pygame
import math

# Globala variabler här nedanför
cell_size = 18

grid = []
grid_x_count = 19
grid_y_count = 14

# Funktioner här nedanför


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if x == selected_x and y == selected_y:
                if pygame.mouse.get_pressed()[0] == 1:
                    draw_cell('uncovered', x, y)
                else:
                    draw_cell('covered_highlighted', x, y)
            else:
                draw_cell('covered', x, y)

            if grid[y][x]['flower']:
                draw_cell('flower', x, y)


# Kod för att starta appen
for y in range(grid_y_count):
    grid.append([])
    for x in range(grid_x_count):
        grid[y].append({
            'flower': False
        })

    # Temporary
    grid[0][0]['flower'] = True
    grid[0][1]['flower'] = True


pgzrun.go()  # måste vara sista raden

```
  
</details>

## Växla blommor
För teständamål, högerklickar du på en cell för att växla dess blomma.

📝 Lägg in koden efter funktionen `update()` och testkör. Fungerar högerklick som det ska?

```python
def on_mouse_up(button):
    # Temporary
    if button == mouse.RIGHT:
        grid[selected_y][selected_x]['flower'] = not grid[selected_y][selected_x]['flower']
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python
import pgzrun
import pygame
import math

# Globala variabler här nedanför
cell_size = 18

grid = []
grid_x_count = 19
grid_y_count = 14

# Funktioner här nedanför


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def on_mouse_up(button):
    # Temporary
    if button == mouse.RIGHT:
        grid[selected_y][selected_x]['flower'] = not grid[selected_y][selected_x]['flower']


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if x == selected_x and y == selected_y:
                if pygame.mouse.get_pressed()[0] == 1:
                    draw_cell('uncovered', x, y)
                else:
                    draw_cell('covered_highlighted', x, y)
            else:
                draw_cell('covered', x, y)

            if grid[y][x]['flower']:
                draw_cell('flower', x, y)


# Kod för att starta appen
for y in range(grid_y_count):
    grid.append([])
    for x in range(grid_x_count):
        grid[y].append({
            'flower': False
        })

    # Temporary
    grid[0][0]['flower'] = True
    grid[0][1]['flower'] = True


pgzrun.go()  # måste vara sista raden

```
  
</details>


## Visa antalet blommor runt cellen
För att räkna ut antalet blommor runt en cell, loopar vi igenom de 8 grannarna runt varje cell. 
Om någon av dessa positioner är inuti rutnätet och cellen vid positionen har en blomma, ökar vi antalet blommor med 1.

Om det omgivande antalet blommor är större än 0, så ritas, för närvarande, lämplig nummerbild över cellen.

✏️ Uppdatera funktionen `draw` genom att lägga till kod i slutet. Testkör!

```python
def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if x == selected_x and y == selected_y:
                if pygame.mouse.get_pressed()[0] == 1:
                    draw_cell('uncovered', x, y)
                else:
                    draw_cell('covered_highlighted', x, y)
            else:
                draw_cell('covered', x, y)

            surrounding_flower_count = 0

            for dy in range(-1, 2): #nytt
                for dx in range(-1, 2): #nytt
                    if ( #nytt 
                        not (dy == 0 and dx == 0) #nytt
                        and 0 <= (y + dy) < len(grid) #nytt
                        and 0 <= (x + dx) < len(grid[y + dy]) #nytt
                        and grid[y + dy][x + dx]['flower'] #nytt 
                    ): #nytt
                        surrounding_flower_count += 1 #nytt

            if grid[y][x]['flower']:
                draw_cell('flower', x, y)
            elif surrounding_flower_count > 0: #nytt
                draw_cell(str(surrounding_flower_count), x, y) #nytt
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python
import pgzrun
import pygame
import math

# Globala variabler här nedanför
cell_size = 18

grid = []
grid_x_count = 19
grid_y_count = 14

# Funktioner här nedanför


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def on_mouse_up(button):
    # Temporary
    if button == mouse.RIGHT:
        grid[selected_y][selected_x]['flower'] = not grid[selected_y][selected_x]['flower']


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if x == selected_x and y == selected_y:
                if pygame.mouse.get_pressed()[0] == 1:
                    draw_cell('uncovered', x, y)
                else:
                    draw_cell('covered_highlighted', x, y)
            else:
                draw_cell('covered', x, y)

            surrounding_flower_count = 0

            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if (
                        not (dy == 0 and dx == 0)
                        and 0 <= (y + dy) < len(grid)
                        and 0 <= (x + dx) < len(grid[y + dy])
                        and grid[y + dy][x + dx]['flower']
                    ):
                        surrounding_flower_count += 1

            if grid[y][x]['flower']:
                draw_cell('flower', x, y)
            elif surrounding_flower_count > 0:
                draw_cell(str(surrounding_flower_count), x, y)


# Kod för att starta appen
for y in range(grid_y_count):
    grid.append([])
    for x in range(grid_x_count):
        grid[y].append({
            'flower': False
        })

    # Temporary
    grid[0][0]['flower'] = True
    grid[0][1]['flower'] = True


pgzrun.go()  # måste vara sista raden

```
  
</details>

![image](https://user-images.githubusercontent.com/4598641/226451615-217a10c0-cf61-41f0-80fd-df17ef8c238e.png)

## Slumpmässig placering av blommor
En lista skapas som innehåller varje X- och Y-position i rutnätet.


Slumpmässiga positioner tas upprepade gånger bort från den här listan och cellerna på dessa positioner är inställda på att ha en blomma.

```python
import pgzrun
import pygame
import math
import random #nytt 🔔

# Globala variabler här nedanför
cell_size = 18

grid = []
grid_x_count = 19
grid_y_count = 14

possible_flower_positions = [] #nytt 🔔

# etc.

# Kod för att starta appen
for y in range(grid_y_count):
    grid.append([])
    for x in range(grid_x_count):
        grid[y].append({
            'flower': False
        })

for y in range(grid_y_count): #nytt
    for x in range(grid_x_count): #nytt
        possible_flower_positions.append({'x': x, 'y': y}) #nytt 🔔

for flower_index in range(40): #nytt
    position = possible_flower_positions.pop( #nytt
        random.randrange(len(possible_flower_positions))) #nytt 🔔
    grid[position['y']][position['x']]['flower'] = True #nytt 🔔
 
pgzrun.go()  # måste vara sista raden
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python
import pgzrun
import pygame
import math
import random

# Globala variabler här nedanför
cell_size = 18

grid = []
grid_x_count = 19
grid_y_count = 14

possible_flower_positions = []

# Funktioner här nedanför


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def on_mouse_up(button):
    # Temporary
    if button == mouse.RIGHT:
        grid[selected_y][selected_x]['flower'] = not grid[selected_y][selected_x]['flower']


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if x == selected_x and y == selected_y:
                if pygame.mouse.get_pressed()[0] == 1:
                    draw_cell('uncovered', x, y)
                else:
                    draw_cell('covered_highlighted', x, y)
            else:
                draw_cell('covered', x, y)

            surrounding_flower_count = 0

            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if (
                        not (dy == 0 and dx == 0)
                        and 0 <= (y + dy) < len(grid)
                        and 0 <= (x + dx) < len(grid[y + dy])
                        and grid[y + dy][x + dx]['flower']
                    ):
                        surrounding_flower_count += 1

            if grid[y][x]['flower']:
                draw_cell('flower', x, y)
            elif surrounding_flower_count > 0:
                draw_cell(str(surrounding_flower_count), x, y)


# Kod för att starta appen
for y in range(grid_y_count):
    grid.append([])
    for x in range(grid_x_count):
        grid[y].append({
            'flower': False
        })

for y in range(grid_y_count):
    for x in range(grid_x_count):
        possible_flower_positions.append({'x': x, 'y': y})

for flower_index in range(40):
    position = possible_flower_positions.pop(
        random.randrange(len(possible_flower_positions)))
    grid[position['y']][position['x']]['flower'] = True

pgzrun.go()  # måste vara sista raden

```
  
</details>

![image](https://user-images.githubusercontent.com/4598641/226451656-7aac2925-cd35-488f-a397-0a2efc8d269b.png)

## Återställa spelet
En funktion skapas som ställer in spelets initiala tillstånd.

Denna funktion anropas innan spelet börjar och när någon knapp trycks ned.

```python

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python

```
  
</details>

## Att avslöja celler
Cellerna får en ny nyckel för cellens tillstånd. För närvarande är detta bara om cellen är täckt eller avtäckt.

För närvarande, när en cell vänsterklickas är dess tillstånd inställt på " avtäckt" .

Om en cells tillstånd är "avtäckt" ritas den avtäckta bilden istället för den täckta bilden.

```python

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python

```
  
</details>

![image](https://user-images.githubusercontent.com/4598641/226451742-496e7414-d3d4-4be4-b251-df824a393c09.png)


## Översvämningsfyllning: avtäck stapeln
En lista över cellpositioner skapas, och så småningom kommer alla cellpositioner som ska avslöjas att läggas till i denna lista.

För närvarande kommer denna "avtäckstapel" bara att innehålla den valda positionen, så den kommer bara att avslöja den valda cellen som tidigare.

Medan det finns positioner i avtäckningsstacken, tas en position bort från den och cellen vid denna position på rutnätet avtäcks.

```python

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python

```
  
</details>


## Översvämningspåfyllning: lägga till i högen
Varje position i de 8 riktningarna runt varje cell slingras igenom, och om positionen är inuti rutnätet och den är täckt, så läggs den till i avtäckningsstacken.

Detta resulterar i att alla celler blir avslöjade.

```python

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python

```
  
</details>

![image](https://user-images.githubusercontent.com/4598641/226451814-b25ebd8c-a36b-445d-9512-a291112a56f4.png)

## Översvämningsfyllning: med omgivande blommängd
De omgivande cellerna i en position som tagits bort från avtäckningsstacken läggs bara till stapeln om ingen av de omgivande cellerna har blommor.

Att hitta antalet omgivande blommor återanvänds från att rita det, så en funktion skapas.

```python

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python

```
  
</details>

![image](https://user-images.githubusercontent.com/4598641/226451877-3422c1a8-a0ff-49d3-8df1-f46e50c52424.png)


## Rita flaggor och frågetecken
En cells tillstånd kan också vara en flagga eller ett frågetecken.

Om en cells tillstånd är en flagga/frågetecken, ritas flaggan/frågeteckenbilden över cellen.

För att testa detta ändras tillståndet för två celler till att ha en flagga och ett frågetecken.

```python

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python

```
  
</details>


![image](https://user-images.githubusercontent.com/4598641/226451916-0675c6bd-8039-4926-b164-3cf556ff3a08.png)


## Cykelflaggor och frågetecken
Att högerklicka på en cell växlar dess tillstånd genom att det inte finns någonting, en flagga och ett frågetecken.

```python

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python

```
  
</details>

## Förhindra att flaggor avslöjas
Om en cell har en flagga kan den inte avslöjas med ett vänsterklick.

```python

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python

```
  
</details>

## Frågetecken slutar inte fyllas
Positioner läggs till i avtäckningsstacken om cellens tillstånd är täckt eller ett frågetecken (men inte en flagga).

```python

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python

```
  
</details>

## Ändra cellbild när vänster musknapp är nere över flaggan
Om vänster musknapp är nere när musen är på en cell med en flagga, så ritas cellen med den täckta bilden.

```python

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python

```
  
</details>

## Spelet slut
Om en blomma avslöjas är spelet över.

En variabel görs för att lagra om spelet är över eller inte.

För närvarande gör det ingenting att klicka på celler om spelet är över.

```python

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python

```
  
</details>

## Spelet vunnet
Om det inte finns några celler som är täckta och inte har en blomma, är spelet vunnet.

```python

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python

```
  
</details>

## Nytt spel vid nästa klick
Om spelet är över och en musknapp klickas, återställs spelet.

```python

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python

```
  
</details>

## Markera inte när spelet är över
När spelet är över markerar musen inte längre celler.

```python

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python

```
  
</details>


## Göm blommor tills spelet är över
Blommorna dras inte förrän spelet är över.

```python

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python

```
  
</details>


![image](https://user-images.githubusercontent.com/4598641/226452171-3df8c25a-b72c-4d16-9ff4-c654bb0e6db3.png)


## Dölj nummer för täckta celler
Om en cell inte avtäcks, visas inte dess omgivande blommängd.

```python

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python

```
  
</details>

![image](https://user-images.githubusercontent.com/4598641/226452196-f8755175-df82-4650-be3a-73491516082d.png)


## Förhindra att du klickar på blomman vid det första klicket
För att det första klicket inte ska avslöja en blomma, flyttas koden för att placera blommor så att den körs när vänster musknapp klickas, och cellen under muspekaren läggs inte till de möjliga blompositionerna.

En variabel skapas för att lagra om ett klick är det första klicket i spelet.

```python

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python

```
  
</details>





# Källor
https://simplegametutorials.github.io/pygamezero/flowers/
