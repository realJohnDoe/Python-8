# Fifteen ⭐⭐⭐

## En handledning för Python och Pygame Zero 1.2

![image](https://user-images.githubusercontent.com/4598641/226436083-7b0b90b9-9c13-4b83-bfd8-3534ac8291c0.png)

# Regler

Det finns en tavla med 15 bitar och en tom ruta. 
Flytta runt bitarna tills de är i nummerordning genom att använda piltangenterna för att flytta en bit i taget till den tomma rutan.

## Kontroller

**Piltangenter**	Flytta en bit

# Översikt
Bitarna lagras som ett rutnät med siffror.

Siffran 16 representerar den tomma rutan.

![image](https://user-images.githubusercontent.com/4598641/226436258-85719c97-8e01-4aca-85b0-82d3cc184876.png)

Grannbiten flyttas till den tomma rutan när en piltangent trycks ned.

I början av spelet är bitarna i stigande nummerordning och slumpmässiga drag görs för att blanda det. Om bitarnas position blandas helt slumpmässigt kan det resultera i en uppställning som inte går att lösa.

Efter att en bit har flyttats, gås bitarna igenom. Om alla har sina ursprungliga värden i nummerordning är spelet över.

# Kodning

## Rita bitarna

Bitarna ritas som rutor.

Just nu ritas en bit där den tomma rutan ska vara.

✏️ Se till att du är inloggad i repl.it. Öppna startprojektet https://replit.com/@RobertStorlind/fifteen-starter och spara en egen kopia med knappen "Fork".
Testkör!

```python
import pgzrun
# Globala variabler här under
WIDTH, HEIGHT = 400, 400

# Funktioner (def) här under

def draw():
    screen.fill((0, 0, 0))
    piece_size = 100

    for y in range(4):
        for x in range(4):
            piece_draw_size = piece_size - 1

            screen.draw.filled_rect(
                Rect(
                    x * piece_size, y * piece_size,
                    piece_draw_size, piece_draw_size
                ),
                color=(100, 20, 150)
            )

# Kod för att starta appen här under

pgzrun.go()  # Ska alltid vara sist
```

![image](https://user-images.githubusercontent.com/4598641/226436463-1d10dd82-ed1c-429b-b0bc-e855b4969551.png)

## Rita siffrorna

Numren ritas ovanpå bitarna.

Bitens nummer beräknas genom att addera Y-koordinaten (dvs. radnummer) multiplicerat med antalet bitar i en rad till X-koordinaten plus 1.

Till exempel, på den första raden är Y-koordinaten 0, så ingenting läggs till varje X-koordinat, så den första siffran på den första raden är 1.
På den andra raden läggs 4 till varje X-koordinat, så den första nummer på andra raden är 5.

✏️ Uppdatera koden och testkör.

```python
def draw():
    screen.fill((0, 0, 0))

    for y in range(4):
        for x in range(4):
            piece_size = 100
            piece_draw_size = piece_size - 1

            screen.draw.filled_rect(
                Rect(
                    x * piece_size, y * piece_size,
                    piece_draw_size, piece_draw_size
                ),
                color=(100, 20, 150)
            )
            screen.draw.text( #nyrad 🔲
                str(y * 4 + x + 1), #nyrad 🔲
                (x * piece_size, y * piece_size), #nyrad 🔲
                fontsize=60 #nyrad 🔲
            ) #nyrad 🔲
            

# Kod för att starta appen här under

pgzrun.go() # Ska alltid vara sist
```

![image](https://user-images.githubusercontent.com/4598641/226436562-731e3960-4198-4bef-8635-e239557be6c9.png)

## Skapa rutnätet
Ett rutnät skapas med varje bits nummer lagrat på sin plats på rutnätet, och detta nummer ritas.

Antalet bitar på X- och Y-axlarna återanvänds från att rita bitarna, så de görs till variabler.

✏️ Uppdatera koden och testkör.

```python
import pgzrun
# Globala variabler här under
WIDTH, HEIGHT = 400, 400

grid_x_count = 4 #nyrad 🔲
grid_y_count = 4 #nyrad 🔲
grid = [] #nyrad 🔲

# Funktioner (def) här under
def draw():
    screen.fill((0, 0, 0))
    piece_size = 100

    for y in range(grid_y_count): #ändrad 🔲
        for x in range(grid_x_count): #ändrad 🔲
            piece_draw_size = piece_size - 1

            screen.draw.filled_rect(
                Rect(
                    x * piece_size, y * piece_size,
                    piece_draw_size, piece_draw_size
                ),
                color=(100, 20, 150)
            )
            screen.draw.text(
                str(grid[y][x]), #ändrad 🔲
                (x * piece_size, y * piece_size),
                fontsize=60
            )


# Kod för att starta appen här under
for y in range(grid_y_count): #nyrad 🔲
    grid.append([]) #nyrad 🔲
    for x in range(grid_x_count): #nyrad 🔲
        grid[y].append(y * grid_x_count + x + 1) #nyrad 🔲

pgzrun.go()  # Ska alltid vara sist
```

## Rita inte den tomma rutan
Antalet bitar på varje axel multiplicerat tillsammans ger det totala antalet bitar (dvs. 4 gånger 4 betyder 16 bitar), och en bit ritas bara om numret är skilt från 16.

✏️ Uppdatera koden och testkör.

```python
# etc.
def draw():
    screen.fill((0, 0, 0))
    piece_size = 100

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            if grid[y][x] == grid_x_count * grid_y_count: #ändrad 🔲
                continue  # hoppa över detta x och gå till nästa värde i "for x" #ändrad 🔲
# etc.
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun
# Globala variabler här under
WIDTH, HEIGHT = 400, 400

grid_x_count = 4
grid_y_count = 4
grid = []

# Funktioner (def) här under


def draw():
    screen.fill((0, 0, 0))
    piece_size = 100

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            if grid[y][x] == grid_x_count * grid_y_count:
                continue  # hoppa över detta x och gå till nästa värde i "for x"

            piece_draw_size = piece_size - 1

            screen.draw.filled_rect(
                Rect(
                    x * piece_size, y * piece_size,
                    piece_draw_size, piece_draw_size
                ),
                color=(100, 20, 150)
            )
            screen.draw.text(
                str(grid[y][x]),
                (x * piece_size, y * piece_size),
                fontsize=60
            )


# Kod för att starta appen här under
for y in range(grid_y_count):
    grid.append([])
    for x in range(grid_x_count):
        grid[y].append(y * grid_x_count + x + 1)

pgzrun.go()  # Ska alltid vara sist
```
  
</details>

![image](https://user-images.githubusercontent.com/4598641/226437183-8e41b05e-77bc-488b-b400-4785be077050.png)

## Hitta den tomma rutans position
Det första steget i att flytta en bit är att hitta positionen för den tomma rutan.

När en tangent trycks in, loopar vi igenom rutnätet. Om en bit är lika med antalet bitar på varje axel multiplicerat med varandra (dvs det är den tomma rutan), så skrivs dess position för närvarande ut.

✏️ Lägg till funktionen `on_key_down()` och testkör genom att klicka på tangentbordet. Utskriften kommer i det svarta konsollfönstret.

```python
def on_key_down(key): #
    for y in range(grid_y_count):
        for x in range(grid_x_count):
            if grid[y][x] == grid_x_count * grid_y_count:
                empty_x = x
                empty_y = y

    # Tillfälligt
    print(f"empty x: {empty_x}, empty y: {empty_y}")
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun
# Globala variabler här under
WIDTH, HEIGHT = 400, 400

grid_x_count = 4
grid_y_count = 4
grid = []

# Funktioner (def) här under


def on_key_down(key):
    for y in range(grid_y_count):
        for x in range(grid_x_count):
            if grid[y][x] == grid_x_count * grid_y_count:
                empty_x = x
                empty_y = y

    # Tillfälligt
    print(f"empty x: {empty_x}, empty y: {empty_y}")


def draw():
    screen.fill((0, 0, 0))
    piece_size = 100

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            if grid[y][x] == grid_x_count * grid_y_count:
                continue  # hoppa över detta x och gå till nästa värde i "for x"

            piece_draw_size = piece_size - 1

            screen.draw.filled_rect(
                Rect(
                    x * piece_size, y * piece_size,
                    piece_draw_size, piece_draw_size
                ),
                color=(100, 20, 150)
            )
            screen.draw.text(
                str(grid[y][x]),
                (x * piece_size, y * piece_size),
                fontsize=60
            )


# Kod för att starta appen här under
for y in range(grid_y_count):
    grid.append([])
    for x in range(grid_x_count):
        grid[y].append(y * grid_x_count + x + 1)

pgzrun.go()  # Ska alltid vara sist
```
  
</details>

Så här ska det se ut i det svarta konsollfönstret:
```
tom x: 3, tom y: 3
```

## Flytta en bit neråt
Om Y-koordinaten för den tomma rutan är större än 0, betyder det att det finns en bit ovanför den tomma rutan, så det är möjligt att flytta en bit neråt.

Den tomma rutan ändras till bitnumret ovanför rutan. Biten ovanför rutan ändras till den lediga rutan (16).

Just nu flyttar vilken tangent som helst en bit ner.

✏️ Uppdatera koden och testkör genom att trycka på någon tangent. Flyttas biten neråt som den ska?

```python
def on_key_down(key):
    for y in range(grid_y_count):
        for x in range(grid_x_count):
            if grid[y][x] == grid_x_count * grid_y_count:
                empty_x = x
                empty_y = y

    # Tillfälligt
    print(f"empty x: {empty_x}, empty y: {empty_y}")

    if empty_y > 0: #nyrad 🔲
        changed = (grid[empty_y][empty_x], grid[empty_y - 1][empty_x]) #nyrad 🔲
        grid[empty_y - 1][empty_x], grid[empty_y][empty_x] = changed #nyrad 🔲
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun
# Globala variabler här under
WIDTH, HEIGHT = 400, 400

grid_x_count = 4
grid_y_count = 4
grid = []

# Funktioner (def) här under


def on_key_down(key):
    for y in range(grid_y_count):
        for x in range(grid_x_count):
            if grid[y][x] == grid_x_count * grid_y_count:
                empty_x = x
                empty_y = y

    # Tillfälligt
    print(f"empty x: {empty_x}, empty y: {empty_y}")

    if empty_y > 0:
        changed = (grid[empty_y][empty_x], grid[empty_y - 1][empty_x])
        grid[empty_y - 1][empty_x], grid[empty_y][empty_x] = changed


def draw():
    screen.fill((0, 0, 0))
    piece_size = 100

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            if grid[y][x] == grid_x_count * grid_y_count:
                continue  # hoppa över detta x och gå till nästa värde i "for x"

            piece_draw_size = piece_size - 1

            screen.draw.filled_rect(
                Rect(
                    x * piece_size, y * piece_size,
                    piece_draw_size, piece_draw_size
                ),
                color=(100, 20, 150)
            )
            screen.draw.text(
                str(grid[y][x]),
                (x * piece_size, y * piece_size),
                fontsize=60
            )


# Kod för att starta appen här under
for y in range(grid_y_count):
    grid.append([])
    for x in range(grid_x_count):
        grid[y].append(y * grid_x_count + x + 1)

pgzrun.go()  # Ska alltid vara sist
```
  
</details>

![image](https://user-images.githubusercontent.com/4598641/226437400-e5f88975-05ce-4b80-80ca-50862059eb21.png)

## Flytta upp bitar
Om Y-koordinaten för den tomma rutan är mindre än antalet rader i rutnätet, betyder det att det finns en bit under den tomma rutan,
så att det är möjligt att flytta biten uppåt.

Y-koordinaten för den bit som det tomma rutan byter med görs till en variabel. 
När upp-tangenten trycks in ställs den till positionen under den tomma rutan (dvs plus 1 på Y-axeln).

✏️ Uppdatera koden och testkör.

```python
###
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
###
```
  
</details>


## Flytta bitar åt vänster och höger
X-koordinaten för den bit som den tomma rutan byter med görs till en variabel, och den ändras när vänster- eller högerpilen trycks ned.

✏️ Uppdatera koden och testkör.

```python
###
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
###
```
  
</details>


![image](https://user-images.githubusercontent.com/4598641/226437516-322ed925-e617-41a9-94a7-fc3e9329aeeb.png)



## Blanda rutorna
I början av spelet görs ett antal slumpmässiga drag för att blanda brädet.

Ett slumptal mellan 1 och 4 genereras och ett drag görs i en av de fyra rörelseriktningarna baserat på detta nummer.

Slumpmodulen importeras så att random.randint kan användas.

✏️ Uppdatera koden och testkör.

```python
###
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
###
```
  
</details>


![image](https://user-images.githubusercontent.com/4598641/226437586-c1a482c0-b465-4214-822a-68f8b2530839.png)

## Förenkla koden
Den enda skillnaden mellan blandningskoden och den tangentbordskontrollerade koden är hur riktningen för förflyttningen bestäms,
så en funktion görs med riktningen som parameter.

✏️ Uppdatera koden och testkör.

```python
###
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
###
```
  
</details>



## Gör den nedre högra positionen tom
Den tomma rutan ska vara längst ner till höger när spelet börjar. Därför flyttas bitarna åt vänster och uppåt flera gånger. 
Antalet bitar på en axel minus 1 är det maximala antalet drag det skulle ta för att flytta den tomma rutan från ena sidan till den andra.

✏️ Uppdatera koden och testkör.

```python
###
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
###
```
  
</details>


![image](https://user-images.githubusercontent.com/4598641/226437694-caf5182b-39da-41bf-95d7-4ef3c098baf8.png)


## Återställa spelet
En funktion skapas som ställer in spelets initiala tillstånd.

Denna funktion anropas innan spelet börjar och när r- tangenten trycks ned.

✏️ Uppdatera koden och testkör.

```python
###
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
###
```
  
</details>


## Kontrollera om vi är klara
Efter att ett drag har gjorts, loopar vi genom bitarna, och om ingen av bitarna inte är lika med numret som de fick från början 
(dvs de är alla i sina sorterade positioner), återställs spelet.

## Förenkla koden
Koden för att beräkna startvärdet för en bit återanvänds, så den görs till en funktion.
✏️ Uppdatera koden och testkör.

```python
###
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
###
```
  
</details>




## Blanda igen om det råkar vara klart efter blandningen
Om bitarna fortfarande är i sin ursprungliga ordning efter att de har blandats, sker blandningsprocessen igen.

Koden för att kontrollera om bitarna är i sin ursprungliga ordning återanvänds, så den görs till en funktion.

✏️ Uppdatera koden och testkör.

```python
###
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
###
```
  
</details>



# Källor

Översatt och bearbetat för repl.it baserat på originalet: https://simplegametutorials.github.io/pygamezero/fifteen/
