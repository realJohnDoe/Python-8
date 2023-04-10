# Blocks ⭐⭐⭐
## En handledning för Python och Pygame Zero 1.2

![image](https://user-images.githubusercontent.com/4598641/226001268-afea64f1-d51c-48e0-b4b8-0bff27a3e893.png)

## Innehåll
[**Regler**](#regler) [Kontroller](#kontroller) &bull;
[**Översikt**](#översikt) &bull;
[**Kodning**](#kodning)
[Rita rutnätet med block](#rita-rutnätet-med-block)
&bull; [Lagring av orörliga block](#lagring-av-orörliga-block)
&bull; [Färglägg blocken](#färglägg-blocken)
&bull; [Hur vi sparar bitarnas utseende](#hur-vi-sparar-bitarnas-utseende)
&bull; [Lagra biten som faller just nu](#lagra-biten-som-faller-just-nu)
&bull; [Rita biten](#rita-biten)
&bull; [Förenkla koden](#förenkla-koden)
&bull; [Rotation](#rotation)
&bull; [Testa bitar](#testa-bitar)
&bull; [Placera nästa bit](#placera-nästa-bit)
&bull; [Flytta biten](#flytta-biten)
&bull; [Timer](#timer)
&bull; [Fallande bit](#fallande-bit)
&bull; [Begränsa rörelsefriheten](#begränsa-rörelsefriheten)
&bull; [Kolla vänsterkanten](#kolla-vänsterkanten)
&bull; [Förenkla koden](#förenkla-koden-1)
&bull; [Kolla högerkanten](#kolla-högerkanten)
&bull; [Kolla underkanten](#kolla-underkanten)
&bull; [Kolla orörliga block](#kolla-orörliga-block)
&bull; [Förenkla koden](#förenkla-koden-2)
&bull; [Släppa ner en bit](#släppa-ner-en-bit)
&bull; [Återställa biten](#återställa-biten)
&bull; [Förenkla koden](#förenkla-koden-3)
&bull; [Håll reda på kommande bitar](#håll-reda-på-kommande-bitar)
&bull; [Nästa bit från listan](#nästa-bit-från-listan)
&bull; [Lägg till orörliga block](#lägg-till-orörliga-block)
&bull; [Ny bit direkt efter släpp](#ny-bit-direkt-efter-släpp)
&bull; [Hitta fyllda rader](#hitta-fyllda-rader)
&bull; [Ta bort fyllda rader](#ta-bort-fyllda-rader)
&bull; [Game over](#game-over)
&bull; [Förskjutning av spelplanen](#förskjutning-av-spelplanen)
&bull; [Rita nästa bit](#rita-nästa-bit)

  

# Regler

Det finns sju typer av bitar. Varje bit innehåller fyra rutor.

![image](https://user-images.githubusercontent.com/4598641/226001342-33230a9a-d8a3-4218-9a37-3cc579827ad0.png)

Bitar faller från toppen av spelplanen. 
Spelaren kan flytta bitar åt vänster och höger och rotera dem. 
När en bit landar, faller nästa bit.

Hur nästa bit ser ut visas ovanför spelplanen som en hjälp till spelaren.

![image](https://user-images.githubusercontent.com/4598641/226001405-e8e90545-4b84-4dc6-87a5-374f584ade98.png)

När en obruten rad av rutor bildas, försvinner raden och alla rutor ovanför flyttas ner en rad.

Spelet slutar när en bit har landat och nästa bit skulle omedelbart överlappa en tidigare nerfallen bit.

## Kontroller

**Vänsterpil**	Flytta vänster ⬅️<br>
**Högerpil**	Flytta höger ➡️<br>
**Z**	Rotera moturs 🔄<br>
**X**	Rotera medurs 🔃<br>
**C**	Släpp ⏬


# Översikt

*Detta är ungefär vad vi behöver göra. Vi kommer att göra det i små steg. Du behöver inte förstå alla detaljerna från början.*

Ett rutnät lagrar de orörliga rutorna från nerfallna bitar.

En ruta är antingen tom eller fylld med en viss färg.

- Tecknet `' '` är ett mellanslag och betyder en tom ruta.
- Tecknen  `'i'`, `'j'`, `'l'`, `'o'`, `'s'`, `'t'` och `'z'` betyder rutor med olika färger.

![image](https://user-images.githubusercontent.com/4598641/226003821-3a435de3-4843-421e-ab20-477e93bf3fe8.png)

Alla olika typer av bitar lagras med sina roterade varianter.

![image](https://user-images.githubusercontent.com/4598641/226003959-15932dfd-3435-47dd-b1f2-78b050e562fb.png)

Den fallande biten lagras som 
- ett tal som representerar vilken typ av bit det är,
- ett tal som representerar vilken rotation den befinner sig i
- och så X- och Y-koordinaten för biten på spelplanen.

En ny bit skapas längst upp på skärmen. Skulle den hamna direkt på orörligt block är spelet över.

Spelaren kan flytta biten åt vänster och höger, om inte den nya positionen överlappar ett orörligt block eller är utanför spelplanen.

Efter en liten fördröjning flyttas biten nedåt. 
Om den nya positionen överlappar ett orörligt block eller är utanför spelplanen så landar biten.

När någon av rotationsknapparna trycks, ändrar biten sin rotation, om inte den rotationen överlappar ett orörligt block eller är utanför spelplanen.

När spelaren trycker på släppknappen (c), flyttas biten neråt så långt det går utan att den överlappar ett orörligt block eller hamnar utanför spelplanen.
Sen landar biten.

När en bit landar, läggs bitens block till de orörliga blocken och nästa bit skapas.

En sekvens av en av var och en av de sju bitarna i en slumpmässig ordning skapas. 
Nästa bit tas alltid från denna sekvens. 
När alla bitar har tagits, skapas en ny slumpmässig ordning.

# Kodning

## Rita rutnätet med block
En ruta ritas för varje block i spelplanen.

✏️ Se till att du är inloggad i repl.it. Öppna startprojektet https://replit.com/@RobertStorlind/blocks-starter
och spara en egen kopia med knappen Fork.

Testkör!

```python
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
```

![image](https://user-images.githubusercontent.com/4598641/226004861-bb0676e3-8ace-444f-af72-a4c3859483b0.png)

## Lagring av orörliga block

Vi skapar ett variabel `inert` som håller reda på rutnätet för de orörliga blocken. 
Varje block sätts till ett mellanslag, `' '`. Det representerar ett tomt block.

Bredden och höjden på rutnätet räknat i block behöver vi på flera ställen i koden. Därför gör vi bredden och höjden till variabler.

✏️ Uppdatera koden och testkör. Nya och ändrade rader är markerade.

```python
import pgzrun

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10 #nyrad 🟦
grid_y_count = 18 #nyrad 🟦

inert = [] #nyrad 🟦

# Funktioner (def) här nedanför
def draw():
    screen.fill((255, 255, 255))

    for y in range(grid_y_count): #ändrad 🟦
        for x in range(grid_x_count): #ändrad 🟦
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
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad 🟦

pgzrun.go()  # måste vara sista raden
```

## Färglägg blocken

Varje blocktyp ska ha sin unika färg.

För att testa det, sätter vi några block i det orörliga nätet till att ha olika typ.

✏️ Uppdatera koden och testkör!

```python
# Funktioner (def) här nedanför
def draw():
    screen.fill((255, 255, 255))

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            colors = { #nyrad 🟦
                ' ': (222, 222, 222), #nyrad 🟦
                'i': (120, 195, 239), #nyrad 🟦
                'j': (236, 231, 108), #nyrad 🟦
                'l': (124, 218, 193), #nyrad 🟦
                'o': (234, 177, 121), #nyrad 🟦
                's': (211, 136, 236), #nyrad 🟦
                't': (248, 147, 196), #nyrad 🟦
                'z': (169, 221, 118), #nyrad 🟦
            } #nyrad 🟦
            block = inert[y][x] #nyrad 🟦
            color = colors[block] #nyrad 🟦
            block_size = 20
            block_draw_size = block_size - 1
            screen.draw.filled_rect(
                Rect(
                    x * block_size, y * block_size,
                    block_draw_size, block_draw_size
                ),
                color=color #ändra 🟦
            )


# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad 🟦
    inert.append([]) #nyrad 🟦
        inert[y] = [' '] * grid_x_count #nyrad 🟦

# Tillfälligt
inert[17][0] = 'i' #nyrad 🟦
inert[16][1] = 'j' #nyrad 🟦
inert[15][2] = 'l' #nyrad 🟦
inert[14][3] = 'o' #nyrad 🟦
inert[13][4] = 's' #nyrad 🟦
inert[12][5] = 't' #nyrad 🟦
inert[11][6] = 'z' #nyrad 🟦

pgzrun.go()  # måste vara sista raden
```

![image](https://user-images.githubusercontent.com/4598641/226006718-62e1013b-99f3-427b-b095-4cda85184e19.png)

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
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
            colors = { #nyrad
                ' ': (222, 222, 222), #nyrad
                'i': (120, 195, 239), #nyrad
                'j': (236, 231, 108), #nyrad
                'l': (124, 218, 193), #nyrad
                'o': (234, 177, 121), #nyrad
                's': (211, 136, 236), #nyrad
                't': (248, 147, 196), #nyrad
                'z': (169, 221, 118), #nyrad
            } #nyrad
            block = inert[y][x] #nyrad
            color = colors[block] #nyrad
            block_size = 20
            block_draw_size = block_size - 1
            screen.draw.filled_rect(
                Rect(
                    x * block_size, y * block_size,
                    block_draw_size, block_draw_size
                ),
                color=color #ändra
            )


# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

# Tillfälligt
inert[17][0] = 'i' #nyrad
inert[16][1] = 'j' #nyrad
inert[15][2] = 'l' #nyrad
inert[14][3] = 'o' #nyrad
inert[13][4] = 's' #nyrad
inert[12][5] = 't' #nyrad
inert[11][6] = 'z' #nyrad

pgzrun.go()  # måste vara sista raden
```

</details>

## Hur vi sparar bitarnas utseende
Varje rotation av en bit är en 4x4-kvadrat av tecken.

```python
[
    [' ', ' ', ' ', ' '],
    ['i', 'i', 'i', 'i'],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
]
```

Varje bit sparas som en lista av de olika rotationerna.

```python
[ # en lista för biten
    [ # ett element i listan = en av bitens rotationer
        [' ', ' ', ' ', ' '],
        ['i', 'i', 'i', 'i'],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
    ],
    [ # nästa rotation
        [' ', 'i', ' ', ' '],
        [' ', 'i', ' ', ' '],
        [' ', 'i', ' ', ' '],
        [' ', 'i', ' ', ' '],
    ],
]
```

De olika bitarna och deras rotationer sparas som en enda lång lista.

I startprojektet finns allt detta förberett i filen `pieces.py`. 
Funktionen `get_piece_structures()` ger oss listan.

**pieces.py**<br>
**Du behöver inte mata in detta själv.** Titta gärna i pieces.py så du ser hur det är gjort.

```python
def get_piece_structures():
    return [  # lista med alla bitarna
        [  # bit nr 1
            [  # bit 1, rotation nr 1
              [' ', ' ', ' ', ' '],
              ['i', 'i', 'i', 'i'],
              [' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' '],
            ],
            [  # bit 1, rotation nr 2
                [' ', 'i', ' ', ' '],
                [' ', 'i', ' ', ' '],
                [' ', 'i', ' ', ' '],
                [' ', 'i', ' ', ' '],
            ],
        ],
        [  # nästa bit
            [  # bit 2, rotation nr 1 -- den har bara en!
                [' ', ' ', ' ', ' '],
                [' ', 'o', 'o', ' '],
                [' ', 'o', 'o', ' '],
                [' ', ' ', ' ', ' '],
            ],
        ],
        [  # nästa bit
            [  # bit 3, rotation nr 1
                [' ', ' ', ' ', ' '],
                ['j', 'j', 'j', ' '],
                [' ', ' ', 'j', ' '],
                [' ', ' ', ' ', ' '],
            ],
            [  # bit 3, rotation nr 2
                [' ', 'j', ' ', ' '],
                [' ', 'j', ' ', ' '],
                ['j', 'j', ' ', ' '],
                [' ', ' ', ' ', ' '],
            ],
            [  # bit 3, rotation nr 3
                ['j', ' ', ' ', ' '],
                ['j', 'j', 'j', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
            ],
            [  # bit 3, rotation nr 4
                [' ', 'j', 'j', ' '],
                [' ', 'j', ' ', ' '],
                [' ', 'j', ' ', ' '],
                [' ', ' ', ' ', ' '],
            ],
        ],
        [
            [
                [' ', ' ', ' ', ' '],
                ['l', 'l', 'l', ' '],
                ['l', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
            ],
            [
                [' ', 'l', ' ', ' '],
                [' ', 'l', ' ', ' '],
                [' ', 'l', 'l', ' '],
                [' ', ' ', ' ', ' '],
            ],
            [
                [' ', ' ', 'l', ' '],
                ['l', 'l', 'l', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
            ],
            [
                ['l', 'l', ' ', ' '],
                [' ', 'l', ' ', ' '],
                [' ', 'l', ' ', ' '],
                [' ', ' ', ' ', ' '],
            ],
        ],
        [
            [
                [' ', ' ', ' ', ' '],
                ['t', 't', 't', ' '],
                [' ', 't', ' ', ' '],
                [' ', ' ', ' ', ' '],
            ],
            [
                [' ', 't', ' ', ' '],
                [' ', 't', 't', ' '],
                [' ', 't', ' ', ' '],
                [' ', ' ', ' ', ' '],
            ],
            [
                [' ', 't', ' ', ' '],
                ['t', 't', 't', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
            ],
            [
                [' ', 't', ' ', ' '],
                ['t', 't', ' ', ' '],
                [' ', 't', ' ', ' '],
                [' ', ' ', ' ', ' '],
            ],
        ],
        [
            [
                [' ', ' ', ' ', ' '],
                [' ', 's', 's', ' '],
                ['s', 's', ' ', ' '],
                [' ', ' ', ' ', ' '],
            ],
            [
                ['s', ' ', ' ', ' '],
                ['s', 's', ' ', ' '],
                [' ', 's', ' ', ' '],
                [' ', ' ', ' ', ' '],
            ],
        ],
        [
            [
                [' ', ' ', ' ', ' '],
                ['z', 'z', ' ', ' '],
                [' ', 'z', 'z', ' '],
                [' ', ' ', ' ', ' '],
            ],
            [
                [' ', 'z', ' ', ' '],
                ['z', 'z', ' ', ' '],
                ['z', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
            ],
        ],
    ]
```

✏️ Uppdatera din kod med kodblocket här nedanför. Du kan testköra &ndash; det ska då fungera som innan eftersom vi inte gör något med bitarna än. De finns bara i datorns minne.

**main.py**
```python
# Lägg till en import
import pieces

# Lägg detta bland de globala variablerna, nästan högst upp
piece_structures = pieces.get_piece_structures()
```


<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

inert = []
piece_structures = pieces.get_piece_structures()

# Funktioner (def) här nedanför
def draw():
    screen.fill((255, 255, 255))

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            colors = { #nyrad
                ' ': (222, 222, 222), #nyrad
                'i': (120, 195, 239), #nyrad
                'j': (236, 231, 108), #nyrad
                'l': (124, 218, 193), #nyrad
                'o': (234, 177, 121), #nyrad
                's': (211, 136, 236), #nyrad
                't': (248, 147, 196), #nyrad
                'z': (169, 221, 118), #nyrad
            } #nyrad
            block = inert[y][x] #nyrad
            color = colors[block] #nyrad
            block_size = 20
            block_draw_size = block_size - 1
            screen.draw.filled_rect(
                Rect(
                    x * block_size, y * block_size,
                    block_draw_size, block_draw_size
                ),
                color=color #ändra
            )

# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

# Tillfälligt
inert[17][0] = 'i' #nyrad
inert[16][1] = 'j' #nyrad
inert[15][2] = 'l' #nyrad
inert[14][3] = 'o' #nyrad
inert[13][4] = 's' #nyrad
inert[12][5] = 't' #nyrad
inert[11][6] = 'z' #nyrad

pgzrun.go()  # måste vara sista 
```

</details>


## Lagra biten som faller just nu

Biten som faller just nu representeras av
- dels ett tal som anger vilken typ av bit det är &ndash; vi behöver använda det för att indexera i listan över med olika bitar
- dels ett tal som anger vilken rotation biten har &ndash; vi behöver det för att indexera i listan med rotationer för biten.

✏️ Lägg till och testkör att allt fungerar som innan.

```python
# Lägg till som globala variabler nästan högst upp
piece_type = 0
piece_rotation = 0
```

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0

inert = []
piece_structures = pieces.get_piece_structures()

# Funktioner (def) här nedanför
def draw():
    screen.fill((255, 255, 255))

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            colors = { #nyrad
                ' ': (222, 222, 222), #nyrad
                'i': (120, 195, 239), #nyrad
                'j': (236, 231, 108), #nyrad
                'l': (124, 218, 193), #nyrad
                'o': (234, 177, 121), #nyrad
                's': (211, 136, 236), #nyrad
                't': (248, 147, 196), #nyrad
                'z': (169, 221, 118), #nyrad
            } #nyrad
            block = inert[y][x] #nyrad
            color = colors[block] #nyrad
            block_size = 20
            block_draw_size = block_size - 1
            screen.draw.filled_rect(
                Rect(
                    x * block_size, y * block_size,
                    block_draw_size, block_draw_size
                ),
                color=color #ändra
            )


# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

# Tillfälligt
inert[17][0] = 'i' #nyrad
inert[16][1] = 'j' #nyrad
inert[15][2] = 'l' #nyrad
inert[14][3] = 'o' #nyrad
inert[13][4] = 's' #nyrad
inert[12][5] = 't' #nyrad
inert[11][6] = 'z' #nyrad

pgzrun.go()  # måste vara sista 
```

</details>

## Rita biten

Biten ritas genom att loopa genom listan som representerar biten.
Om en viss ruta är fylld så ritar vi en fyrkant med den färg som bestäms av blocktypen.

✏️ Uppdatera koden och testkör! Lägg till koden i slutet av `draw()` och ta bort den tillfälliga ritkoden längst ner.

```python
def draw():
   # Lägg till detta längst ner i funktionen
        for x in range(4):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
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

# Ta bort den tillfälliga koden nästan längst ner
```

![image](https://user-images.githubusercontent.com/4598641/226010899-049e0b7e-591d-4d0b-b296-7fb35778e094.png)

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0

inert = []
piece_structures = pieces.get_piece_structures()

# Funktioner (def) här nedanför
def draw():
    screen.fill((255, 255, 255))

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            colors = { #nyrad
                ' ': (222, 222, 222), #nyrad
                'i': (120, 195, 239), #nyrad
                'j': (236, 231, 108), #nyrad
                'l': (124, 218, 193), #nyrad
                'o': (234, 177, 121), #nyrad
                's': (211, 136, 236), #nyrad
                't': (248, 147, 196), #nyrad
                'z': (169, 221, 118), #nyrad
            } #nyrad
            block = inert[y][x] #nyrad
            color = colors[block] #nyrad
            block_size = 20
            block_draw_size = block_size - 1
            screen.draw.filled_rect(
                Rect(
                    x * block_size, y * block_size,
                    block_draw_size, block_draw_size
                ),
                color=color #ändra
            )
            
    for y in range(4):
        for x in range(4):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
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
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

pgzrun.go()  # måste vara sista raden
```

</details>


## Förenkla koden

Koden för att rita ett orörligt block och för att rita ett block av den fallande biten är samma. 
Därför gör vi en funktion för det.

✏️ Uppdatera hela funktionen `draw()`. Testkör att det fungerar likadant som innan vi snyggade till koden!

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0

inert = []
piece_structures = pieces.get_piece_structures()

# Funktioner (def) här nedanför
def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(4):
        for x in range(4):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x, y)


# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

pgzrun.go()  # måste vara sista raden
```

</details>


## Rotation
När vi trycker på `X`, ökas bitens rotationstal med 1 och biten roteras medurs.
>Om rotationstalet är större än antalet möjliga rotationer sätts rotationstalet till 0. Vi går alltså tillbaks till bitens första rotation.

När vi trycker på `Z` så minskas rotationstalet med 1 och biten roterar moturs.
>Om rotationstalet är mindre än 0, sätts rotationstalet till antalet rotationer minus 1, alltså bitens sista rotation.


✏️ Lägg till funktionen `on_key_down()` och testkör!
>Starta spelet med Run och klicka sen i spelfönstret. Då kan din kod fånga upp tangenttryckningarna.

```python
def on_key_down(key):
    global piece_rotation

    if key == keys.X:
        piece_rotation += 1
        if piece_rotation >= len(piece_structures[piece_type]):
            piece_rotation = 0

    elif key == keys.Z:
        piece_rotation -= 1
        if piece_rotation < 0:
            piece_rotation = len(piece_structures[piece_type]) - 1          
```


![image](https://user-images.githubusercontent.com/4598641/226011415-59b9b18c-2496-4af0-a39c-f854ef940d2e.png)

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0

inert = []
piece_structures = pieces.get_piece_structures()

# Funktioner (def) här nedanför
def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(4):
        for x in range(4):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x, y)

def on_key_down(key):
    global piece_rotation

    if key == keys.X:
        piece_rotation += 1
        if piece_rotation >= len(piece_structures[piece_type]):
            piece_rotation = 0

    elif key == keys.Z:
        piece_rotation -= 1
        if piece_rotation < 0:
            piece_rotation = len(piece_structures[piece_type]) - 1          


# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

pgzrun.go()  # måste vara sista raden
```

</details>

  
## Testa bitar

För att göra det lätt att testa, låter vi upp- och och neråtpil byta mellan olika bitar.

✏️ Uppdatera funktionen `on_key_down()` och testkör! Fungerar upp- och neråtpil och tangenterna `X` och `C` som du tänkt?

```python
def on_key_down(key):
    global piece_rotation, piece_type # uppdatera

    if key == keys.X:
        piece_rotation += 1
        if piece_rotation >= len(piece_structures[piece_type]):
            piece_rotation = 0

    elif key == keys.Z:
        piece_rotation -= 1
        if piece_rotation < 0:
            piece_rotation = len(piece_structures[piece_type]) - 1
    # Resten är nya rader
    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0
```
  
![image](https://user-images.githubusercontent.com/4598641/226011550-d53162ca-1eaf-4674-b2dc-71eefe2fed7d.png)

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0

inert = []
piece_structures = pieces.get_piece_structures()

# Funktioner (def) här nedanför
def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(4):
        for x in range(4):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x, y)

def on_key_down(key):
    global piece_rotation, piece_type # uppdatera

    if key == keys.X:
        piece_rotation += 1
        if piece_rotation >= len(piece_structures[piece_type]):
            piece_rotation = 0

    elif key == keys.Z:
        piece_rotation -= 1
        if piece_rotation < 0:
            piece_rotation = len(piece_structures[piece_type]) - 1
    # Resten är nya rader
    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0


# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

pgzrun.go()  # måste vara sista raden
```

</details>

## Placera nästa bit

Bitens position på spelplanen sparas och biten ritas på den positionen.

✏️ Lägg till de två globala variablerna och ändra en rad i `draw()`. Testkör sen med pil upp, pil ner, `X` och `C`.

```python
# Läggs bland de globala variablerna
piece_x = 3 #nyrad
piece_y = 0 #nyrad

def draw():
    # etc.

    for y in range(4):
        for x in range(4):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y) #ändrad
```
  
  
![image](https://user-images.githubusercontent.com/4598641/226011946-ae6035af-d12b-4390-bfe8-2a1a3019655b.png)

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()

# Funktioner (def) här nedanför
def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(4):
        for x in range(4):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)

def on_key_down(key):
    global piece_rotation, piece_type # uppdatera

    if key == keys.X:
        piece_rotation += 1
        if piece_rotation >= len(piece_structures[piece_type]):
            piece_rotation = 0

    elif key == keys.Z:
        piece_rotation -= 1
        if piece_rotation < 0:
            piece_rotation = len(piece_structures[piece_type]) - 1
    # Resten är nya rader
    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0


# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

pgzrun.go()  # måste vara sista raden
```

</details>


## Flytta biten

Vänster- och högerpilarna minskar eller ökar bitens X-koordinat med 1.

✏️ Uppdatera `on_key_down()` med regler för `keys.LEFT` och `keys.RIGHT` och testkör! Flyttar sig biten med höger- o vänsterpil?

```python
def on_key_down(key):
    global piece_rotation, piece_type, piece_x

    if key == keys.X:
        piece_rotation += 1
        if piece_rotation >= len(piece_structures[piece_type]):
            piece_rotation = 0

    elif key == keys.Z:
        piece_rotation -= 1
        if piece_rotation < 0:
            piece_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT: #nyrad 
        piece_x -= 1 #nyrad

    elif key == keys.RIGHT: #nyrad
        piece_x += 1 #nyrad

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0
  ```
![image](https://user-images.githubusercontent.com/4598641/226012210-eff3bfe9-dcb6-4579-be14-4eb21ec43338.png)

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()

# Funktioner (def) här nedanför

def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(4):
        for x in range(4):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def on_key_down(key):
    global piece_rotation, piece_type, piece_x

    if key == keys.X:
        piece_rotation += 1
        if piece_rotation >= len(piece_structures[piece_type]):
            piece_rotation = 0

    elif key == keys.Z:
        piece_rotation -= 1
        if piece_rotation < 0:
            piece_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        piece_x -= 1

    elif key == keys.RIGHT:
        piece_x += 1

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0


# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

pgzrun.go()  # måste vara sista raden
```

</details>

## Timer

Bitar kommer att falla med 0.5 s mellanrum.

En timervariabel börjar vid 0 och ökar med `dt` för varje bildruta.
>`dt` talar om hur lång tid det har gått sedan vi senast ritade på skärmen.

När timern har passerat 0.5, återställs den till 0.

För att se hur det fungerar skriver vi just nu 'tick' ut varje gång biten faller.

✏️ Uppdatera koden med den globala variabeln `timer`. Lägg till funktionen `update` och testkör sen! Ser du utskriften i terminalfönstret med text?

```python
# Lägg till ny global variabel
timer = 0

# Längre ner vid funktionerna
def update(dt):
    global timer

    timer += dt
    if timer >= 0.5:
        timer = 0
        # Temporary
        print('tick')
```

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()

timer = 0

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(4):
        for x in range(4):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def update(dt):
    global timer

    timer += dt
    if timer >= 0.5:
        timer = 0
        # Temporary
        print('tick')


def on_key_down(key):
    global piece_rotation, piece_type, piece_x

    if key == keys.X:
        piece_rotation += 1
        if piece_rotation >= len(piece_structures[piece_type]):
            piece_rotation = 0

    elif key == keys.Z:
        piece_rotation -= 1
        if piece_rotation < 0:
            piece_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        piece_x -= 1

    elif key == keys.RIGHT:
        piece_x += 1

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0



# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

pgzrun.go()  # måste vara sista raden
```

</details>

## Fallande bit
Timern används för att öka bitens Y-koordinat var 0.5:e sekund.

✏️ Uppdatera funktionen `update()` och testkör!

```python
def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= 0.5:
        timer = 0
        piece_y += 1
```

![image](https://user-images.githubusercontent.com/4598641/226012579-0a5bce97-00a6-4f54-ba96-95cc123f9a4c.png)

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()

timer = 0

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(4):
        for x in range(4):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= 0.5:
        timer = 0
        piece_y += 1


def on_key_down(key):
    global piece_rotation, piece_type, piece_x

    if key == keys.X:
        piece_rotation += 1
        if piece_rotation >= len(piece_structures[piece_type]):
            piece_rotation = 0

    elif key == keys.Z:
        piece_rotation -= 1
        if piece_rotation < 0:
            piece_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        piece_x -= 1

    elif key == keys.RIGHT:
        piece_x += 1

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0



# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

pgzrun.go()  # måste vara sista raden
```

</details>

## Begränsa rörelsefriheten

Vi vill hindra att biten hamnar till vänster eller höger om spelplanen när den flyttas eller roteras.
Därför kontrollerar vi bitens alla block för att se om de är inom spelplanen innan biten flyttas eller roteras.

Eftersom den här kontrollen kommer att göras på flera ställen, gör vi en funktion med den koden.
Funktionen `can_piece_move` ska kontrollera bitens position och rotation. Den ska svara `True` om biten kan röra sig eller rotera, annars `False`.

Till att börja med kommer funktionen alltid att returnera True, så att vi alltid kan flytta och rotera medan vi testar.

Vi behöver ändra koden från att omedelbart uppdatera bitens position/rotation.
Istället skapar vi variabler för de ändrade värdena.
Om `can_piece_move` svarar `True`, ställs den faktiska positionen/rotationen till de ändrade värdena, annars inte.

✏️ Uppdatera koden. Funktionen `can_piece_move()` är ny. Funktionerna `update()` och `on_key_down` har ändringar. Testkör!

```python
def can_piece_move(test_x, test_y, test_rotation): # ny funktion
    return True # allt är tillåtet just nu

def update(dt):
    global timer
    global piece_y

    timer += dt
    if timer >= 0.5:
        timer = 0

        test_y = piece_y + 1 # nyrad
        if can_piece_move(piece_x, test_y, piece_rotation): # nyrad
            piece_y = test_y # nyrad

def on_key_down(key):
    global piece_rotation, piece_type, piece_x, piece_y

    if key == keys.X: # logiken är ändrad
        test_rotation = piece_rotation + 1 
        if test_rotation > len(piece_structures[piece_type]) - 1:
            test_rotation = 0

        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z: # logiken är ändrad
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.LEFT: # logiken är ändrad
        test_x = piece_x - 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:  # logiken är ändrad
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x
```

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()

timer = 0

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(4):
        for x in range(4):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def can_piece_move(test_x, test_y, test_rotation):
    return True


def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= 0.5:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y


def on_key_down(key):
    global piece_rotation, piece_type, piece_x

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation >= len(piece_structures[piece_type]):
            test_rotation = 0
        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        test_x = piece_x - 1
        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0



# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

pgzrun.go()  # måste vara sista raden
```

</details>

## Kolla vänsterkanten
Om något block inte är tomt och X-koordinaten är mindre än 0, returnerar funktionen `can_piece_move` False. 
Det är när blocket är utanför spelplanens vänstra sida.

✏️ Uppdatera funktionen och testkör! Blir det stopp när du trycker vänsterpil flera gånger?

```python
def can_piece_move(test_x, test_y, test_rotation):
    for y in range(4):
        for x in range(4):
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                test_x + x < 0):
                return False

    return True
```

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()

timer = 0

# Funktioner (def) här nedanför

def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(4):
        for x in range(4):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def can_piece_move(test_x, test_y, test_rotation):
    for y in range(4):
        for x in range(4):
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                test_x + x < 0):
                return False

    return True


def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= 0.5:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y


def on_key_down(key):
    global piece_rotation, piece_type, piece_x

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation >= len(piece_structures[piece_type]):
            test_rotation = 0
        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        test_x = piece_x - 1
        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0



# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

pgzrun.go()  # måste vara sista raden
```

</details>

## Förenkla koden
Storleken på varje bit i X- och Y-led återanvänds från att rita bitarna, så vi gör variabler för det.

✏️ Uppdatera koden. Du ska lägga till två globala variabler och sen använda dem i `can_piece_move()` och `draw()`. Testkör sen att det fungerar lika bra som innan!

```python
# Lägg till bland globala variablerna
piece_x_count = 4
piece_y_count = 4

def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count): # ändra från 4 till piece_y_count
        for x in range(piece_x_count): # ändra från 4
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                test_x + x < 0):
                return False

    return True

def draw():
    # etc.

    for y in range(piece_y_count): # ändra från 4
        for x in range(piece_x_count): # ändra från 4
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)
```                                                                                           
                                                                                           
<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()
piece_x_count = 4
piece_y_count = 4

timer = 0

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                test_x + x < 0):
                return False

    return True


def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= 0.5:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y


def on_key_down(key):
    global piece_rotation, piece_type, piece_x

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation >= len(piece_structures[piece_type]):
            test_rotation = 0
        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        test_x = piece_x - 1
        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0



# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

pgzrun.go()  # måste vara sista raden
```

</details>

## Kolla högerkanten

Om blockets X-koordinat är större än eller lika med spelplanens bredd hamnar det utanför spelplanens högra sida.
Då svarar funktionen `can_piece_move()` också False.

- Tidigare ställde vi frågan om vi var utanför vänsterkanten, alltså `test_x + x < 0`.
- Vi vill lägga till frågan om vi är utanför högerkanten, alltså att `test_x + x >= grid_x_count`.
- Vi kan kombinera de två frågorna så här: `test_x + x in range(grid_x_count)` eftersom `range(grid_x_count)` ger oss en lista med talen från `0` till `grid_x_count - 1`.

✏️ Uppdatera en rad i `can_piece_move()` och testkör! Ser det rätt ut när du flyttar med höger- och vänsterpil och roterar bitarna?

```python
def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_x + x not in range(grid_x_count)): # uppdatera
                return False

    return True
```

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()
piece_x_count = 4
piece_y_count = 4

timer = 0

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_x + x not in range(grid_x_count)): # uppdatera
                return False

    return True


def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= 0.5:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y


def on_key_down(key):
    global piece_rotation, piece_type, piece_x

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation >= len(piece_structures[piece_type]):
            test_rotation = 0
        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        test_x = piece_x - 1
        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0



# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

pgzrun.go()  # måste vara sista raden
```

</details>

## Kolla underkanten
  
Om något blocks Y-koordinat är större än eller lika med höjden på spelplanen är det nedanför botten av spelplanen.
Då returnerar funktionen `can_piece_move()` också False.

Vi delar upp frågan i två rader för att göra det lättare att läsa koden.
- Den första delen, `if piece_structures[piece_type][test_rotation][y][x] != ' '`, frågar om biten har något block i rutan (y, x) med rotationen `test_rotation` 
- Den andra delen, `test_x + x not in range(grid_x_count) or test_y + y >= grid_y_count` frågar om biten får plats i x-led (höger/vänster) och i underkant
  
✏️ Uppdatera `can_piece_move()` och testkör! Fungerar det med underkanten nu?

```python
def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_x + x not in range(grid_x_count) # ändrad
                    or test_y + y >= grid_y_count): #ändrad
                return False

    return True
```

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()
piece_x_count = 4
piece_y_count = 4

timer = 0

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_x + x not in range(grid_x_count)
                    or test_y + y >= grid_y_count):
                return False

    return True


def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= 0.5:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y


def on_key_down(key):
    global piece_rotation, piece_type, piece_x

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation >= len(piece_structures[piece_type]):
            test_rotation = 0
        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        test_x = piece_x - 1
        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0



# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

pgzrun.go()  # måste vara sista raden
```

</details>

## Kolla orörliga block
Om det finns ett orörligt block någonstans där biten skulle hamna, returnerar funktionen `can_piece_move` också False.

För att testa detta lägger vi in ett orörligt block.

✏️ Uppdatera `can_piece_move()` och testkör! Stannar den fallande biten som den ska?

```python
def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_x + x not in range(grid_x_count)
                    or test_y + y >= grid_y_count #ändrad
                    or inert[test_y + y][test_x + x] != ' '): #nyrad
                return False

    return True

# Lägg nästan längst ner, före `pgzrun.go()`
# Tillfälligt
inert[7][4] = 'z'  
```

![image](https://user-images.githubusercontent.com/4598641/226013942-ae181f75-53b1-4b7c-8156-ba22cf2ecc9c.png)

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()
piece_x_count = 4
piece_y_count = 4

timer = 0

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_x + x not in range(grid_x_count)
                    or test_y + y >= grid_y_count
                    or inert[test_y + y][test_x + x] != ' '):
                return False

    return True


def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= 0.5:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y


def on_key_down(key):
    global piece_rotation, piece_type, piece_x

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation >= len(piece_structures[piece_type]):
            test_rotation = 0
        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        test_x = piece_x - 1
        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0



# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

# Tillfälligt
inert[7][4] = 'z'

pgzrun.go()  # måste vara sista raden
```

</details>

## Förenkla koden
De beräknade blockpositionerna som ska testas behövs på fler ställen. Vi sparar dem i variabler så blir koden lite enklare.

✏️ Uppdatera `can_piece_move()` och testkör!

```python
def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            test_block_x = test_x + x #nyrad
            test_block_y = test_y + y #nyrad
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_block_x not in range(grid_x_count) #ändrad
                    or test_block_y >= grid_y_count #ändrad
                    or inert[test_block_y][test_block_x] != ' '): #ändrad
                return False

    return True
```

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()
piece_x_count = 4
piece_y_count = 4

timer = 0

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            test_block_x = test_x + x
            test_block_y = test_y + y
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_block_x not in range(grid_x_count)
                    or test_block_y >= grid_y_count
                    or inert[test_block_y][test_block_x] != ' '):
                return False

    return True


def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= 0.5:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y


def on_key_down(key):
    global piece_rotation, piece_type, piece_x

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation >= len(piece_structures[piece_type]):
            test_rotation = 0
        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        test_x = piece_x - 1
        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0



# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

# Tillfälligt
inert[7][4] = 'z'

pgzrun.go()  # måste vara sista raden
```

</details>

## Släppa ner en bit

När C-tangenten trycks, ska bitens Y-koordinat öka med 1 så länge som biten får plats.

✏️ Uppdatera koden i `on_key_down()` och testkör!

```python
def on_key_down():
    global piece_rotation, piece_type, piece_x, piece_y # uppdatera
  
# Lägg till raderna på lämpligt ställe
    elif key == keys.C: #nyrad
        while can_piece_move(piece_x, piece_y + 1, piece_rotation): #nyrad
            piece_y += 1 #nyrad
```

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()
piece_x_count = 4
piece_y_count = 4

timer = 0

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            test_block_x = test_x + x
            test_block_y = test_y + y
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_block_x not in range(grid_x_count)
                    or test_block_y >= grid_y_count
                    or inert[test_block_y][test_block_x] != ' '):
                return False

    return True


def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= 0.5:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y


def on_key_down(key):
    global piece_rotation, piece_type, piece_x, piece_y

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation >= len(piece_structures[piece_type]):
            test_rotation = 0
        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        test_x = piece_x - 1
        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.C: #nyrad
        while can_piece_move(piece_x, piece_y + 1, piece_rotation): #nyrad
            piece_y += 1 #nyrad

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0



# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

# Tillfälligt
inert[7][4] = 'z'

pgzrun.go()  # måste vara sista raden
```

</details>

## Återställa biten

Om timern tickar och biten inte kan röra sig neråt, återställs biten till sin ursprungliga position, rotation och typ. 
Vi ska ändra det sen.

✏️ Uppdatera koden i `update(dt)` och testkör!

```python
def update(dt):
    global timer, piece_y, piece_x, piece_type, piece_rotation # uppdatera

    timer += dt
    if timer >= 0.5:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y
        else: # nyrad
            piece_x = 3 # nyrad
            piece_y = 0 # nyrad
            piece_type = 0 # nyrad
            piece_rotation = 0 # nyrad    
```

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()
piece_x_count = 4
piece_y_count = 4

timer = 0

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            test_block_x = test_x + x
            test_block_y = test_y + y
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_block_x not in range(grid_x_count)
                    or test_block_y >= grid_y_count
                    or inert[test_block_y][test_block_x] != ' '):
                return False

    return True


def update(dt):
    global timer, piece_y, piece_x, piece_type, piece_rotation

    timer += dt
    if timer >= 0.5:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y
        else:
            piece_x = 3
            piece_y = 0
            piece_type = 0
            piece_rotation = 0        


def on_key_down(key):
    global piece_rotation, piece_type, piece_x, piece_y

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation >= len(piece_structures[piece_type]):
            test_rotation = 0
        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        test_x = piece_x - 1
        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.C: #nyrad
        while can_piece_move(piece_x, piece_y + 1, piece_rotation): #nyrad
            piece_y += 1 #nyrad

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0



# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

# Tillfälligt
inert[7][4] = 'z'

pgzrun.go()  # måste vara sista raden
```

</details>

## Förenkla koden

Biten sätts till sitt startläge på två ställen. Vi gör en funktion för det, `new_piece`.

✏️ Uppdatera koden och testkör! Lägg till `new_piece`, ändra i `update` och anropa `new_piece` längst ner.

```python
def new_piece(): # lägg till funktionen
    global piece_x, piece_y, piece_type, piece_rotation

    piece_x = 3
    piece_y = 0
    piece_type = 0
    piece_rotation = 0
 
def update(dt): # ändra i denna
    global timer, piece_y
    # ta bort piece_x, piece_type och piece_rotation från listan med globala

    timer += dt
    if timer >= 0.5:
        timer = 0

        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y
        else:
            new_piece() # förenkla här


# Kod för att starta appen här nedanför
for y in range(grid_y_count): 
    inert.append([]) 
        inert[y] = [' '] * grid_x_count 

new_piece() # nyrad
```

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()
piece_x_count = 4
piece_y_count = 4

timer = 0

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            test_block_x = test_x + x
            test_block_y = test_y + y
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_block_x not in range(grid_x_count)
                    or test_block_y >= grid_y_count
                    or inert[test_block_y][test_block_x] != ' '):
                return False

    return True

def new_piece():
    global piece_x, piece_y, piece_type, piece_rotation

    piece_x = 3
    piece_y = 0
    piece_type = 0
    piece_rotation = 0

def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= 0.5:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y
        else:
            new_piece()


def on_key_down(key):
    global piece_rotation, piece_type, piece_x, piece_y

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation >= len(piece_structures[piece_type]):
            test_rotation = 0
        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        test_x = piece_x - 1
        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.C: #nyrad
        while can_piece_move(piece_x, piece_y + 1, piece_rotation): #nyrad
            piece_y += 1 #nyrad

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0



# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

new_piece()

# Tillfälligt
inert[7][4] = 'z'

pgzrun.go()  # måste vara sista raden
```

</details>

## Håll reda på kommande bitar
De kommande bitarna lagrar vi som en lista som innehåller numren som representerar bittyper i slumpmässig ordning.

Vi gör en lista med talen från 0 till `len(piece_structures) - 1`. 
Sedan slumpar vi ordningen på den listan med `random.shuffle`.

För att testa, skapar vi  en ny sekvens när S-tangenten trycks ned och skriver ut sekvensen.

Slumpmodulen importeras vi så att vi kan använda `random.shuffle`.

✏️ Uppdatera koden och testkör!

```python
import random # lägg till högt upp

sequence = [] # lägg högt uppe bland variablerna

def new_sequence(): # lägg till bland funktionerna, före new_piece
    global sequence

    sequence = list(range(len(piece_structures)))
    random.shuffle(sequence)

# etc.
def on_key_down(key):
    # etc.

    # Tillfälligt
    elif key == keys.S: # nyrad
        new_sequence() # nyrad
        print(sequence) # nyrad

# Lägg till detta nästan längst ner, före `new_piece()`
new_sequence()
``` 

```python
[3, 2, 4, 1, 0, 5, 6]
```

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces
import random

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()
piece_x_count = 4
piece_y_count = 4

sequence = []

timer = 0

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            test_block_x = test_x + x
            test_block_y = test_y + y
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_block_x not in range(grid_x_count)
                    or test_block_y >= grid_y_count
                    or inert[test_block_y][test_block_x] != ' '):
                return False

    return True

def new_sequence():
    global sequence

    sequence = list(range(len(piece_structures)))
    random.shuffle(sequence)
  

def new_piece():
    global piece_x, piece_y, piece_type, piece_rotation

    piece_x = 3
    piece_y = 0
    piece_type = 0
    piece_rotation = 0

  
def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= 0.5:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y
        else:
            new_piece()


def on_key_down(key):
    global piece_rotation, piece_type, piece_x, piece_y

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation >= len(piece_structures[piece_type]):
            test_rotation = 0
        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        test_x = piece_x - 1
        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.C:  # nyrad
        while can_piece_move(piece_x, piece_y + 1, piece_rotation):  # nyrad
            piece_y += 1  # nyrad

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.S:
        new_sequence()
        print(sequence)



# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

new_sequence()
new_piece()

# Tillfälligt
inert[7][4] = 'z'

pgzrun.go()  # måste vara sista raden
```

</details>

## Nästa bit från listan
När en ny bit behöver skapas tar vi bort det sista talet från listan och använder det för att bestämma typen av bit.

När listan med bitar är tom skapas en ny sådan lista.

✏️ Uppdatera koden i `new_piece()` och testkör!

```python
def new_piece():
    global piece_x, piece_y, piece_type, piece_rotation

    piece_x = 3
    piece_y = 0
    piece_type = sequence.pop() # nyrad
    if len(sequence) == 0: # nyrad
        new_sequence() # nyrad
    piece_rotation = 0
```

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces
import random

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()
piece_x_count = 4
piece_y_count = 4

sequence = []

timer = 0

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            test_block_x = test_x + x
            test_block_y = test_y + y
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_block_x not in range(grid_x_count)
                    or test_block_y >= grid_y_count
                    or inert[test_block_y][test_block_x] != ' '):
                return False

    return True


def new_sequence():
    global sequence

    sequence = list(range(len(piece_structures)))
    random.shuffle(sequence)


def new_piece():
    global piece_x, piece_y, piece_type, piece_rotation

    piece_x = 3
    piece_y = 0
    piece_type = sequence.pop()  # nyrad
    if len(sequence) == 0:  # nyrad
        new_sequence()  # nyrad
    piece_rotation = 0


def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= 0.5:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y
        else:
            new_piece()


def on_key_down(key):
    global piece_rotation, piece_type, piece_x, piece_y

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation >= len(piece_structures[piece_type]):
            test_rotation = 0
        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        test_x = piece_x - 1
        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.C:  # nyrad
        while can_piece_move(piece_x, piece_y + 1, piece_rotation):  # nyrad
            piece_y += 1  # nyrad

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.S:
        new_sequence()
        print(sequence)



# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

new_sequence()
new_piece()

# Tillfälligt
inert[7][4] = 'z'

pgzrun.go()  # måste vara sista raden
```

</details>

## Lägg bitens block till de orörliga blocken
  
När en bit har landat läggs bitens block till de orörliga blocken.

Bitens block gås igenom. 
Om ett block inte är tomt, sätter vi det orörliga blocket på den positionen till värdet som vi hämtar från biten.

✏️ Uppdatera koden i `update()` och testkör!

```python
def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= 0.5:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y
        else: # byt ut resten
            # Lägg till biten bland de orörliga blocken
            for y in range(piece_y_count):
                for x in range(piece_x_count):
                    block = piece_structures[piece_type][piece_rotation][y][x]
                    if block != ' ':
                        inert[piece_y + y][piece_x + x] = block
            new_piece()
```

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces
import random

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()
piece_x_count = 4
piece_y_count = 4

sequence = []

timer = 0

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            test_block_x = test_x + x
            test_block_y = test_y + y
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_block_x not in range(grid_x_count)
                    or test_block_y >= grid_y_count
                    or inert[test_block_y][test_block_x] != ' '):
                return False

    return True


def new_sequence():
    global sequence

    sequence = list(range(len(piece_structures)))
    random.shuffle(sequence)


def new_piece():
    global piece_x, piece_y, piece_type, piece_rotation

    piece_x = 3
    piece_y = 0
    piece_type = sequence.pop()  # nyrad
    if len(sequence) == 0:  # nyrad
        new_sequence()  # nyrad
    piece_rotation = 0


def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= 0.5:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y
        else:
            # Lägg till biten bland de orörliga blocken
            for y in range(piece_y_count):
                for x in range(piece_x_count):
                    block = piece_structures[piece_type][piece_rotation][y][x]
                    if block != ' ':
                        inert[piece_y + y][piece_x + x] = block
            new_piece()


def on_key_down(key):
    global piece_rotation, piece_type, piece_x, piece_y

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation >= len(piece_structures[piece_type]):
            test_rotation = 0
        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        test_x = piece_x - 1
        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.C:  # nyrad
        while can_piece_move(piece_x, piece_y + 1, piece_rotation):  # nyrad
            piece_y += 1  # nyrad

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.S:
        new_sequence()
        print(sequence)



# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

new_sequence()
new_piece()

# Tillfälligt
inert[7][4] = 'z'

pgzrun.go()  # måste vara sista raden
```

</details>

## Ny bit direkt efter släpp
  
När en bit släpps ner, sätter vi timern så att den löper ut direkt.
Då kommer nästa bit att skapas direkt istället för att vänta på timern.

Timergränsen behöver vi på fler ställen, så vi gör den till en variabel.

✏️ Uppdatera koden i `update()` och `on_key_down()` och testkör! Det behövs också en ny global variabel.

```python
# Lägg bland de globala variablerna högst upp
timer_limit = 0.5

def update(dt):
    # etc.
    if timer >= timer_limit:
    # etc.

def on_key_down(key):
    # etc.
    global timer, piece_y
    # etc.
    elif key == keys.C:
        while can_piece_move(piece_x, piece_y + 1, piece_rotation):
            piece_y += 1
            timer = timer_limit # uppdatera
```

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces
import random

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()
piece_x_count = 4
piece_y_count = 4

sequence = []

timer = 0
timer_limit = 0.5

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            test_block_x = test_x + x
            test_block_y = test_y + y
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_block_x not in range(grid_x_count)
                    or test_block_y >= grid_y_count
                    or inert[test_block_y][test_block_x] != ' '):
                return False

    return True


def new_sequence():
    global sequence

    sequence = list(range(len(piece_structures)))
    random.shuffle(sequence)


def new_piece():
    global piece_x, piece_y, piece_type, piece_rotation

    piece_x = 3
    piece_y = 0
    piece_type = sequence.pop() 
    if len(sequence) == 0: 
        new_sequence() 
    piece_rotation = 0


def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= timer_limit:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y
        else:
            # Lägg till biten bland de orörliga blocken
            for y in range(piece_y_count):
                for x in range(piece_x_count):
                    block = piece_structures[piece_type][piece_rotation][y][x]
                    if block != ' ':
                        inert[piece_y + y][piece_x + x] = block
            new_piece()


def on_key_down(key):
    global piece_rotation, piece_type, piece_x, piece_y

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation >= len(piece_structures[piece_type]):
            test_rotation = 0
        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        test_x = piece_x - 1
        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.C: 
        while can_piece_move(piece_x, piece_y + 1, piece_rotation):  
            piece_y += 1
            timer = timer_limit 

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.S:
        new_sequence()
        print(sequence)



# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

new_sequence()
new_piece()

# Tillfälligt
inert[7][4] = 'z'

pgzrun.go()  # måste vara sista raden
```

</details>

## Hitta fyllda rader
 
Varje rad med orörliga block loopas igenom. 
Om ingen av kolumnerna i raden är ett tomt block så är raden fylld.

För att göra det lättare att testa, skrivs de fullständiga radnumren ut just nu.

✏️ Lägg till i funktionen `update()` och testkör!

```python
def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= timer_limit:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y
        else:
            # Lägg till biten bland de orörliga blocken
            for y in range(piece_y_count):
                for x in range(piece_x_count):
                    block = piece_structures[piece_type][piece_rotation][y][x]
                    if block != ' ':
                        inert[piece_y + y][piece_x + x] = block
            # Hitta fyllda rader # nyrad
            for y in range(grid_y_count): # nyrad
                complete = True  # nyrad
                for x in range(grid_x_count):  # nyrad
                    if inert[y][x] == ' ':  # nyrad
                        complete = False # nyrad
                        break # nyrad

                if complete: # nyrad
                    # Tillfälligt  # nyrad
                    print(f"Complete row: {y}") # nyrad

            new_piece()
```

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces
import random

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()
piece_x_count = 4
piece_y_count = 4

sequence = []

timer = 0
timer_limit = 0.5

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            test_block_x = test_x + x
            test_block_y = test_y + y
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_block_x not in range(grid_x_count)
                    or test_block_y >= grid_y_count
                    or inert[test_block_y][test_block_x] != ' '):
                return False

    return True


def new_sequence():
    global sequence

    sequence = list(range(len(piece_structures)))
    random.shuffle(sequence)


def new_piece():
    global piece_x, piece_y, piece_type, piece_rotation

    piece_x = 3
    piece_y = 0
    piece_type = sequence.pop()
    if len(sequence) == 0:
        new_sequence()
    piece_rotation = 0


def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= timer_limit:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y
        else:
            # Lägg till biten bland de orörliga blocken
            for y in range(piece_y_count):
                for x in range(piece_x_count):
                    block = piece_structures[piece_type][piece_rotation][y][x]
                    if block != ' ':
                        inert[piece_y + y][piece_x + x] = block
            # Hitta fyllda rader
            for y in range(grid_y_count):
                complete = True
                for x in range(grid_x_count):
                    if inert[y][x] == ' ':
                        complete = False
                        break

                if complete:
                    # Tillfälligt
                    print(f"Complete row: {y}")

            new_piece()


def on_key_down(key):
    global piece_rotation, piece_type, piece_x, piece_y

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation >= len(piece_structures[piece_type]):
            test_rotation = 0
        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        test_x = piece_x - 1
        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.C:
        while can_piece_move(piece_x, piece_y + 1, piece_rotation):
            piece_y += 1
            timer = timer_limit

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.S:
        new_sequence()
        print(sequence)



# Kod för att starta appen här nedanför
for y in range(grid_y_count): #nyrad
    inert.append([]) #nyrad
        inert[y] = [' '] * grid_x_count #nyrad

new_sequence()
new_piece()

# Tillfälligt
inert[7][4] = 'z'

pgzrun.go()  # måste vara sista raden
```

</details>

## Ta bort fyllda rader
Om raden är fylld, loopar vi igenom raderna ända till näst översta raden.

Varje block i raden loopas igenom och ställs in på värdet för blocket ovanför det.
Eftersom det inte finns något ovanför den översta raden behöver den inte loopas igenom.

Den översta raden kommer då att vara helt tom.

✏️ Uppdatera koden i `update()` och testkör!

```python
def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= timer_limit:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y
        else:
            # Lägg till biten bland de orörliga blocken
            for y in range(piece_y_count):
                for x in range(piece_x_count):
                    block = piece_structures[piece_type][piece_rotation][y][x]
                    if block != ' ':
                        inert[piece_y + y][piece_x + x] = block
            # Hitta fyllda rader
            for y in range(grid_y_count):
                if not ' ' in inert[y]:  # inga tomma rutor på rad y, alltså fylld rad
                    # kopiera ner raderna ett steg så rad y skrivs över
                    inert[1:y+1] = inert[0:y]
                    # sätt in grid_x_count tomma rutor på rad 0
                    inert[0] = [' '] * grid_x_count

            new_piece()
```

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces
import random

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()
piece_x_count = 4
piece_y_count = 4

sequence = []

timer = 0
timer_limit = 0.5

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            test_block_x = test_x + x
            test_block_y = test_y + y
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_block_x not in range(grid_x_count)
                    or test_block_y >= grid_y_count
                    or inert[test_block_y][test_block_x] != ' '):
                return False

    return True


def new_sequence():
    global sequence

    sequence = list(range(len(piece_structures)))
    random.shuffle(sequence)


def new_piece():
    global piece_x, piece_y, piece_type, piece_rotation

    piece_x = 3
    piece_y = 0
    piece_type = sequence.pop()
    if len(sequence) == 0:
        new_sequence()
    piece_rotation = 0


def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= timer_limit:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y
        else:
            # Lägg till biten bland de orörliga blocken
            for y in range(piece_y_count):
                for x in range(piece_x_count):
                    block = piece_structures[piece_type][piece_rotation][y][x]
                    if block != ' ':
                        inert[piece_y + y][piece_x + x] = block
            # Hitta fyllda rader
            for y in range(grid_y_count):
                if not ' ' in inert[y]:  # inga tomma rutor på rad y, alltså fylld rad
                    # kopiera ner raderna ett steg så rad y skrivs över
                    inert[1:y+1] = inert[0:y]
                    # sätt in grid_x_count tomma rutor på rad 0
                    inert[0] = [' '] * grid_x_count

            new_piece()


def on_key_down(key):
    global piece_rotation, piece_type, piece_x, piece_y

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation >= len(piece_structures[piece_type]):
            test_rotation = 0
        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        test_x = piece_x - 1
        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.C:
        while can_piece_move(piece_x, piece_y + 1, piece_rotation):
            piece_y += 1
            timer = timer_limit

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.S:
        new_sequence()
        print(sequence)


# Kod för att starta appen här nedanför
for y in range(grid_y_count):
    inert.append([])
    inert[y] = [' '] * grid_x_count

new_sequence()
new_piece()

# Tillfälligt
# inert[7][4] = 'z'

pgzrun.go()  # måste vara sista raden
```

</details>

## Game over

Om en nyskapad bit är i en orörlig position är spelet över.

Vi gör en funktion som ställer in spelets startläge.
Den anropas innan spelet börjar och när spelet är över.

✏️ Uppdatera koden och testkör! Lägg till funktionen `reset()`, anropa den i `update()` och förenkla koden längst ner där appen startar.

```python
def new_sequence():
    # etc.

def new_piece():
    # etc.

def reset():
    global inert, timer

    inert = []
    for y in range(grid_y_count):
        inert.append([])
        inert[y] = [' '] * grid_x_count

    timer = 0
    new_sequence()
    new_piece()

# etc.

def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= timer_limit:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y
        else:
            # Lägg till biten bland de orörliga blocken
            for y in range(piece_y_count):
                for x in range(piece_x_count):
                    block = piece_structures[piece_type][piece_rotation][y][x]
                    if block != ' ':
                        inert[piece_y + y][piece_x + x] = block
            # Hitta fyllda rader
            for y in range(grid_y_count):
                if not ' ' in inert[y]:  # inga tomma rutor på rad y, alltså fylld rad
                    # kopiera ner raderna ett steg så rad y skrivs över
                    inert[1:y+1] = inert[0:y]
                    # sätt in grid_x_count tomma rutor på rad 0
                    inert[0] = [' '] * grid_x_count

            new_piece()
            if not can_piece_move(piece_x, piece_y, piece_rotation):
                reset()
# etc.

# Kod för att starta appen här nedanför
reset()

pgzrun.go()  # måste vara sista raden
```

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces
import random

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()
piece_x_count = 4
piece_y_count = 4

sequence = []

timer = 0
timer_limit = 0.5

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x, y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x, y + piece_y)


def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            test_block_x = test_x + x
            test_block_y = test_y + y
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_block_x not in range(grid_x_count)
                    or test_block_y >= grid_y_count
                    or inert[test_block_y][test_block_x] != ' '):
                return False

    return True


def new_sequence():
    global sequence

    sequence = list(range(len(piece_structures)))
    random.shuffle(sequence)


def new_piece():
    global piece_x, piece_y, piece_type, piece_rotation

    piece_x = 3
    piece_y = 0
    piece_type = sequence.pop()
    if len(sequence) == 0:
        new_sequence()
    piece_rotation = 0

def reset():
    global inert, timer

    inert = []
    for y in range(grid_y_count):
        inert.append([])
        inert[y] = [' '] * grid_x_count

    timer = 0
    new_sequence()
    new_piece()

def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= timer_limit:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y
        else:
            # Lägg till biten bland de orörliga blocken
            for y in range(piece_y_count):
                for x in range(piece_x_count):
                    block = piece_structures[piece_type][piece_rotation][y][x]
                    if block != ' ':
                        inert[piece_y + y][piece_x + x] = block
            # Hitta fyllda rader
            for y in range(grid_y_count):
                if not ' ' in inert[y]:  # inga tomma rutor på rad y, alltså fylld rad
                    # kopiera ner raderna ett steg så rad y skrivs över
                    inert[1:y+1] = inert[0:y]
                    # sätt in grid_x_count tomma rutor på rad 0
                    inert[0] = [' '] * grid_x_count

            new_piece()
            if not can_piece_move(piece_x, piece_y, piece_rotation):
                reset()


def on_key_down(key):
    global piece_rotation, piece_type, piece_x, piece_y

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation >= len(piece_structures[piece_type]):
            test_rotation = 0
        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        test_x = piece_x - 1
        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.C:
        while can_piece_move(piece_x, piece_y + 1, piece_rotation):
            piece_y += 1
            timer = timer_limit

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.S:
        new_sequence()
        print(sequence)


# Kod för att starta appen här nedanför
reset()

# Tillfälligt
# inert[7][4] = 'z'

pgzrun.go()  # måste vara sista raden
```

</details>

## Förskjutning av spelplanen
Spelplanen ritas 2 block från vänster på skärmen och 5 block från toppen av skärmen.

✏️ Uppdatera koden i `draw()` och testkör!

```python
def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
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

    offset_x = 2 #nyrad
    offset_y = 5 #nyrad
    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x + offset_x, y + offset_y) #ändrad

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x + offset_x, y + piece_y + offset_y) #ändrad
```

![image](https://user-images.githubusercontent.com/4598641/226016663-cb1d5333-1bd0-4943-91e7-8d22d195f2ef.png)

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
```

</details>

## Rita nästa bit

Den sista biten i sekvensen, alltså nästa bit som faller, ritas med sin första rotationsstil.
Den är förskjuten fem rutor från vänster och en ruta uppifrån.

✏️ Uppdatera koden i `draw()` och testkör!

```python
def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
        colors = {
            ' ': (222, 222, 222),
            'i': (120, 195, 239),
            'j': (236, 231, 108),
            'l': (124, 218, 193),
            'o': (234, 177, 121),
            's': (211, 136, 236),
            't': (248, 147, 196),
            'z': (169, 221, 118),
            'preview': (190, 190, 190), #nyrad
        }
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

    offset_x = 2
    offset_y = 5
    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x + offset_x, y + offset_y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x + offset_x,
                           y + piece_y + offset_y)

    for y in range(piece_y_count): #nyrad
        for x in range(piece_x_count): #nyrad
            block = piece_structures[sequence[-1]][0][y][x] #nyrad 
            if block != ' ': #nyrad
                draw_block('preview', x + 5, y + 1) #nyrad
```

![image](https://user-images.githubusercontent.com/4598641/226016912-b2e1d0a6-fbf5-41b8-b808-9fdacaea6fb0.png)

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import pieces
import random

# Globala variabler här nedanför
WIDTH = 20 * 14
HEIGHT = 20 * 25

grid_x_count = 10
grid_y_count = 18

piece_type = 0
piece_rotation = 0
piece_x = 3
piece_y = 0

inert = []
piece_structures = pieces.get_piece_structures()
piece_x_count = 4
piece_y_count = 4

sequence = []

timer = 0
timer_limit = 0.5

# Funktioner (def) här nedanför


def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
        colors = {
            ' ': (222, 222, 222),
            'i': (120, 195, 239),
            'j': (236, 231, 108),
            'l': (124, 218, 193),
            'o': (234, 177, 121),
            's': (211, 136, 236),
            't': (248, 147, 196),
            'z': (169, 221, 118),
            'preview': (190, 190, 190),
        }
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

    offset_x = 2
    offset_y = 5
    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x + offset_x, y + offset_y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(block, x + piece_x + offset_x,
                           y + piece_y + offset_y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[sequence[-1]][0][y][x]
            if block != ' ':
                draw_block('preview', x + 5, y + 1)


def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            test_block_x = test_x + x
            test_block_y = test_y + y
            if piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    test_block_x not in range(grid_x_count)
                    or test_block_y >= grid_y_count
                    or inert[test_block_y][test_block_x] != ' '):
                return False

    return True


def new_sequence():
    global sequence

    sequence = list(range(len(piece_structures)))
    random.shuffle(sequence)


def new_piece():
    global piece_x, piece_y, piece_type, piece_rotation

    piece_x = 3
    piece_y = 0
    piece_type = sequence.pop()
    if len(sequence) == 0:
        new_sequence()
    piece_rotation = 0


def reset():
    global inert, timer

    inert = []
    for y in range(grid_y_count):
        inert.append([])
        inert[y] = [' '] * grid_x_count

    timer = 0
    new_sequence()
    new_piece()


def update(dt):
    global timer, piece_y

    timer += dt
    if timer >= timer_limit:
        timer = 0
        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y
        else:
            # Lägg till biten bland de orörliga blocken
            for y in range(piece_y_count):
                for x in range(piece_x_count):
                    block = piece_structures[piece_type][piece_rotation][y][x]
                    if block != ' ':
                        inert[piece_y + y][piece_x + x] = block
            # Hitta fyllda rader
            for y in range(grid_y_count):
                if not ' ' in inert[y]:  # inga tomma rutor på rad y, alltså fylld rad
                    # kopiera ner raderna ett steg så rad y skrivs över
                    inert[1:y+1] = inert[0:y]
                    # sätt in grid_x_count tomma rutor på rad 0
                    inert[0] = [' '] * grid_x_count

            new_piece()
            if not can_piece_move(piece_x, piece_y, piece_rotation):
                reset()


def on_key_down(key):
    global piece_rotation, piece_type, piece_x, piece_y

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation >= len(piece_structures[piece_type]):
            test_rotation = 0
        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

    elif key == keys.LEFT:
        test_x = piece_x - 1
        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.C:
        while can_piece_move(piece_x, piece_y + 1, piece_rotation):
            piece_y += 1
            timer = timer_limit

    # Tillfälligt
    elif key == keys.DOWN:
        piece_type += 1
        if piece_type >= len(piece_structures):
            piece_type = 0
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.UP:
        piece_type -= 1
        if piece_type < 0:
            piece_type = len(piece_structures) - 1
        piece_rotation = 0

    # Tillfälligt
    elif key == keys.S:
        new_sequence()
        print(sequence)


# Kod för att starta appen här nedanför
reset()

pgzrun.go()  # måste vara sista raden
```

</details>

# Uppgifter

## 1. Vad var svårt med kodningen?
Ge ett par exempel.


# Källor

Översatt och bearbetat för repl.it baserat på originalet: https://simplegametutorials.github.io/pygamezero/blocks/
