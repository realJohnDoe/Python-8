# Life
## En handledning för Python och Pygame Zero 1.2

![image](https://user-images.githubusercontent.com/4598641/225728407-f0313924-90f3-4f7e-83ce-43a6303881e7.png)

# Regler
Det finns ett rutnät av celler, där varje enskild cell antingen är levande eller död.

Efter varje tidssteg gäller att:
- Levande celler med exakt två eller tre levande grannar lever vidare.
- Döda celler med exakt tre levande grannar blir levande.

Alla andra celler dör eller förblir döda.

Skapa en första uppsättning med celler, tryck på valfri tangent för att gå framåt i tiden och observera.

## Kontroller
**Vänsterklick**	Gör cellen levande

**Högerklick**	Gör cellen död

**Vilken tangent som helst**	Gå ett steg framåt i tiden

# Översikt
Cellerna i rutnätet lagras som booleska värden: Sant för levande, Falskt för döda.

![image](https://user-images.githubusercontent.com/4598641/225729047-0f4814bc-6527-47b8-b600-dbbf810dd06b.png)

När tiden går framåt skapas ett nytt rutnät. Om cellerna i detta nya rutnät är levande eller döda baseras på det nuvarande rutnätet.

När det nya rutnätet är klart ersätts det nuvarande rutnätet med det nya rutnätet.

# Kodning
## Rita en cell

En cell ritas som en kvadrat.

✏️ Logga in i repl.it och klona startprojektet https://replit.com/@RobertStorlind/life-starter
Mata in koden och testkör!

```python
import pgzrun

def draw():
    screen.fill((255, 255, 255)) # vit färg

    screen.draw.filled_rect(
        Rect(
            (0, 0),
            (4, 4)
        ),
        color=(220, 220, 220)
    )

pgzrun.go()
```

![image](https://user-images.githubusercontent.com/4598641/225729369-04e983ca-eaa8-4009-9b71-fc3d247cf22f.png)


## Rita en rad med celler
En rad med celler ritas, med en pixel mellan varje cell.

✏️ Mata in koden och testkör!

```python
import pgzrun

def draw ():
    screen.fill (( 255 , 255 , 255 ))

    for x in range(70): #nyrad
        cell_size = 5 #nyrad
        cell_draw_size = cell_size - 1 #nyrad

        screen.draw.filled_rect(
            Rect(
                (x * cell_size, 0), #ändra
                (cell_draw_size, cell_draw_size) #nyrad
            ),
            color=(220, 220, 220)
        )

pgzrun.go()
```

![image](https://user-images.githubusercontent.com/4598641/225729839-7b0261e5-a2cc-4995-b1b2-d4db4d796737.png)

## Rita alla celler

Vi ritar alla raderna.

✏️ Uppdatera funktionen och testkör din kod.
>Glöm inte att dra in raderna under `for y`.

```python
def draw():
    screen.fill((255, 255, 255))

    for y in range(50): #nyrad
        for x in range(70):
            cell_size = 5
            cell_draw_size = cell_size - 1

            screen.draw.filled_rect(
                Rect(
                    (x * cell_size, y * cell_size), #nyrad
                    (cell_draw_size, cell_draw_size)
                ),
                color=(220, 220, 220)
            )
```

![image](https://user-images.githubusercontent.com/4598641/225730301-6313d4de-4505-417b-8dd3-6c138d1b2ea7.png)

## Markera celler

Cellpositionen som muspekaren är över lagras.

Detta beräknas genom att ta muspositionen och dividera den med cellstorleken och avrunda neråt.

Exempel: om musen har x-koordinat 17 och cellstorleken är 5, dividerar vi 17 med 5 vilket ger 3,4. Vi avrundar neråt och får 3.
Det betyder att musen är över cellen med ett index på 3 på X-axeln .

Cellstorleken behövs för att beräkna detta, så den flyttas till att vara en global variabel.
Vi skriver det värdet på skärmen medan vi testar vår kod.

Vi importerar modulen pygame så att `pygame.mouse.get_pos` kan användas för att läsa av muspekarens koordinater.

Matematikmodulen importerar vi så att vi kan använda `math.floor` för att avrunda ett tal neråt till närmast mindre heltal.

✏️ Mata in koden och testkör!

```python
import pgzrun
import pygame
import math

cell_size = 5

def update():
    global selected_x
    global selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = math.floor(mouse_x / cell_size)
    selected_y = math.floor(mouse_y / cell_size)

def draw():
    screen.fill((255, 255, 255))

    for y in range(50):
        for x in range(70):
            # Ta bort: cell_size = 5

            # etc.

    # Tillfälligt
    screen.draw.text(
        f"selected x: {selected_x}, selected y: {selected_y}",
        (0, 0),
        color=(0, 0, 0)
    )

pgzrun.go()
```

![image](https://user-images.githubusercontent.com/4598641/225734422-569de346-61f2-4246-905c-1838b95ff534.png)

## Begränsa vald cell till rutnätet
`min` används för att ge den valda positionen ett maximalt värde, så att den inte kommer att vara utanför rutnätet även om musen är utanför rutnätet.

Rutnätets bredd/höjd i celler återanvänds från att rita cellerna, så vi sparar bredden och höjden i variabler.

✏️ Mata in koden och testkör!

```python
grid_x_count = 70
grid_y_count = 50

def update():
    # etc.

    selected_x = min(math.floor(mouse_x / cell_size), grid_x_count - 1) #uppdatera
    selected_y = min(math.floor(mouse_y / cell_size), grid_y_count - 1) #uppdatera

def draw():
    screen.fill((255, 255, 255))

    for y in range(grid_y_count): #uppdatera
        for x in range(grid_x_count): #uppdatera
            # etc.
```

## Markera celler
Cellen (rutan) under muspekaren är inställd på markeringsfärgen.

✏️ Mata in koden och testkör!

```python
def draw():
    screen.fill((255, 255, 255))

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            cell_draw_size = cell_size - 1

            if x == selected_x and y == selected_y: #nyrad
                color = (0, 255, 255) #nyrad
            else: #nyrad
                color = (220, 220, 220) #nyrad

            screen.draw.filled_rect(
                Rect(
                    (x * cell_size, y * cell_size),
                    (cell_draw_size, cell_draw_size)
                ),
                color=color #nyrad
            )
```

![image](https://user-images.githubusercontent.com/4598641/225734958-fe8dfa7b-59c6-422c-9ba2-0561436c5add.png)


## Skapa rutnätet
Ett rutnät skapas för att lagra cellerna.

Varje cell representeras av ett booleskt värde: Sant för levande, Falskt för död.

Om cellen är levande används den levande färgen för att rita cellen.

För att testa detta ställs vissa celler manuellt in på att leva.

✏️ Mata in koden och testkör!

```python
# etc.

grid = []

for y in range(grid_y_count):
    grid.append([])
    for x in range(grid_x_count):
        grid[y].append(False)

# Temporary
grid[0][0] = True
grid[0][1] = True

def draw():
    screen.fill((255, 255, 255))

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            cell_draw_size = cell_size - 1

            if x == selected_x and y == selected_y:
                color = (0, 255, 255)
            elif grid[y][x]: #nyrad
                color = (255, 0, 255) #nyrad
            else:
                color = (220, 220, 220)

            # etc.
```

![image](https://user-images.githubusercontent.com/4598641/225735062-e17dd79f-3542-40fd-a9f5-58c797f89297.png)


## Gör celler levande med vänster musknapp
Om vänster musknapp är nedtryckt är den valda cellen inställd på att leva.

✏️ Mata in koden och testkör!

```python
def update():
    # etc.

    if pygame.mouse.get_pressed()[0]: #nyrad
        grid[selected_y][selected_x] = True #nyrad
```
![image](https://user-images.githubusercontent.com/4598641/225735163-0a7b10dd-a3f4-4756-8673-713fe5a6eb05.png)



## Räkna dina grannar
Att uppdatera rutnätet efter ett steg kräver att man vet hur många levande grannar varje cell har.

Just nu kommer högerklick på en cell att skriva ut hur många levande grannar den har.

✏️ Mata in koden och testkör!

```python
# Tillfälligt
def on_mouse_down(pos, button):
    if button == mouse.RIGHT:
        neighbor_count = 0

        print(f"Finding neighbors of grid[{selected_y)}][{selected_x}]")

        for dy in range(-1, 2):
            for dx in range(-1, 2):

                print(f" Checking grid[{selected_y + dy}][{selected_x + dx}]")

                if (not (dy == 0 and dx == 0)
                    and 0 <= (selected_y + dy) < grid_y_count
                    and 0 <= (selected_x + dx) < grid_x_count
                    and grid[selected_y + dy][selected_x + dx]):

                    print('  Neighbor found')
                    neighbor_count += 1

        print(f"Total neighbors: {neighbor_count}")
        print()
```

```bash
Finding neighbors of grid[10][10]
 Checking grid[9][9]
 Checking grid[9][10]
 Checking grid[9][11]
  Neighbor found
 Checking grid[10][9]
 Checking grid[10][11]
 Checking grid[11][9]
 Checking grid[11][10]
  Neighbor found
 Checking grid[11][11]
Total neighbors: 2
```

## Uppdatera rutnätet vid knapptryckning
När en tangent trycks, skapas ett nytt rutnät och det gamla rutnätet ersätts av det nya rutnätet.

Till en början kommer alla celler i det nya rutnätet att vara levande.

✏️ Mata in koden och testkör!

```python
def on_key_down():
    global grid
    next_grid = []

    for y in range(grid_y_count):
        next_grid.append([])
        for x in range(grid_x_count):
            next_grid[y].append(True)

    grid = next_grid
```

![image](https://user-images.githubusercontent.com/4598641/225735624-4f103937-7ed2-4efd-978d-ac6ffde64ccd.png)


## Ändra rutnät baserat på grannar
Koden för att hitta antalet levande grannar en cell har flyttas hit.

En cell i det nya rutnätet är vid liv om den har 3 grannar, eller så är den levande i det gamla rutnätet och har 2 grannar.

✏️ Mata in koden och testkör!

```python
def on_key_down():
    global grid

    next_grid = []

    for y in range(grid_y_count):
        next_grid.append([])
        for x in range(grid_x_count):
            # Moved
            neighbor_count = 0

            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if (not (dy == 0 and dx == 0)
                        and 0 <= (y + dy) < grid_y_count
                        and 0 <= (x + dx) < grid_x_count
                        and grid[y + dy][x + dx]):

                        neighbor_count += 1

            next_grid[y].append(
                neighbor_count == 3 or #nyrad
                (grid[y][x] and neighbor_count == 2) #nyrad
            )

    grid = next_grid

# Borttaget: def on_mouse_down(pos, button):
```

![image](https://user-images.githubusercontent.com/4598641/225735719-0d1f5745-9252-449f-9d62-60f076b37e3c.png)

## Döda celler med högerklick
När en cell högerklickas dör den.

✏️ Mata in koden och testkör!

```python
def update():
    # etc.

    if pygame.mouse.get_pressed()[0]:
        grid[selected_y][selected_x] = True
    elif pygame.mouse.get_pressed()[2]: #nyrad
        grid[selected_y][selected_x] = False #nyrad
```

# Källor
Efter originalet på https://simplegametutorials.github.io/pygamezero/life/
