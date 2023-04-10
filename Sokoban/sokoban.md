# Sokoban ⭐⭐⭐
## En handledning för Python och Pygame Zero 1.2

![image](https://user-images.githubusercontent.com/4598641/226440407-e4b478ca-f453-48b3-a640-38e4858d1c56.png)

[Spelnivåerna i den här handledningen är hämtade från Rockbox-projektet](http://git.rockbox.org/?p=rockbox.git;a=blob_plain;f=apps/plugins/sokoban.levels)

# Innehåll

**[Regler](#regler)**
   [Teckenförklaring](#teckenförklaring)
  &bull; [Kontroller](#kontroller)

**[Översikt](#översikt)**

**[Kodning](#kodning)**
   [Rita en nivå](#rita-en-nivå)
  &bull; [Skriv celltypen i varje cell](#skriv-celltypen-i-varje-cell)
  &bull; [Ställa in färger](#ställa-in-färger)
  &bull; [Ge celltyperna namn](#ge-celltyperna-namn)
  &bull; [Hitta spelarens cell](#hitta-spelarens-cell)
  &bull; [Hitta celltyp i den riktning som piltangenten pekar](#hitta-celltyp-i-den-riktning-som-piltangenten-pekar)
  &bull; [Skapa en testnivå](#skapa-en-testnivå)
  &bull; [Flytta spelaren till en tom ruta](#flytta-spelaren-till-en-tom-ruta)
  &bull; [Flytta spelaren till lagerplats](#flytta-spelaren-till-lagerplats)
  &bull; [Förenkla koden](#förenkla-koden)
  &bull; [Flytta spelare från lagerplats](#flytta-spelare-från-lagerplats)
  &bull; [Förenkla koden](#förenkla-koden-1)
  &bull; [Putta lådan till tom plats](#putta-lådan-till-tom-plats)
  &bull; [Putta lådan till en lagerplats](#putta-lådan-till-en-lagerplats)
  &bull; [Förenkla koden](#förenkla-koden-2)
  &bull; [Putta lådan till en lagerplats](#putta-lådan-till-en-lagerplats-1)
  &bull; [Förenkla koden](#förenkla-koden-3)
  &bull; [Ladda spelnivåer från en lista](#ladda-spelnivåer-från-en-lista)
  &bull; [Återställ nivån](#återställ-nivån)
  &bull; [Nästa och föregående nivå](#nästa-och-föregående-nivå)
  &bull; [Slå över när vi går till nästa och föregående nivå](#slå-över-när-vi-går-till-nästa-och-föregående-nivå)
  &bull; [Gå till nästa nivå när en nivå är avklarad](#gå-till-nästa-nivå-när-en-nivå-är-avklarad)
  &bull; [Fler nivåer](#fler-nivåer)

**[Uppgifter](#uppgifter)**

**[Källor](#källor)**

# Regler
Skjut in alla lådorna på lagerplatserna.

En låda kan bara flyttas om det finns ett ledigt utrymme bredvid den &ndash; inte en vägg eller annan låda.

## Teckenförklaring

![image](https://user-images.githubusercontent.com/4598641/226440572-913c4152-7a92-415b-82c2-ebf0f5817183.png)
Spelare<br>
![image](https://user-images.githubusercontent.com/4598641/226440611-a41f140d-f21d-4e68-a216-17f9fe4ef197.png)
Spelare på lagerplats<br>
![image](https://user-images.githubusercontent.com/4598641/226440626-7c18df09-a547-48eb-ab11-13b1e372e626.png)
Låda<br>
![image](https://user-images.githubusercontent.com/4598641/226440685-78b3e349-3357-44c4-abc7-5fffb41ff9b6.png)
Låda på lagerplats<br>
![image](https://user-images.githubusercontent.com/4598641/226440711-2682f8f3-d36c-448d-a9c4-7f37e79a1840.png)
Lagerplats<br>
![image](https://user-images.githubusercontent.com/4598641/226440721-3dafc158-56c0-4038-8c98-8dd8bb8b512a.png)
Vägg

## Kontroller
**Piltangenter**	Flytta<br>
**R**	Återställ nivån<br>
**N**	Nästa nivå<br>
**P**	Förra nivån<br>

# Översikt
De olika tillstånden en ruta kan ha motsvaras av följande tecken/strängar:

__@__	Spelare &ndash; *player*<br>
__+__	Spelare på lagerplats &ndash; *player_on_storage*<br>
__$__	Låda &ndash; *box*<br>
__*__	Låda på lagerplats &ndash; *box_on_storage*<br>
__.__	Lagerplats &ndash; *storage*<br>
__#__	Vägg &ndash; *wall*

Varje spelnivå (level) lagras som ett rutnät av dessa strängar.

![image](https://user-images.githubusercontent.com/4598641/226441339-fc46c4d7-6fd0-414c-9829-4755286aa054.png)

När en piltangent trycks, loopar vi genom rutnätet för att hitta var spelaren är.

Om spelaren kan gå i piltangentens riktning, flyttar vi spelaren dit och ritar om med rätt grafik.
>En gul ruta är tom. Spelaren kan bara stå på tomma rutor och på lagerplatser. Det första exemplet visar när spelaren går ett steg åt höger.

![image](https://user-images.githubusercontent.com/4598641/226441412-0d311596-2d1f-4e54-bf51-e163588f9e16.png)

Om spelaren står vid en låda och rutan bredvid lådan är ledig, kan spelaren putta lådan i den riktningen. Sedan ritar vi om. Det första exemplet visar hur spelaren puttar lådan ett steg åt höger. Tomma rutor är gula.

![image](https://user-images.githubusercontent.com/4598641/226441447-3953051d-e11b-4f3c-8f92-5589f177cd2d.png)

Om det inte finns några lådor kvar som inte finns på lagerplatser är nivån klar.


# Kodning
## Rita en nivå
Varje nivå lagras som ett rutnät av strängar. 
För närvarande har vi en enda nivå och en kvadrat ritas för varje cell som inte är ett mellanslag, dvs. tom.

✏️ Se till att du är inloggad i repl.it. Öppna startprojektet https://replit.com/@RobertStorlind/sokoban-starter
och spara en egen kopia med knappen "Fork". Testkör!

```python
import pgzrun

# Globala variabler här nedanför

level = [
    [' ', ' ', '#', '#', '#'],
    [' ', ' ', '#', '.', '#'],
    [' ', ' ', '#', ' ', '#', '#', '#', '#'],
    ['#', '#', '#', '$', ' ', '$', '.', '#'],
    ['#', '.', ' ', '$', '@', '#', '#', '#'],
    ['#', '#', '#', '#', '$', '#'],
    [' ', ' ', ' ', '#', '.', '#'],
    [' ', ' ', ' ', '#', '#', '#'],
]


# Funktioner här nedanför
def draw():
    screen.fill((0, 0, 0))
    
    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != ' ':
                cell_size = 23
                
                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=(255, 255, 255)
                )  
# Kod för att starta appen här nedanför

pgzrun.go() # måste vara sista raden
```

![image](https://user-images.githubusercontent.com/4598641/226441552-531f43b9-788f-4e53-9f34-84ab40932038.png)

## Skriv celltypen i varje cell
Rutans sträng visas i varje ruta.

✏️ Uppdatera koden. Ser det ut som i exempelbilden här nere?

```python
def draw():
    screen.fill((0, 0, 0))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != ' ':
                # etc.

                screen.draw.text( #nytt  🔲
                    cell, #nytt 🔲
                    (x * cell_size, y * cell_size), #nytt 🔲
                    color=(0, 0, 0) #nytt 🔲
                ) #nytt 🔲
```


<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun

# Globala variabler här nedanför

level = [
    [' ', ' ', '#', '#', '#'],
    [' ', ' ', '#', '.', '#'],
    [' ', ' ', '#', ' ', '#', '#', '#', '#'],
    ['#', '#', '#', '$', ' ', '$', '.', '#'],
    ['#', '.', ' ', '$', '@', '#', '#', '#'],
    ['#', '#', '#', '#', '$', '#'],
    [' ', ' ', ' ', '#', '.', '#'],
    [' ', ' ', ' ', '#', '#', '#'],
]


# Funktioner här nedanför
def draw():
    screen.fill((0, 0, 0))
    
    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != ' ':
                cell_size = 23
                
                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=(255, 255, 255)
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(0, 0, 0)
                )

# Kod för att starta appen här nedanför

pgzrun.go() # måste vara sista raden
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226441595-3f2259b1-970d-46d2-98f1-b1ba305e126b.png)

## Ställa in färger
Bakgrundsfärgen ändras och färgen på varje cell ställs in baserat på dess typ.

✏️ Uppdatera koden. Testkör. Ser det rimligt ut?


```python
def draw():
    screen.fill((255, 255, 190)) #nytt 🔲

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != ' ':
                cell_size = 23

                colors = { #nytt 🔲
                    '@': (167, 135, 255),
                    '+': (158, 119, 255),
                    '$': (255, 201, 126),
                    '*': (150, 255, 127),
                    '.': (156, 229, 255),
                    '#': (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell] #nytt 🔲
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255) #nytt 🔲
                )
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun

# Globala variabler här nedanför

level = [
    [' ', ' ', '#', '#', '#'],
    [' ', ' ', '#', '.', '#'],
    [' ', ' ', '#', ' ', '#', '#', '#', '#'],
    ['#', '#', '#', '$', ' ', '$', '.', '#'],
    ['#', '.', ' ', '$', '@', '#', '#', '#'],
    ['#', '#', '#', '#', '$', '#'],
    [' ', ' ', ' ', '#', '.', '#'],
    [' ', ' ', ' ', '#', '#', '#'],
]


# Funktioner här nedanför
def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != ' ':
                cell_size = 23

                colors = {
                    '@': (167, 135, 255),
                    '+': (158, 119, 255),
                    '$': (255, 201, 126),
                    '*': (150, 255, 127),
                    '.': (156, 229, 255),
                    '#': (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )

# Kod för att starta appen här nedanför


pgzrun.go()  # måste vara sista raden
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226441696-30c32370-c672-422b-9a3c-4f8851498f74.png)

## Ge celltyperna namn
För att slippa komma ihåg vilken symbol som motsvarar en viss celltyp, lagrar vi typerna i variabler.

✏️ Uppdatera koden. Testkör och se att det fungerar som innan vi städade koden.

```python
import pgzrun

# Globala variabler här nedanför

level = 
# etc.

player = '@' #nytt 🔲
player_on_storage = '+' #nytt 🔲
box = '$' #nytt 🔲
box_on_storage = '*' #nytt 🔲
storage = '.' #nytt 🔲
wall = '#' #nytt 🔲
empty = ' ' #nytt 🔲

# Funktioner här nedanför
def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty: #nytt 🔲
                cell_size = 23

                colors = {
                    player: (167, 135, 255), #nytt 🔲
                    player_on_storage: (158, 119, 255), #nytt 🔲
                    box: (255, 201, 126), #nytt 🔲
                    box_on_storage: (150, 255, 127), #nytt 🔲
                    storage: (156, 229, 255), #nytt 🔲
                    wall: (255, 147, 209), #nytt 🔲
                }
# etc.
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun

# Globala variabler här nedanför

level = [
    [' ', ' ', '#', '#', '#'],
    [' ', ' ', '#', '.', '#'],
    [' ', ' ', '#', ' ', '#', '#', '#', '#'],
    ['#', '#', '#', '$', ' ', '$', '.', '#'],
    ['#', '.', ' ', '$', '@', '#', '#', '#'],
    ['#', '#', '#', '#', '$', '#'],
    [' ', ' ', ' ', '#', '.', '#'],
    [' ', ' ', ' ', '#', '#', '#'],
]

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför
def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )

# Kod för att starta appen här nedanför


pgzrun.go()  # måste vara sista raden

```

</details>

## Hitta spelarens cell
Det första steget i att flytta spelaren är att hitta vilken cell spelaren är i.

Cellerna på varje nivå loopas igenom. Om celltypen är en spelare eller en spelare på lagerplats, så skrivs spelarens position ut för tillfället.
Så här ser det ut i konsollfönstret:

```
4 4
```

✏️ Lägg till funktionen `on_key_down()`. Ser du utskriften i konsollfönstret i repl.it?

```python
# Funktioner här nedanför
def on_key_down(key): # hela funktionen är ny 🔲
    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        # Temporary
        print(player_x, player_y)

def draw(): # etc.
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun

# Globala variabler här nedanför

level = [
    [' ', ' ', '#', '#', '#'],
    [' ', ' ', '#', '.', '#'],
    [' ', ' ', '#', ' ', '#', '#', '#', '#'],
    ['#', '#', '#', '$', ' ', '$', '.', '#'],
    ['#', '.', ' ', '$', '@', '#', '#', '#'],
    ['#', '#', '#', '#', '$', '#'],
    [' ', ' ', ' ', '#', '.', '#'],
    [' ', ' ', ' ', '#', '#', '#'],
]

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför
def on_key_down(key):
    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y
        
        # Temporary
        print(player_x, player_y)

def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )

# Kod för att starta appen här nedanför


pgzrun.go()  # måste vara sista raden
```

</details>

## Hitta celltypen i den riktning som piltangenten pekar

Celltypen för spelarens nuvarande position och celltypen för den intilliggande positionen i riktningen för den nedtryckta piltangenten lagras i variabler och skrivs  ut just nu.

✏️ Uppdatera koden i `on_key_down`. Vad händer när du trycker på piltangenterna? Ser du utskriften i konsollfönstret?
>Kom ihåg att klicka i spelfönstret när du klickat på Run. Då kan din kod fånga upp tangenttryckningarna.

```python
# Funktioner här nedanför
def on_key_down(key):
    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        # Temporary
        print(f"current = level[{player_y}][{player_x}] ({current})")
        print(f"adjacent = level[{player_y + dy}][{player_x + dx}] ({adjacent})")
        print()

# etc.
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun

# Globala variabler här nedanför

level = [
    [' ', ' ', '#', '#', '#'],
    [' ', ' ', '#', '.', '#'],
    [' ', ' ', '#', ' ', '#', '#', '#', '#'],
    ['#', '#', '#', '$', ' ', '$', '.', '#'],
    ['#', '.', ' ', '$', '@', '#', '#', '#'],
    ['#', '#', '#', '#', '$', '#'],
    [' ', ' ', ' ', '#', '.', '#'],
    [' ', ' ', ' ', '#', '#', '#'],
]

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför
def on_key_down(key):
    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        # Temporary
        print(f"current = level[{player_y}][{player_x}] ({current})")
        print(f"adjacent = level[{player_y + dy}][{player_x + dx}] ({adjacent})")
        print()


def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )

# Kod för att starta appen här nedanför


pgzrun.go()  # måste vara sista raden
```

</details>
Så här kan utskriften se ut i konsollfönstret:

```python
current = level[4][4] (@)
adjacent = level[3][4] ( )

current = level[4][4] (@)
adjacent = level[4][5] (#)

current = level[4][4] (@)
adjacent = level[5][4] ($)

current = level[4][4] (@)
adjacent = level[4][3] ($)
```

## Skapa en testnivå
Vi gör en testnivå för att lättare kunna testa spelarens rörelse.

✏️ Uppdatera variabeln `level`. Testkör. Ritas testnivån på skärmen?

```python
import pgzrun

# Globala variabler här nedanför
level = [ #ändra variabeln level 🔲
    ['#', '#', '#', '#', '#'],
    ['#', '@', ' ', '.', '#'],
    ['#', ' ', '$', ' ', '#'],
    ['#', '.', '$', ' ', '#'],
    ['#', ' ', '$', '.', '#'],
    ['#', '.', '$', '.', '#'],
    ['#', '.', '*', ' ', '#'],
    ['#', ' ', '*', '.', '#'],
    ['#', ' ', '*', ' ', '#'],
    ['#', '.', '*', '.', '#'],
    ['#', '#', '#', '#', '#'],
]

# etc.
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun

# Globala variabler här nedanför
level = [
    ['#', '#', '#', '#', '#'],
    ['#', '@', ' ', '.', '#'],
    ['#', ' ', '$', ' ', '#'],
    ['#', '.', '$', ' ', '#'],
    ['#', ' ', '$', '.', '#'],
    ['#', '.', '$', '.', '#'],
    ['#', '.', '*', ' ', '#'],
    ['#', ' ', '*', '.', '#'],
    ['#', ' ', '*', ' ', '#'],
    ['#', '.', '*', '.', '#'],
    ['#', '#', '#', '#', '#'],
]

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför
def on_key_down(key):
    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        # Temporary
        print(f"current = level[{player_y}][{player_x}] ({current})")
        print(f"adjacent = level[{player_y + dy}][{player_x + dx}] ({adjacent})")
        print()


def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )

# Kod för att starta appen här nedanför


pgzrun.go()  # måste vara sista raden
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226441985-25fde8b7-f083-443e-bc3c-3e0082023c45.png)


## Flytta spelaren till en tom ruta
Om värdet på spelarens nuvarande position är `player`, alltså inte `player_on_storage` *och* cellen intill är tom, flyttar vi spelaren till den tomma cellen.

✏️ Uppdatera koden i `on_key_down`. Vad händer när du går runt med piltangenterna?

```python
# Funktioner här nedanför
def on_key_down(key):
# etc.

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        if current == player and adjacent == empty: #nytt 🔲
            level[player_y][player_x] = empty #nytt 🔲
            level[player_y + dy][player_x + dx] = player #nytt 🔲
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun

# Globala variabler här nedanför
level = [
    ['#', '#', '#', '#', '#'],
    ['#', '@', ' ', '.', '#'],
    ['#', ' ', '$', ' ', '#'],
    ['#', '.', '$', ' ', '#'],
    ['#', ' ', '$', '.', '#'],
    ['#', '.', '$', '.', '#'],
    ['#', '.', '*', ' ', '#'],
    ['#', ' ', '*', '.', '#'],
    ['#', ' ', '*', ' ', '#'],
    ['#', '.', '*', '.', '#'],
    ['#', '#', '#', '#', '#'],
]

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför
def on_key_down(key):
    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        if current == player and adjacent == empty:
            level[player_y][player_x] = empty
            level[player_y + dy][player_x + dx] = player


def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )

# Kod för att starta appen här nedanför


pgzrun.go()  # måste vara sista raden
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226442037-607ab9cd-4a59-47de-a13e-6ea0b696a3da.png)

## Flytta spelaren till lagerplats
Om rutan dit spelaren vill gå är av typen `storage`, blir den nya rutan `player_on_storage`.

Just nu kan spelaren gå till en lagerplats, men inte lämna den. Vi ska fixa den buggen om en liten stund 🐛

✏️ Uppdatera koden i `on_key_down`. Vad händer när spelaren går till en lagerplats?

```python
def on_key_down(key):
   # etc.

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        if current == player:
            if adjacent == empty: #nytt 🔲
                level[player_y][player_x] = empty
                level[player_y + dy][player_x + dx] = player
            elif adjacent == storage: #nytt 🔲
                level[player_y][player_x] = empty #nytt 🔲
                level[player_y + dy][player_x + dx] = player_on_storage #nytt 🔲
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun

# Globala variabler här nedanför
level = [
    ['#', '#', '#', '#', '#'],
    ['#', '@', ' ', '.', '#'],
    ['#', ' ', '$', ' ', '#'],
    ['#', '.', '$', ' ', '#'],
    ['#', ' ', '$', '.', '#'],
    ['#', '.', '$', '.', '#'],
    ['#', '.', '*', ' ', '#'],
    ['#', ' ', '*', '.', '#'],
    ['#', ' ', '*', ' ', '#'],
    ['#', '.', '*', '.', '#'],
    ['#', '#', '#', '#', '#'],
]

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför


def on_key_down(key):
    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        if current == player:
            if adjacent == empty:
                level[player_y][player_x] = empty
                level[player_y + dy][player_x + dx] = player
            elif adjacent == storage:
                level[player_y][player_x] = empty
                level[player_y + dy][player_x + dx] = player_on_storage


def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )

# Kod för att starta appen här nedanför

pgzrun.go()  # måste vara sista raden
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226442060-dddc88af-c52b-4d75-bafc-d202d9069ae1.png)

## Förenkla koden
Den nya grannrutan &ndash; antingen `player` eller `player_on_storage` &ndash; ställs in baserat på typen av `adjacent`.
Därför skapar vi en ordlista som ger nästa intilliggande celltyp när den indexeras av den aktuella intilliggande celltypen.

Den används också för att kontrollera om spelaren kan flytta till den intilliggande positionen genom att kontrollera om den har en nyckel med värdet `adjacent` .


✏️ Uppdatera koden. Testkör. Fungerar det som innan?

```python
def on_key_down(key):
    # etc.

        next_adjacent = { #nytt 🔲
            empty: player, #nytt 🔲
            storage: player_on_storage, #nytt 🔲
        } #nytt 🔲

        if current == player and adjacent in next_adjacent: #ändrat 🔲
            level[player_y][player_x] = empty
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent] #ändrat 🔲
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun

# Globala variabler här nedanför
level = [
    ['#', '#', '#', '#', '#'],
    ['#', '@', ' ', '.', '#'],
    ['#', ' ', '$', ' ', '#'],
    ['#', '.', '$', ' ', '#'],
    ['#', ' ', '$', '.', '#'],
    ['#', '.', '$', '.', '#'],
    ['#', '.', '*', ' ', '#'],
    ['#', ' ', '*', '.', '#'],
    ['#', ' ', '*', ' ', '#'],
    ['#', '.', '*', '.', '#'],
    ['#', '#', '#', '#', '#'],
]

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför


def on_key_down(key):
    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        next_adjacent = {
            empty: player,
            storage: player_on_storage,
        }

        if current == player and adjacent in next_adjacent:
            level[player_y][player_x] = empty
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]


def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )

# Kod för att starta appen här nedanför

pgzrun.go()  # måste vara sista raden
```

</details>

## Flytta spelare från lagerplats

Om spelaren är på en lagerplats, `player_on_storage`, sätts spelarens nuvarande position till &raquo;bara&laquo; `storage` när spelaren lämnar.

✏️ Uppdatera koden. Vad händer när du går till och från en lagerplats?

```python
def on_key_down(key):
    # etc.

        next_adjacent = {
            empty: player,
            storage: player_on_storage,
        }

        if adjacent in next_adjacent:
            if current == player: #nytt 🔲
                level[player_y][player_x] = empty
                level[player_y + dy][player_x + dx] = next_adjacent[adjacent]
            elif current == player_on_storage: #nytt 🔲
                level[player_y][player_x] = storage #nytt 🔲
                level[player_y + dy][player_x + dx] = next_adjacent[adjacent] #nytt 🔲
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun

# Globala variabler här nedanför
level = [
    ['#', '#', '#', '#', '#'],
    ['#', '@', ' ', '.', '#'],
    ['#', ' ', '$', ' ', '#'],
    ['#', '.', '$', ' ', '#'],
    ['#', ' ', '$', '.', '#'],
    ['#', '.', '$', '.', '#'],
    ['#', '.', '*', ' ', '#'],
    ['#', ' ', '*', '.', '#'],
    ['#', ' ', '*', ' ', '#'],
    ['#', '.', '*', '.', '#'],
    ['#', '#', '#', '#', '#'],
]

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför


def on_key_down(key):
    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        next_adjacent = {
            empty: player,
            storage: player_on_storage,
        }

        if adjacent in next_adjacent:
            if current == player:
                level[player_y][player_x] = empty
                level[player_y + dy][player_x + dx] = next_adjacent[adjacent]
            elif current == player_on_storage:
                level[player_y][player_x] = storage
                level[player_y + dy][player_x + dx] = next_adjacent[adjacent]


def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )

# Kod för att starta appen här nedanför


pgzrun.go()  # måste vara sista raden
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226442123-828097c9-b89f-449a-9de0-e83d8a774464.png)

## Förenkla koden
Vi gör en ordlista som ger nästa celltyp för spelarens tidigare position när den indexeras av celltypen där spelaren är just nu.

✏️ Uppdatera koden. Fungerar koden som innan?

```python
def on_key_down(key):
    # etc.

        next_current = { #nytt 🔲
            player: empty, #nytt 🔲
            player_on_storage: storage, #nytt 🔲
        }

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current] #nytt 🔲
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun

# Globala variabler här nedanför
level = [
    ['#', '#', '#', '#', '#'],
    ['#', '@', ' ', '.', '#'],
    ['#', ' ', '$', ' ', '#'],
    ['#', '.', '$', ' ', '#'],
    ['#', ' ', '$', '.', '#'],
    ['#', '.', '$', '.', '#'],
    ['#', '.', '*', ' ', '#'],
    ['#', ' ', '*', '.', '#'],
    ['#', ' ', '*', ' ', '#'],
    ['#', '.', '*', '.', '#'],
    ['#', '#', '#', '#', '#'],
]

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför


def on_key_down(key):
    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        next_adjacent = {
            empty: player,
            storage: player_on_storage,
        }

        next_current = {
            player: empty,
            player_on_storage: storage,
        }

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]


def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )

# Kod för att starta appen här nedanför


pgzrun.go()  # måste vara sista raden
```

</details>


## Putta lådan till tom plats
Cellen bortom den intilliggande cellen lagras i en variabel. Vi behöver hålla reda på om vi nära någon av kanterna på rutnätet.
- `player_y + dy + dy` kontrolleras för att se om det är större än eller lika med 0 och mindre än `len(level)`, dvs det är inom nivån i y-led.
- `player_x + dx + dx` kontrolleras för att se om det är större än eller lika med 0 och mindre än `len(level[player_y + dy + dy])`, dvs det är inom nivån i x-led.

Den intilliggande rutan kollas inte på samma sätt eftersom det alltid finns en kant av väggar runt varje nivå, så `player_y + dy` eller `player_x + dx` kommer aldrig att vara utanför spelområdet.

Om den intilliggande cellen är en låda och cellen bortom lådan är tom, sätter vi den intilliggande cellen till `player` och positionen bortom till `box`. Spelaren har alltså puttat lådan ett steg i den valda riktningen.

✏️ Uppdatera koden. Vad händer när spelaren puttar en låda?

```python
def on_key_down(key):
    # etc.

        beyond = '' #nytt 🔲
        if ( #nytt 🔲
            0 <= player_y + dy + dy < len(level) #nytt 🔲
            and 0 <= player_x + dx + dx < len(level[player_y + dy + dy]) #nytt 🔲
        ): #nytt 🔲
            beyond = level[player_y + dy + dy][player_x + dx + dx] #nytt 🔲

        next_adjacent = {
            empty: player,
            storage: player_on_storage,
        }
        next_current = {
            player: empty,
            player_on_storage: storage,
        }

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]

        elif adjacent == box and beyond == empty: #nytt 🔲
            level[player_y][player_x] = next_current[current] #nytt 🔲
            level[player_y + dy][player_x + dx] = player #nytt 🔲
            level[player_y + dy + dy][player_x + dx + dx] = box #nytt 🔲
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun

# Globala variabler här nedanför
level = [
    ['#', '#', '#', '#', '#'],
    ['#', '@', ' ', '.', '#'],
    ['#', ' ', '$', ' ', '#'],
    ['#', '.', '$', ' ', '#'],
    ['#', ' ', '$', '.', '#'],
    ['#', '.', '$', '.', '#'],
    ['#', '.', '*', ' ', '#'],
    ['#', ' ', '*', '.', '#'],
    ['#', ' ', '*', ' ', '#'],
    ['#', '.', '*', '.', '#'],
    ['#', '#', '#', '#', '#'],
]

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför


def on_key_down(key):
    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        beyond = ''
        if (
            0 <= player_y + dy + dy < len(level)
            and 0 <= player_x + dx + dx < len(level[player_y + dy + dy])
        ):
            beyond = level[player_y + dy + dy][player_x + dx + dx]

        next_adjacent = {
            empty: player,
            storage: player_on_storage,
        }
        next_current = {
            player: empty,
            player_on_storage: storage,
        }

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]

        elif adjacent == box and beyond == empty:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = player
            level[player_y + dy + dy][player_x + dx + dx] = box


def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )

# Kod för att starta appen här nedanför


pgzrun.go()  # måste vara sista raden
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226442221-e7c86311-2b78-4175-94f7-29befecbb32e.png)

## Putta lådan till en lagerplats
Om positionen två steg bort är `storage`, så ställs den positionen till `box_on_storage`.

✏️ Uppdatera koden. Vad händer när spelaren försöker putta en låda till en lagerplats?
```python
def on_key_down(key):
    # etc.

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]

        elif adjacent == box:
            if beyond == empty: #nytt 🔲
                level[player_y][player_x] = next_current[current]
                level[player_y + dy][player_x + dx] = player
                level[player_y + dy + dy][player_x + dx + dx] = box
            elif beyond == storage: #nytt 🔲
                level[player_y][player_x] = next_current[current] #nytt 🔲
                level[player_y + dy][player_x + dx] = player #nytt 🔲
                level[player_y + dy + dy][player_x + dx + dx] = box_on_storage #nytt 🔲
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun

# Globala variabler här nedanför
level = [
    ['#', '#', '#', '#', '#'],
    ['#', '@', ' ', '.', '#'],
    ['#', ' ', '$', ' ', '#'],
    ['#', '.', '$', ' ', '#'],
    ['#', ' ', '$', '.', '#'],
    ['#', '.', '$', '.', '#'],
    ['#', '.', '*', ' ', '#'],
    ['#', ' ', '*', '.', '#'],
    ['#', ' ', '*', ' ', '#'],
    ['#', '.', '*', '.', '#'],
    ['#', '#', '#', '#', '#'],
]

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför


def on_key_down(key):
    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        beyond = ''
        if (
            0 <= player_y + dy + dy < len(level)
            and 0 <= player_x + dx + dx < len(level[player_y + dy + dy])
        ):
            beyond = level[player_y + dy + dy][player_x + dx + dx]

        next_adjacent = {
            empty: player,
            storage: player_on_storage,
        }
        next_current = {
            player: empty,
            player_on_storage: storage,
        }

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]

        elif adjacent == box:
            if beyond == empty:
                level[player_y][player_x] = next_current[current]
                level[player_y + dy][player_x + dx] = player
                level[player_y + dy + dy][player_x + dx + dx] = box
            elif beyond == storage:
                level[player_y][player_x] = next_current[current]
                level[player_y + dy][player_x + dx] = player
                level[player_y + dy + dy][player_x + dx + dx] = box_on_storage


def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )

# Kod för att starta appen här nedanför


pgzrun.go()  # måste vara sista raden
```

</details>


![image](https://user-images.githubusercontent.com/4598641/226442270-45099ac7-095b-4291-a2e4-344aa34e1862.png)


## Förenkla koden

Vi gör en ordlista som ger nästa celltyp när den indexeras av den aktuella celltypen.

✏️ Uppdatera koden. Fungerar koden som innan?

```python
def on_key_down(key):
    # etc.

        next_beyond = { #nytt 🔲
            empty: box, #nytt 🔲
            storage: box_on_storage, #nytt 🔲
        } #nytt 🔲

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]

        elif adjacent == box and beyond in next_beyond: #nytt 🔲
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = player
            level[player_y + dy + dy][player_x + dx + dx] = next_beyond[beyond] #nytt 🔲
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun

# Globala variabler här nedanför
level = [
    ['#', '#', '#', '#', '#'],
    ['#', '@', ' ', '.', '#'],
    ['#', ' ', '$', ' ', '#'],
    ['#', '.', '$', ' ', '#'],
    ['#', ' ', '$', '.', '#'],
    ['#', '.', '$', '.', '#'],
    ['#', '.', '*', ' ', '#'],
    ['#', ' ', '*', '.', '#'],
    ['#', ' ', '*', ' ', '#'],
    ['#', '.', '*', '.', '#'],
    ['#', '#', '#', '#', '#'],
]

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför


def on_key_down(key):
    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        beyond = ''
        if (
            0 <= player_y + dy + dy < len(level)
            and 0 <= player_x + dx + dx < len(level[player_y + dy + dy])
        ):
            beyond = level[player_y + dy + dy][player_x + dx + dx]

        next_adjacent = {
            empty: player,
            storage: player_on_storage,
        }
        next_current = {
            player: empty,
            player_on_storage: storage,
        }

        next_beyond = {
            empty: box,
            storage: box_on_storage,
        }

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]

        elif adjacent == box and beyond in next_beyond:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = player
            level[player_y + dy + dy][player_x + dx + dx] = next_beyond[beyond]


def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )

# Kod för att starta appen här nedanför


pgzrun.go()  # måste vara sista raden
```

</details>

## Putta lådan till en lagerplats
Om den intilliggande cellen är en låda på lagerplats, så sätts den intilliggande cellen till `player_on_storage`. Spelaren står då på en (tom) lagerplats.

✏️ Uppdatera koden. Vad händer när du ...?

```python
def on_key_down(key):
    # etc.

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]

        elif beyond in next_beyond:
            level[player_y][player_x] = next_current[current]

            if adjacent == box: #nytt 🔲
                level[player_y + dy][player_x + dx] = player
            elif adjacent == box_on_storage: #nytt 🔲
                level[player_y + dy][player_x + dx] = player_on_storage #nytt 🔲

            level[player_y + dy + dy][player_x + dx + dx] = next_beyond[beyond]
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun

# Globala variabler här nedanför
level = [
    ['#', '#', '#', '#', '#'],
    ['#', '@', ' ', '.', '#'],
    ['#', ' ', '$', ' ', '#'],
    ['#', '.', '$', ' ', '#'],
    ['#', ' ', '$', '.', '#'],
    ['#', '.', '$', '.', '#'],
    ['#', '.', '*', ' ', '#'],
    ['#', ' ', '*', '.', '#'],
    ['#', ' ', '*', ' ', '#'],
    ['#', '.', '*', '.', '#'],
    ['#', '#', '#', '#', '#'],
]

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför


def on_key_down(key):
    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        beyond = ''
        if (
            0 <= player_y + dy + dy < len(level)
            and 0 <= player_x + dx + dx < len(level[player_y + dy + dy])
        ):
            beyond = level[player_y + dy + dy][player_x + dx + dx]

        next_adjacent = {
            empty: player,
            storage: player_on_storage,
        }
        next_current = {
            player: empty,
            player_on_storage: storage,
        }

        next_beyond = {
            empty: box,
            storage: box_on_storage,
        }

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]

        elif adjacent == box and beyond in next_beyond:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = player
            level[player_y + dy + dy][player_x + dx + dx] = next_beyond[beyond]


def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )

# Kod för att starta appen här nedanför

pgzrun.go()  # måste vara sista raden
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226442358-30a184b9-f44a-4b1f-b418-b73c8b0cd8b9.png)

## Förenkla koden
En ordlista skapas som returnerar nästa intilliggande celltyp när en ruta trycks när den indexeras av den aktuella intilliggande celltypen.

✏️ Uppdatera koden. Vad händer när du ...?
#nytt 🔲
```python
def on_key_down(key):
    # etc.

        next_adjacent_push = { #nytt 🔲
            box: player, #nytt 🔲
            box_on_storage: player_on_storage, #nytt 🔲
        } #nytt 🔲

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]

        elif beyond in next_beyond and adjacent in next_adjacent_push: #nytt 🔲
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent_push[adjacent] #nytt 🔲
            level[player_y + dy + dy][player_x + dx + dx] = next_beyond[beyond]
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun

# Globala variabler här nedanför
level = [
    ['#', '#', '#', '#', '#'],
    ['#', '@', ' ', '.', '#'],
    ['#', ' ', '$', ' ', '#'],
    ['#', '.', '$', ' ', '#'],
    ['#', ' ', '$', '.', '#'],
    ['#', '.', '$', '.', '#'],
    ['#', '.', '*', ' ', '#'],
    ['#', ' ', '*', '.', '#'],
    ['#', ' ', '*', ' ', '#'],
    ['#', '.', '*', '.', '#'],
    ['#', '#', '#', '#', '#'],
]

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför


def on_key_down(key):
    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        beyond = ''
        if (
            0 <= player_y + dy + dy < len(level)
            and 0 <= player_x + dx + dx < len(level[player_y + dy + dy])
        ):
            beyond = level[player_y + dy + dy][player_x + dx + dx]

        next_adjacent = {
            empty: player,
            storage: player_on_storage,
        }

        next_current = {
            player: empty,
            player_on_storage: storage,
        }

        next_beyond = {
            empty: box,
            storage: box_on_storage,
        }

        next_adjacent_push = {
            box: player,
            box_on_storage: player_on_storage,
        }

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]

        elif beyond in next_beyond and adjacent in next_adjacent_push:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent_push[adjacent]
            level[player_y + dy + dy][player_x + dx + dx] = next_beyond[beyond]


def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )

# Kod för att starta appen här nedanför


pgzrun.go()  # måste vara sista raden
```

</details>

## Ladda spelnivåer från en lista
Nivåerna sparas i en lista.

Numret på den aktuella nivån sparas också.

Den aktuella nivån kopieras från listan som innehåller alla nivåer.

Kopieringsmodulen importeras så att [Pythons `copy.deepcopy`](https://docs.python.org/3/library/copy.html) kan användas.
>Varför behövs deepcopy? För att kunna återställa nivån till sitt ursprungliga utseende behöver vi en egen kopia av nivån och det får vi med hjälp av Pythons `deepcopy`-funktion. 

✏️ Uppdatera koden. Kommer du till första nivån när du testkör?

```python
import pgzrun
import copy #nytt 🔲

# Globala variabler här nedanför
levels = [ #ny variabel 🔲
    [
        [' ', ' ', '#', '#', '#'],
        [' ', ' ', '#', '.', '#'],
        [' ', ' ', '#', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '$', ' ', '$', '.', '#'],
        ['#', '.', ' ', '$', '@', '#', '#', '#'],
        ['#', '#', '#', '#', '$', '#'],
        [' ', ' ', ' ', '#', '.', '#'],
        [' ', ' ', ' ', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', '@', '$', '$', '#', ' ', '#', '#', '#'],
        ['#', ' ', '$', ' ', '#', ' ', '#', '.', '#'],
        ['#', '#', '#', ' ', '#', '#', '#', '.', '#'],
        [' ', '#', '#', ' ', ' ', ' ', ' ', '.', '#'],
        [' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', '#', '$', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '@', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '.', '.', '#', ' ', '$', ' ', '#', '#'],
        ['#', '#', '.', '.', '#', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
]

current_level = 0 #nytt 🔲

level = copy.deepcopy(levels[current_level]) #nytt 🔲
# etc.
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun
import copy

# Globala variabler här nedanför
levels = [
    [
        [' ', ' ', '#', '#', '#'],
        [' ', ' ', '#', '.', '#'],
        [' ', ' ', '#', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '$', ' ', '$', '.', '#'],
        ['#', '.', ' ', '$', '@', '#', '#', '#'],
        ['#', '#', '#', '#', '$', '#'],
        [' ', ' ', ' ', '#', '.', '#'],
        [' ', ' ', ' ', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', '@', '$', '$', '#', ' ', '#', '#', '#'],
        ['#', ' ', '$', ' ', '#', ' ', '#', '.', '#'],
        ['#', '#', '#', ' ', '#', '#', '#', '.', '#'],
        [' ', '#', '#', ' ', ' ', ' ', ' ', '.', '#'],
        [' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', '#', '$', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '@', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '.', '.', '#', ' ', '$', ' ', '#', '#'],
        ['#', '#', '.', '.', '#', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
]

current_level = 0

level = copy.deepcopy(levels[current_level])
player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför


def on_key_down(key):
    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        beyond = ''
        if (
            0 <= player_y + dy + dy < len(level)
            and 0 <= player_x + dx + dx < len(level[player_y + dy + dy])
        ):
            beyond = level[player_y + dy + dy][player_x + dx + dx]

        next_adjacent = {
            empty: player,
            storage: player_on_storage,
        }

        next_current = {
            player: empty,
            player_on_storage: storage,
        }

        next_beyond = {
            empty: box,
            storage: box_on_storage,
        }

        next_adjacent_push = {
            box: player,
            box_on_storage: player_on_storage,
        }

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]

        elif beyond in next_beyond and adjacent in next_adjacent_push:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent_push[adjacent]
            level[player_y + dy + dy][player_x + dx + dx] = next_beyond[beyond]


def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )

# Kod för att starta appen här nedanför

pgzrun.go()  # måste vara sista raden
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226442656-f303feef-223f-4342-a498-17eb88ffb112.png)

## Återställ nivån
När R-tangenten trycks ned återställs nivån.

Koden för att kopiera den aktuella nivån återanvänds, så vi gör en funktion av det.


✏️ Uppdatera koden. Vad händer när du trycker på `R`?

```python
# etc.
# Funktioner här nedanför
def load_level(): #nytt 🔲
    global level #nytt 🔲
    level = copy.deepcopy(levels[current_level]) #flyttad 🔲

# etc.

def on_key_down(key):
        elif beyond in next_beyond and adjacent in next_adjacent_push:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent_push[adjacent]
            level[player_y + dy + dy][player_x + dx + dx] = next_beyond[beyond]

    elif key == keys.R: #nytt 🔲
        load_level() #nytt 🔲

# etc.
# Kod för att starta appen här nedanför
load_level() #nytt 🔲

pgzrun.go()  # måste vara sista raden
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun
import copy

# Globala variabler här nedanför
levels = [
    [
        [' ', ' ', '#', '#', '#'],
        [' ', ' ', '#', '.', '#'],
        [' ', ' ', '#', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '$', ' ', '$', '.', '#'],
        ['#', '.', ' ', '$', '@', '#', '#', '#'],
        ['#', '#', '#', '#', '$', '#'],
        [' ', ' ', ' ', '#', '.', '#'],
        [' ', ' ', ' ', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', '@', '$', '$', '#', ' ', '#', '#', '#'],
        ['#', ' ', '$', ' ', '#', ' ', '#', '.', '#'],
        ['#', '#', '#', ' ', '#', '#', '#', '.', '#'],
        [' ', '#', '#', ' ', ' ', ' ', ' ', '.', '#'],
        [' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', '#', '$', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '@', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '.', '.', '#', ' ', '$', ' ', '#', '#'],
        ['#', '#', '.', '.', '#', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
]

current_level = 0

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför
def load_level():
    global level
    level = copy.deepcopy(levels[current_level])


def on_key_down(key):
    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        beyond = ''
        if (
            0 <= player_y + dy + dy < len(level)
            and 0 <= player_x + dx + dx < len(level[player_y + dy + dy])
        ):
            beyond = level[player_y + dy + dy][player_x + dx + dx]

        next_adjacent = {
            empty: player,
            storage: player_on_storage,
        }

        next_current = {
            player: empty,
            player_on_storage: storage,
        }

        next_beyond = {
            empty: box,
            storage: box_on_storage,
        }

        next_adjacent_push = {
            box: player,
            box_on_storage: player_on_storage,
        }

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]

        elif beyond in next_beyond and adjacent in next_adjacent_push:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent_push[adjacent]
            level[player_y + dy + dy][player_x + dx + dx] = next_beyond[beyond]

    elif key == keys.R:
        load_level()


def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )

# Kod för att starta appen här nedanför
load_level()

pgzrun.go()  # måste vara sista raden
```

</details>

## Nästa och föregående nivå
När spelaren trycker `N`, laddas nästa spelnivå. När `P`-tangenten trycks, laddas föregående spelnivå.

✏️ Uppdatera koden. Vad händer när du trycker på `P` eller `N` en eller flera gånger?

```python
def on_key_down(key):
    global current_level #nytt 🔲

    # etc.

    elif key == keys.N: #nytt 🔲
        current_level += 1 #nytt 🔲
        load_level() #nytt 🔲

    elif key == keys.P: #nytt 🔲
        current_level -= 1 #nytt 🔲
        load_level() #nytt 🔲
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun
import copy

# Globala variabler här nedanför
levels = [
    [
        [' ', ' ', '#', '#', '#'],
        [' ', ' ', '#', '.', '#'],
        [' ', ' ', '#', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '$', ' ', '$', '.', '#'],
        ['#', '.', ' ', '$', '@', '#', '#', '#'],
        ['#', '#', '#', '#', '$', '#'],
        [' ', ' ', ' ', '#', '.', '#'],
        [' ', ' ', ' ', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', '@', '$', '$', '#', ' ', '#', '#', '#'],
        ['#', ' ', '$', ' ', '#', ' ', '#', '.', '#'],
        ['#', '#', '#', ' ', '#', '#', '#', '.', '#'],
        [' ', '#', '#', ' ', ' ', ' ', ' ', '.', '#'],
        [' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', '#', '$', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '@', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '.', '.', '#', ' ', '$', ' ', '#', '#'],
        ['#', '#', '.', '.', '#', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
]

current_level = 0

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför


def load_level():
    global level
    level = copy.deepcopy(levels[current_level])


def on_key_down(key):
    global current_level

    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        beyond = ''
        if (
            0 <= player_y + dy + dy < len(level)
            and 0 <= player_x + dx + dx < len(level[player_y + dy + dy])
        ):
            beyond = level[player_y + dy + dy][player_x + dx + dx]

        next_adjacent = {
            empty: player,
            storage: player_on_storage,
        }

        next_current = {
            player: empty,
            player_on_storage: storage,
        }

        next_beyond = {
            empty: box,
            storage: box_on_storage,
        }

        next_adjacent_push = {
            box: player,
            box_on_storage: player_on_storage,
        }

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]

        elif beyond in next_beyond and adjacent in next_adjacent_push:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent_push[adjacent]
            level[player_y + dy + dy][player_x + dx + dx] = next_beyond[beyond]

    elif key == keys.R:
        load_level()

    elif key == keys.N:
        current_level += 1
        load_level()

    elif key == keys.P:
        current_level -= 1
        load_level()


def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )


# Kod för att starta appen här nedanför
load_level()

pgzrun.go()  # måste vara sista raden
```

</details>


## Slå över när vi går till nästa och föregående nivå
Om nästa nivå är efter den sista nivån laddas den första nivån.

Om den föregående nivån är före den första nivån laddas den sista nivån.

✏️ Uppdatera koden. Vad händer när du startar spelet och försöker backa en nivå med `P`?

```python
def on_key_down(key):
    # etc.

    elif key == keys.N:
        current_level += 1
        if current_level >= len(levels): #nytt 🔲
            current_level = 0 #nytt 🔲
        load_level()

    elif key == keys.P:
        current_level -= 1
        if current_level < 0: #nytt 🔲
            current_level = len(levels) - 1 #nytt 🔲
        load_level()
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun
import copy

# Globala variabler här nedanför
levels = [
    [
        [' ', ' ', '#', '#', '#'],
        [' ', ' ', '#', '.', '#'],
        [' ', ' ', '#', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '$', ' ', '$', '.', '#'],
        ['#', '.', ' ', '$', '@', '#', '#', '#'],
        ['#', '#', '#', '#', '$', '#'],
        [' ', ' ', ' ', '#', '.', '#'],
        [' ', ' ', ' ', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', '@', '$', '$', '#', ' ', '#', '#', '#'],
        ['#', ' ', '$', ' ', '#', ' ', '#', '.', '#'],
        ['#', '#', '#', ' ', '#', '#', '#', '.', '#'],
        [' ', '#', '#', ' ', ' ', ' ', ' ', '.', '#'],
        [' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', '#', '$', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '@', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '.', '.', '#', ' ', '$', ' ', '#', '#'],
        ['#', '#', '.', '.', '#', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
]

current_level = 0

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför


def load_level():
    global level
    level = copy.deepcopy(levels[current_level])


def on_key_down(key):
    global current_level

    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        beyond = ''
        if (
            0 <= player_y + dy + dy < len(level)
            and 0 <= player_x + dx + dx < len(level[player_y + dy + dy])
        ):
            beyond = level[player_y + dy + dy][player_x + dx + dx]

        next_adjacent = {
            empty: player,
            storage: player_on_storage,
        }

        next_current = {
            player: empty,
            player_on_storage: storage,
        }

        next_beyond = {
            empty: box,
            storage: box_on_storage,
        }

        next_adjacent_push = {
            box: player,
            box_on_storage: player_on_storage,
        }

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]

        elif beyond in next_beyond and adjacent in next_adjacent_push:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent_push[adjacent]
            level[player_y + dy + dy][player_x + dx + dx] = next_beyond[beyond]

    elif key == keys.R:
        load_level()

    elif key == keys.N:
        current_level += 1
        if current_level >= len(levels):
            current_level = 0
        load_level()

    elif key == keys.P:
        current_level -= 1
        if current_level < 0:
            current_level = len(levels) - 1
        load_level()


def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )


# Kod för att starta appen här nedanför
load_level()

pgzrun.go()  # måste vara sista raden
```

</details>

## Gå till nästa nivå när en nivå är avklarad
Efter varje drag går vi igenom alla cellerna. 
   
Om ingen av cellerna är lådor,  dvs. alla lådor är på lagerplats, är nivån klar och nästa nivå laddas.

✏️ Uppdatera koden. Vad händer när du klarar en nivå?

```python
def on_key_down(key):
    # etc.

        elif beyond in next_beyond and adjacent in next_adjacent_push:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent_push[adjacent]
            level[player_y + dy + dy][player_x + dx + dx] = next_beyond[beyond]

        complete = True #nytt 🔲

        for y, row in enumerate(level): #nytt 🔲
            for x, cell in enumerate(row): #nytt 🔲
                if cell == box: #nytt 🔲
                    complete = False #nytt 🔲

        if complete: #nytt 🔲
            current_level += 1 #nytt 🔲
            if current_level >= len(levels): #nytt 🔲
                current_level = 0 #nytt 🔲
            load_level() #nytt 🔲 
    
    elif key == keys.R:
        load_level()
    # etc.
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun
import copy

# Globala variabler här nedanför
levels = [
    [
        [' ', ' ', '#', '#', '#'],
        [' ', ' ', '#', '.', '#'],
        [' ', ' ', '#', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '$', ' ', '$', '.', '#'],
        ['#', '.', ' ', '$', '@', '#', '#', '#'],
        ['#', '#', '#', '#', '$', '#'],
        [' ', ' ', ' ', '#', '.', '#'],
        [' ', ' ', ' ', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', '@', '$', '$', '#', ' ', '#', '#', '#'],
        ['#', ' ', '$', ' ', '#', ' ', '#', '.', '#'],
        ['#', '#', '#', ' ', '#', '#', '#', '.', '#'],
        [' ', '#', '#', ' ', ' ', ' ', ' ', '.', '#'],
        [' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', '#', '$', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '@', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '.', '.', '#', ' ', '$', ' ', '#', '#'],
        ['#', '#', '.', '.', '#', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
]

current_level = 0

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför


def load_level():
    global level
    level = copy.deepcopy(levels[current_level])


def on_key_down(key):
    global current_level

    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        beyond = ''
        if (
            0 <= player_y + dy + dy < len(level)
            and 0 <= player_x + dx + dx < len(level[player_y + dy + dy])
        ):
            beyond = level[player_y + dy + dy][player_x + dx + dx]

        next_adjacent = {
            empty: player,
            storage: player_on_storage,
        }

        next_current = {
            player: empty,
            player_on_storage: storage,
        }

        next_beyond = {
            empty: box,
            storage: box_on_storage,
        }

        next_adjacent_push = {
            box: player,
            box_on_storage: player_on_storage,
        }

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]

        elif beyond in next_beyond and adjacent in next_adjacent_push:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent_push[adjacent]
            level[player_y + dy + dy][player_x + dx + dx] = next_beyond[beyond]

        complete = True

        for y, row in enumerate(level):
            for x, cell in enumerate(row):
                if cell == box:
                    complete = False

        if complete:
            current_level += 1
            if current_level >= len(levels):
                current_level = 0
            load_level()

    elif key == keys.R:
        load_level()

    elif key == keys.N:
        current_level += 1
        if current_level >= len(levels):
            current_level = 0
        load_level()

    elif key == keys.P:
        current_level -= 1
        if current_level < 0:
            current_level = len(levels) - 1
        load_level()


def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )


# Kod för att starta appen här nedanför
load_level()

pgzrun.go()  # måste vara sista raden
```

</details>

## Fler nivåer

Lägg till hela uppsättningen med nivåer och testkör.

<details>
  <summary>✏️ Klipp och klistra in variabeln `levels` med alla nivåerna &ndash; du behöver inte mata in det för hand. Testkör!</summary>
   
```python
import pgzrun
import copy

# Globala variabler här nedanför
levels = [ #nytt 🔲
    [
        [' ', ' ', '#', '#', '#'],
        [' ', ' ', '#', '.', '#'],
        [' ', ' ', '#', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '$', ' ', '$', '.', '#'],
        ['#', '.', ' ', '$', '@', '#', '#', '#'],
        ['#', '#', '#', '#', '$', '#'],
        [' ', ' ', ' ', '#', '.', '#'],
        [' ', ' ', ' ', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', '@', '$', '$', '#', ' ', '#', '#', '#'],
        ['#', ' ', '$', ' ', '#', ' ', '#', '.', '#'],
        ['#', '#', '#', ' ', '#', '#', '#', '.', '#'],
        [' ', '#', '#', ' ', ' ', ' ', ' ', '.', '#'],
        [' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', '#', '$', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '@', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '.', '.', '#', ' ', '$', ' ', '#', '#'],
        ['#', '#', '.', '.', '#', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', ' ', ' ', '.', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', '*', '#'],
        ['#', ' ', '$', '$', ' ', '$', '.', '#'],
        ['#', '#', '@', '#', '#', '.', '.', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#'],
        [' ', '#', '@', ' ', '#', '#', '#'],
        [' ', '#', ' ', '$', ' ', ' ', '#'],
        ['#', '#', '#', ' ', '#', ' ', '#', '#'],
        ['#', '.', '#', ' ', '#', ' ', ' ', '#'],
        ['#', '.', '$', ' ', ' ', '#', ' ', '#'],
        ['#', '.', ' ', ' ', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', '#', ' ', ' ', '#', ' ', '@', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', ' ', '#', '$', ' ', '$', ' ', '$', ' ', '#'],
        [' ', ' ', '#', ' ', '$', '#', '#', ' ', ' ', '#'],
        ['#', '#', '#', ' ', '$', ' ', '#', ' ', '#', '#'],
        ['#', '.', '.', '.', '.', '.', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '.', ' ', '$', '#', '#', ' ', '#', '#'],
        ['#', '.', '.', '$', ' ', '$', ' ', ' ', '@', '#'],
        ['#', '.', '.', ' ', '$', ' ', '$', ' ', '#', '#'],
        ['#', '#', '#', '#', '#', '#', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '$', '$', '$', ' ', '#'],
        ['#', '@', ' ', '$', '.', '.', ' ', '#'],
        ['#', ' ', '$', '.', '.', '.', '#', '#'],
        ['#', '#', '#', '#', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', '#', '.', '.', '#'],
        [' ', '#', '#', ' ', '.', '#', '#'],
        [' ', '#', ' ', ' ', '$', '.', '#'],
        ['#', '#', ' ', '$', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', '#', '$', '$', ' ', '#'],
        ['#', ' ', ' ', '@', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', '#', ' ', ' ', '@', '#'],
        ['#', ' ', ' ', '$', '.', ' ', '#', '#'],
        ['#', ' ', ' ', '.', '$', '.', ' ', '#'],
        ['#', '#', '#', ' ', '*', '$', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', '#', '#'],
        [' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', '.', '.', '$', ' ', '#'],
        ['#', '@', '$', '.', '*', ' ', '#', '#'],
        ['#', ' ', '$', '.', '.', '$', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', '#'],
        [' ', ' ', '#', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', ' ', '$', ' ', '#', '#', ' ', '#'],
        ['#', '.', '.', '.', ' ', '$', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '.', '$', '#', '$', ' ', '#', '#'],
        ['#', '#', '#', '#', ' ', '#', ' ', '$', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', '@', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', '$', '$', '#', '#'],
        ['#', ' ', ' ', '#', '.', '.', '#', '#', '#'],
        ['#', '#', ' ', ' ', '.', '.', '$', ' ', '#'],
        [' ', '#', ' ', '@', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', '#', '.', ' ', '#'],
        [' ', '#', '#', ' ', ' ', '$', '.', '.', '.', '#'],
        [' ', '#', ' ', ' ', '$', ' ', '#', '*', '.', '#'],
        ['#', '#', ' ', '#', '#', '$', '#', ' ', '#', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '@', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '.', '.', '.', '.', ' ', '#'],
        ['#', '#', '#', '.', '.', '.', '$', '#', '#', '#'],
        ['#', ' ', ' ', '$', '#', '$', ' ', '$', ' ', '#'],
        ['#', ' ', '$', '$', ' ', ' ', '#', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', '@', ' ', '#', '#', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', ' ', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '$', ' ', '$', '@', '#'],
        ['#', '$', '#', '$', '$', '$', '#', '#'],
        ['#', '.', '.', '$', ' ', '$', ' ', '#'],
        ['#', '.', '.', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', '$', '$', ' ', ' ', '#'],
        ['#', ' ', '.', '.', '.', '#', ' ', '#'],
        ['#', '#', '.', '.', '.', '$', ' ', '#', '#'],
        [' ', '#', ' ', '#', '#', ' ', '$', ' ', '#'],
        [' ', '#', '$', ' ', ' ', '$', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', ' ', ' ', '@', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', '$', ' ', '@', '#'],
        ['#', '#', '#', '$', '$', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', '.', '.', '#'],
        [' ', ' ', '#', '.', '.', '.', '.', '#'],
        [' ', ' ', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '*', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', '.', '$', '.', ' ', '@', '#'],
        ['#', ' ', '.', '$', '.', '$', '.', ' ', '#'],
        ['#', ' ', '$', '.', '$', '.', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', '*', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', '$', '#', '$', ' ', '#'],
        ['#', ' ', '$', '$', ' ', ' ', '.', '$', '.', '#'],
        ['#', ' ', '@', '#', '#', '#', '.', '.', '.', '#'],
        ['#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '.', ' ', '.', '.', '#'],
        [' ', '#', '.', ' ', '$', '.', '#'],
        ['#', '#', '#', ' ', ' ', '$', '#', '#'],
        ['#', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '#', '$', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '@', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
        ['#', '#', ' ', '#', '$', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', '$', '$', ' ', '#'],
        ['#', ' ', '#', '$', '#', '.', '*', '.', '#'],
        ['#', ' ', ' ', ' ', '@', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', '$', ' ', '$', ' ', ' ', ' ', '#'],
        ['#', '@', '#', '.', '*', '.', '#', ' ', '#'],
        ['#', ' ', '#', '.', '*', '.', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', '$', ' ', '#'],
        ['#', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '.', ' ', ' ', '#', '#'],
        ['#', ' ', '$', '.', '$', '.', ' ', ' ', '#'],
        ['#', '@', '$', '#', ' ', '#', '$', ' ', '#'],
        ['#', ' ', '$', '.', ' ', '.', ' ', ' ', '#'],
        ['#', '#', '#', '#', '$', '#', '$', ' ', '#'],
        [' ', ' ', '#', '.', ' ', '.', ' ', ' ', '#'],
        [' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', ' ', ' ', ' ', ' ', '.', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '$', ' ', '$', '.', ' ', '#'],
        ['#', ' ', ' ', '.', '#', '#', '#', '#', '.', '#', '#'],
        ['#', ' ', '$', '.', '$', ' ', '$', ' ', '@', '#'],
        ['#', ' ', ' ', '.', ' ', ' ', ' ', ' ', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', ' ', '$', ' ', '.', '*', '.', ' ', '$', ' ', '#'],
        ['#', '@', '$', '.', '*', ' ', '*', '.', '$', ' ', '#'],
        ['#', ' ', '$', ' ', '.', '*', '.', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', '#', '#', '#', '#'],
        ['#', ' ', '$', '*', '.', '.', '*', ' ', '#'],
        ['#', ' ', '*', '.', '.', '*', '$', ' ', '#'],
        ['#', '#', '#', '#', ' ', ' ', '$', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', '@', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '.', ' ', ' ', '@', '#'],
        ['#', ' ', ' ', '$', '$', '$', ' ', ' ', '#'],
        ['#', '.', '#', '#', '.', '#', '#', '.', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', '.', '#', ' ', '#', '#'],
        ['#', '#', '#', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', ' ', ' ', '$', '.', ' ', '@', '#'],
        ['#', ' ', '.', '$', '.', '$', ' ', ' ', '#'],
        ['#', '#', '$', '.', '$', ' ', '$', '#', '#'],
        ['#', ' ', '.', '$', '.', '$', ' ', ' ', '#'],
        ['#', '.', ' ', ' ', '$', '.', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', '@', ' ', ' ', '#'],
        ['#', '#', '$', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', '$', '$', '#', '#'],
        ['#', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', '$', ' ', '#', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', '@', '$', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', '#', '$', ' ', '#'],
        ['#', '#', '#', '.', '#', '#', ' ', '#', '#', '#'],
        [' ', '#', '.', '.', '.', '$', ' ', '$', ' ', '#'],
        [' ', '#', '#', '.', '.', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', '#', '.', '.', ' ', '#', '#'],
        ['#', ' ', '$', '.', ' ', '$', '*', ' ', '#'],
        ['#', ' ', ' ', '$', '@', '$', ' ', ' ', '#'],
        ['#', ' ', '*', '$', ' ', '.', '$', ' ', '#'],
        ['#', '#', ' ', '.', '.', '#', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', ' ', ' ', '*', ' ', ' ', '#', '#'],
        ['#', ' ', '.', ' ', '.', ' ', '.', ' ', '#'],
        ['#', ' ', '$', ' ', '*', ' ', ' ', ' ', '#'],
        ['#', '*', '$', '$', '*', '$', '$', '*', '#'],
        ['#', ' ', ' ', ' ', '*', ' ', '$', ' ', '#'],
        ['#', ' ', '.', ' ', '.', '@', '.', ' ', '#'],
        ['#', '#', ' ', ' ', '*', ' ', ' ', '#', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '.', '$', ' ', '@', '#'],
        ['#', ' ', '$', ' ', '*', ' ', '$', ' ', '#'],
        ['#', '*', '.', '.', '.', '*', '.', '*', '#'],
        ['#', ' ', '$', '$', '*', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '.', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#', '.', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', '.', '.', '#', '#', ' ', '#'],
        [' ', '#', ' ', ' ', '$', '.', '.', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', ' ', '.', '#', ' ', '#', '#'],
        ['#', '#', '#', ' ', '#', '#', '$', '#', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', ' ', '$', '$', ' ', '#'],
        ['#', ' ', '#', '$', '#', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', '@', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', ' ', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', '#', '#', '#', '$', ' ', '#', '#', '#'],
        ['#', ' ', '$', ' ', '$', ' ', ' ', '$', '$', ' ', '#'],
        ['#', '@', ' ', '$', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', '$', ' ', ' ', ' ', '#'],
        [' ', '#', '$', ' ', '#', '#', '#', ' ', '$', '#'],
        [' ', '#', ' ', '#', '.', '.', '.', '#', ' ', '#'],
        ['#', '#', ' ', '#', '.', '.', '.', '#', ' ', '#', '#'],
        ['#', ' ', '$', ' ', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '@', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', '#', '.', '$', '$', '$', ' ', '#'],
        ['#', ' ', '#', '.', '*', '#', ' ', '#', '#', '#'],
        ['#', ' ', ' ', '.', '.', '#', ' ', '#'],
        ['#', '#', '#', '.', '.', '$', ' ', '#', '#'],
        [' ', ' ', '#', '.', '#', ' ', '$', ' ', '#'],
        [' ', '#', '#', ' ', '#', ' ', '#', '@', '#'],
        [' ', '#', ' ', '$', ' ', ' ', '$', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '@', ' ', '$', '$', '$', ' ', '$', ' ', ' ', '#'],
        ['#', '#', ' ', '$', ' ', ' ', '$', ' ', '$', ' ', '#'],
        [' ', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', '$', ' ', '#', '#'],
        ['#', '#', '#', ' ', '#', '#', '$', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '@', ' ', '$', '#', ' ', '#'],
        ['#', '#', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', '#', '.', '#', ' ', '#'],
        ['#', ' ', ' ', '.', '*', '.', '$', '#'],
        ['#', '#', ' ', '#', '.', '#', ' ', '#'],
        [' ', '#', ' ', '#', '.', ' ', ' ', '#', '#'],
        ['#', '#', ' ', '$', '.', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', '#', '#', '#'],
        ['#', ' ', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '@', ' ', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '.', '#', '#', '#', ' ', '#', '#'],
        ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', '#', ' ', '$', ' ', '$', '#', '.', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', '*', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', '.', '#', '$', ' ', '$', ' ', '#', ' ', '#'],
        ['#', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'],
        [' ', '#', ' ', '#', '#', '#', '.', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '$', ' ', '@', '#'],
        ['#', '#', '#', '.', ' ', '#'],
        [' ', ' ', '#', '.', '#', '#'],
        [' ', ' ', '#', '.', ' ', '#'],
        ['#', '#', '#', '.', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', '#', '#'],
        [' ', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#'],
        ['#', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '.', ' ', ' ', '#', ' ', '#'],
        ['#', '#', '$', '#', ' ', ' ', '.', '#'],
        [' ', '#', ' ', '#', '$', '#', ' ', '#'],
        ['#', '#', '.', ' ', ' ', '.', ' ', '#'],
        ['#', ' ', ' ', '#', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', '*', '#'],
        ['#', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '$', '#', '*', ' ', '@', '#'],
        ['#', ' ', ' ', '#', '.', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#'],
        [' ', ' ', ' ', '#', '.', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '.', '$', ' ', '#', ' ', ' ', '#'],
        [' ', '#', '.', '.', '.', ' ', ' ', '#', '$', ' ', '#'],
        [' ', '#', '.', '#', '#', ' ', '$', ' ', ' ', ' ', '#'],
        ['#', '#', '.', '$', ' ', '$', '#', '#', ' ', '#', '#'],
        ['#', '.', '$', ' ', '#', ' ', '#', '#', ' ', '#'],
        ['#', '.', '#', '$', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '.', '$', ' ', ' ', '#', '$', ' ', '$', '#'],
        ['#', '.', ' ', '$', '#', '#', ' ', '@', ' ', '#'],
        ['#', '.', '$', ' ', ' ', ' ', ' ', '$', ' ', '#'],
        ['#', '.', ' ', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', '#', '#', '#', ' ', ' ', '#', '#'],
        [' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#'],
        [' ', '#', ' ', ' ', ' ', '#', ' ', '.', '.', '#'],
        ['#', '#', ' ', '$', '#', '*', '#', '$', '.', '#'],
        ['#', ' ', ' ', '$', ' ', '#', ' ', '$', '.', '#'],
        ['#', ' ', ' ', '$', ' ', '@', ' ', '$', '.', '#'],
        ['#', ' ', ' ', '$', ' ', '#', ' ', '$', '.', '#'],
        ['#', '#', '$', '$', '#', '*', '#', '$', '.', '#'],
        [' ', '#', '.', ' ', ' ', '#', ' ', '.', '.', '#'],
        [' ', '#', '#', '.', ' ', ' ', ' ', ' ', '#', '#'],
        [' ', ' ', '#', '#', '#', ' ', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
        ['#', ' ', '$', '$', ' ', ' ', '#', ' ', '#'],
        ['#', '@', '$', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', '#', ' ', '#', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', '$', ' ', '#'],
        ['#', ' ', '$', '#', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', '$', '#', ' ', '#'],
        ['#', '.', '.', '.', '#', ' ', ' ', ' ', '#'],
        ['#', '.', '#', '.', '#', '$', '#', '#', '#'],
        ['#', '.', '.', '.', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '.', '#'],
        ['#', ' ', '#', '$', '#', '.', '.', '#', '#'],
        ['#', ' ', ' ', ' ', '$', '.', '.', '.', '#'],
        ['#', '#', ' ', '#', '#', '.', '$', '.', '#'],
        [' ', '#', ' ', '#', '#', ' ', ' ', '#', '#'],
        [' ', '#', '$', '#', '#', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', ' ', '#', '$', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', '#', '#', '#', '#'],
        ['#', ' ', '$', ' ', '$', ' ', ' ', ' ', '@', '#'],
        ['#', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#'],
        ['#', ' ', ' ', '#', '#', '#', '#'],
        ['#', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', '#', '.', '#', ' ', '#'],
        ['#', ' ', '#', ' ', '#', ' ', '#'],
        ['#', '.', '$', '.', '$', '.', '#'],
        ['#', ' ', '#', ' ', '#', ' ', '#'],
        ['#', ' ', '#', '.', '#', ' ', '#'],
        ['#', ' ', ' ', '$', '$', ' ', '#'],
        ['#', '#', ' ', '@', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', '#', '#'],
        [' ', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', '#'],
        ['#', ' ', '$', '$', ' ', ' ', '#', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', ' ', '#', '#', ' ', '$', '#', ' ', ' ', '#'],
        [' ', '#', ' ', '#', '.', '.', '.', ' ', ' ', '#', '#'],
        [' ', '#', ' ', ' ', '.', '.', '.', '#', '$', '#', '#'],
        [' ', '#', ' ', '#', '.', '.', '.', '#', ' ', ' ', '#'],
        ['#', '#', ' ', '#', ' ', '#', '#', '#', '@', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '#', '$', '#', '#', '#', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '$', ' ', '$', ' ', '*', '.', '#'],
        ['#', '.', '*', ' ', '$', ' ', '$', '.', '.', '#'],
        ['#', '#', '.', '$', ' ', '$', ' ', '*', '#', '#'],
        [' ', '#', '*', ' ', '$', ' ', '$', '.', '#'],
        [' ', '#', '.', '$', ' ', '$', ' ', '.', '#'],
        [' ', '#', '.', ' ', '$', ' ', '$', '.', '#'],
        [' ', '#', '.', '$', '@', '$', ' ', '*', '#'],
        ['#', '#', '*', ' ', '$', ' ', '$', '.', '#', '#'],
        ['#', '.', '.', '$', ' ', '$', ' ', '*', '.', '#'],
        ['#', '.', '*', ' ', '$', ' ', '$', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', '#', '$', ' ', ' ', '#'],
        [' ', ' ', '#', '#', '#', ' ', ' ', '$', '#', '#'],
        [' ', ' ', '#', ' ', ' ', '$', ' ', '$', ' ', '#'],
        ['#', '#', '#', ' ', '#', ' ', '#', '#', ' ', '#',
            ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', '#',
            '#', '#', '#', '#', ' ', ' ', '.', '.', '#'],
        ['#', ' ', '$', ' ', ' ', '$', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', '.', '.', '#'],
        ['#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ',
            '#', '@', '#', '#', ' ', ' ', '.', '.', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', '.', '.', ' ', ' ', '#', ' ', '$', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', '.', '.', ' ', ' ', '#', '$', '#', '#', '#', '#', ' ', ' ', '#'],
        ['#', '.', '.', ' ', ' ', ' ', ' ', '@', ' ', '#', '#', ' ', ' ', '#'],
        ['#', '.', '.', ' ', ' ', '#', ' ', '#', ' ', ' ', '$', ' ', '#', '#'],
        ['#', '#', '#', '#', '#', '#', ' ', '#', '#', '$', ' ', '$', ' ', '#'],
        [' ', ' ', '#', ' ', '$', ' ', ' ', '$', ' ', '$', ' ', '$', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', ' ', ' ', ' ', ' ', ' ', '@', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', ' ', '$', '#', '$', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', ' ', '$', ' ', ' ', '$', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', '#', '$', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#',
            ' ', '$', ' ', '#', ' ', '#', '#', '#'],
        ['#', '.', '.', '.', '.', ' ', ' ', '#', '#',
            ' ', '$', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', '#', '.', '.', '.', ' ', ' ', ' ', ' ',
            '$', ' ', ' ', '$', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '.', '.', ' ', ' ', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', '#', ' ', ' ', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', ' ', ' ', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '$', ' ',
            '$', ' ', ' ', ' ', '.', '.', '.', '.', '#'],
        ['#', ' ', '$', '$', '$', '#', '$', ' ', ' ', '$',
            ' ', '#', ' ', ' ', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', '$', ' ', ' ', ' ', ' ', ' ', '$',
            ' ', '#', ' ', ' ', '.', '.', '.', '.', '#'],
        ['#', ' ', '$', '$', ' ', '#', '$', ' ', '$', ' ',
            '$', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', '$', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '$', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', '$', '$', '#', '$', '$', ' ', ' ', '@', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',
            ' ', ' ', ' ', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',
            ' ', '#', '$', '#', '#', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',
            ' ', ' ', ' ', ' ', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#',
            ' ', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '.', '.', ' ', ' ', '#', '#',
            ' ', '$', ' ', ' ', '$', '#', '#', '#'],
        ['#', '.', '.', '.', '.', ' ', ' ', ' ',
            ' ', '$', ' ', '$', '$', ' ', '#', '#'],
        ['#', '.', '.', '.', '.', ' ', ' ', '#',
            '#', '$', ' ', ' ', '$', ' ', '@', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#',
            '#', ' ', ' ', '$', ' ', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', ' ', '$', ' ', '$', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', '#', '#', ' ', '#', '#', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#'],
        ['#', '.', '.', ' ', ' ', '#', ' ', '#', '#', '@', '#', '#'],
        ['#', '.', '.', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', '.', '.', ' ', ' ', ' ', ' ', ' ', '$', '$', ' ', '#'],
        ['#', '.', '.', ' ', ' ', '#', ' ', '#', ' ', '$', ' ', '#'],
        ['#', '.', '.', '#', '#', '#', ' ', '#', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', ' ', '$', ' ', '#', '$', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', '$', '#', ' ', '$', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', '$', ' ', ' ', '$', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#', '#'],
        ['#', '#', ' ', '#', ' ', '@', '#', '#', ' ', '$', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '$', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', ' ', '#', '#', '#', '#', '#', '$', '#', '#', '#'],
        ['#', ' ', '$', ' ', ' ', '#', '#', '#', ' ', '.', '.', '#'],
        ['#', ' ', '$', ' ', '$', ' ', '$', ' ', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', '#', '#', '.', '.', '.', '#'],
        ['#', ' ', '$', '$', ' ', '#', ' ', '#', '.', '.', '.', '#'],
        ['#', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', '$',
            ' ', ' ', ' ', '$', ' ', '$', ' ', '#'],
        [' ', ' ', '#', ' ', '$', '#', ' ', '$',
            ' ', '#', ' ', ' ', '$', ' ', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', '$', ' ', '$',
            ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', ' ', '$', '#', ' ', '#',
            ' ', ' ', '#', '#', '#', '#', ' ', '#'],
        ['#', '@', '#', '$', ' ', '$', ' ', '$',
            ' ', ' ', '#', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '$', ' ', '#',
            '$', '#', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', ' ', ' ',
            ' ', '$', ' ', '$', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', '#', ' ', ' ', '#',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', '#', '.', '.', '.', '.', '.', '.', '#'],
        [' ', ' ', '#', '.', '.', '.', '.', '.', '.', '#'],
        [' ', ' ', '#', '.', '.', '.', '.', '.', '.', '#'],
        [' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', '#', ' ', ' ', '.', '.', '.', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#',
            '#', '#', ' ', ' ', '.', '.', '.', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', ' ', ' ', ' ', '.', ' ', '.', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ',
            '#', '#', ' ', ' ', '.', '.', '.', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ',
            '#', '#', ' ', ' ', '.', '.', '.', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', ' ', '$', '$', '$', ' ', '#', '#'],
        [' ', '#', '#', '#', '#', '#', ' ', ' ', '$',
            ' ', '$', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', ' ', ' ', ' ', '#', '$', ' ', '$',
            ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '@', ' ', '$', ' ', ' ', '$', ' ', ' ',
            ' ', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', ' ', '$', '$',
            ' ', '$', ' ', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', ' ', ' ', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '@', '#', '#', '#', '#', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', '$', ' ', ' ', ' ', '$', '$', ' ',
            ' ', '$', ' ', '$', ' ', '.', '.', '.', '#'],
        ['#', ' ', ' ', '$', '$', '$', '#', ' ', ' ', ' ',
            ' ', '$', ' ', ' ', '#', '.', '.', '.', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', '#', ' ', '$', '$',
            ' ', '$', '$', ' ', '#', '.', '.', '.', '#'],
        ['#', '#', '#', ' ', ' ', ' ', '#', ' ', ' ', '$',
            ' ', ' ', ' ', ' ', '#', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '$', ' ',
            '$', ' ', '$', ' ', '#', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#',
            '#', ' ', '#', '#', '#', '.', '.', '.', '#'],
        ['#', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', '$',
            ' ', '$', ' ', ' ', '#', '.', '.', '.', '#'],
        ['#', ' ', ' ', '#', '#', ' ', '#', ' ', '$', '$',
            ' ', '$', ' ', '$', '#', '#', '.', '.', '#'],
        ['#', ' ', '.', '.', '#', ' ', '#', ' ', ' ', '$',
            ' ', ' ', ' ', ' ', ' ', ' ', '#', '.', '#'],
        ['#', ' ', '.', '.', '#', ' ', '#', ' ', '$', '$',
            '$', ' ', '$', '$', '$', ' ', '#', '.', '#'],
        ['#', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', '#', ' ', '#', '.', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', ' ', '#', '.', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', '#', '.', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', '#', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '#', '#', ' ', ' ', '#', '#', '#', '$', ' ', '#'],
        [' ', ' ', '#', '#', ' ', ' ', ' ', '@', ' ', ' ', '$', ' ', ' ', '#'],
        [' ', '#', '#', ' ', ' ', '$', ' ', '$', '$', '#', '#', ' ', '#', '#'],
        [' ', '#', ' ', ' ', '#', '$', '#', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', '#', ' ', '$', ' ', '$',
            '$', ' ', '#', ' ', '#', '#', '#'],
        [' ', '#', ' ', ' ', ' ', '$', ' ', '#', ' ', ' ',
            '#', ' ', '$', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', ' ', ' ', ' ', ' ', '#', ' ',
            ' ', '$', '$', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', '#', '#', ' ', '$', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '.', ' ', ' ', ' ', ' ', '#', '#', '#', ' ',
            ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', ' ', '.', '.', '#', ' ', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '#', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', '#', '#', '#', '#',
            '#', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', '$', ' ', '$',
            ' ', '$', ' ', '$', '#', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '$', '@', '$',
            ' ', ' ', ' ', '#', '#', ' ', '#', '#'],
        ['#', ' ', '#', ' ', '#', '$', ' ', '$', ' ',
            '$', '#', '#', '#', '.', '.', '.', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '$', ' ', '$',
            ' ', ' ', '#', '#', '.', '.', '.', '#'],
        ['#', ' ', '#', '#', '#', '$', '$', '$', ' ',
            '$', ' ', '#', '#', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#',
            '#', ' ', '#', '#', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', ' ', ' ', ' ', '#',
            '#', ' ', '#', '#', '.', '.', '.', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#',
            ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', '#', ' ', ' ', ' ', '#', '#',
            ' ', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ',
            ' ', '#', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', ' ', ' ', '$', ' ', '#', '$', ' ', '#', ' ',
            ' ', '#', ' ', ' ', '.', '.', '.', ' ', '#'],
        ['#', ' ', '#', ' ', '$', '#', '@', '$', '#', '#',
            ' ', '#', ' ', '#', '.', '#', '.', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', '#', '$', ' ', ' ', '#',
            ' ', ' ', ' ', ' ', '.', ' ', '.', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', ' ', '$', ' ', '#',
            ' ', '#', ' ', '#', '.', '#', '.', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', '#', ' ', ' ', '#', '#',
            '$', ' ', '$', ' ', '.', ' ', '.', ' ', '#'],
        ['#', ' ', '$', ' ', '#', ' ', ' ', ' ', '#', ' ',
            ' ', '#', '$', '#', '.', '#', '.', ' ', '#'],
        ['#', '#', ' ', '$', ' ', ' ', '$', ' ', ' ', ' ',
            '$', ' ', ' ', '$', '.', '.', '.', ' ', '#'],
        [' ', '#', '$', ' ', '#', '#', '#', '#', '#', '#',
            ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '$', '@', '$', ' ', '#'],
        [' ', '#', '$', '$', ' ', '#', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', '#', '#', '#', '.', '.', '.',
            '.', '.', '.', '#', '#', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', '$', '.', '.', '.',
            '.', '.', '.', '#', '#', ' ', '#', ' ', '#'],
        [' ', '#', ' ', '#', '#', '#', '.', '.', '.',
            '.', '.', '.', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', ' ', '#', '#', '#', '#',
            ' ', '#', '#', '#', ' ', '#', '$', '#', '#'],
        ['#', ' ', ' ', '#', '$', ' ', ' ', ' ', '#',
            ' ', ' ', '$', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '$', '$', '$', ' ',
            ' ', '#', ' ', '$', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', '$', ' ', '#',
            '#', '#', '$', '$', ' ', '#', ' ', '#'],
        ['#', '#', '#', '#', '#', ' ', ' ', ' ', ' ',
            ' ', '$', ' ', ' ', ' ', '#', ' ', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#',
            '#', '#', ' ', ' ', ' ', '#', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#',
            '#', '#', '#', '#', '#', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', '$', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', ' ', '#', '$', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', '$', ' ', ' ', '#', '#', '$', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', ' ', '@', ' ', '$', ' ', '#', ' ', '$', '#'],
        [' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ',
            ' ', ' ', '$', ' ', '#', '#', '#', '#'],
        [' ', '#', '#', ' ', '#', '#', '#', '#', '$',
            '#', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', '$', '#', '.', '.', '.', '.',
            '.', '#', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '$', '.', '.', '*', '*',
            '.', ' ', '$', '#', ' ', '#', '#', '#'],
        ['#', '#', ' ', ' ', '#', '.', '.', '.',
            '.', '.', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', '#', '#', ' ',
            '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', '$', '$', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#'],
        ['#', ' ', '$', ' ', ' ', '#', '#', '#', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', '$', ' ', '$', ' ', ' ', ' ', '$', '#'],
        ['#', '#', '#', '@', ' ', '#', '$', ' ', ' ', ' ', ' ', '#', '#'],
        [' ', '#', ' ', ' ', '#', '#', ' ', ' ', '$', ' ', '$', ' ', '#', '#'],
        [' ', '#', ' ', '$', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '.', '#'],
        [' ', '#', ' ', ' ', '#', '$', '#', '#', '$', ' ', ' ', '#', '.', '#'],
        [' ', '#', '#', '#', ' ', ' ', ' ', '$', '.', '.', '#', '#', '.', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '.', '*', '.', '.', '.', '#'],
        [' ', ' ', '#', ' ', '$', '$', ' ', '#', '.', '.', '.', '.', '.', '#'],
        [' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', '#'],
        [' ', ' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', '.', '.', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '.', '.', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '.', '.', ' ', ' ',
            '#', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', '#', '#', '#', '#', '#', '#',
            '#', ' ', ' ', '#', ' ', ' ', '#', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', '#', ' ', ' ',
            '#', '#', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', '#', '#', ' ',
            ' ', '#', '#', '#', '#', ' ', '#', '#'],
        ['#', ' ', ' ', '$', ' ', ' ', '#', '#',
            '#', '#', '#', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', '$', ' ', ' ', '$',
            ' ', ' ', '#', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', '@', '$', ' ', ' ', '$', ' ',
            ' ', ' ', '#', ' ', ' ', ' ', '#', '#'],
        ['#', '#', '#', '#', ' ', '#', '#', ' ',
            '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', ' ', ' ',
            '.', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', ' ', '#',
            '.', ' ', ' ', ' ', ' ', '@', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', ' ', '#', '#',
            '.', '.', '#', ' ', '#', '#', '#', '#'],
        ['#', '#', ' ', ' ', '#', ' ', '.', '.', '#', '#',
            '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', ' ', '$', ' ', '#', '.', '.', '.', ' ', ' ',
            ' ', '$', ' ', '#', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '.', '.', ' ', '#', '#',
            ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#'],
        ['#', '#', '#', '#', '$', '#', '#', '$', '#', ' ',
            '$', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
        [' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', ' ',
            '#', '$', ' ', '$', '$', ' ', '#', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', '$', ' ', '#', ' ', '#',
            ' ', ' ', '#', ' ', '$', '#', '#', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', ' ', ' ', '#'],
        [' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', '@', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', ' ', '$', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        ['#', ' ', '$', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', '#'],
        ['#', '#', ' ', '$', ' ', ' ', '$', ' ', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', '#', ' ', '$', ' ', '$', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
        ['#', '#', ' ', '#', ' ', ' ', '$', ' ', ' ', '#', ' ', '#', ' ', '#'],
        ['#', '#', ' ', '#', ' ', '#', '$', '#', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', '#', ' ', '#', '#', '#', ' ', ' ', ' ', '#',
            ' ', '#', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', '$', ' ', ' ', '#', '#', '#', '#',
            ' ', '#', ' ', '#', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', '$', ' ', ' ', ' ', ' ',
            '$', ' ', ' ', ' ', '.', '.', '#', '.', '#'],
        ['#', '#', '#', '#', '$', ' ', ' ', '$', '#', ' ',
            '$', ' ', ' ', ' ', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ',
            ' ', '#', '#', ' ', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', '$', ' ', ' ', '#', '@', ' ', '#'],
        ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '$',
            '#', '#', '#', '#', ' ', ' ', '#', '#', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ',
            '#', ' ', ' ', '#', '$', ' ', '.', '.', '#'],
        ['#', ' ', '#', ' ', '$', ' ', ' ', '$', ' ', ' ',
            '#', ' ', ' ', '#', ' ', ' ', '#', '.', '#'],
        ['#', ' ', '#', ' ', '$', ' ', ' ', '#', ' ', ' ',
            ' ', ' ', ' ', '#', '$', ' ', '.', '.', '#'],
        ['#', ' ', '#', ' ', ' ', '#', '#', '#', ' ', '#',
            '#', ' ', ' ', ' ', ' ', ' ', '#', '.', '#'],
        ['#', ' ', '#', '#', '#', ' ', ' ', '#', ' ', ' ',
            '#', ' ', ' ', '#', '$', ' ', '.', '.', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '$',
            '#', '#', '#', '#', ' ', ' ', '#', '.', '#'],
        ['#', ' ', '#', '$', ' ', ' ', ' ', '$', ' ', ' ',
            '$', ' ', ' ', '#', '*', ' ', '.', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', '$', ' ', '#', ' ', '$',
            ' ', '$', ' ', '#', ' ', ' ', '#', '.', '#'],
        ['#', '#', '#', '#', ' ', '$', '#', '#', '#', ' ',
            ' ', ' ', ' ', '#', '*', ' ', '.', '.', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '$', '$',
            ' ', '#', '#', '#', '.', '.', '.', '.', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', '#', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        ['#', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', ' ', '#'],
        ['#', '#', ' ', '#', '@', '#', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', '$', '$', ' ', '$', ' ', ' ', '$', '$', '#'],
        ['#', ' ', ' ', '#', ' ', '#', '#', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', '#', '#', ' ',
            ' ', '$', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '#', ' ', ' ', '$', '$',
            '$', ' ', '$', '#', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', '#', '#', ' ',
            ' ', ' ', '.', '.', '.', '.', '#'],
        [' ', '#', ' ', '#', ' ', ' ', ' ', '#',
            ' ', '#', '.', '.', ' ', '.', '#'],
        [' ', '#', ' ', ' ', ' ', '#', ' ', '#',
            ' ', '#', '#', '.', '.', '.', '#'],
        [' ', '#', '#', '#', '#', '#', ' ', '$',
            ' ', ' ', '#', '.', '.', '.', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', ' ',
            ' ', ' ', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', ' ', ' ',
            ' ', ' ', ' ', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#',
            '#', '#', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '$', '#', ' ', ' ', '#', ' ',
            ' ', '$', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', ' ', '$', ' ', ' ', '$',
            ' ', '#', ' ', '$', ' ', '$', ' ', ' ', '#'],
        ['#', '#', '$', ' ', '$', ' ', ' ', ' ', '#', ' ',
            '@', '#', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', ' ', '#', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '#', '.', '.',
            '.', '.', '.', '.', '.', '#', ' ', '$', '#'],
        ['#', ' ', '#', '#', ' ', ' ', '#', ' ', '.',
            '.', '.', '.', '.', '.', '#', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '$', '.', '.',
            '.', '.', '.', '.', '.', '.', '$', ' ', '#'],
        ['#', ' ', '#', ' ', '$', ' ', '#', '.', '.',
            '.', '.', ' ', '.', '.', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '$', '#', '#', '#',
            '#', '$', '#', '#', '#', '#', ' ', '$', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', '#', '#', '#', ' ',
            '$', ' ', ' ', ' ', '$', ' ', ' ', '#', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', ' ', ' ', '$', ' ',
            '$', ' ', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ',
            '$', ' ', '#', '#', '#', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', ' ', '$', '#',
            '$', ' ', '#', ' ', ' ', '#', '#'],
        ['#', '.', '.', ' ', '#', ' ', ' ', '#',
            ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '.', '.', ' ', '#', ' ', '$', '#', '$',
            ' ', '#', ' ', ' ', '$', '#', '#', '#', '#'],
        ['#', '.', ' ', ' ', '#', ' ', ' ', ' ', ' ',
            ' ', '#', '$', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', '.', '.', ' ', ' ', ' ', '$', '#', ' ',
            ' ', '#', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '@', '#', ' ', ' ', '#', '$',
            ' ', '#', '$', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', '.', '.', ' ', '#', ' ', '$', '#', ' ',
            ' ', ' ', ' ', ' ', '$', '#', ' ', ' ', '#'],
        ['#', '.', '.', ' ', '#', ' ', ' ', '#', '$', '$',
            '#', '$', ' ', ' ', '#', ' ', ' ', '#', '#'],
        ['#', '.', '.', ' ', '#', ' ', '$', '#', ' ', ' ',
            '#', ' ', ' ', '$', '#', '$', ' ', ' ', '#'],
        ['#', '.', '.', ' ', '#', ' ', ' ', '#', ' ', ' ',
            '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '.', ' ', '#', '#', '#', '#', ' ', ' ',
            '#', '#', '#', '#', '#', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', ' ', ' ', '#', '#', '#',
            '#', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.',
            '.', '.', ' ', ' ', '.', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.',
            '.', '.', '$', '$', '.', '#', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '$', ' ', '#', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '$', ' ', ' ',
            '$', ' ', ' ', ' ', ' ', ' ', '$', ' ', '#'],
        ['#', '#', ' ', '#', '#', '#', '#', ' ', ' ', ' ',
            '#', ' ', ' ', '$', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', '#', '#', ' ', ' ', '#', ' ', '#', '#'],
        ['#', ' ', ' ', '$', '#', ' ', ' ', '#', ' ',
            '#', '#', ' ', ' ', '#', '#', '#', ' ', '#'],
        ['#', ' ', '$', ' ', '#', '$', '#', '#', '#',
            ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'],
        ['#', '#', '#', ' ', ' ', '$', ' ', '#', ' ',
            ' ', '#', ' ', ' ', '#', '#', '#', ' ', '#'],
        [' ', '#', '#', ' ', ' ', ' ', ' ', '$', ' ', '#',
            '#', ' ', '#', ' ', ' ', '#', ' ', '#', '#'],
        [' ', '#', ' ', '$', ' ', ' ', '#', ' ', ' ', '$',
            ' ', ' ', '$', ' ', '$', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '$', ' ', ' ', '$', '#', '$',
            '$', '$', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', ' ', ' ', '$', ' ', ' ',
            ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', '@', '#', '#', ' ', ' ',
            '#', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#'],
        ['#', ' ', ' ', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', ' ', '.', '.',
            '#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', '#', ' ', '#', ' ', '#', '#',
            '#', '#', '#', ' ', '.', '.', '.', '#'],
        ['#', '#', '$', '#', ' ', ' ', ' ', ' ', '.',
            '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', '#', '#', '$', '#', '#', '#',
            '#', '#', '#', ' ', ' ', '#', '#', '#', '#'],
        ['#', ' ', '$', ' ', '#', ' ', ' ', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '@', ' ', '#'],
        ['#', '#', '$', ' ', '#', ' ', '$', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '#', '$', '$', '$', '#',
            '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', ' ', '#', '$', '#', '$', '#', '#', '#'],
        ['#', ' ', '#', '#', '#', '#', ' ', '#', '$',
            '$', '$', '$', '$', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', ' ', '$', ' ',
            ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', '#',
            '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', ' ', '#', '#', '#', '#', '#', '#', '$', '#',
            '#', '#', '#', '#', '#', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',
            ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', ' ', ' ', '#', ' ', ' ', '#', '.', '.', '.', '#', '#', '#'],
        ['#', ' ', ' ', '$', '#', ' ', ' ', '#', '.', '.', '.', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', '#', '$', '$', ' ', '.', '.', '.', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', '#', ' ', ' ', '#', '.', '.', '.', ' ', '.', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', '$', '#',
            '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '$', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', '$', ' ', '$', ' ', '#'],
        ['#', '#', ' ', ' ', '#', ' ', ' ', '$',
            '$', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', ' ',
            ' ', '#', '#', '$', '$', '@', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ',
            ' ', ' ', ' ', ' ', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '.', '.', '.', ' ', ' ', ' ', '#', ' ',
            ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#'],
        ['#', '#', '.', '.', '.', '.', '.', ' ', ' ', '$',
            '#', '#', ' ', '#', ' ', '#', '$', ' ', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#', ' ', ' ',
            '$', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#', ' ', ' ',
            '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', ' ',
            '$', ' ', ' ', '$', ' ', '$', ' ', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '$',
            '#', '#', '$', ' ', '#', '#', '$', '#', '#'],
        [' ', '#', '#', ' ', ' ', ' ', '$', ' ', ' ', ' ',
            ' ', '#', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', '#', ' ', '#', '#', '#',
            ' ', '#', ' ', ' ', '#', '#', '$', ' ', '#'],
        [' ', '#', ' ', '$', ' ', '$', '$', ' ', ' ', ' ',
            ' ', ' ', '$', ' ', ' ', '$', ' ', ' ', '#'],
        [' ', '#', ' ', '$', ' ', ' ', ' ', ' ', '$', '#',
            '#', '$', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '@', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', '#', '#', ' ', '$', ' ',
            ' ', '$', ' ', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', ' ', '$', ' ', ' ',
            '$', ' ', '$', ' ', '#', '#', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '$',
            '$', ' ', ' ', '#', '#', '.', '.', '#'],
        ['#', ' ', ' ', '#', '#', '#', '#', '#', '#',
            ' ', '#', '#', '#', '.', '.', ' ', '#'],
        ['#', '#', ' ', '#', ' ', ' ', '#', ' ', ' ',
            ' ', ' ', '#', '.', '.', '.', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', ' ', '#', '.', '.', '.', ' ', '#'],
        ['#', '@', ' ', '#', '$', ' ', '#', '#', ' ',
            '#', '#', '#', '#', '.', '.', '.', '#'],
        ['#', '#', '#', '#', ' ', ' ', '$', ' ', '$',
            '$', ' ', ' ', '#', '#', '.', '.', '#'],
        [' ', ' ', ' ', '#', '#', ' ', ' ', '$', ' ',
            '$', ' ', ' ', '$', '.', '.', '.', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', '$', '$', ' ',
            ' ', '$', ' ', '#', ' ', ' ', '.', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '$',
            ' ', '$', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', '$', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', '#', ' ', '#', ' ', ' ', ' ', '$', '#', '$',
            '#', '@', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ',
            '$', ' ', '#', ' ', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', ' ', '#', '#'],
        ['#', ' ', ' ', '#', '#', ' ', '.', '.', '*', '.',
            '.', '.', '.', '.', ' ', '#', ' ', '#', '#'],
        ['#', '#', ' ', '#', '#', ' ', '*', '.', '*', '.',
            '.', '*', '.', '*', ' ', '#', ' ', '#', '#'],
        ['#', ' ', '$', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', ' ', '#', '#', '$', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', ' ', ' ', '$', ' ', ' ',
            '$', ' ', ' ', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ',
            ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', ' ', ' ', '#', ' ',
            ' ', ' ', ' ', ' ', '$', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', '#', '#', '#', '#',
            ' ', '$', '#', '#', ' ', '#', ' ', '#', '#'],
        ['#', ' ', '$', ' ', '#', '#', ' ', ' ', ' ',
            '#', ' ', '#', '#', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', '@', '$', '$', ' ',
            '#', ' ', '#', '#', '$', '$', '$', ' ', '#'],
        ['#', '#', ' ', '#', '#', '#', ' ', ' ', ' ',
            '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', ' ', '#', ' ', ' ', ' ', '#', '#',
            '#', ' ', '#', '#', '#', '#', '#', '$', '#'],
        ['#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ',
            '$', ' ', ' ', '#', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', '#', '#', '#', ' ', '#', '#', ' ',
            '$', ' ', '#', '.', '.', '.', '.', '#', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', '$', ' ', '#', ' ',
            ' ', ' ', '#', '.', '.', '$', '.', ' ', '#'],
        ['#', ' ', ' ', '#', '#', ' ', '$', ' ', '#', ' ',
            ' ', '#', '#', '.', '.', '.', '.', ' ', '#'],
        ['#', '#', '#', '#', '#', ' ', ' ', ' ', '#', '#',
            '#', '#', '#', '#', '.', '.', '.', '#', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#',
            ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', ' ', ' ', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '$', '#', ' ', '$', '@',
            '$', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', '$', ' ', ' ', '$', ' ', ' ', '#',
            ' ', '$', ' ', '$', '#', ' ', ' ', '#', '#'],
        ['#', '#', ' ', ' ', '$', '#', '#', ' ', '#',
            '$', ' ', '$', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', '#', ' ', '#',
            ' ', ' ', ' ', '$', '$', '$', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', ' ', '$', ' ',
            ' ', '$', '#', '#', ' ', '#', '#', '#', '#'],
        ['#', ' ', '$', ' ', '$', ' ', '#', '$',
            '#', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', '#', '#', '#', ' ',
            ' ', '#', '#', '#', '$', ' ', '#'],
        [' ', '#', ' ', ' ', '#', '.', '.', '.',
            '.', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '.', '.', '.',
            '.', '.', '.', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', '.', '.', '.', '.', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', '.', '.', '.', '#', '#'],
        [' ', ' ', ' ', '#', '.', '.', '.', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#'],
        [' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '$', '#'],
        ['#', '#', ' ', '$', ' ', ' ', '#', '#', ' ', '#', '#', '#'],
        ['#', '@', '$', ' ', '$', ' ', '#', ' ', '$', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', '#', '#', ' ', ' ', ' ', '$', '#'],
        [' ', '#', '.', '.', '.', '.', '#', '$', ' ', '$', ' ', '#'],
        [' ', '#', '.', '.', '.', '.', '#', ' ', ' ', ' ', '$', '#'],
        [' ', '#', '.', '.', '.', '.', ' ', ' ', '$', '$', ' ', '#', '#'],
        [' ', '#', '.', '.', '.', ' ', '#', ' ', '$', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '$', ' ', '$', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '$', ' ', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', ' ', '$', ' ', ' ', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', ' ', '#', '#', ' ', '$', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', '$', '$', ' ', '#', ' ', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', '$', ' ', '#', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '$', '#', ' ', '$', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '.', '.', '#', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '.', '.', ' ', '$', ' ', '#', '@', '#'],
        ['#', '.', '.', '.', '.', '.', '#', ' ', '$', '#', ' ', '#'],
        ['#', '#', '.', '.', '.', '.', '#', ' ', ' ', '$', ' ', '#'],
        ['#', '#', '#', '.', '.', '#', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '.', '.', '.', '.', ' ', ' ', ' ', '#', '#'],
        [' ', '#', '.', '#', '.', '#', ' ', ' ', '$', ' ', '#', '#'],
        ['#', '#', '.', '.', '.', '.', '#', ' ', '#', ' ', '@', '#', '#'],
        ['#', ' ', '.', '.', '.', '.', '#', ' ', ' ', '#', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#', '$', ' ', '#', '#', '$', ' ', '#'],
        ['#', '#', ' ', '#', '#', '#', ' ', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', '$', ' ', ' ', '$', ' ', '$', ' ', '$', '#', ' ', ' ', '#'],
        [' ', '#', ' ', '#', ' ', ' ', '$', ' ', '$', ' ', '#', '#', ' ', '#'],
        [' ', '#', ' ', ' ', '#', '#', '#', ' ', ' ', '#', '#', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#'],
        [' ', '#', ' ', ' ', '$', ' ', '#', ' ', ' ', '$', ' ', ' ', '#'],
        [' ', '#', '#', '#', '$', ' ', '$', ' ', ' ', ' ', '#', '#', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#',
            ' ', '#', '#', '#', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', '$', '$', '#', ' ', ' ', ' ',
            '@', ' ', ' ', '.', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', '#', '#', '#', ' ',
            ' ', ' ', '#', ' ', '.', '.', '.', '.', '#'],
        ['#', '#', ' ', '#', '#', ' ', '#', '#', '#', ' ',
            ' ', '#', ' ', ' ', '.', '.', '.', '.', '#'],
        [' ', '#', ' ', '$', ' ', '$', ' ', ' ', ' ', ' ',
            ' ', '#', ' ', '#', ' ', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', '$', ' ', '$', '#', '#', ' ',
            ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', '#', ' ', ' ', '#', '#',
            '#', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', '#', '$', ' ', ' ', ' ',
            '#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', '$', ' ', ' ', '#', ' ',
            '#', '#', ' ', '#', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', '#', ' ', '$', ' ', '$', ' ', ' ',
            ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '#', '#', ' ', '#',
            '#', ' ', '#', ' ', '#', '#', '#', '#', '#'],
        ['#', ' ', '$', '$', ' ', ' ', ' ', ' ', ' ', '$', '$', ' ', ' ', '#'],
        ['#', '#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '$', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', ' ', ' ', '#', '#',
            '#', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', '#', '#', '#', ' ',
            ' ', '$', ' ', '$', ' ', '$', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', '#', '#', ' ',
            '#', '#', ' ', '#', '#', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', '$', ' ', ' ',
            ' ', ' ', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', '#', '#', ' ', '$', ' ', ' ', '#', '#', ' ',
            '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#'],
        [' ', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ',
            '#', '#', '#', '#', '#', '$', '$', ' ', '#'],
        [' ', '#', '#', '$', '#', '#', '#', '#', '#', ' ',
            '@', '#', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', '$', ' ', ' ', '#', '#', '#', '$',
            '#', '#', '#', ' ', '$', ' ', ' ', '#', '#'],
        [' ', '#', ' ', '$', ' ', ' ', '#', ' ', ' ',
            ' ', '#', '#', '#', ' ', ' ', '#', '#', '#'],
        [' ', '#', ' ', '$', '$', ' ', '$', ' ',
            '#', ' ', ' ', ' ', '$', '$', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', '#',
            ' ', ' ', ' ', '#', '#', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#',
            '.', '.', ' ', '.', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', '.', '.', '.',
            '.', '.', '.', '.', '.', '.', '#'],
        [' ', ' ', ' ', ' ', '#', '.', '.', '.',
            '.', '.', '.', '.', '.', '.', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', ' ', ' ', ' ',
            '#', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '#', '#', '#', ' ', '$', ' ', ' ',
            ' ', ' ', '$', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '.', ' ', '$', ' ', '$', ' ', '#',
            ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '.', '#', '$', '#', '#', '#', '#',
            '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', '#', '$', ' ', ' ', '#', '$', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', '$', '$', ' ', '$', ' ',
            '$', ' ', ' ', '$', '#', '#', ' ', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', '$', ' ', ' ', ' ', '#',
            '$', '#', '$', ' ', '#', '#', '$', ' ', '#'],
        [' ', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#',
            ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', '$', ' ', '$', ' ',
            '#', '#', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', ' ', ' ',
            '$', ' ', ' ', '$', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '#', ' ', ' ', ' ',
            '#', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', '#',
            '#', '@', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '#', ' ', '@', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '$', '#', '#', ' ', '$', '#'],
        ['#', '#', '$', '#', '.', '.', '.', '#', ' ', '#'],
        [' ', '#', ' ', '$', '.', '.', '.', ' ', ' ', '#'],
        [' ', '#', ' ', '#', '.', ' ', '.', '#', ' ', '#', '#'],
        [' ', '#', ' ', ' ', ' ', '#', ' ', '#', '$', ' ', '#'],
        [' ', '#', '$', ' ', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '.', '.', '.', '.', '#'],
        ['#', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ',
            ' ', ' ', '#', '#', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', '$', '$', '#', '#', ' ', ' ', '$',
            ' ', '@', '#', '#', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '$', '$', ' ',
            '$', '#', ' ', ' ', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', '$', ' ', '#', '#', ' ', '$', '$',
            ' ', '#', ' ', '#', ' ', '.', '.', '.', '#'],
        ['#', ' ', ' ', '$', ' ', '#', '#', ' ', '$', ' ',
            ' ', '#', ' ', ' ', '.', '.', '.', '.', '#'],
        ['#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#',
            '#', '#', ' ', '#', '#', '.', '#', '#', '#'],
        ['#', '#', ' ', ' ', ' ', '$', ' ', ' ', '$', ' ',
            '#', '#', ' ', ' ', ' ', '.', ' ', ' ', '#'],
        ['#', ' ', '$', '#', '#', '#', ' ', ' ', '#', ' ',
            '#', '#', '#', '#', '#', ' ', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', ' ', ' ', '#',
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '#', '$', ' ', '$',
            ' ', '$', '#', '#', '#', ' ', ' ', '#'],
        ['#', ' ', '$', '$', '$', '#', ' ', '$', ' ',
            ' ', ' ', '#', ' ', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '$', '$', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ',
            '#', '$', '$', ' ', '$', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', '#', '$', ' ', '#', '$',
            '#', ' ', ' ', '#', '#', ' ', '@', '#'],
        [' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ',
            '#', ' ', '$', ' ', '#', ' ', '#', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', ' ', '$',
            ' ', '#', '$', ' ', ' ', '#', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', ' ', '#',
            ' ', '$', ' ', ' ', ' ', '#', ' ', '#'],
        [' ', ' ', ' ', '#', '#', ' ', '$', ' ',
            '$', ' ', ' ', ' ', '#', '#', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', '#', ' ',
            ' ', '#', '#', ' ', ' ', '$', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', ' ', ' ',
            '#', '#', ' ', '$', '$', '#', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '$', '$',
            ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '.', '.', '#', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '#', '.', '.', '.', ' ', '#', '#'],
        ['#', '.', '.', '.', '.', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '.', '.', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', '#', '#', ' ', ' ', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',
            '#', ' ', ' ', '$', '$', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#',
            ' ', '$', '$', ' ', ' ', '$', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ',
            '$', ' ', ' ', ' ', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', '$', '$', ' ', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#',
            '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', '$', '$', '$', '@', '#'],
        ['#', '.', '#', ' ', '#', '#', '#', '#', '#', '#',
            '#', ' ', '#', '#', ' ', ' ', ' ', '#', '#'],
        ['#', '.', '#', ' ', '#', '#', '#', '#', '#', '#',
            '#', '.', ' ', '#', '$', ' ', '$', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.',
            '.', '.', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', ' ', ' ', '$', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', '#', '#', ' ', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ',
            ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#',
            ' ', '$', ' ', '$', ' ', ' ', ' ', '@', '#'],
        [' ', ' ', '#', ' ', '#', '#', ' ', '#', '#',
            '$', '#', '$', ' ', '$', ' ', '$', '#', '#'],
        ['#', '#', '#', ' ', '.', '.', '.', '.', '.',
            '.', '#', ' ', ' ', '$', '$', ' ', '#', '#'],
        ['#', ' ', ' ', ' ', '.', '.', '.', '.', '.',
            '.', '#', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', '.', '.', '.', '.', '.',
            '.', '#', '$', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', '.', '.', '.', '.', '.',
            '.', ' ', '$', '$', '#', ' ', '$', ' ', '#'],
        ['#', ' ', '$', ' ', '#', '#', '#', ' ', '#',
            '#', '#', '$', ' ', ' ', '$', ' ', '#', '#'],
        ['#', '#', '#', ' ', ' ', '$', ' ', ' ', '$',
            ' ', ' ', '$', ' ', ' ', '$', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', '$', ' ', ' ', '$',
            ' ', ' ', '$', ' ', ' ', '$', ' ', '#'],
        [' ', ' ', '#', '#', '#', '#', '#', '#', ' ',
            ' ', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#',
            ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#',
            ' ', ' ', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', ' ', '#', '$', '$',
            ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ',
            '#', ' ', ' ', '#', '#', ' ', '#', '#', '#'],
        ['#', ' ', ' ', '#', '#', '#', ' ', '$', '#', '$',
            ' ', ' ', '$', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', '.', '.', '.', ' ', ' ', ' ', ' ', '#', ' ',
            '#', '#', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '.', '#', ' ', ' ', ' ', ' ', '@',
            ' ', '#', ' ', '#', '#', '#', ' ', '#', '#'],
        ['#', '.', '.', '.', '#', ' ', ' ', '#', '#', '#',
            ' ', ' ', '$', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', ' ', '#',
            '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', ' ',
            '$', '@', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', '$', ' ', '#', '#', '$',
            ' ', '#', '#', '#', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', '#', '#', '#', '#', ' ',
            '$', ' ', ' ', ' ', ' ', '$', ' ', '#'],
        [' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#',
            ' ', ' ', '#', '$', ' ', '#', '#', '#', '#'],
        ['#', '#', ' ', ' ', '#', '#', '#', '#', ' ', '#',
            '#', '$', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', '#', ' ', ' ', '$', ' ', ' ',
            '#', ' ', '#', '#', ' ', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', ' ', '#', '.', '.', '.', '#', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#',
            '#', ' ', ' ', '.', '.', '.', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ',
            '#', ' ', '#', '.', '.', '.', '#', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', ' ', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '#', ' ', '#', ' ', ' ', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '#', '#', '#', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', '.', '.', '.', '.', '#', '#', ' ',
            '$', ' ', ' ', '$', '#', '#', '#'],
        ['#', '#', '.', '.', '.', '.', '#', '#',
            ' ', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', '#', '#', '.', '.', '.', ' ', '#',
            '#', ' ', '$', ' ', '$', ' ', '#'],
        ['#', ' ', '#', '#', ' ', ' ', ' ', ' ',
            '#', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', '#', ' ', '#', ' ',
            '#', '#', '#', ' ', '#', '#', '#', '#'],
        ['#', ' ', '$', ' ', '#', ' ', '#', '$',
            ' ', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '@', ' ', '$',
            ' ', ' ', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', '$', ' ',
            '$', '$', ' ', '$', ' ', '#', '#', '#'],
        ['#', ' ', ' ', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#'],
        ['#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        ['#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', ' ', '#', '#'],
        ['#', ' ', '#', ' ', '$', ' ', '$', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '$', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '$', ' ', ' ', '$', '$', '#', ' ', ' ', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', '#', '#', ' ', '#', ' ', '$', '#', '#'],
        [' ', ' ', '#', '#', '$', '#', ' ', ' ', ' ', '$', ' ', '@', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', '$', ' ', '$', ' ', '#', '#', '#'],
        [' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '$', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#'],
        [' ', ' ', '#', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', '#', '.', '.', '.', '.', '.', '.', '.', '#', '#', '#'],
        [' ', ' ', '#', '.', '.', '.', '.', '.', '.', '.', '#'],
        [' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#'],
        ['#', '#', ' ', ' ', '$', ' ', ' ', ' ', ' ',
            ' ', ' ', '$', ' ', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', '#', ' ', '#', '#',
            ' ', ' ', ' ', '#', '#', '.', '.', '.', '#'],
        ['#', ' ', '#', '$', '$', ' ', '$', ' ', '$',
            '$', '#', '$', '#', '#', '.', '.', '.', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', ' ', '@', ' ',
            ' ', '#', ' ', ' ', ' ', '.', '.', '.', '#'],
        ['#', ' ', ' ', '$', '#', ' ', '#', '#', '#',
            '$', '$', ' ', ' ', ' ', '.', '.', '.', '#'],
        ['#', ' ', '$', ' ', ' ', '$', '$', ' ', ' ',
            '$', ' ', '#', '#', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '$', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', '*', '.', '*', '#', '*', '.', '*', '#'],
        [' ', ' ', '#', '.', '*', '.', '*', '.', '*', '.', '#'],
        [' ', ' ', '#', '*', '.', '*', '.', '*', '.', '*', '#'],
        [' ', ' ', '#', '.', '*', '.', '*', '.', '*', '.', '#'],
        [' ', ' ', '#', '*', '.', '*', '.', '*', '.', '*', '#'],
        [' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', '$', ' ', '$', ' ', '$', ' ', '$', ' ', '#'],
        ['#', '#', ' ', '$', ' ', '$', ' ', '$', ' ', '$', ' ', '#', '#'],
        [' ', '#', '$', ' ', '$', ' ', '$', ' ', '$', ' ', '$', '#'],
        [' ', '#', ' ', ' ', ' ', '$', '@', '$', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '$', '$', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#',
            '$', ' ', ' ', '$', ' ', '#', '#'],
        [' ', ' ', '#', '#', '#', '#', ' ', ' ',
            ' ', ' ', '$', ' ', ' ', ' ', '#'],
        ['#', '#', '#', ' ', ' ', '#', ' ', '#',
            '#', '#', '#', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', '#',
            '.', '.', '.', '.', '$', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '$', ' ',
            '.', '.', '.', '.', '#', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '#', ' ', '#',
            '.', '*', '.', '.', '#', ' ', '#'],
        ['#', '#', '#', ' ', ' ', '#', '#', '#',
            '#', ' ', '#', '#', '#', ' ', '#'],
        [' ', ' ', '#', '#', '#', '#', ' ', '@',
            '$', ' ', ' ', '#', '#', '$', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#',
            ' ', '$', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',
            ' ', ' ', '#', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',
            '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '.', '.',
            ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '.', '.', '*',
            ' ', '$', ' ', ' ', ' ', ' ', '$', ' ', '#'],
        [' ', ' ', ' ', '#', '#', '.', '.', '*', '.',
            '#', ' ', '#', ' ', '#', '$', ' ', '#', '#'],
        [' ', ' ', ' ', '#', '.', '.', '*', '.', '#',
            ' ', '#', ' ', '#', ' ', '$', ' ', ' ', '#'],
        ['#', '#', '#', '#', '.', '.', '.', '#', ' ',
            ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '@', '$', ' ', '$', ' ', '#', '#',
            '#', ' ', ' ', '#', ' ', '#', ' ', '#', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', '$', ' ', ' ',
            ' ', '#', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '$', '$', ' ', ' ', ' ', '#',
            ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', '$', ' ', ' ', ' ',
            '#', ' ', '#', ' ', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', '$', '#', ' ', '#', '#', '#',
            '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', '#', '$', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', '#', '#', '#', ' ', ' ',
            ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ',
            ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#'],
        [' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ',
            ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#',
            ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', '#', '$', ' ', '$', ' ', ' ', '#',
            ' ', '$', '$', ' ', '#', ' ', '$', ' ', '#'],
        ['#', '.', '#', ' ', '.', ' ', '.', '$', ' ', '#',
            ' ', '#', '.', '.', '#', ' ', '#', '.', '#'],
        ['#', '.', '#', '#', '#', '#', '.', '#', ' ', '#',
            ' ', '#', ' ', '#', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ',
            ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '#', ' ', '#', ' ', '#',
            '#', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#',
            '.', '$', ' ', '#', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', '$', '$', '.', '#', ' ', '#', ' ', '#',
            '#', ' ', ' ', '#', ' ', '#', '#', ' ', '#'],
        ['#', '$', ' ', '#', ' ', '#', ' ', '#', ' ', ' ',
            '#', ' ', '#', '#', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', '.', '#', ' ', '#', ' ', '#', '#', ' ',
            '#', ' ', '#', ' ', ' ', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ',
            '#', ' ', '#', ' ', '#', '#', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', ' ', '#', '#', ' ', '#', ' ',
            '#', ' ', '#', ' ', '#', ' ', '$', '.', '#'],
        ['#', '#', '#', ' ', '#', '#', '#', ' ', '$', '.',
            '#', ' ', '$', '.', '#', ' ', '$', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ',
            '#', ' ', ' ', ' ', '#', ' ', ' ', '@', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
]
```

</details>
   
<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun
import copy

# Globala variabler här nedanför
levels = [
    [
        [' ', ' ', '#', '#', '#'],
        [' ', ' ', '#', '.', '#'],
        [' ', ' ', '#', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '$', ' ', '$', '.', '#'],
        ['#', '.', ' ', '$', '@', '#', '#', '#'],
        ['#', '#', '#', '#', '$', '#'],
        [' ', ' ', ' ', '#', '.', '#'],
        [' ', ' ', ' ', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', '@', '$', '$', '#', ' ', '#', '#', '#'],
        ['#', ' ', '$', ' ', '#', ' ', '#', '.', '#'],
        ['#', '#', '#', ' ', '#', '#', '#', '.', '#'],
        [' ', '#', '#', ' ', ' ', ' ', ' ', '.', '#'],
        [' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', '#', '$', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '@', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '.', '.', '#', ' ', '$', ' ', '#', '#'],
        ['#', '#', '.', '.', '#', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', ' ', ' ', '.', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', '*', '#'],
        ['#', ' ', '$', '$', ' ', '$', '.', '#'],
        ['#', '#', '@', '#', '#', '.', '.', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#'],
        [' ', '#', '@', ' ', '#', '#', '#'],
        [' ', '#', ' ', '$', ' ', ' ', '#'],
        ['#', '#', '#', ' ', '#', ' ', '#', '#'],
        ['#', '.', '#', ' ', '#', ' ', ' ', '#'],
        ['#', '.', '$', ' ', ' ', '#', ' ', '#'],
        ['#', '.', ' ', ' ', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', '#', ' ', ' ', '#', ' ', '@', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', ' ', '#', '$', ' ', '$', ' ', '$', ' ', '#'],
        [' ', ' ', '#', ' ', '$', '#', '#', ' ', ' ', '#'],
        ['#', '#', '#', ' ', '$', ' ', '#', ' ', '#', '#'],
        ['#', '.', '.', '.', '.', '.', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '.', ' ', '$', '#', '#', ' ', '#', '#'],
        ['#', '.', '.', '$', ' ', '$', ' ', ' ', '@', '#'],
        ['#', '.', '.', ' ', '$', ' ', '$', ' ', '#', '#'],
        ['#', '#', '#', '#', '#', '#', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '$', '$', '$', ' ', '#'],
        ['#', '@', ' ', '$', '.', '.', ' ', '#'],
        ['#', ' ', '$', '.', '.', '.', '#', '#'],
        ['#', '#', '#', '#', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', '#', '.', '.', '#'],
        [' ', '#', '#', ' ', '.', '#', '#'],
        [' ', '#', ' ', ' ', '$', '.', '#'],
        ['#', '#', ' ', '$', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', '#', '$', '$', ' ', '#'],
        ['#', ' ', ' ', '@', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', '#', ' ', ' ', '@', '#'],
        ['#', ' ', ' ', '$', '.', ' ', '#', '#'],
        ['#', ' ', ' ', '.', '$', '.', ' ', '#'],
        ['#', '#', '#', ' ', '*', '$', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', '#', '#'],
        [' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', '.', '.', '$', ' ', '#'],
        ['#', '@', '$', '.', '*', ' ', '#', '#'],
        ['#', ' ', '$', '.', '.', '$', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', '#'],
        [' ', ' ', '#', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', ' ', '$', ' ', '#', '#', ' ', '#'],
        ['#', '.', '.', '.', ' ', '$', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '.', '$', '#', '$', ' ', '#', '#'],
        ['#', '#', '#', '#', ' ', '#', ' ', '$', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', '@', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', '$', '$', '#', '#'],
        ['#', ' ', ' ', '#', '.', '.', '#', '#', '#'],
        ['#', '#', ' ', ' ', '.', '.', '$', ' ', '#'],
        [' ', '#', ' ', '@', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', '#', '.', ' ', '#'],
        [' ', '#', '#', ' ', ' ', '$', '.', '.', '.', '#'],
        [' ', '#', ' ', ' ', '$', ' ', '#', '*', '.', '#'],
        ['#', '#', ' ', '#', '#', '$', '#', ' ', '#', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '@', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '.', '.', '.', '.', ' ', '#'],
        ['#', '#', '#', '.', '.', '.', '$', '#', '#', '#'],
        ['#', ' ', ' ', '$', '#', '$', ' ', '$', ' ', '#'],
        ['#', ' ', '$', '$', ' ', ' ', '#', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', '@', ' ', '#', '#', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', ' ', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '$', ' ', '$', '@', '#'],
        ['#', '$', '#', '$', '$', '$', '#', '#'],
        ['#', '.', '.', '$', ' ', '$', ' ', '#'],
        ['#', '.', '.', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', '$', '$', ' ', ' ', '#'],
        ['#', ' ', '.', '.', '.', '#', ' ', '#'],
        ['#', '#', '.', '.', '.', '$', ' ', '#', '#'],
        [' ', '#', ' ', '#', '#', ' ', '$', ' ', '#'],
        [' ', '#', '$', ' ', ' ', '$', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', ' ', ' ', '@', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', '$', ' ', '@', '#'],
        ['#', '#', '#', '$', '$', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', '.', '.', '#'],
        [' ', ' ', '#', '.', '.', '.', '.', '#'],
        [' ', ' ', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '*', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', '.', '$', '.', ' ', '@', '#'],
        ['#', ' ', '.', '$', '.', '$', '.', ' ', '#'],
        ['#', ' ', '$', '.', '$', '.', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', '*', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', '$', '#', '$', ' ', '#'],
        ['#', ' ', '$', '$', ' ', ' ', '.', '$', '.', '#'],
        ['#', ' ', '@', '#', '#', '#', '.', '.', '.', '#'],
        ['#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '.', ' ', '.', '.', '#'],
        [' ', '#', '.', ' ', '$', '.', '#'],
        ['#', '#', '#', ' ', ' ', '$', '#', '#'],
        ['#', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '#', '$', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '@', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
        ['#', '#', ' ', '#', '$', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', '$', '$', ' ', '#'],
        ['#', ' ', '#', '$', '#', '.', '*', '.', '#'],
        ['#', ' ', ' ', ' ', '@', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', '$', ' ', '$', ' ', ' ', ' ', '#'],
        ['#', '@', '#', '.', '*', '.', '#', ' ', '#'],
        ['#', ' ', '#', '.', '*', '.', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', '$', ' ', '#'],
        ['#', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '.', ' ', ' ', '#', '#'],
        ['#', ' ', '$', '.', '$', '.', ' ', ' ', '#'],
        ['#', '@', '$', '#', ' ', '#', '$', ' ', '#'],
        ['#', ' ', '$', '.', ' ', '.', ' ', ' ', '#'],
        ['#', '#', '#', '#', '$', '#', '$', ' ', '#'],
        [' ', ' ', '#', '.', ' ', '.', ' ', ' ', '#'],
        [' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', ' ', ' ', ' ', ' ', '.', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '$', ' ', '$', '.', ' ', '#'],
        ['#', ' ', ' ', '.', '#', '#', '#', '#', '.', '#', '#'],
        ['#', ' ', '$', '.', '$', ' ', '$', ' ', '@', '#'],
        ['#', ' ', ' ', '.', ' ', ' ', ' ', ' ', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', ' ', '$', ' ', '.', '*', '.', ' ', '$', ' ', '#'],
        ['#', '@', '$', '.', '*', ' ', '*', '.', '$', ' ', '#'],
        ['#', ' ', '$', ' ', '.', '*', '.', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', '#', '#', '#', '#'],
        ['#', ' ', '$', '*', '.', '.', '*', ' ', '#'],
        ['#', ' ', '*', '.', '.', '*', '$', ' ', '#'],
        ['#', '#', '#', '#', ' ', ' ', '$', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', '@', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '.', ' ', ' ', '@', '#'],
        ['#', ' ', ' ', '$', '$', '$', ' ', ' ', '#'],
        ['#', '.', '#', '#', '.', '#', '#', '.', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', '.', '#', ' ', '#', '#'],
        ['#', '#', '#', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', ' ', ' ', '$', '.', ' ', '@', '#'],
        ['#', ' ', '.', '$', '.', '$', ' ', ' ', '#'],
        ['#', '#', '$', '.', '$', ' ', '$', '#', '#'],
        ['#', ' ', '.', '$', '.', '$', ' ', ' ', '#'],
        ['#', '.', ' ', ' ', '$', '.', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', '@', ' ', ' ', '#'],
        ['#', '#', '$', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', '$', '$', '#', '#'],
        ['#', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', '$', ' ', '#', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', '@', '$', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', '#', '$', ' ', '#'],
        ['#', '#', '#', '.', '#', '#', ' ', '#', '#', '#'],
        [' ', '#', '.', '.', '.', '$', ' ', '$', ' ', '#'],
        [' ', '#', '#', '.', '.', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', '#', '.', '.', ' ', '#', '#'],
        ['#', ' ', '$', '.', ' ', '$', '*', ' ', '#'],
        ['#', ' ', ' ', '$', '@', '$', ' ', ' ', '#'],
        ['#', ' ', '*', '$', ' ', '.', '$', ' ', '#'],
        ['#', '#', ' ', '.', '.', '#', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', ' ', ' ', '*', ' ', ' ', '#', '#'],
        ['#', ' ', '.', ' ', '.', ' ', '.', ' ', '#'],
        ['#', ' ', '$', ' ', '*', ' ', ' ', ' ', '#'],
        ['#', '*', '$', '$', '*', '$', '$', '*', '#'],
        ['#', ' ', ' ', ' ', '*', ' ', '$', ' ', '#'],
        ['#', ' ', '.', ' ', '.', '@', '.', ' ', '#'],
        ['#', '#', ' ', ' ', '*', ' ', ' ', '#', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '.', '$', ' ', '@', '#'],
        ['#', ' ', '$', ' ', '*', ' ', '$', ' ', '#'],
        ['#', '*', '.', '.', '.', '*', '.', '*', '#'],
        ['#', ' ', '$', '$', '*', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '.', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#', '.', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', '.', '.', '#', '#', ' ', '#'],
        [' ', '#', ' ', ' ', '$', '.', '.', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', ' ', '.', '#', ' ', '#', '#'],
        ['#', '#', '#', ' ', '#', '#', '$', '#', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', ' ', '$', '$', ' ', '#'],
        ['#', ' ', '#', '$', '#', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', '@', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', ' ', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', '#', '#', '#', '$', ' ', '#', '#', '#'],
        ['#', ' ', '$', ' ', '$', ' ', ' ', '$', '$', ' ', '#'],
        ['#', '@', ' ', '$', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', '$', ' ', ' ', ' ', '#'],
        [' ', '#', '$', ' ', '#', '#', '#', ' ', '$', '#'],
        [' ', '#', ' ', '#', '.', '.', '.', '#', ' ', '#'],
        ['#', '#', ' ', '#', '.', '.', '.', '#', ' ', '#', '#'],
        ['#', ' ', '$', ' ', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '@', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', '#', '.', '$', '$', '$', ' ', '#'],
        ['#', ' ', '#', '.', '*', '#', ' ', '#', '#', '#'],
        ['#', ' ', ' ', '.', '.', '#', ' ', '#'],
        ['#', '#', '#', '.', '.', '$', ' ', '#', '#'],
        [' ', ' ', '#', '.', '#', ' ', '$', ' ', '#'],
        [' ', '#', '#', ' ', '#', ' ', '#', '@', '#'],
        [' ', '#', ' ', '$', ' ', ' ', '$', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '@', ' ', '$', '$', '$', ' ', '$', ' ', ' ', '#'],
        ['#', '#', ' ', '$', ' ', ' ', '$', ' ', '$', ' ', '#'],
        [' ', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', '$', ' ', '#', '#'],
        ['#', '#', '#', ' ', '#', '#', '$', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '@', ' ', '$', '#', ' ', '#'],
        ['#', '#', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', '#', '.', '#', ' ', '#'],
        ['#', ' ', ' ', '.', '*', '.', '$', '#'],
        ['#', '#', ' ', '#', '.', '#', ' ', '#'],
        [' ', '#', ' ', '#', '.', ' ', ' ', '#', '#'],
        ['#', '#', ' ', '$', '.', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', '#', '#', '#'],
        ['#', ' ', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '@', ' ', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '.', '#', '#', '#', ' ', '#', '#'],
        ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', '#', ' ', '$', ' ', '$', '#', '.', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', '*', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', '.', '#', '$', ' ', '$', ' ', '#', ' ', '#'],
        ['#', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'],
        [' ', '#', ' ', '#', '#', '#', '.', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '$', ' ', '@', '#'],
        ['#', '#', '#', '.', ' ', '#'],
        [' ', ' ', '#', '.', '#', '#'],
        [' ', ' ', '#', '.', ' ', '#'],
        ['#', '#', '#', '.', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', '#', '#'],
        [' ', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#'],
        ['#', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '.', ' ', ' ', '#', ' ', '#'],
        ['#', '#', '$', '#', ' ', ' ', '.', '#'],
        [' ', '#', ' ', '#', '$', '#', ' ', '#'],
        ['#', '#', '.', ' ', ' ', '.', ' ', '#'],
        ['#', ' ', ' ', '#', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', '*', '#'],
        ['#', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '$', '#', '*', ' ', '@', '#'],
        ['#', ' ', ' ', '#', '.', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#'],
        [' ', ' ', ' ', '#', '.', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '.', '$', ' ', '#', ' ', ' ', '#'],
        [' ', '#', '.', '.', '.', ' ', ' ', '#', '$', ' ', '#'],
        [' ', '#', '.', '#', '#', ' ', '$', ' ', ' ', ' ', '#'],
        ['#', '#', '.', '$', ' ', '$', '#', '#', ' ', '#', '#'],
        ['#', '.', '$', ' ', '#', ' ', '#', '#', ' ', '#'],
        ['#', '.', '#', '$', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '.', '$', ' ', ' ', '#', '$', ' ', '$', '#'],
        ['#', '.', ' ', '$', '#', '#', ' ', '@', ' ', '#'],
        ['#', '.', '$', ' ', ' ', ' ', ' ', '$', ' ', '#'],
        ['#', '.', ' ', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', '#', '#', '#', ' ', ' ', '#', '#'],
        [' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#'],
        [' ', '#', ' ', ' ', ' ', '#', ' ', '.', '.', '#'],
        ['#', '#', ' ', '$', '#', '*', '#', '$', '.', '#'],
        ['#', ' ', ' ', '$', ' ', '#', ' ', '$', '.', '#'],
        ['#', ' ', ' ', '$', ' ', '@', ' ', '$', '.', '#'],
        ['#', ' ', ' ', '$', ' ', '#', ' ', '$', '.', '#'],
        ['#', '#', '$', '$', '#', '*', '#', '$', '.', '#'],
        [' ', '#', '.', ' ', ' ', '#', ' ', '.', '.', '#'],
        [' ', '#', '#', '.', ' ', ' ', ' ', ' ', '#', '#'],
        [' ', ' ', '#', '#', '#', ' ', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
        ['#', ' ', '$', '$', ' ', ' ', '#', ' ', '#'],
        ['#', '@', '$', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', '#', ' ', '#', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', '$', ' ', '#'],
        ['#', ' ', '$', '#', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', '$', '#', ' ', '#'],
        ['#', '.', '.', '.', '#', ' ', ' ', ' ', '#'],
        ['#', '.', '#', '.', '#', '$', '#', '#', '#'],
        ['#', '.', '.', '.', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '.', '#'],
        ['#', ' ', '#', '$', '#', '.', '.', '#', '#'],
        ['#', ' ', ' ', ' ', '$', '.', '.', '.', '#'],
        ['#', '#', ' ', '#', '#', '.', '$', '.', '#'],
        [' ', '#', ' ', '#', '#', ' ', ' ', '#', '#'],
        [' ', '#', '$', '#', '#', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', ' ', '#', '$', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', '#', '#', '#', '#'],
        ['#', ' ', '$', ' ', '$', ' ', ' ', ' ', '@', '#'],
        ['#', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#'],
        ['#', ' ', ' ', '#', '#', '#', '#'],
        ['#', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', '#', '.', '#', ' ', '#'],
        ['#', ' ', '#', ' ', '#', ' ', '#'],
        ['#', '.', '$', '.', '$', '.', '#'],
        ['#', ' ', '#', ' ', '#', ' ', '#'],
        ['#', ' ', '#', '.', '#', ' ', '#'],
        ['#', ' ', ' ', '$', '$', ' ', '#'],
        ['#', '#', ' ', '@', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', '#', '#'],
        [' ', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', '#'],
        ['#', ' ', '$', '$', ' ', ' ', '#', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', ' ', '#', '#', ' ', '$', '#', ' ', ' ', '#'],
        [' ', '#', ' ', '#', '.', '.', '.', ' ', ' ', '#', '#'],
        [' ', '#', ' ', ' ', '.', '.', '.', '#', '$', '#', '#'],
        [' ', '#', ' ', '#', '.', '.', '.', '#', ' ', ' ', '#'],
        ['#', '#', ' ', '#', ' ', '#', '#', '#', '@', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '#', '$', '#', '#', '#', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '$', ' ', '$', ' ', '*', '.', '#'],
        ['#', '.', '*', ' ', '$', ' ', '$', '.', '.', '#'],
        ['#', '#', '.', '$', ' ', '$', ' ', '*', '#', '#'],
        [' ', '#', '*', ' ', '$', ' ', '$', '.', '#'],
        [' ', '#', '.', '$', ' ', '$', ' ', '.', '#'],
        [' ', '#', '.', ' ', '$', ' ', '$', '.', '#'],
        [' ', '#', '.', '$', '@', '$', ' ', '*', '#'],
        ['#', '#', '*', ' ', '$', ' ', '$', '.', '#', '#'],
        ['#', '.', '.', '$', ' ', '$', ' ', '*', '.', '#'],
        ['#', '.', '*', ' ', '$', ' ', '$', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', '#', '$', ' ', ' ', '#'],
        [' ', ' ', '#', '#', '#', ' ', ' ', '$', '#', '#'],
        [' ', ' ', '#', ' ', ' ', '$', ' ', '$', ' ', '#'],
        ['#', '#', '#', ' ', '#', ' ', '#', '#', ' ', '#',
            ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', '#',
            '#', '#', '#', '#', ' ', ' ', '.', '.', '#'],
        ['#', ' ', '$', ' ', ' ', '$', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', '.', '.', '#'],
        ['#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ',
            '#', '@', '#', '#', ' ', ' ', '.', '.', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', '.', '.', ' ', ' ', '#', ' ', '$', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', '.', '.', ' ', ' ', '#', '$', '#', '#', '#', '#', ' ', ' ', '#'],
        ['#', '.', '.', ' ', ' ', ' ', ' ', '@', ' ', '#', '#', ' ', ' ', '#'],
        ['#', '.', '.', ' ', ' ', '#', ' ', '#', ' ', ' ', '$', ' ', '#', '#'],
        ['#', '#', '#', '#', '#', '#', ' ', '#', '#', '$', ' ', '$', ' ', '#'],
        [' ', ' ', '#', ' ', '$', ' ', ' ', '$', ' ', '$', ' ', '$', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', ' ', ' ', ' ', ' ', ' ', '@', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', ' ', '$', '#', '$', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', ' ', '$', ' ', ' ', '$', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', '#', '$', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#',
            ' ', '$', ' ', '#', ' ', '#', '#', '#'],
        ['#', '.', '.', '.', '.', ' ', ' ', '#', '#',
            ' ', '$', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', '#', '.', '.', '.', ' ', ' ', ' ', ' ',
            '$', ' ', ' ', '$', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '.', '.', ' ', ' ', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', '#', ' ', ' ', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', ' ', ' ', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '$', ' ',
            '$', ' ', ' ', ' ', '.', '.', '.', '.', '#'],
        ['#', ' ', '$', '$', '$', '#', '$', ' ', ' ', '$',
            ' ', '#', ' ', ' ', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', '$', ' ', ' ', ' ', ' ', ' ', '$',
            ' ', '#', ' ', ' ', '.', '.', '.', '.', '#'],
        ['#', ' ', '$', '$', ' ', '#', '$', ' ', '$', ' ',
            '$', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', '$', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '$', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', '$', '$', '#', '$', '$', ' ', ' ', '@', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',
            ' ', ' ', ' ', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',
            ' ', '#', '$', '#', '#', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',
            ' ', ' ', ' ', ' ', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#',
            ' ', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '.', '.', ' ', ' ', '#', '#',
            ' ', '$', ' ', ' ', '$', '#', '#', '#'],
        ['#', '.', '.', '.', '.', ' ', ' ', ' ',
            ' ', '$', ' ', '$', '$', ' ', '#', '#'],
        ['#', '.', '.', '.', '.', ' ', ' ', '#',
            '#', '$', ' ', ' ', '$', ' ', '@', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#',
            '#', ' ', ' ', '$', ' ', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', ' ', '$', ' ', '$', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', '#', '#', ' ', '#', '#', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#'],
        ['#', '.', '.', ' ', ' ', '#', ' ', '#', '#', '@', '#', '#'],
        ['#', '.', '.', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', '.', '.', ' ', ' ', ' ', ' ', ' ', '$', '$', ' ', '#'],
        ['#', '.', '.', ' ', ' ', '#', ' ', '#', ' ', '$', ' ', '#'],
        ['#', '.', '.', '#', '#', '#', ' ', '#', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', ' ', '$', ' ', '#', '$', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', '$', '#', ' ', '$', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', '$', ' ', ' ', '$', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#', '#'],
        ['#', '#', ' ', '#', ' ', '@', '#', '#', ' ', '$', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '$', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', ' ', '#', '#', '#', '#', '#', '$', '#', '#', '#'],
        ['#', ' ', '$', ' ', ' ', '#', '#', '#', ' ', '.', '.', '#'],
        ['#', ' ', '$', ' ', '$', ' ', '$', ' ', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', '#', '#', '.', '.', '.', '#'],
        ['#', ' ', '$', '$', ' ', '#', ' ', '#', '.', '.', '.', '#'],
        ['#', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', '$',
            ' ', ' ', ' ', '$', ' ', '$', ' ', '#'],
        [' ', ' ', '#', ' ', '$', '#', ' ', '$',
            ' ', '#', ' ', ' ', '$', ' ', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', '$', ' ', '$',
            ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', ' ', '$', '#', ' ', '#',
            ' ', ' ', '#', '#', '#', '#', ' ', '#'],
        ['#', '@', '#', '$', ' ', '$', ' ', '$',
            ' ', ' ', '#', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '$', ' ', '#',
            '$', '#', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', ' ', ' ',
            ' ', '$', ' ', '$', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', '#', ' ', ' ', '#',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', '#', '.', '.', '.', '.', '.', '.', '#'],
        [' ', ' ', '#', '.', '.', '.', '.', '.', '.', '#'],
        [' ', ' ', '#', '.', '.', '.', '.', '.', '.', '#'],
        [' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', '#', ' ', ' ', '.', '.', '.', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#',
            '#', '#', ' ', ' ', '.', '.', '.', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', ' ', ' ', ' ', '.', ' ', '.', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ',
            '#', '#', ' ', ' ', '.', '.', '.', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ',
            '#', '#', ' ', ' ', '.', '.', '.', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', ' ', '$', '$', '$', ' ', '#', '#'],
        [' ', '#', '#', '#', '#', '#', ' ', ' ', '$',
            ' ', '$', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', ' ', ' ', ' ', '#', '$', ' ', '$',
            ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '@', ' ', '$', ' ', ' ', '$', ' ', ' ',
            ' ', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', ' ', '$', '$',
            ' ', '$', ' ', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', ' ', ' ', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '@', '#', '#', '#', '#', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', '$', ' ', ' ', ' ', '$', '$', ' ',
            ' ', '$', ' ', '$', ' ', '.', '.', '.', '#'],
        ['#', ' ', ' ', '$', '$', '$', '#', ' ', ' ', ' ',
            ' ', '$', ' ', ' ', '#', '.', '.', '.', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', '#', ' ', '$', '$',
            ' ', '$', '$', ' ', '#', '.', '.', '.', '#'],
        ['#', '#', '#', ' ', ' ', ' ', '#', ' ', ' ', '$',
            ' ', ' ', ' ', ' ', '#', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '$', ' ',
            '$', ' ', '$', ' ', '#', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#',
            '#', ' ', '#', '#', '#', '.', '.', '.', '#'],
        ['#', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', '$',
            ' ', '$', ' ', ' ', '#', '.', '.', '.', '#'],
        ['#', ' ', ' ', '#', '#', ' ', '#', ' ', '$', '$',
            ' ', '$', ' ', '$', '#', '#', '.', '.', '#'],
        ['#', ' ', '.', '.', '#', ' ', '#', ' ', ' ', '$',
            ' ', ' ', ' ', ' ', ' ', ' ', '#', '.', '#'],
        ['#', ' ', '.', '.', '#', ' ', '#', ' ', '$', '$',
            '$', ' ', '$', '$', '$', ' ', '#', '.', '#'],
        ['#', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', '#', ' ', '#', '.', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', ' ', '#', '.', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', '#', '.', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', '#', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '#', '#', ' ', ' ', '#', '#', '#', '$', ' ', '#'],
        [' ', ' ', '#', '#', ' ', ' ', ' ', '@', ' ', ' ', '$', ' ', ' ', '#'],
        [' ', '#', '#', ' ', ' ', '$', ' ', '$', '$', '#', '#', ' ', '#', '#'],
        [' ', '#', ' ', ' ', '#', '$', '#', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', '#', ' ', '$', ' ', '$',
            '$', ' ', '#', ' ', '#', '#', '#'],
        [' ', '#', ' ', ' ', ' ', '$', ' ', '#', ' ', ' ',
            '#', ' ', '$', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', ' ', ' ', ' ', ' ', '#', ' ',
            ' ', '$', '$', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', '#', '#', ' ', '$', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '.', ' ', ' ', ' ', ' ', '#', '#', '#', ' ',
            ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', ' ', '.', '.', '#', ' ', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '#', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', '#', '#', '#', '#',
            '#', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', '$', ' ', '$',
            ' ', '$', ' ', '$', '#', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '$', '@', '$',
            ' ', ' ', ' ', '#', '#', ' ', '#', '#'],
        ['#', ' ', '#', ' ', '#', '$', ' ', '$', ' ',
            '$', '#', '#', '#', '.', '.', '.', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '$', ' ', '$',
            ' ', ' ', '#', '#', '.', '.', '.', '#'],
        ['#', ' ', '#', '#', '#', '$', '$', '$', ' ',
            '$', ' ', '#', '#', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#',
            '#', ' ', '#', '#', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', ' ', ' ', ' ', '#',
            '#', ' ', '#', '#', '.', '.', '.', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#',
            ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', '#', ' ', ' ', ' ', '#', '#',
            ' ', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ',
            ' ', '#', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', ' ', ' ', '$', ' ', '#', '$', ' ', '#', ' ',
            ' ', '#', ' ', ' ', '.', '.', '.', ' ', '#'],
        ['#', ' ', '#', ' ', '$', '#', '@', '$', '#', '#',
            ' ', '#', ' ', '#', '.', '#', '.', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', '#', '$', ' ', ' ', '#',
            ' ', ' ', ' ', ' ', '.', ' ', '.', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', ' ', '$', ' ', '#',
            ' ', '#', ' ', '#', '.', '#', '.', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', '#', ' ', ' ', '#', '#',
            '$', ' ', '$', ' ', '.', ' ', '.', ' ', '#'],
        ['#', ' ', '$', ' ', '#', ' ', ' ', ' ', '#', ' ',
            ' ', '#', '$', '#', '.', '#', '.', ' ', '#'],
        ['#', '#', ' ', '$', ' ', ' ', '$', ' ', ' ', ' ',
            '$', ' ', ' ', '$', '.', '.', '.', ' ', '#'],
        [' ', '#', '$', ' ', '#', '#', '#', '#', '#', '#',
            ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '$', '@', '$', ' ', '#'],
        [' ', '#', '$', '$', ' ', '#', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', '#', '#', '#', '.', '.', '.',
            '.', '.', '.', '#', '#', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', '$', '.', '.', '.',
            '.', '.', '.', '#', '#', ' ', '#', ' ', '#'],
        [' ', '#', ' ', '#', '#', '#', '.', '.', '.',
            '.', '.', '.', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', ' ', '#', '#', '#', '#',
            ' ', '#', '#', '#', ' ', '#', '$', '#', '#'],
        ['#', ' ', ' ', '#', '$', ' ', ' ', ' ', '#',
            ' ', ' ', '$', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '$', '$', '$', ' ',
            ' ', '#', ' ', '$', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', '$', ' ', '#',
            '#', '#', '$', '$', ' ', '#', ' ', '#'],
        ['#', '#', '#', '#', '#', ' ', ' ', ' ', ' ',
            ' ', '$', ' ', ' ', ' ', '#', ' ', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#',
            '#', '#', ' ', ' ', ' ', '#', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#',
            '#', '#', '#', '#', '#', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', '$', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', ' ', '#', '$', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', '$', ' ', ' ', '#', '#', '$', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', ' ', '@', ' ', '$', ' ', '#', ' ', '$', '#'],
        [' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ',
            ' ', ' ', '$', ' ', '#', '#', '#', '#'],
        [' ', '#', '#', ' ', '#', '#', '#', '#', '$',
            '#', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', '$', '#', '.', '.', '.', '.',
            '.', '#', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '$', '.', '.', '*', '*',
            '.', ' ', '$', '#', ' ', '#', '#', '#'],
        ['#', '#', ' ', ' ', '#', '.', '.', '.',
            '.', '.', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', '#', '#', ' ',
            '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', '$', '$', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#'],
        ['#', ' ', '$', ' ', ' ', '#', '#', '#', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', '$', ' ', '$', ' ', ' ', ' ', '$', '#'],
        ['#', '#', '#', '@', ' ', '#', '$', ' ', ' ', ' ', ' ', '#', '#'],
        [' ', '#', ' ', ' ', '#', '#', ' ', ' ', '$', ' ', '$', ' ', '#', '#'],
        [' ', '#', ' ', '$', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '.', '#'],
        [' ', '#', ' ', ' ', '#', '$', '#', '#', '$', ' ', ' ', '#', '.', '#'],
        [' ', '#', '#', '#', ' ', ' ', ' ', '$', '.', '.', '#', '#', '.', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '.', '*', '.', '.', '.', '#'],
        [' ', ' ', '#', ' ', '$', '$', ' ', '#', '.', '.', '.', '.', '.', '#'],
        [' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', '#'],
        [' ', ' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', '.', '.', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '.', '.', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '.', '.', ' ', ' ',
            '#', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', '#', '#', '#', '#', '#', '#',
            '#', ' ', ' ', '#', ' ', ' ', '#', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', '#', ' ', ' ',
            '#', '#', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', '#', '#', ' ',
            ' ', '#', '#', '#', '#', ' ', '#', '#'],
        ['#', ' ', ' ', '$', ' ', ' ', '#', '#',
            '#', '#', '#', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', '$', ' ', ' ', '$',
            ' ', ' ', '#', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', '@', '$', ' ', ' ', '$', ' ',
            ' ', ' ', '#', ' ', ' ', ' ', '#', '#'],
        ['#', '#', '#', '#', ' ', '#', '#', ' ',
            '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', ' ', ' ',
            '.', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', ' ', '#',
            '.', ' ', ' ', ' ', ' ', '@', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', ' ', '#', '#',
            '.', '.', '#', ' ', '#', '#', '#', '#'],
        ['#', '#', ' ', ' ', '#', ' ', '.', '.', '#', '#',
            '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', ' ', '$', ' ', '#', '.', '.', '.', ' ', ' ',
            ' ', '$', ' ', '#', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '.', '.', ' ', '#', '#',
            ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#'],
        ['#', '#', '#', '#', '$', '#', '#', '$', '#', ' ',
            '$', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
        [' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', ' ',
            '#', '$', ' ', '$', '$', ' ', '#', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', '$', ' ', '#', ' ', '#',
            ' ', ' ', '#', ' ', '$', '#', '#', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', ' ', ' ', '#'],
        [' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', '@', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', ' ', '$', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        ['#', ' ', '$', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', '#'],
        ['#', '#', ' ', '$', ' ', ' ', '$', ' ', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', '#', ' ', '$', ' ', '$', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
        ['#', '#', ' ', '#', ' ', ' ', '$', ' ', ' ', '#', ' ', '#', ' ', '#'],
        ['#', '#', ' ', '#', ' ', '#', '$', '#', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', '#', ' ', '#', '#', '#', ' ', ' ', ' ', '#',
            ' ', '#', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', '$', ' ', ' ', '#', '#', '#', '#',
            ' ', '#', ' ', '#', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', '$', ' ', ' ', ' ', ' ',
            '$', ' ', ' ', ' ', '.', '.', '#', '.', '#'],
        ['#', '#', '#', '#', '$', ' ', ' ', '$', '#', ' ',
            '$', ' ', ' ', ' ', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ',
            ' ', '#', '#', ' ', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', '$', ' ', ' ', '#', '@', ' ', '#'],
        ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '$',
            '#', '#', '#', '#', ' ', ' ', '#', '#', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ',
            '#', ' ', ' ', '#', '$', ' ', '.', '.', '#'],
        ['#', ' ', '#', ' ', '$', ' ', ' ', '$', ' ', ' ',
            '#', ' ', ' ', '#', ' ', ' ', '#', '.', '#'],
        ['#', ' ', '#', ' ', '$', ' ', ' ', '#', ' ', ' ',
            ' ', ' ', ' ', '#', '$', ' ', '.', '.', '#'],
        ['#', ' ', '#', ' ', ' ', '#', '#', '#', ' ', '#',
            '#', ' ', ' ', ' ', ' ', ' ', '#', '.', '#'],
        ['#', ' ', '#', '#', '#', ' ', ' ', '#', ' ', ' ',
            '#', ' ', ' ', '#', '$', ' ', '.', '.', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '$',
            '#', '#', '#', '#', ' ', ' ', '#', '.', '#'],
        ['#', ' ', '#', '$', ' ', ' ', ' ', '$', ' ', ' ',
            '$', ' ', ' ', '#', '*', ' ', '.', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', '$', ' ', '#', ' ', '$',
            ' ', '$', ' ', '#', ' ', ' ', '#', '.', '#'],
        ['#', '#', '#', '#', ' ', '$', '#', '#', '#', ' ',
            ' ', ' ', ' ', '#', '*', ' ', '.', '.', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '$', '$',
            ' ', '#', '#', '#', '.', '.', '.', '.', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', '#', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        ['#', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', ' ', '#'],
        ['#', '#', ' ', '#', '@', '#', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', '$', '$', ' ', '$', ' ', ' ', '$', '$', '#'],
        ['#', ' ', ' ', '#', ' ', '#', '#', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', '#', '#', ' ',
            ' ', '$', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '#', ' ', ' ', '$', '$',
            '$', ' ', '$', '#', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', '#', '#', ' ',
            ' ', ' ', '.', '.', '.', '.', '#'],
        [' ', '#', ' ', '#', ' ', ' ', ' ', '#',
            ' ', '#', '.', '.', ' ', '.', '#'],
        [' ', '#', ' ', ' ', ' ', '#', ' ', '#',
            ' ', '#', '#', '.', '.', '.', '#'],
        [' ', '#', '#', '#', '#', '#', ' ', '$',
            ' ', ' ', '#', '.', '.', '.', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', ' ',
            ' ', ' ', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', ' ', ' ',
            ' ', ' ', ' ', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#',
            '#', '#', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '$', '#', ' ', ' ', '#', ' ',
            ' ', '$', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', ' ', '$', ' ', ' ', '$',
            ' ', '#', ' ', '$', ' ', '$', ' ', ' ', '#'],
        ['#', '#', '$', ' ', '$', ' ', ' ', ' ', '#', ' ',
            '@', '#', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', ' ', '#', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '#', '.', '.',
            '.', '.', '.', '.', '.', '#', ' ', '$', '#'],
        ['#', ' ', '#', '#', ' ', ' ', '#', ' ', '.',
            '.', '.', '.', '.', '.', '#', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '$', '.', '.',
            '.', '.', '.', '.', '.', '.', '$', ' ', '#'],
        ['#', ' ', '#', ' ', '$', ' ', '#', '.', '.',
            '.', '.', ' ', '.', '.', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '$', '#', '#', '#',
            '#', '$', '#', '#', '#', '#', ' ', '$', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', '#', '#', '#', ' ',
            '$', ' ', ' ', ' ', '$', ' ', ' ', '#', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', ' ', ' ', '$', ' ',
            '$', ' ', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ',
            '$', ' ', '#', '#', '#', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', ' ', '$', '#',
            '$', ' ', '#', ' ', ' ', '#', '#'],
        ['#', '.', '.', ' ', '#', ' ', ' ', '#',
            ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '.', '.', ' ', '#', ' ', '$', '#', '$',
            ' ', '#', ' ', ' ', '$', '#', '#', '#', '#'],
        ['#', '.', ' ', ' ', '#', ' ', ' ', ' ', ' ',
            ' ', '#', '$', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', '.', '.', ' ', ' ', ' ', '$', '#', ' ',
            ' ', '#', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '@', '#', ' ', ' ', '#', '$',
            ' ', '#', '$', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', '.', '.', ' ', '#', ' ', '$', '#', ' ',
            ' ', ' ', ' ', ' ', '$', '#', ' ', ' ', '#'],
        ['#', '.', '.', ' ', '#', ' ', ' ', '#', '$', '$',
            '#', '$', ' ', ' ', '#', ' ', ' ', '#', '#'],
        ['#', '.', '.', ' ', '#', ' ', '$', '#', ' ', ' ',
            '#', ' ', ' ', '$', '#', '$', ' ', ' ', '#'],
        ['#', '.', '.', ' ', '#', ' ', ' ', '#', ' ', ' ',
            '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '.', ' ', '#', '#', '#', '#', ' ', ' ',
            '#', '#', '#', '#', '#', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', ' ', ' ', '#', '#', '#',
            '#', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.',
            '.', '.', ' ', ' ', '.', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.',
            '.', '.', '$', '$', '.', '#', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '$', ' ', '#', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '$', ' ', ' ',
            '$', ' ', ' ', ' ', ' ', ' ', '$', ' ', '#'],
        ['#', '#', ' ', '#', '#', '#', '#', ' ', ' ', ' ',
            '#', ' ', ' ', '$', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', '#', '#', ' ', ' ', '#', ' ', '#', '#'],
        ['#', ' ', ' ', '$', '#', ' ', ' ', '#', ' ',
            '#', '#', ' ', ' ', '#', '#', '#', ' ', '#'],
        ['#', ' ', '$', ' ', '#', '$', '#', '#', '#',
            ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'],
        ['#', '#', '#', ' ', ' ', '$', ' ', '#', ' ',
            ' ', '#', ' ', ' ', '#', '#', '#', ' ', '#'],
        [' ', '#', '#', ' ', ' ', ' ', ' ', '$', ' ', '#',
            '#', ' ', '#', ' ', ' ', '#', ' ', '#', '#'],
        [' ', '#', ' ', '$', ' ', ' ', '#', ' ', ' ', '$',
            ' ', ' ', '$', ' ', '$', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '$', ' ', ' ', '$', '#', '$',
            '$', '$', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', ' ', ' ', '$', ' ', ' ',
            ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', '@', '#', '#', ' ', ' ',
            '#', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#'],
        ['#', ' ', ' ', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', ' ', '.', '.',
            '#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', '#', ' ', '#', ' ', '#', '#',
            '#', '#', '#', ' ', '.', '.', '.', '#'],
        ['#', '#', '$', '#', ' ', ' ', ' ', ' ', '.',
            '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', '#', '#', '$', '#', '#', '#',
            '#', '#', '#', ' ', ' ', '#', '#', '#', '#'],
        ['#', ' ', '$', ' ', '#', ' ', ' ', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '@', ' ', '#'],
        ['#', '#', '$', ' ', '#', ' ', '$', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '#', '$', '$', '$', '#',
            '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', ' ', '#', '$', '#', '$', '#', '#', '#'],
        ['#', ' ', '#', '#', '#', '#', ' ', '#', '$',
            '$', '$', '$', '$', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', ' ', '$', ' ',
            ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', '#',
            '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', ' ', '#', '#', '#', '#', '#', '#', '$', '#',
            '#', '#', '#', '#', '#', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',
            ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', ' ', ' ', '#', ' ', ' ', '#', '.', '.', '.', '#', '#', '#'],
        ['#', ' ', ' ', '$', '#', ' ', ' ', '#', '.', '.', '.', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', '#', '$', '$', ' ', '.', '.', '.', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', '#', ' ', ' ', '#', '.', '.', '.', ' ', '.', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', '$', '#',
            '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '$', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', '$', ' ', '$', ' ', '#'],
        ['#', '#', ' ', ' ', '#', ' ', ' ', '$',
            '$', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', ' ',
            ' ', '#', '#', '$', '$', '@', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ',
            ' ', ' ', ' ', ' ', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '.', '.', '.', ' ', ' ', ' ', '#', ' ',
            ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#'],
        ['#', '#', '.', '.', '.', '.', '.', ' ', ' ', '$',
            '#', '#', ' ', '#', ' ', '#', '$', ' ', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#', ' ', ' ',
            '$', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#', ' ', ' ',
            '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', ' ',
            '$', ' ', ' ', '$', ' ', '$', ' ', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '$',
            '#', '#', '$', ' ', '#', '#', '$', '#', '#'],
        [' ', '#', '#', ' ', ' ', ' ', '$', ' ', ' ', ' ',
            ' ', '#', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', '#', ' ', '#', '#', '#',
            ' ', '#', ' ', ' ', '#', '#', '$', ' ', '#'],
        [' ', '#', ' ', '$', ' ', '$', '$', ' ', ' ', ' ',
            ' ', ' ', '$', ' ', ' ', '$', ' ', ' ', '#'],
        [' ', '#', ' ', '$', ' ', ' ', ' ', ' ', '$', '#',
            '#', '$', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '@', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', '#', '#', ' ', '$', ' ',
            ' ', '$', ' ', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', ' ', '$', ' ', ' ',
            '$', ' ', '$', ' ', '#', '#', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '$',
            '$', ' ', ' ', '#', '#', '.', '.', '#'],
        ['#', ' ', ' ', '#', '#', '#', '#', '#', '#',
            ' ', '#', '#', '#', '.', '.', ' ', '#'],
        ['#', '#', ' ', '#', ' ', ' ', '#', ' ', ' ',
            ' ', ' ', '#', '.', '.', '.', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', ' ', '#', '.', '.', '.', ' ', '#'],
        ['#', '@', ' ', '#', '$', ' ', '#', '#', ' ',
            '#', '#', '#', '#', '.', '.', '.', '#'],
        ['#', '#', '#', '#', ' ', ' ', '$', ' ', '$',
            '$', ' ', ' ', '#', '#', '.', '.', '#'],
        [' ', ' ', ' ', '#', '#', ' ', ' ', '$', ' ',
            '$', ' ', ' ', '$', '.', '.', '.', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', '$', '$', ' ',
            ' ', '$', ' ', '#', ' ', ' ', '.', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '$',
            ' ', '$', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', '$', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', '#', ' ', '#', ' ', ' ', ' ', '$', '#', '$',
            '#', '@', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ',
            '$', ' ', '#', ' ', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', ' ', '#', '#'],
        ['#', ' ', ' ', '#', '#', ' ', '.', '.', '*', '.',
            '.', '.', '.', '.', ' ', '#', ' ', '#', '#'],
        ['#', '#', ' ', '#', '#', ' ', '*', '.', '*', '.',
            '.', '*', '.', '*', ' ', '#', ' ', '#', '#'],
        ['#', ' ', '$', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', ' ', '#', '#', '$', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', ' ', ' ', '$', ' ', ' ',
            '$', ' ', ' ', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ',
            ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', ' ', ' ', '#', ' ',
            ' ', ' ', ' ', ' ', '$', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', '#', '#', '#', '#',
            ' ', '$', '#', '#', ' ', '#', ' ', '#', '#'],
        ['#', ' ', '$', ' ', '#', '#', ' ', ' ', ' ',
            '#', ' ', '#', '#', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', '@', '$', '$', ' ',
            '#', ' ', '#', '#', '$', '$', '$', ' ', '#'],
        ['#', '#', ' ', '#', '#', '#', ' ', ' ', ' ',
            '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', ' ', '#', ' ', ' ', ' ', '#', '#',
            '#', ' ', '#', '#', '#', '#', '#', '$', '#'],
        ['#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ',
            '$', ' ', ' ', '#', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', '#', '#', '#', ' ', '#', '#', ' ',
            '$', ' ', '#', '.', '.', '.', '.', '#', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', '$', ' ', '#', ' ',
            ' ', ' ', '#', '.', '.', '$', '.', ' ', '#'],
        ['#', ' ', ' ', '#', '#', ' ', '$', ' ', '#', ' ',
            ' ', '#', '#', '.', '.', '.', '.', ' ', '#'],
        ['#', '#', '#', '#', '#', ' ', ' ', ' ', '#', '#',
            '#', '#', '#', '#', '.', '.', '.', '#', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#',
            ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', ' ', ' ', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '$', '#', ' ', '$', '@',
            '$', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', '$', ' ', ' ', '$', ' ', ' ', '#',
            ' ', '$', ' ', '$', '#', ' ', ' ', '#', '#'],
        ['#', '#', ' ', ' ', '$', '#', '#', ' ', '#',
            '$', ' ', '$', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', '#', ' ', '#',
            ' ', ' ', ' ', '$', '$', '$', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', ' ', '$', ' ',
            ' ', '$', '#', '#', ' ', '#', '#', '#', '#'],
        ['#', ' ', '$', ' ', '$', ' ', '#', '$',
            '#', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', '#', '#', '#', ' ',
            ' ', '#', '#', '#', '$', ' ', '#'],
        [' ', '#', ' ', ' ', '#', '.', '.', '.',
            '.', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '.', '.', '.',
            '.', '.', '.', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', '.', '.', '.', '.', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', '.', '.', '.', '#', '#'],
        [' ', ' ', ' ', '#', '.', '.', '.', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#'],
        [' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '$', '#'],
        ['#', '#', ' ', '$', ' ', ' ', '#', '#', ' ', '#', '#', '#'],
        ['#', '@', '$', ' ', '$', ' ', '#', ' ', '$', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', '#', '#', ' ', ' ', ' ', '$', '#'],
        [' ', '#', '.', '.', '.', '.', '#', '$', ' ', '$', ' ', '#'],
        [' ', '#', '.', '.', '.', '.', '#', ' ', ' ', ' ', '$', '#'],
        [' ', '#', '.', '.', '.', '.', ' ', ' ', '$', '$', ' ', '#', '#'],
        [' ', '#', '.', '.', '.', ' ', '#', ' ', '$', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '$', ' ', '$', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '$', ' ', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', ' ', '$', ' ', ' ', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', ' ', '#', '#', ' ', '$', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', '$', '$', ' ', '#', ' ', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', '$', ' ', '#', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '$', '#', ' ', '$', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '.', '.', '#', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '.', '.', ' ', '$', ' ', '#', '@', '#'],
        ['#', '.', '.', '.', '.', '.', '#', ' ', '$', '#', ' ', '#'],
        ['#', '#', '.', '.', '.', '.', '#', ' ', ' ', '$', ' ', '#'],
        ['#', '#', '#', '.', '.', '#', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '.', '.', '.', '.', ' ', ' ', ' ', '#', '#'],
        [' ', '#', '.', '#', '.', '#', ' ', ' ', '$', ' ', '#', '#'],
        ['#', '#', '.', '.', '.', '.', '#', ' ', '#', ' ', '@', '#', '#'],
        ['#', ' ', '.', '.', '.', '.', '#', ' ', ' ', '#', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#', '$', ' ', '#', '#', '$', ' ', '#'],
        ['#', '#', ' ', '#', '#', '#', ' ', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', '$', ' ', ' ', '$', ' ', '$', ' ', '$', '#', ' ', ' ', '#'],
        [' ', '#', ' ', '#', ' ', ' ', '$', ' ', '$', ' ', '#', '#', ' ', '#'],
        [' ', '#', ' ', ' ', '#', '#', '#', ' ', ' ', '#', '#', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#'],
        [' ', '#', ' ', ' ', '$', ' ', '#', ' ', ' ', '$', ' ', ' ', '#'],
        [' ', '#', '#', '#', '$', ' ', '$', ' ', ' ', ' ', '#', '#', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#',
            ' ', '#', '#', '#', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', '$', '$', '#', ' ', ' ', ' ',
            '@', ' ', ' ', '.', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', '#', '#', '#', ' ',
            ' ', ' ', '#', ' ', '.', '.', '.', '.', '#'],
        ['#', '#', ' ', '#', '#', ' ', '#', '#', '#', ' ',
            ' ', '#', ' ', ' ', '.', '.', '.', '.', '#'],
        [' ', '#', ' ', '$', ' ', '$', ' ', ' ', ' ', ' ',
            ' ', '#', ' ', '#', ' ', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', '$', ' ', '$', '#', '#', ' ',
            ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', '#', ' ', ' ', '#', '#',
            '#', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', '#', '$', ' ', ' ', ' ',
            '#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', '$', ' ', ' ', '#', ' ',
            '#', '#', ' ', '#', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', '#', ' ', '$', ' ', '$', ' ', ' ',
            ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '#', '#', ' ', '#',
            '#', ' ', '#', ' ', '#', '#', '#', '#', '#'],
        ['#', ' ', '$', '$', ' ', ' ', ' ', ' ', ' ', '$', '$', ' ', ' ', '#'],
        ['#', '#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '$', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', ' ', ' ', '#', '#',
            '#', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', '#', '#', '#', ' ',
            ' ', '$', ' ', '$', ' ', '$', ' ', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', '#', '#', ' ',
            '#', '#', ' ', '#', '#', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', '$', ' ', ' ',
            ' ', ' ', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', '#', '#', ' ', '$', ' ', ' ', '#', '#', ' ',
            '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#'],
        [' ', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ',
            '#', '#', '#', '#', '#', '$', '$', ' ', '#'],
        [' ', '#', '#', '$', '#', '#', '#', '#', '#', ' ',
            '@', '#', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', '$', ' ', ' ', '#', '#', '#', '$',
            '#', '#', '#', ' ', '$', ' ', ' ', '#', '#'],
        [' ', '#', ' ', '$', ' ', ' ', '#', ' ', ' ',
            ' ', '#', '#', '#', ' ', ' ', '#', '#', '#'],
        [' ', '#', ' ', '$', '$', ' ', '$', ' ',
            '#', ' ', ' ', ' ', '$', '$', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', '#',
            ' ', ' ', ' ', '#', '#', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#',
            '.', '.', ' ', '.', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', '.', '.', '.',
            '.', '.', '.', '.', '.', '.', '#'],
        [' ', ' ', ' ', ' ', '#', '.', '.', '.',
            '.', '.', '.', '.', '.', '.', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', ' ', ' ', ' ',
            '#', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '#', '#', '#', ' ', '$', ' ', ' ',
            ' ', ' ', '$', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '.', ' ', '$', ' ', '$', ' ', '#',
            ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '.', '#', '$', '#', '#', '#', '#',
            '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', '#', '$', ' ', ' ', '#', '$', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', '$', '$', ' ', '$', ' ',
            '$', ' ', ' ', '$', '#', '#', ' ', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', '$', ' ', ' ', ' ', '#',
            '$', '#', '$', ' ', '#', '#', '$', ' ', '#'],
        [' ', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#',
            ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', '$', ' ', '$', ' ',
            '#', '#', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', ' ', ' ',
            '$', ' ', ' ', '$', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '#', ' ', ' ', ' ',
            '#', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', '#',
            '#', '@', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '#', ' ', '@', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '$', '#', '#', ' ', '$', '#'],
        ['#', '#', '$', '#', '.', '.', '.', '#', ' ', '#'],
        [' ', '#', ' ', '$', '.', '.', '.', ' ', ' ', '#'],
        [' ', '#', ' ', '#', '.', ' ', '.', '#', ' ', '#', '#'],
        [' ', '#', ' ', ' ', ' ', '#', ' ', '#', '$', ' ', '#'],
        [' ', '#', '$', ' ', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '.', '.', '.', '.', '#'],
        ['#', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ',
            ' ', ' ', '#', '#', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', '$', '$', '#', '#', ' ', ' ', '$',
            ' ', '@', '#', '#', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '$', '$', ' ',
            '$', '#', ' ', ' ', '.', '.', '.', '.', '#'],
        ['#', ' ', ' ', '$', ' ', '#', '#', ' ', '$', '$',
            ' ', '#', ' ', '#', ' ', '.', '.', '.', '#'],
        ['#', ' ', ' ', '$', ' ', '#', '#', ' ', '$', ' ',
            ' ', '#', ' ', ' ', '.', '.', '.', '.', '#'],
        ['#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#',
            '#', '#', ' ', '#', '#', '.', '#', '#', '#'],
        ['#', '#', ' ', ' ', ' ', '$', ' ', ' ', '$', ' ',
            '#', '#', ' ', ' ', ' ', '.', ' ', ' ', '#'],
        ['#', ' ', '$', '#', '#', '#', ' ', ' ', '#', ' ',
            '#', '#', '#', '#', '#', ' ', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', ' ', ' ', '#',
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '#', '$', ' ', '$',
            ' ', '$', '#', '#', '#', ' ', ' ', '#'],
        ['#', ' ', '$', '$', '$', '#', ' ', '$', ' ',
            ' ', ' ', '#', ' ', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '$', '$', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ',
            '#', '$', '$', ' ', '$', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', '#', '$', ' ', '#', '$',
            '#', ' ', ' ', '#', '#', ' ', '@', '#'],
        [' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ',
            '#', ' ', '$', ' ', '#', ' ', '#', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', ' ', '$',
            ' ', '#', '$', ' ', ' ', '#', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', ' ', '#',
            ' ', '$', ' ', ' ', ' ', '#', ' ', '#'],
        [' ', ' ', ' ', '#', '#', ' ', '$', ' ',
            '$', ' ', ' ', ' ', '#', '#', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', '#', ' ',
            ' ', '#', '#', ' ', ' ', '$', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', ' ', ' ',
            '#', '#', ' ', '$', '$', '#', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '$', '$',
            ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '.', '.', '#', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '#', '.', '.', '.', ' ', '#', '#'],
        ['#', '.', '.', '.', '.', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '.', '.', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', '#', '#', ' ', ' ', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',
            '#', ' ', ' ', '$', '$', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#',
            ' ', '$', '$', ' ', ' ', '$', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ',
            '$', ' ', ' ', ' ', ' ', '$', ' ', '#'],
        ['#', '#', '#', '#', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', '$', '$', ' ', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#',
            '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', '$', '$', '$', '@', '#'],
        ['#', '.', '#', ' ', '#', '#', '#', '#', '#', '#',
            '#', ' ', '#', '#', ' ', ' ', ' ', '#', '#'],
        ['#', '.', '#', ' ', '#', '#', '#', '#', '#', '#',
            '#', '.', ' ', '#', '$', ' ', '$', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.',
            '.', '.', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', ' ', ' ', '$', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', '#', '#', ' ', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ',
            ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#',
            ' ', '$', ' ', '$', ' ', ' ', ' ', '@', '#'],
        [' ', ' ', '#', ' ', '#', '#', ' ', '#', '#',
            '$', '#', '$', ' ', '$', ' ', '$', '#', '#'],
        ['#', '#', '#', ' ', '.', '.', '.', '.', '.',
            '.', '#', ' ', ' ', '$', '$', ' ', '#', '#'],
        ['#', ' ', ' ', ' ', '.', '.', '.', '.', '.',
            '.', '#', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', '.', '.', '.', '.', '.',
            '.', '#', '$', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', '.', '.', '.', '.', '.',
            '.', ' ', '$', '$', '#', ' ', '$', ' ', '#'],
        ['#', ' ', '$', ' ', '#', '#', '#', ' ', '#',
            '#', '#', '$', ' ', ' ', '$', ' ', '#', '#'],
        ['#', '#', '#', ' ', ' ', '$', ' ', ' ', '$',
            ' ', ' ', '$', ' ', ' ', '$', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', '$', ' ', ' ', '$',
            ' ', ' ', '$', ' ', ' ', '$', ' ', '#'],
        [' ', ' ', '#', '#', '#', '#', '#', '#', ' ',
            ' ', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#',
            ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#',
            ' ', ' ', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', ' ', '#', '$', '$',
            ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ',
            '#', ' ', ' ', '#', '#', ' ', '#', '#', '#'],
        ['#', ' ', ' ', '#', '#', '#', ' ', '$', '#', '$',
            ' ', ' ', '$', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', '.', '.', '.', ' ', ' ', ' ', ' ', '#', ' ',
            '#', '#', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '.', '.', '.', '#', ' ', ' ', ' ', ' ', '@',
            ' ', '#', ' ', '#', '#', '#', ' ', '#', '#'],
        ['#', '.', '.', '.', '#', ' ', ' ', '#', '#', '#',
            ' ', ' ', '$', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', ' ', '#',
            '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', ' ',
            '$', '@', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', '$', ' ', '#', '#', '$',
            ' ', '#', '#', '#', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', '#', '#', '#', '#', ' ',
            '$', ' ', ' ', ' ', ' ', '$', ' ', '#'],
        [' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#',
            ' ', ' ', '#', '$', ' ', '#', '#', '#', '#'],
        ['#', '#', ' ', ' ', '#', '#', '#', '#', ' ', '#',
            '#', '$', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', '#', ' ', ' ', '$', ' ', ' ',
            '#', ' ', '#', '#', ' ', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', ' ', '#', '.', '.', '.', '#', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#',
            '#', ' ', ' ', '.', '.', '.', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ',
            '#', ' ', '#', '.', '.', '.', '#', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', ' ', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '#', ' ', '#', ' ', ' ', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '#', '#', '#', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', '.', '.', '.', '.', '#', '#', ' ',
            '$', ' ', ' ', '$', '#', '#', '#'],
        ['#', '#', '.', '.', '.', '.', '#', '#',
            ' ', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', '#', '#', '.', '.', '.', ' ', '#',
            '#', ' ', '$', ' ', '$', ' ', '#'],
        ['#', ' ', '#', '#', ' ', ' ', ' ', ' ',
            '#', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', '#', ' ', '#', ' ',
            '#', '#', '#', ' ', '#', '#', '#', '#'],
        ['#', ' ', '$', ' ', '#', ' ', '#', '$',
            ' ', ' ', '$', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '@', ' ', '$',
            ' ', ' ', ' ', ' ', '$', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', '$', ' ',
            '$', '$', ' ', '$', ' ', '#', '#', '#'],
        ['#', ' ', ' ', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#'],
        ['#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        ['#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', ' ', '#', '#'],
        ['#', ' ', '#', ' ', '$', ' ', '$', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '$', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '$', ' ', ' ', '$', '$', '#', ' ', ' ', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', '#', '#', ' ', '#', ' ', '$', '#', '#'],
        [' ', ' ', '#', '#', '$', '#', ' ', ' ', ' ', '$', ' ', '@', '#'],
        [' ', ' ', ' ', '#', ' ', ' ', '$', ' ', '$', ' ', '#', '#', '#'],
        [' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '$', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#'],
        [' ', ' ', '#', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', '#', '.', '.', '.', '.', '.', '.', '.', '#', '#', '#'],
        [' ', ' ', '#', '.', '.', '.', '.', '.', '.', '.', '#'],
        [' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#'],
        ['#', '#', ' ', ' ', '$', ' ', ' ', ' ', ' ',
            ' ', ' ', '$', ' ', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', '#', ' ', '#', '#',
            ' ', ' ', ' ', '#', '#', '.', '.', '.', '#'],
        ['#', ' ', '#', '$', '$', ' ', '$', ' ', '$',
            '$', '#', '$', '#', '#', '.', '.', '.', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', ' ', '@', ' ',
            ' ', '#', ' ', ' ', ' ', '.', '.', '.', '#'],
        ['#', ' ', ' ', '$', '#', ' ', '#', '#', '#',
            '$', '$', ' ', ' ', ' ', '.', '.', '.', '#'],
        ['#', ' ', '$', ' ', ' ', '$', '$', ' ', ' ',
            '$', ' ', '#', '#', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '$', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', '*', '.', '*', '#', '*', '.', '*', '#'],
        [' ', ' ', '#', '.', '*', '.', '*', '.', '*', '.', '#'],
        [' ', ' ', '#', '*', '.', '*', '.', '*', '.', '*', '#'],
        [' ', ' ', '#', '.', '*', '.', '*', '.', '*', '.', '#'],
        [' ', ' ', '#', '*', '.', '*', '.', '*', '.', '*', '#'],
        [' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '$', ' ', '$', ' ', '$', ' ', '$', ' ', '$', ' ', '#'],
        ['#', '#', ' ', '$', ' ', '$', ' ', '$', ' ', '$', ' ', '#', '#'],
        [' ', '#', '$', ' ', '$', ' ', '$', ' ', '$', ' ', '$', '#'],
        [' ', '#', ' ', ' ', ' ', '$', '@', '$', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '$', '$', ' ', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#',
            '$', ' ', ' ', '$', ' ', '#', '#'],
        [' ', ' ', '#', '#', '#', '#', ' ', ' ',
            ' ', ' ', '$', ' ', ' ', ' ', '#'],
        ['#', '#', '#', ' ', ' ', '#', ' ', '#',
            '#', '#', '#', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', '#',
            '.', '.', '.', '.', '$', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '$', ' ',
            '.', '.', '.', '.', '#', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '#', ' ', '#',
            '.', '*', '.', '.', '#', ' ', '#'],
        ['#', '#', '#', ' ', ' ', '#', '#', '#',
            '#', ' ', '#', '#', '#', ' ', '#'],
        [' ', ' ', '#', '#', '#', '#', ' ', '@',
            '$', ' ', ' ', '#', '#', '$', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '#',
            ' ', '$', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',
            ' ', ' ', '#', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',
            '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', ' ', ' ', '#', '#', '.', '.',
            ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', '#', '#', '.', '.', '*',
            ' ', '$', ' ', ' ', ' ', ' ', '$', ' ', '#'],
        [' ', ' ', ' ', '#', '#', '.', '.', '*', '.',
            '#', ' ', '#', ' ', '#', '$', ' ', '#', '#'],
        [' ', ' ', ' ', '#', '.', '.', '*', '.', '#',
            ' ', '#', ' ', '#', ' ', '$', ' ', ' ', '#'],
        ['#', '#', '#', '#', '.', '.', '.', '#', ' ',
            ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '@', '$', ' ', '$', ' ', '#', '#',
            '#', ' ', ' ', '#', ' ', '#', ' ', '#', '#'],
        ['#', ' ', '$', ' ', ' ', ' ', '$', ' ', ' ',
            ' ', '#', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '$', '$', ' ', ' ', ' ', '#',
            ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', ' ', '$', ' ', ' ', ' ',
            '#', ' ', '#', ' ', '#', '#', '#', '#', '#'],
        [' ', ' ', '#', ' ', '$', '#', ' ', '#', '#', '#',
            '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', '#', '$', ' ', ' ', ' ', '#', ' ', ' ',
            ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', '#', '#', '#', ' ', ' ',
            ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ',
            ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#'],
        [' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ',
            ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#',
            ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', '#', '$', ' ', '$', ' ', ' ', '#',
            ' ', '$', '$', ' ', '#', ' ', '$', ' ', '#'],
        ['#', '.', '#', ' ', '.', ' ', '.', '$', ' ', '#',
            ' ', '#', '.', '.', '#', ' ', '#', '.', '#'],
        ['#', '.', '#', '#', '#', '#', '.', '#', ' ', '#',
            ' ', '#', ' ', '#', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ',
            ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', '$', ' ', '#', ' ', '#', ' ', '#',
            '#', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#',
            '.', '$', ' ', '#', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', '$', '$', '.', '#', ' ', '#', ' ', '#',
            '#', ' ', ' ', '#', ' ', '#', '#', ' ', '#'],
        ['#', '$', ' ', '#', ' ', '#', ' ', '#', ' ', ' ',
            '#', ' ', '#', '#', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', '.', '#', ' ', '#', ' ', '#', '#', ' ',
            '#', ' ', '#', ' ', ' ', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ',
            '#', ' ', '#', ' ', '#', '#', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', ' ', '#', '#', ' ', '#', ' ',
            '#', ' ', '#', ' ', '#', ' ', '$', '.', '#'],
        ['#', '#', '#', ' ', '#', '#', '#', ' ', '$', '.',
            '#', ' ', '$', '.', '#', ' ', '$', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ',
            '#', ' ', ' ', ' ', '#', ' ', ' ', '@', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
]

current_level = 0

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

# Funktioner här nedanför


def load_level():
    global level
    level = copy.deepcopy(levels[current_level])


def on_key_down(key):
    global current_level

    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y

        dx = 0
        dy = 0
        if key == keys.LEFT:
            dx = -1
        elif key == keys.RIGHT:
            dx = 1
        elif key == keys.UP:
            dy = -1
        elif key == keys.DOWN:
            dy = 1

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        beyond = ''
        if (
            0 <= player_y + dy + dy < len(level)
            and 0 <= player_x + dx + dx < len(level[player_y + dy + dy])
        ):
            beyond = level[player_y + dy + dy][player_x + dx + dx]

        next_adjacent = {
            empty: player,
            storage: player_on_storage,
        }

        next_current = {
            player: empty,
            player_on_storage: storage,
        }

        next_beyond = {
            empty: box,
            storage: box_on_storage,
        }

        next_adjacent_push = {
            box: player,
            box_on_storage: player_on_storage,
        }

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]

        elif beyond in next_beyond and adjacent in next_adjacent_push:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent_push[adjacent]
            level[player_y + dy + dy][player_x + dx + dx] = next_beyond[beyond]

        complete = True

        for y, row in enumerate(level):
            for x, cell in enumerate(row):
                if cell == box:
                    complete = False

        if complete:
            current_level += 1
            if current_level >= len(levels):
                current_level = 0
            load_level()

    elif key == keys.R:
        load_level()

    elif key == keys.N:
        current_level += 1
        if current_level >= len(levels):
            current_level = 0
        load_level()

    elif key == keys.P:
        current_level -= 1
        if current_level < 0:
            current_level = len(levels) - 1
        load_level()


def draw():
    screen.fill((255, 255, 190))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 23

                colors = {
                    player: (167, 135, 255),
                    player_on_storage: (158, 119, 255),
                    box: (255, 201, 126),
                    box_on_storage: (150, 255, 127),
                    storage: (156, 229, 255),
                    wall: (255, 147, 209),
                }

                screen.draw.filled_rect(
                    Rect(
                        (x * cell_size, y * cell_size),
                        (cell_size, cell_size)
                    ),
                    color=colors[cell]
                )

                screen.draw.text(
                    cell,
                    (x * cell_size, y * cell_size),
                    color=(255, 255, 255)
                )


# Kod för att starta appen här nedanför
load_level()

pgzrun.go()  # måste vara sista raden
```

</details>

# Uppgifter
## 1. Vad tyckte du var svårt med kodningen?
Ge ett par exempel. Glöm inte kodexempel!

## 2. Gör det ännu bättre
- Beskriv kort vad förändringen är och hur den ska fungera. Kanske bättre grafik, en introskärm med förklaringar eller poängräknare?
- Beskriv hur du fick ändra koden för att göra ändringen. Glöm inte kodexempel.
- Om det inte gick att genomföra, förklara med några meningar vad du försökte och vad som hände. Glöm inte kodexempel.

   
# Källor
Engelska originalprojektet: https://simplegametutorials.github.io/pygamezero/sokoban/
