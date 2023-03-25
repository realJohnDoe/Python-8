# Flowers ⭐⭐⭐
## En handledning för Python och Pygame Zero 1.2

[**Regler**](#regler) [Kontroller](#kontroller)

[**Översikt**](#översikt)

[**Kodning**](#kodning)
[Rita celler](#rita-celler)
&bull; [Markera celler](#markera-celler)
&bull; [Bara celler inom rutnätet ska gå att välja](#bara-celler-inom-rutnätet-ska-gå-att-välja)
&bull; [Markera celler](#markera-celler)
&bull; [Ändra cellens utseende när vänster musknapp klickas](#ändra-cellens-utseende-när-vänster-musknapp-klickas)
&bull; [Rita blommor](#rita-blommor)
&bull; [Förenkla koden](#förenkla-koden)
&bull; [Växla blommor](#växla-blommor)
&bull; [Visa antalet blommor runt cellen](#visa-antalet-blommor-runt-cellen)
&bull; [Slumpmässig placering av blommor](#slumpmässig-placering-av-blommor)
&bull; [Återställa spelet](#återställa-spelet)
&bull; [Att avtäcka celler](#att-avtäcka-celler)
&bull; [En stack som sparar celler som ska avtäckas](#en-stack-som-sparar-celler-som-ska-avtäckas)
&bull; [Lägg till fler celler på stacken](#lägg-till-fler-celler-på-stacken)
&bull; [Håll reda på antalet grannar när vi avtäcker](#håll-reda-på-antalet-grannar-när-vi-avtäcker)
&bull; [Rita flaggor och frågetecken](#rita-flaggor-och-frågetecken)
&bull; [Ändra cellens status mellan blank, flagga och frågetecken](#ändra-cellens-status-mellan-blank-flagga-och-frågetecken)
&bull; [Hindra att flaggade celler avtäcks](#hindra-att-flaggade-celler-avtäcks)
&bull; [Celler med frågetecken får avtäckas](#celler-med-frågetecken-får-avtäckas)
&bull; [Ändra grafiken när vänster musknapp klickar på en flaggad cell](#ändra-grafiken-när-vänster-musknapp-klickar-på-en-flaggad-cell)
&bull; [Slut på spelet](#slut-på-spelet)
&bull; [Att vinna spelet](#att-vinna-spelet)
&bull; [Nytt spel vid nästa klick](#nytt-spel-vid-nästa-klick)
&bull; [Stäng av musklick när spelet är slut](#stäng-av-musklick-när-spelet-är-slut)
&bull; [Göm blommorna tills spelet är slut](#göm-blommorna-tills-spelet-är-slut)
&bull; [Göm antalet blomgrannar för täckta celler](#göm-antalet-blomgrannar-för-täckta-celler)
&bull; [Hindra att man klickar på en blomma vid första klicket](#hindra-att-man-klickar-på-en-blomma-vid-första-klicket)

[**Källor**](#källor)

>Det här projektet använder bilder från [flowers.zip](https://simplegametutorials.github.io/pygamezero/flowers/flowers.zip). 
>De filerna finns redan med i startprojektet på https://replit.com/@RobertStorlind/flowers-starter.

![image](https://user-images.githubusercontent.com/4598641/226450608-0fb4fbf9-c465-4d93-8acd-c3f38ac4225d.png)

# Regler
Spelet börjar med ett rutnät av täckta celler. Under några av cellerna finns blommor. Spelet är över när en cell med blomma avtäcks.

Vänsterklick på en cell avtäcker den. Om ingen av de intilliggande cellerna innehåller blommor, avtäcks de också och för de avtäckta cellerna, om ingen av deras intilliggande celler innehåller blommor, avtäcks de också, och så vidare.

Att högerklicka på en cell växlar mellan en flagga, ett frågetecken eller ingenting. 
- Flaggor förhindrar att en cell avtäckas med ett vänsterklick. 
- Frågetecken är  markeringar som inte påverkar vad som händer när cellen klickas.

Spelet är slut när alla celler utan blommor har avtäckts.

## Kontroller

**Vänsterklick med musen**	Avtäck en cell

**Högerklick med musen** Växla en dold cell mellan att ha en flagga, ett frågetecken eller ingenting.

# Översikt

Cellerna representeras av ordböcker som innehåller ett booleskt värde som anger om den innehåller en blomma eller inte, och ett strängvärde som anger vilken status cellen har. 
Det finns fyra olika statusar: 
1. täckt, 
1. täckt med en flagga, 
1. täckt med ett frågetecken eller
1. avtäckt.

De celler som har blommor är slumpmässigt valda. Den första cellen som klickas utesluts från de möjliga alternativen.

När en cell klickas läggs dess position till i listan "avtäckningsstacken".

Så länge finns något kvar i avtäckningsstacken:
- En position tas bort från slutet av stacken.
- Denna position är inställd på avtäckt.
- Om det inte finns några blommor som omger denna position läggs de omgivande täckta och frågemarkerade positionerna  till avtäckningsstacken. Celler som redan är avtäcka eller har en flagga läggs inte till avtäckningsstacken.

Cellerna ritas genom att sätta ihop följande bilder:

![image](https://user-images.githubusercontent.com/4598641/226450949-d9e02014-22b1-4aac-84ed-d00dfe9f782b.png)

# Kodning
## Rita celler
Den täckta cellbilden ritas för varje cell.

>Om du vill så hittar du bildfilerna som används i den här handledningen genom att ladda ner och packa upp .zip-filen som länkas till högst upp på den här sidan. Det är redan förberett i startprojektet.

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

Detta behöver cellstorleken, så det flyttas till att vara en global variabel.

För närvarande är denna position ritad som text.

Module `pygame` importeras så att vi kan använda `pygame.mouse.get_pos` för att få reda på var muspekaren är.

Matematikmodulen är importerad så vi kan använda `math.floor` för avrundning.

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
            # Borttaget: cell_size = 18
            screen.blit('covered', (x * cell_size, y * cell_size))

    # Tillfälligt
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

![image](https://user-images.githubusercontent.com/4598641/226451363-15f4d3b2-c3f1-4187-9d11-949fd2691b7d.png)

📝 Så här ser koden ut nu:
```python
import pgzrun
import pygame
import math

# Globala variabler här nedanför
cell_size = 18

grid_x_count = 19 #nyrad 🌻
grid_y_count = 14 #nyrad 🌻

# Funktioner här nedanför

def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1: #nyrad 🌻
        selected_x = grid_x_count - 1 #nyrad 🌻
    if selected_y > grid_y_count - 1: #nyrad 🌻
        selected_y = grid_y_count - 1 #nyrad 🌻

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


## Markera celler
Den markerade cellen ritas med grafiken som heter 'covered_highlighted'. Du kan se hur den ser ut i mappen `images` i repl.it, till vänster i fönstret.

✏️ Uppdatera koden för `draw()` och testkör. Ritas markeringen rätt?

```python
def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            if x == selected_x and y == selected_y: #nytt 🌻
                image = 'covered_highlighted' #nytt 🌻
            else: #nytt 🌻
                image = 'covered' #nytt 🌻
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

## Ändra cellens utseende när vänster musknapp klickas
När vänster musknapp klickas, ritas den markerade cellen som en avtäckt cell. 
>Bildfilen heter 'uncovered' och du hittar den i mappen 'images' i repl.it.

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
Ett rutnät skapas för att hålla reda på läget i varje cell.

Varje cell kommer att representeras av en ordbok som lagrar två värden: om den har en blomma och om den är avtäckt/flaggad/frågemarkerad/ingenting.

För närvarande kommer det bara att lagra blomvärdet.

Om en cells "blomma"-nyckel är sann, ritas just nu blombilden över cellbilden. Vi kommer att ändra det sen så klart 🙂

Uppdatera koden och testkör. Ritas blommorna rätt?

```python
grid = [] #nytt 🌻
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

            if grid[y][x]['flower']: #nytt 🌻
                screen.blit('flower', (x * cell_size, y * cell_size)) #nytt 🌻

# Kod för att starta appen
for y in range(grid_y_count): #nytt 🌻
    grid.append([]) #nytt 🌻
    for x in range(grid_x_count): #nytt 🌻
        grid[y].append({ #nytt 🌻
            'flower': False #nytt 🌻
        }) #nytt 🌻

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

## Förenkla koden
Koden för att rita celler och för att rita blomman är samma förutom vilken grafik som ska användas.
Därför gör vi en funktion med bilden och X- och Y-värdena som parametrar.

```python
def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y): #nytt 🌻
                screen.blit(image, (x * cell_size, y * cell_size)) #nytt 🌻

            if x == selected_x and y == selected_y:
                if pygame.mouse.get_pressed()[0] == 1:
                    draw_cell('uncovered', x, y) #nytt 🌻
                else:
                    draw_cell('covered_highlighted', x, y) #nytt 🌻
            else:
                draw_cell('covered', x, y) #nytt 🌻

            if grid[y][x]['flower']:
                draw_cell('flower', x, y) #nytt 🌻
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
För att kunna testa vill vi kunna högerklicka  på en cell för att byta om det ska vara en blomma där eller inte.

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
För att räkna antalet blommor runt en cell, loopar vi igenom de åtta grannarna runt varje cell. 
Om någon av de positionerna är inuti rutnätet och cellen vid den positionen har en blomma, ökar vi antalet blommor med 1.

Om det omgivande antalet blommor är större än 0, så ritar vi rätt nummer (bild) över cellen.

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

            for dy in range(-1, 2): #nytt 🌻
                for dx in range(-1, 2): #nytt 🌻
                    if ( #nytt 🌻
                        not (dy == 0 and dx == 0) #nytt 🌻
                        and 0 <= (y + dy) < len(grid) #nytt 🌻
                        and 0 <= (x + dx) < len(grid[y + dy]) #nytt 🌻
                        and grid[y + dy][x + dx]['flower'] #nytt 🌻
                    ): #nytt 🌻
                        surrounding_flower_count += 1 #nytt 🌻

            if grid[y][x]['flower']:
                draw_cell('flower', x, y)
            elif surrounding_flower_count > 0: #nytt 🌻
                draw_cell(str(surrounding_flower_count), x, y) #nytt 🌻
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

Vi tar ut ett antal slumpmässiga positioner från den listan. 
Cellerna på de positionerna tilldelas en blomma.

```python
import pgzrun
import pygame
import math
import random #nytt 🌻

# Globala variabler här nedanför
cell_size = 18

grid = []
grid_x_count = 19
grid_y_count = 14

possible_flower_positions = [] #nytt 🌻

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
        possible_flower_positions.append({'x': x, 'y': y}) #nytt 🌻

for flower_index in range(40): #nytt
    position = possible_flower_positions.pop( #nytt
        random.randrange(len(possible_flower_positions))) #nytt 🌻
    grid[position['y']][position['x']]['flower'] = True #nytt 🌻
 
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
Vi gör en funktion som heter `reset()`. Den ska ställa in spelets startläge. 
Nästan all kod som just nu ligger längst ner under "Kod för att starta appen" flyttar vi dit.

`reset()` anropas innan spelet börjar och när någon knapp trycks ned.

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

# Funktioner här nedanför

# Ny funktion 🌻
def reset():
    global grid
    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append({
                'flower': False
            })

    possible_flower_positions = []

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            possible_flower_positions.append({'x': x, 'y': y})

    for flower_index in range(40):
        position = possible_flower_positions.pop(
            random.randrange(len(possible_flower_positions)))
        grid[position['y']][position['x']]['flower'] = True
   
# etc.

def on_key_down(): #nyrad 🌻
    reset() #nyrad 🌻

# Kod för att starta appen
reset() #nyrad 🌻

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

# Funktioner här nedanför

def reset():
    global grid
    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append({
                'flower': False
            })

    possible_flower_positions = []

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            possible_flower_positions.append({'x': x, 'y': y})

    for flower_index in range(40):
        position = possible_flower_positions.pop(
            random.randrange(len(possible_flower_positions)))
        grid[position['y']][position['x']]['flower'] = True


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

def on_key_down():
    reset()

# Kod för att starta appen
reset()

pgzrun.go()  # måste vara sista raden
```
  
</details>

## Att avtäcka celler
Varje cell behöver en egenskap som talar om cellens status.
För närvarande är detta bara om cellen är täckt eller avtäckt.

Just nu gör vi så att cellen sätts till "avtäckt" när vi vänsterklickar med musen.

Om en cells status är "avtäckt" ritas den avtäckta bilden istället för den täckta bilden.

```python
def reset():
    global grid

    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append({
                'flower': False,
                'state': 'covered', # 'covered', 'uncovered' #nyrad 🌻
            })

    # etc.

def on_mouse_up(button): # funktionen ändrad
    if button == mouse.LEFT: #nyrad 🌻
        grid[selected_y][selected_x]['state'] = 'uncovered' #nyrad 🌻

def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if grid[y][x]['state'] == 'uncovered': #nyrad 🌻
                draw_cell('uncovered', x, y) #nyrad 🌻
            else: #nyrad 🌻 Kom ihåg att dra in raderna under
                if x == selected_x and y == selected_y:
                    if pygame.mouse.get_pressed()[0] == 1:
                        draw_cell('uncovered', x, y)
                    else:
                        draw_cell('covered_highlighted', x, y)
                else:
                    draw_cell('covered', x, y)

            # etc.
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

# Funktioner här nedanför

def reset():
    global grid
    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append({
                'flower': False,
                'state': 'covered', # 'covered', 'uncovered'
            })

    possible_flower_positions = []

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            possible_flower_positions.append({'x': x, 'y': y})

    for flower_index in range(40):
        position = possible_flower_positions.pop(
            random.randrange(len(possible_flower_positions)))
        grid[position['y']][position['x']]['flower'] = True


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
    if button == mouse.LEFT:
        grid[selected_y][selected_x]['state'] = 'uncovered'

def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if grid[y][x]['state'] == 'uncovered':
                draw_cell('uncovered', x, y)
            else:
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

def on_key_down():
    reset()

# Kod för att starta appen
reset()

pgzrun.go()  # måste vara sista raden
```
  
</details>

![image](https://user-images.githubusercontent.com/4598641/226451742-496e7414-d3d4-4be4-b251-df824a393c09.png)


## En stack som sparar celler som ska avtäckas

En lista över cellpositioner skapas. Så småningom kommer alla cellpositioner som ska avtäckas att läggas till i denna lista.

För närvarande kommer denna "avtäckningsstack" bara att innehålla den valda positionen, så den kommer bara att avtäcka den valda cellen som tidigare.

Medan det finns positioner i avtäckningsstacken, tas en position bort från den och cellen vid denna position på rutnätet avtäcks.

✏️ Uppdatera funktionen `on_mouse_up()` och testkör vad som händer när du klickar!

```python
def on_mouse_up(button):
    if button == mouse.LEFT:
        stack = [
            {
                'x': selected_x,
                'y': selected_y,
            }
        ]

        while len(stack) > 0:
            current = stack.pop()
            x = current['x']
            y = current['y']

            grid[y][x]['state'] = 'uncovered'
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

# Funktioner här nedanför


def reset():
    global grid
    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append({
                'flower': False,
                'state': 'covered',  # 'covered', 'uncovered'
            })

    possible_flower_positions = []

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            possible_flower_positions.append({'x': x, 'y': y})

    for flower_index in range(40):
        position = possible_flower_positions.pop(
            random.randrange(len(possible_flower_positions)))
        grid[position['y']][position['x']]['flower'] = True


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
    if button == mouse.LEFT:
        stack = [
            {
                'x': selected_x,
                'y': selected_y,
            }
        ]

        while len(stack) > 0:
            current = stack.pop()
            x = current['x']
            y = current['y']

            grid[y][x]['state'] = 'uncovered'


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if grid[y][x]['state'] == 'uncovered':
                draw_cell('uncovered', x, y)
            else:
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


def on_key_down():
    reset()


# Kod för att starta appen
reset()

pgzrun.go()  # måste vara sista raden
```
  
</details>


## Lägg till fler celler på stacken
Varje position i de åtta riktningarna runt varje cell loopas igenom.
Om en position är inuti rutnätet och den är täckt så läggs den till i avtäckningsstacken.

Detta gör att alla celler blir avtäckta. Vi ska rätta till det problemet lite senare.

✏️ Uppdatera `on_mouse_up()` och testa igen.

```python
def on_mouse_up(button):
    if button == mouse.LEFT:
        stack = [
            {
                'x': selected_x,
                'y': selected_y,
            }
        ]

        while len(stack) > 0:
            current = stack.pop()
            x = current['x']
            y = current['y']

            grid[y][x]['state'] = 'uncovered'

            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if (
                        not (dy == 0 and dx == 0)
                        and 0 <= (y + dy) < len(grid)
                        and 0 <= (x + dx) < len(grid[y + dy])
                        and grid[y + dy][x + dx]['state'] == 'covered'
                    ):
                        stack.append({
                            'x': x + dx,
                            'y': y + dy,
                        })
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

# Funktioner här nedanför


def reset():
    global grid
    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append({
                'flower': False,
                'state': 'covered',  # 'covered', 'uncovered'
            })

    possible_flower_positions = []

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            possible_flower_positions.append({'x': x, 'y': y})

    for flower_index in range(40):
        position = possible_flower_positions.pop(
            random.randrange(len(possible_flower_positions)))
        grid[position['y']][position['x']]['flower'] = True


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
    if button == mouse.LEFT:
        stack = [
            {
                'x': selected_x,
                'y': selected_y,
            }
        ]

        while len(stack) > 0:
            current = stack.pop()
            x = current['x']
            y = current['y']

            grid[y][x]['state'] = 'uncovered'

            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if (
                        not (dy == 0 and dx == 0)
                        and 0 <= (y + dy) < len(grid)
                        and 0 <= (x + dx) < len(grid[y + dy])
                        and grid[y + dy][x + dx]['state'] == 'covered'
                    ):
                        stack.append({
                            'x': x + dx,
                            'y': y + dy,
                        })

def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if grid[y][x]['state'] == 'uncovered':
                draw_cell('uncovered', x, y)
            else:
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


def on_key_down():
    reset()


# Kod för att starta appen
reset()

pgzrun.go()  # måste vara sista raden
```
  
</details>

![image](https://user-images.githubusercontent.com/4598641/226451814-b25ebd8c-a36b-445d-9512-a291112a56f4.png)

## Håll reda på antalet grannar när vi avtäcker

De omgivande cellerna i en position som har tagits bort från avtäckningsstacken läggs bara till i stacken om ingen av de omgivande cellerna har blommor.

Vi behöver kunna räkna ut antalet omgivande blommor på flera ställen. Därför gör vi det till en funktion.

```python
def get_surrounding_flower_count(x, y):
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

    return surrounding_flower_count

def on_mouse_up(button):
    if button == mouse.LEFT:

        stack = [
            {
                'x': selected_x,
                'y': selected_y,
            }
        ]

        while len(stack) > 0:
            current = stack.pop()
            x = current['x']
            y = current['y']

            grid[y][x]['state'] = 'uncovered'

            if get_surrounding_flower_count(x, y) == 0:
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if (
                            not (dy == 0 and dx == 0)
                            and 0 <= (y + dy) < len(grid)
                            and 0 <= (x + dx) < len(grid[y + dy])
                            and grid[y + dy][x + dx]['state'] == 'covered'
                        ):
                            stack.append({
                                'x': x + dx,
                                'y': y + dy,
                            })

def draw():
    # etc.

            if grid[y][x]['flower']:
                draw_cell('flower', x, y)
            elif get_surrounding_flower_count(x, y) > 0:
                draw_cell(str(get_surrounding_flower_count(x, y)), x, y)
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

# Funktioner här nedanför


def reset():
    global grid
    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append({
                'flower': False,
                'state': 'covered',  # 'covered', 'uncovered'
            })

    possible_flower_positions = []

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            possible_flower_positions.append({'x': x, 'y': y})

    for flower_index in range(40):
        position = possible_flower_positions.pop(
            random.randrange(len(possible_flower_positions)))
        grid[position['y']][position['x']]['flower'] = True


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def get_surrounding_flower_count(x, y):
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

    return surrounding_flower_count


def on_mouse_up(button):
    if button == mouse.LEFT:

        stack = [
            {
                'x': selected_x,
                'y': selected_y,
            }
        ]

        while len(stack) > 0:
            current = stack.pop()
            x = current['x']
            y = current['y']

            grid[y][x]['state'] = 'uncovered'

            if get_surrounding_flower_count(x, y) == 0:
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if (
                            not (dy == 0 and dx == 0)
                            and 0 <= (y + dy) < len(grid)
                            and 0 <= (x + dx) < len(grid[y + dy])
                            and grid[y + dy][x + dx]['state'] == 'covered'
                        ):
                            stack.append({
                                'x': x + dx,
                                'y': y + dy,
                            })


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if grid[y][x]['state'] == 'uncovered':
                draw_cell('uncovered', x, y)
            else:
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
            elif get_surrounding_flower_count(x, y) > 0:
                draw_cell(str(get_surrounding_flower_count(x, y)), x, y)


def on_key_down():
    reset()


# Kod för att starta appen
reset()

pgzrun.go()  # måste vara sista raden

```
  
</details>

![image](https://user-images.githubusercontent.com/4598641/226451877-3422c1a8-a0ff-49d3-8df1-f46e50c52424.png)


## Rita flaggor och frågetecken
En cells status kan också vara en flagga eller ett frågetecken.

Om en cells status är flagga eller frågetecken, ritas flaggan-/frågeteckenbilden över cellen.

För att testa detta ändras status för två celler till att ha en flagga och ett frågetecken.

```python
def reset():
    # etc.

            grid[y].append({
                'flower': False,
                'state': 'covered', # 'covered', 'uncovered', 'flag', 'question'
            })

def draw():
    # etc.

            if grid[y][x]['flower']:
                draw_cell('flower', x, y)
            elif get_surrounding_flower_count(x, y) > 0:
                draw_cell(str(get_surrounding_flower_count(x, y)), x, y)

            if grid[y][x]['state'] == 'flag':
                draw_cell('flag', x, y)
            elif grid[y][x]['state'] == 'question':
                draw_cell('question', x, y)

# etc.

# Kod för att starta appen
reset()
grid[0][0]['state'] = 'flag'
grid[0][1]['state'] = 'question'

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

# Funktioner här nedanför


def reset():
    global grid
    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append({
                'flower': False,
                'state': 'covered',  # 'covered', 'uncovered', 'flag', 'question'
            })

    possible_flower_positions = []

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            possible_flower_positions.append({'x': x, 'y': y})

    for flower_index in range(40):
        position = possible_flower_positions.pop(
            random.randrange(len(possible_flower_positions)))
        grid[position['y']][position['x']]['flower'] = True


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def get_surrounding_flower_count(x, y):
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

    return surrounding_flower_count


def on_mouse_up(button):
    if button == mouse.LEFT:

        stack = [
            {
                'x': selected_x,
                'y': selected_y,
            }
        ]

        while len(stack) > 0:
            current = stack.pop()
            x = current['x']
            y = current['y']

            grid[y][x]['state'] = 'uncovered'

            if get_surrounding_flower_count(x, y) == 0:
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if (
                            not (dy == 0 and dx == 0)
                            and 0 <= (y + dy) < len(grid)
                            and 0 <= (x + dx) < len(grid[y + dy])
                            and grid[y + dy][x + dx]['state'] == 'covered'
                        ):
                            stack.append({
                                'x': x + dx,
                                'y': y + dy,
                            })


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if grid[y][x]['state'] == 'uncovered':
                draw_cell('uncovered', x, y)
            else:
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
            elif get_surrounding_flower_count(x, y) > 0:
                draw_cell(str(get_surrounding_flower_count(x, y)), x, y)

            if grid[y][x]['state'] == 'flag':
                draw_cell('flag', x, y)
            elif grid[y][x]['state'] == 'question':
                draw_cell('question', x, y)


def on_key_down():
    reset()


# Kod för att starta appen
reset()
grid[0][0]['state'] = 'flag'
grid[0][1]['state'] = 'question'

pgzrun.go()  # måste vara sista raden
  
```
  
</details>


![image](https://user-images.githubusercontent.com/4598641/226451916-0675c6bd-8039-4926-b164-3cf556ff3a08.png)


## Ändra cellens status mellan blank, flagga och frågetecken
När man högerklickar på en cell ska statusen ändras mellan blank, flagga och frågetecken.

```python
def on_mouse_up(button):
    if button == mouse.LEFT:
        # etc.

    elif button == mouse.RIGHT:
        if grid[selected_y][selected_x]['state'] == 'covered':
            grid[selected_y][selected_x]['state'] = 'flag'

        elif grid[selected_y][selected_x]['state'] == 'flag':
            grid[selected_y][selected_x]['state'] = 'question'

        elif grid[selected_y][selected_x]['state'] == 'question':
            grid[selected_y][selected_x]['state'] = 'covered'

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

# Funktioner här nedanför


def reset():
    global grid
    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append({
                'flower': False,
                'state': 'covered',  # 'covered', 'uncovered', 'flag', 'question'
            })

    possible_flower_positions = []

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            possible_flower_positions.append({'x': x, 'y': y})

    for flower_index in range(40):
        position = possible_flower_positions.pop(
            random.randrange(len(possible_flower_positions)))
        grid[position['y']][position['x']]['flower'] = True


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def get_surrounding_flower_count(x, y):
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

    return surrounding_flower_count


def on_mouse_up(button):
    if button == mouse.LEFT:

        stack = [
            {
                'x': selected_x,
                'y': selected_y,
            }
        ]

        while len(stack) > 0:
            current = stack.pop()
            x = current['x']
            y = current['y']

            grid[y][x]['state'] = 'uncovered'

            if get_surrounding_flower_count(x, y) == 0:
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if (
                            not (dy == 0 and dx == 0)
                            and 0 <= (y + dy) < len(grid)
                            and 0 <= (x + dx) < len(grid[y + dy])
                            and grid[y + dy][x + dx]['state'] == 'covered'
                        ):
                            stack.append({
                                'x': x + dx,
                                'y': y + dy,
                            })

    elif button == mouse.RIGHT:
        if grid[selected_y][selected_x]['state'] == 'covered':
            grid[selected_y][selected_x]['state'] = 'flag'

        elif grid[selected_y][selected_x]['state'] == 'flag':
            grid[selected_y][selected_x]['state'] = 'question'

        elif grid[selected_y][selected_x]['state'] == 'question':
            grid[selected_y][selected_x]['state'] = 'covered'


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if grid[y][x]['state'] == 'uncovered':
                draw_cell('uncovered', x, y)
            else:
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
            elif get_surrounding_flower_count(x, y) > 0:
                draw_cell(str(get_surrounding_flower_count(x, y)), x, y)

            if grid[y][x]['state'] == 'flag':
                draw_cell('flag', x, y)
            elif grid[y][x]['state'] == 'question':
                draw_cell('question', x, y)


def on_key_down():
    reset()


# Kod för att starta appen
reset()
grid[0][0]['state'] = 'flag'
grid[0][1]['state'] = 'question'

pgzrun.go()  # måste vara sista raden
```
  
</details>

## Hindra att flaggade celler avtäcks
Om en cell har en flagga ska den inte kunna avtäckas med ett vänsterklick.

```python
def on_mouse_up(button):
    if button == mouse.LEFT and grid[selected_y][selected_x]['state'] != 'flag':
        # etc.
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

# Funktioner här nedanför


def reset():
    global grid
    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append({
                'flower': False,
                'state': 'covered',  # 'covered', 'uncovered', 'flag', 'question'
            })

    possible_flower_positions = []

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            possible_flower_positions.append({'x': x, 'y': y})

    for flower_index in range(40):
        position = possible_flower_positions.pop(
            random.randrange(len(possible_flower_positions)))
        grid[position['y']][position['x']]['flower'] = True


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def get_surrounding_flower_count(x, y):
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

    return surrounding_flower_count


def on_mouse_up(button):
    if button == mouse.LEFT and grid[selected_y][selected_x]['state'] != 'flag':

        stack = [
            {
                'x': selected_x,
                'y': selected_y,
            }
        ]

        while len(stack) > 0:
            current = stack.pop()
            x = current['x']
            y = current['y']

            grid[y][x]['state'] = 'uncovered'

            if get_surrounding_flower_count(x, y) == 0:
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if (
                            not (dy == 0 and dx == 0)
                            and 0 <= (y + dy) < len(grid)
                            and 0 <= (x + dx) < len(grid[y + dy])
                            and grid[y + dy][x + dx]['state'] == 'covered'
                        ):
                            stack.append({
                                'x': x + dx,
                                'y': y + dy,
                            })

    elif button == mouse.RIGHT:
        if grid[selected_y][selected_x]['state'] == 'covered':
            grid[selected_y][selected_x]['state'] = 'flag'

        elif grid[selected_y][selected_x]['state'] == 'flag':
            grid[selected_y][selected_x]['state'] = 'question'

        elif grid[selected_y][selected_x]['state'] == 'question':
            grid[selected_y][selected_x]['state'] = 'covered'


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if grid[y][x]['state'] == 'uncovered':
                draw_cell('uncovered', x, y)
            else:
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
            elif get_surrounding_flower_count(x, y) > 0:
                draw_cell(str(get_surrounding_flower_count(x, y)), x, y)

            if grid[y][x]['state'] == 'flag':
                draw_cell('flag', x, y)
            elif grid[y][x]['state'] == 'question':
                draw_cell('question', x, y)


def on_key_down():
    reset()


# Kod för att starta appen
reset()
grid[0][0]['state'] = 'flag'
grid[0][1]['state'] = 'question'

pgzrun.go()  # måste vara sista raden

```
  
</details>

## Celler med frågetecken får avtäckas
Positioner läggs till i avtäckningsstacken om cellens status är täckt eller ett frågetecken. 
Celler som är flaggade avtäcks inte automatiskt.

```python
def on_mouse_up(button):
    # etc.

            if get_surrounding_flower_count(x, y) == 0:
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if (
                            not (dy == 0 and dx == 0)
                            and 0 <= (y + dy) < len(grid)
                            and 0 <= (x + dx) < len(grid[y + dy])
                            and grid[y + dy][x + dx]['state'] in ('covered', 'question')
                        ):
                            stack.append({
                                'x': x + dx,
                                'y': y + dy,
                            })

    # etc.
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

# Funktioner här nedanför


def reset():
    global grid
    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append({
                'flower': False,
                'state': 'covered',  # 'covered', 'uncovered', 'flag', 'question'
            })

    possible_flower_positions = []

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            possible_flower_positions.append({'x': x, 'y': y})

    for flower_index in range(40):
        position = possible_flower_positions.pop(
            random.randrange(len(possible_flower_positions)))
        grid[position['y']][position['x']]['flower'] = True


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def get_surrounding_flower_count(x, y):
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

    return surrounding_flower_count


def on_mouse_up(button):
    if button == mouse.LEFT and grid[selected_y][selected_x]['state'] != 'flag':

        stack = [
            {
                'x': selected_x,
                'y': selected_y,
            }
        ]

        while len(stack) > 0:
            current = stack.pop()
            x = current['x']
            y = current['y']

            grid[y][x]['state'] = 'uncovered'

            if get_surrounding_flower_count(x, y) == 0:
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if (
                            not (dy == 0 and dx == 0)
                            and 0 <= (y + dy) < len(grid)
                            and 0 <= (x + dx) < len(grid[y + dy])
                            and grid[y + dy][x + dx]['state'] in ('covered', 'question')
                        ):
                            stack.append({
                                'x': x + dx,
                                'y': y + dy,
                            })

    elif button == mouse.RIGHT:
        if grid[selected_y][selected_x]['state'] == 'covered':
            grid[selected_y][selected_x]['state'] = 'flag'

        elif grid[selected_y][selected_x]['state'] == 'flag':
            grid[selected_y][selected_x]['state'] = 'question'

        elif grid[selected_y][selected_x]['state'] == 'question':
            grid[selected_y][selected_x]['state'] = 'covered'


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if grid[y][x]['state'] == 'uncovered':
                draw_cell('uncovered', x, y)
            else:
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
            elif get_surrounding_flower_count(x, y) > 0:
                draw_cell(str(get_surrounding_flower_count(x, y)), x, y)

            if grid[y][x]['state'] == 'flag':
                draw_cell('flag', x, y)
            elif grid[y][x]['state'] == 'question':
                draw_cell('question', x, y)


def on_key_down():
    reset()


# Kod för att starta appen
reset()
grid[0][0]['state'] = 'flag'
grid[0][1]['state'] = 'question'

pgzrun.go()  # måste vara sista raden

```
  
</details>

## Ändra grafiken när vänster musknapp klickar på en flaggad cell
Om man klickar med vänster musknapp på en flaggad cell, så ritas cellen med den täckta bilden.

```python
def draw():
    # etc.

                    if pygame.mouse.get_pressed()[0] == 1:
                        if grid[y][x]['state'] == 'flag':
                            draw_cell('covered', x, y)
                        else:
                            draw_cell('uncovered', x, y)
                    else:
                        draw_cell('covered_highlighted', x, y)
    # etc.
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

# Funktioner här nedanför


def reset():
    global grid
    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append({
                'flower': False,
                'state': 'covered',  # 'covered', 'uncovered', 'flag', 'question'
            })

    possible_flower_positions = []

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            possible_flower_positions.append({'x': x, 'y': y})

    for flower_index in range(40):
        position = possible_flower_positions.pop(
            random.randrange(len(possible_flower_positions)))
        grid[position['y']][position['x']]['flower'] = True


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def get_surrounding_flower_count(x, y):
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

    return surrounding_flower_count


def on_mouse_up(button):
    if button == mouse.LEFT and grid[selected_y][selected_x]['state'] != 'flag':

        stack = [
            {
                'x': selected_x,
                'y': selected_y,
            }
        ]

        while len(stack) > 0:
            current = stack.pop()
            x = current['x']
            y = current['y']

            grid[y][x]['state'] = 'uncovered'

            if get_surrounding_flower_count(x, y) == 0:
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if (
                            not (dy == 0 and dx == 0)
                            and 0 <= (y + dy) < len(grid)
                            and 0 <= (x + dx) < len(grid[y + dy])
                            and grid[y + dy][x + dx]['state'] in ('covered', 'question')
                        ):
                            stack.append({
                                'x': x + dx,
                                'y': y + dy,
                            })

    elif button == mouse.RIGHT:
        if grid[selected_y][selected_x]['state'] == 'covered':
            grid[selected_y][selected_x]['state'] = 'flag'

        elif grid[selected_y][selected_x]['state'] == 'flag':
            grid[selected_y][selected_x]['state'] = 'question'

        elif grid[selected_y][selected_x]['state'] == 'question':
            grid[selected_y][selected_x]['state'] = 'covered'


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if grid[y][x]['state'] == 'uncovered':
                draw_cell('uncovered', x, y)
            else:
                if x == selected_x and y == selected_y:
                    if pygame.mouse.get_pressed()[0] == 1:
                        if grid[y][x]['state'] == 'flag':
                            draw_cell('covered', x, y)
                        else:
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
            elif get_surrounding_flower_count(x, y) > 0:
                draw_cell(str(get_surrounding_flower_count(x, y)), x, y)

            if grid[y][x]['state'] == 'flag':
                draw_cell('flag', x, y)
            elif grid[y][x]['state'] == 'question':
                draw_cell('question', x, y)


def on_key_down():
    reset()


# Kod för att starta appen
reset()
grid[0][0]['state'] = 'flag'
grid[0][1]['state'] = 'question'

pgzrun.go()  # måste vara sista raden

```
  
</details>

## Slut på spelet
Om en blomma avtäcks är spelet över.

Vi behöver en variabel för att hålla reda på om spelet är över eller inte.

För närvarande kan man klicka på celler även när spelet är slut.

```python
def reset():
    global grid, game_over # ändrad

    # etc.

    game_over = False # sista raden i funktionen

def on_mouse_up(button):
    global game_over # ny rad

    if game_over: # ny rad
        return # ny rad

    if button == mouse.LEFT and grid[selected_y][selected_x]['state'] != 'flag':
        if grid[selected_y][selected_x]['flower']: # ny rad
            grid[selected_y][selected_x]['state'] = 'uncovered' # ny rad
            game_over = True # ny rad
        else: # ny rad. Kom ihåg att dra in raderna här under ändra ner till "elif"
            stack = [
                {
                    'x': selected_x,
                    'y': selected_y,
                }
            ]
            # etc.
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

# Funktioner här nedanför


def reset():
    global grid, game_over
    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append({
                'flower': False,
                'state': 'covered',  # 'covered', 'uncovered', 'flag', 'question'
            })

    possible_flower_positions = []

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            possible_flower_positions.append({'x': x, 'y': y})

    for flower_index in range(40):
        position = possible_flower_positions.pop(
            random.randrange(len(possible_flower_positions)))
        grid[position['y']][position['x']]['flower'] = True

    game_over = False


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def get_surrounding_flower_count(x, y):
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

    return surrounding_flower_count


def on_mouse_up(button):
    global game_over

    if game_over:
        return

    if button == mouse.LEFT and grid[selected_y][selected_x]['state'] != 'flag':
        if grid[selected_y][selected_x]['flower']:
            grid[selected_y][selected_x]['state'] = 'uncovered'
            game_over = True
        else:
            stack = [
                {
                    'x': selected_x,
                    'y': selected_y,
                }
            ]

            while len(stack) > 0:
                current = stack.pop()
                x = current['x']
                y = current['y']

                grid[y][x]['state'] = 'uncovered'

                if get_surrounding_flower_count(x, y) == 0:
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            if (
                                not (dy == 0 and dx == 0)
                                and 0 <= (y + dy) < len(grid)
                                and 0 <= (x + dx) < len(grid[y + dy])
                                and grid[y + dy][x + dx]['state'] in ('covered', 'question')
                            ):
                                stack.append({
                                    'x': x + dx,
                                    'y': y + dy,
                                })

    elif button == mouse.RIGHT:
        if grid[selected_y][selected_x]['state'] == 'covered':
            grid[selected_y][selected_x]['state'] = 'flag'

        elif grid[selected_y][selected_x]['state'] == 'flag':
            grid[selected_y][selected_x]['state'] = 'question'

        elif grid[selected_y][selected_x]['state'] == 'question':
            grid[selected_y][selected_x]['state'] = 'covered'


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if grid[y][x]['state'] == 'uncovered':
                draw_cell('uncovered', x, y)
            else:
                if x == selected_x and y == selected_y:
                    if pygame.mouse.get_pressed()[0] == 1:
                        if grid[y][x]['state'] == 'flag':
                            draw_cell('covered', x, y)
                        else:
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
            elif get_surrounding_flower_count(x, y) > 0:
                draw_cell(str(get_surrounding_flower_count(x, y)), x, y)

            if grid[y][x]['state'] == 'flag':
                draw_cell('flag', x, y)
            elif grid[y][x]['state'] == 'question':
                draw_cell('question', x, y)


def on_key_down():
    reset()


# Kod för att starta appen
reset()
grid[0][0]['state'] = 'flag'
grid[0][1]['state'] = 'question'

pgzrun.go()  # måste vara sista raden

```
  
</details>

## Att vinna spelet
Om det inte finns några celler som är täckta och inte har en blomma, har spelaren vunnit.

```python
def on_mouse_up(button):
   # etc. 
                while len(stack) > 0:
                    current = stack.pop()
                    x = current['x']
                    y = current['y']

                    grid[y][x]['state'] = 'uncovered'

                    if get_surrounding_flower_count(x, y) == 0:
                        for dy in range(-1, 2):
                            for dx in range(-1, 2):
                                if (
                                    not (dy == 0 and dx == 0)
                                    and 0 <= (y + dy) < len(grid)
                                    and 0 <= (x + dx) < len(grid[y + dy])
                                    and grid[y + dy][x + dx]['state'] in ('covered', 'question')
                                ):
                                    stack.append({
                                        'x': x + dx,
                                        'y': y + dy,
                                    })

                complete = True # ny rad

                for y in range(grid_y_count): # ny rad
                    for x in range(grid_x_count): # ny rad
                        if grid[y][x]['state'] != 'uncovered' and not grid[y][x]['flower']: # ny rad
                            complete = False # ny rad

                if complete: # ny rad
                    game_over = True # ny rad

```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>

```python

```
  
</details>

## Nytt spel vid nästa klick
Om spelet är slut och en musknapp klickas, återställs spelet.

```python
def on_mouse_up(button):
    global game_over

    if game_over:
        reset() # ny rad
        return
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

# Funktioner här nedanför


def reset():
    global grid, game_over
    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append({
                'flower': False,
                'state': 'covered',  # 'covered', 'uncovered', 'flag', 'question'
            })

    possible_flower_positions = []

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            possible_flower_positions.append({'x': x, 'y': y})

    for flower_index in range(40):
        position = possible_flower_positions.pop(
            random.randrange(len(possible_flower_positions)))
        grid[position['y']][position['x']]['flower'] = True

    game_over = False


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def get_surrounding_flower_count(x, y):
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

    return surrounding_flower_count


def on_mouse_up(button):
    global game_over

    if game_over:
        reset()
        return

    if button == mouse.LEFT and grid[selected_y][selected_x]['state'] != 'flag':
        if grid[selected_y][selected_x]['flower']:
            grid[selected_y][selected_x]['state'] = 'uncovered'
            game_over = True
        else:
            stack = [
                {
                    'x': selected_x,
                    'y': selected_y,
                }
            ]

            while len(stack) > 0:
                current = stack.pop()
                x = current['x']
                y = current['y']

                grid[y][x]['state'] = 'uncovered'

                if get_surrounding_flower_count(x, y) == 0:
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            if (
                                not (dy == 0 and dx == 0)
                                and 0 <= (y + dy) < len(grid)
                                and 0 <= (x + dx) < len(grid[y + dy])
                                and grid[y + dy][x + dx]['state'] in ('covered', 'question')
                            ):
                                stack.append({
                                    'x': x + dx,
                                    'y': y + dy,
                                })
            complete = True

            for y in range(grid_y_count):
                for x in range(grid_x_count):
                    if grid[y][x]['state'] != 'uncovered' and not grid[y][x]['flower']:
                        complete = False

            if complete:
                game_over = True

    elif button == mouse.RIGHT:
        if grid[selected_y][selected_x]['state'] == 'covered':
            grid[selected_y][selected_x]['state'] = 'flag'

        elif grid[selected_y][selected_x]['state'] == 'flag':
            grid[selected_y][selected_x]['state'] = 'question'

        elif grid[selected_y][selected_x]['state'] == 'question':
            grid[selected_y][selected_x]['state'] = 'covered'


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if grid[y][x]['state'] == 'uncovered':
                draw_cell('uncovered', x, y)
            else:
                if x == selected_x and y == selected_y:
                    if pygame.mouse.get_pressed()[0] == 1:
                        if grid[y][x]['state'] == 'flag':
                            draw_cell('covered', x, y)
                        else:
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
            elif get_surrounding_flower_count(x, y) > 0:
                draw_cell(str(get_surrounding_flower_count(x, y)), x, y)

            if grid[y][x]['state'] == 'flag':
                draw_cell('flag', x, y)
            elif grid[y][x]['state'] == 'question':
                draw_cell('question', x, y)


def on_key_down():
    reset()


# Kod för att starta appen
reset()
grid[0][0]['state'] = 'flag'
grid[0][1]['state'] = 'question'

pgzrun.go()  # måste vara sista raden

```
  
</details>

## Stäng av musklick spelet är slut
När spelet är slut ska musen inte markera cellerna längre.

```python
def draw():
    # etc.

            if grid[y][x]['state'] == 'uncovered':
                draw_cell('uncovered', x, y)
            else:
                if x == selected_x and y == selected_y and not game_over: # ändrad

    # etc.
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

# Funktioner här nedanför


def reset():
    global grid, game_over
    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append({
                'flower': False,
                'state': 'covered',  # 'covered', 'uncovered', 'flag', 'question'
            })

    possible_flower_positions = []

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            possible_flower_positions.append({'x': x, 'y': y})

    for flower_index in range(40):
        position = possible_flower_positions.pop(
            random.randrange(len(possible_flower_positions)))
        grid[position['y']][position['x']]['flower'] = True

    game_over = False


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def get_surrounding_flower_count(x, y):
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

    return surrounding_flower_count


def on_mouse_up(button):
    global game_over

    if game_over:
        reset()
        return

    if button == mouse.LEFT and grid[selected_y][selected_x]['state'] != 'flag':
        if grid[selected_y][selected_x]['flower']:
            grid[selected_y][selected_x]['state'] = 'uncovered'
            game_over = True
        else:
            stack = [
                {
                    'x': selected_x,
                    'y': selected_y,
                }
            ]

            while len(stack) > 0:
                current = stack.pop()
                x = current['x']
                y = current['y']

                grid[y][x]['state'] = 'uncovered'

                if get_surrounding_flower_count(x, y) == 0:
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            if (
                                not (dy == 0 and dx == 0)
                                and 0 <= (y + dy) < len(grid)
                                and 0 <= (x + dx) < len(grid[y + dy])
                                and grid[y + dy][x + dx]['state'] in ('covered', 'question')
                            ):
                                stack.append({
                                    'x': x + dx,
                                    'y': y + dy,
                                })
            complete = True

            for y in range(grid_y_count):
                for x in range(grid_x_count):
                    if grid[y][x]['state'] != 'uncovered' and not grid[y][x]['flower']:
                        complete = False

            if complete:
                game_over = True

    elif button == mouse.RIGHT:
        if grid[selected_y][selected_x]['state'] == 'covered':
            grid[selected_y][selected_x]['state'] = 'flag'

        elif grid[selected_y][selected_x]['state'] == 'flag':
            grid[selected_y][selected_x]['state'] = 'question'

        elif grid[selected_y][selected_x]['state'] == 'question':
            grid[selected_y][selected_x]['state'] = 'covered'


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if grid[y][x]['state'] == 'uncovered':
                draw_cell('uncovered', x, y)
            else:
                if x == selected_x and y == selected_y and not game_over:
                    if pygame.mouse.get_pressed()[0] == 1:
                        if grid[y][x]['state'] == 'flag':
                            draw_cell('covered', x, y)
                        else:
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
            elif get_surrounding_flower_count(x, y) > 0:
                draw_cell(str(get_surrounding_flower_count(x, y)), x, y)

            if grid[y][x]['state'] == 'flag':
                draw_cell('flag', x, y)
            elif grid[y][x]['state'] == 'question':
                draw_cell('question', x, y)


def on_key_down():
    reset()


# Kod för att starta appen
reset()
grid[0][0]['state'] = 'flag'
grid[0][1]['state'] = 'question'

pgzrun.go()  # måste vara sista raden

```
  
</details>


## Göm blommorna tills spelet är slut
Vi ska inte rita några blommor förrän spelet är slut.

```python
def draw():
    # etc.
            if grid[y][x]['flower'] and game_over: # ändrad
                draw_cell('flower', x, y)

    # etc.
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

# Funktioner här nedanför


def reset():
    global grid, game_over
    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append({
                'flower': False,
                'state': 'covered',  # 'covered', 'uncovered', 'flag', 'question'
            })

    possible_flower_positions = []

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            possible_flower_positions.append({'x': x, 'y': y})

    for flower_index in range(40):
        position = possible_flower_positions.pop(
            random.randrange(len(possible_flower_positions)))
        grid[position['y']][position['x']]['flower'] = True

    game_over = False


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def get_surrounding_flower_count(x, y):
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

    return surrounding_flower_count


def on_mouse_up(button):
    global game_over

    if game_over:
        reset()
        return

    if button == mouse.LEFT and grid[selected_y][selected_x]['state'] != 'flag':
        if grid[selected_y][selected_x]['flower']:
            grid[selected_y][selected_x]['state'] = 'uncovered'
            game_over = True
        else:
            stack = [
                {
                    'x': selected_x,
                    'y': selected_y,
                }
            ]

            while len(stack) > 0:
                current = stack.pop()
                x = current['x']
                y = current['y']

                grid[y][x]['state'] = 'uncovered'

                if get_surrounding_flower_count(x, y) == 0:
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            if (
                                not (dy == 0 and dx == 0)
                                and 0 <= (y + dy) < len(grid)
                                and 0 <= (x + dx) < len(grid[y + dy])
                                and grid[y + dy][x + dx]['state'] in ('covered', 'question')
                            ):
                                stack.append({
                                    'x': x + dx,
                                    'y': y + dy,
                                })
            complete = True

            for y in range(grid_y_count):
                for x in range(grid_x_count):
                    if grid[y][x]['state'] != 'uncovered' and not grid[y][x]['flower']:
                        complete = False

            if complete:
                game_over = True

    elif button == mouse.RIGHT:
        if grid[selected_y][selected_x]['state'] == 'covered':
            grid[selected_y][selected_x]['state'] = 'flag'

        elif grid[selected_y][selected_x]['state'] == 'flag':
            grid[selected_y][selected_x]['state'] = 'question'

        elif grid[selected_y][selected_x]['state'] == 'question':
            grid[selected_y][selected_x]['state'] = 'covered'


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if grid[y][x]['state'] == 'uncovered':
                draw_cell('uncovered', x, y)
            else:
                if x == selected_x and y == selected_y and not game_over:
                    if pygame.mouse.get_pressed()[0] == 1:
                        if grid[y][x]['state'] == 'flag':
                            draw_cell('covered', x, y)
                        else:
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

            if grid[y][x]['flower'] and game_over:
                draw_cell('flower', x, y)
            elif get_surrounding_flower_count(x, y) > 0:
                draw_cell(str(get_surrounding_flower_count(x, y)), x, y)

            if grid[y][x]['state'] == 'flag':
                draw_cell('flag', x, y)
            elif grid[y][x]['state'] == 'question':
                draw_cell('question', x, y)


def on_key_down():
    reset()


# Kod för att starta appen
reset()

pgzrun.go()  # måste vara sista raden
```
  
</details>


![image](https://user-images.githubusercontent.com/4598641/226452171-3df8c25a-b72c-4d16-9ff4-c654bb0e6db3.png)


## Göm antalet blomgrannar för täckta celler
Om en cell är täckt, ska vi inte visa antalet grannceller med blommor.

```python
def draw():
    # etc.

            if grid[y][x]['flower'] and game_over:
                draw_cell('flower', x, y)
            elif get_surrounding_flower_count(x, y) > 0 and grid[y][x]['state'] == 'uncovered': # ändrad
                draw_cell(str(get_surrounding_flower_count(x, y)), x, y)

    # etc.
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

# Funktioner här nedanför


def reset():
    global grid, game_over
    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append({
                'flower': False,
                'state': 'covered',  # 'covered', 'uncovered', 'flag', 'question'
            })

    possible_flower_positions = []

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            possible_flower_positions.append({'x': x, 'y': y})

    for flower_index in range(40):
        position = possible_flower_positions.pop(
            random.randrange(len(possible_flower_positions)))
        grid[position['y']][position['x']]['flower'] = True

    game_over = False


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def get_surrounding_flower_count(x, y):
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

    return surrounding_flower_count


def on_mouse_up(button):
    global game_over

    if game_over:
        reset()
        return

    if button == mouse.LEFT and grid[selected_y][selected_x]['state'] != 'flag':
        if grid[selected_y][selected_x]['flower']:
            grid[selected_y][selected_x]['state'] = 'uncovered'
            game_over = True
        else:
            stack = [
                {
                    'x': selected_x,
                    'y': selected_y,
                }
            ]

            while len(stack) > 0:
                current = stack.pop()
                x = current['x']
                y = current['y']

                grid[y][x]['state'] = 'uncovered'

                if get_surrounding_flower_count(x, y) == 0:
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            if (
                                not (dy == 0 and dx == 0)
                                and 0 <= (y + dy) < len(grid)
                                and 0 <= (x + dx) < len(grid[y + dy])
                                and grid[y + dy][x + dx]['state'] in ('covered', 'question')
                            ):
                                stack.append({
                                    'x': x + dx,
                                    'y': y + dy,
                                })
            complete = True

            for y in range(grid_y_count):
                for x in range(grid_x_count):
                    if grid[y][x]['state'] != 'uncovered' and not grid[y][x]['flower']:
                        complete = False

            if complete:
                game_over = True

    elif button == mouse.RIGHT:
        if grid[selected_y][selected_x]['state'] == 'covered':
            grid[selected_y][selected_x]['state'] = 'flag'

        elif grid[selected_y][selected_x]['state'] == 'flag':
            grid[selected_y][selected_x]['state'] = 'question'

        elif grid[selected_y][selected_x]['state'] == 'question':
            grid[selected_y][selected_x]['state'] = 'covered'


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if grid[y][x]['state'] == 'uncovered':
                draw_cell('uncovered', x, y)
            else:
                if x == selected_x and y == selected_y and not game_over:
                    if pygame.mouse.get_pressed()[0] == 1:
                        if grid[y][x]['state'] == 'flag':
                            draw_cell('covered', x, y)
                        else:
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

            if grid[y][x]['flower'] and game_over:
                draw_cell('flower', x, y)
            elif get_surrounding_flower_count(x, y) > 0 and grid[y][x]['state'] == 'uncovered':
                draw_cell(str(get_surrounding_flower_count(x, y)), x, y)

            if grid[y][x]['state'] == 'flag':
                draw_cell('flag', x, y)
            elif grid[y][x]['state'] == 'question':
                draw_cell('question', x, y)


def on_key_down():
    reset()


# Kod för att starta appen
reset()

pgzrun.go()  # måste vara sista raden

```
  
</details>

![image](https://user-images.githubusercontent.com/4598641/226452196-f8755175-df82-4650-be3a-73491516082d.png)


## Hindra att man klickar på en blomma vid första klicket
För att det första klicket inte ska avtäcka en blomma, flyttar vi koden för att placera blommor så att den körs när vänster musknapp klickas.

Cellen vi klickade på läggs inte till de möjliga blompositionerna.

En variabel skapas för att hålla reeda på om ett klick är det första klicket i spelet.

```python
def draw():
    # etc.

            if grid[y][x]['flower'] and game_over:
                draw_cell('flower', x, y)
            elif get_surrounding_flower_count(x, y) > 0 and grid[y][x]['state'] == 'uncovered': # ändrad
                draw_cell(str(get_surrounding_flower_count(x, y)), x, y)

    # etc.
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

# Funktioner här nedanför


def reset():
    global grid, game_over
    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append({
                'flower': False,
                'state': 'covered',  # 'covered', 'uncovered', 'flag', 'question'
            })

    possible_flower_positions = []

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            possible_flower_positions.append({'x': x, 'y': y})

    for flower_index in range(40):
        position = possible_flower_positions.pop(
            random.randrange(len(possible_flower_positions)))
        grid[position['y']][position['x']]['flower'] = True

    game_over = False


def update():
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

    if selected_x > grid_x_count - 1:
        selected_x = grid_x_count - 1
    if selected_y > grid_y_count - 1:
        selected_y = grid_y_count - 1


def get_surrounding_flower_count(x, y):
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

    return surrounding_flower_count


def on_mouse_up(button):
    global game_over

    if game_over:
        reset()
        return

    if button == mouse.LEFT and grid[selected_y][selected_x]['state'] != 'flag':
        if grid[selected_y][selected_x]['flower']:
            grid[selected_y][selected_x]['state'] = 'uncovered'
            game_over = True
        else:
            stack = [
                {
                    'x': selected_x,
                    'y': selected_y,
                }
            ]

            while len(stack) > 0:
                current = stack.pop()
                x = current['x']
                y = current['y']

                grid[y][x]['state'] = 'uncovered'

                if get_surrounding_flower_count(x, y) == 0:
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            if (
                                not (dy == 0 and dx == 0)
                                and 0 <= (y + dy) < len(grid)
                                and 0 <= (x + dx) < len(grid[y + dy])
                                and grid[y + dy][x + dx]['state'] in ('covered', 'question')
                            ):
                                stack.append({
                                    'x': x + dx,
                                    'y': y + dy,
                                })
            complete = True

            for y in range(grid_y_count):
                for x in range(grid_x_count):
                    if grid[y][x]['state'] != 'uncovered' and not grid[y][x]['flower']:
                        complete = False

            if complete:
                game_over = True

    elif button == mouse.RIGHT:
        if grid[selected_y][selected_x]['state'] == 'covered':
            grid[selected_y][selected_x]['state'] = 'flag'

        elif grid[selected_y][selected_x]['state'] == 'flag':
            grid[selected_y][selected_x]['state'] = 'question'

        elif grid[selected_y][selected_x]['state'] == 'question':
            grid[selected_y][selected_x]['state'] = 'covered'


def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):

            def draw_cell(image, x, y):
                screen.blit(image, (x * cell_size, y * cell_size))

            if grid[y][x]['state'] == 'uncovered':
                draw_cell('uncovered', x, y)
            else:
                if x == selected_x and y == selected_y and not game_over:
                    if pygame.mouse.get_pressed()[0] == 1:
                        if grid[y][x]['state'] == 'flag':
                            draw_cell('covered', x, y)
                        else:
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

            if grid[y][x]['flower'] and game_over:
                draw_cell('flower', x, y)
            elif get_surrounding_flower_count(x, y) > 0 and grid[y][x]['state'] == 'uncovered':
                draw_cell(str(get_surrounding_flower_count(x, y)), x, y)

            if grid[y][x]['state'] == 'flag':
                draw_cell('flag', x, y)
            elif grid[y][x]['state'] == 'question':
                draw_cell('question', x, y)


def on_key_down():
    reset()


# Kod för att starta appen
reset()
grid[0][0]['state'] = 'flag'
grid[0][1]['state'] = 'question'

pgzrun.go()  # måste vara sista raden

```
  
</details>





# Källor
https://simplegametutorials.github.io/pygamezero/flowers/
