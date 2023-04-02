# Sokoban ⭐⭐⭐
## En handledning för Python och Pygame Zero 1.2

![image](https://user-images.githubusercontent.com/4598641/226440407-e4b478ca-f453-48b3-a640-38e4858d1c56.png)

[Spelnivåerna i den här handledningen är hämtade från Rockbox-projektet.](http://git.rockbox.org/?p=rockbox.git;a=blob_plain;f=apps/plugins/sokoban.levels)

# Regler
Skjut in alla lådorna på lagerplatserna.

Lådor kan endast flyttas om det finns ett ledigt utrymme bredvid den (inte en vägg eller annan låda).

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
**P**	Tidigare nivå<br>

# Översikt
De olika tillstånden en ruta kan vara i representeras av följande strängar:

__@__	Spelare<br>
__+__	Spelare på lagerplats<br>
__$__	Låda<br>
__*__	Låda på lagerplats<br>
__.__	Lagerplats<br>
__#__	Vägg

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
För närvarande lagras en enstaka nivå och en kvadrat ritas för varje cell som inte är ett mellanslag (dvs. tom).

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

## Rita celltyper
Rutans sträng visas på varje ruta.

✏️ Uppdatera koden. Vad händer när du ...?

```python
def draw():
    screen.fill((0, 0, 0))

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != ' ':
                # etc.

                screen.draw.text( #nytt 
                    cell, #nytt
                    (x * cell_size, y * cell_size), #nytt
                    color=(0, 0, 0) #nytt
                ) #nytt
```

✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226441595-3f2259b1-970d-46d2-98f1-b1ba305e126b.png)

## Ställa in färger
Bakgrundsfärgen ändras och färgen på varje cell ställs in baserat på dess typ.

✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226441696-30c32370-c672-422b-9a3c-4f8851498f74.png)

## Namnge celltyper
Så vi behöver inte komma ihåg vilken sträng som refererar till vilken celltyp, celltypssträngarna lagras i variabler.


✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

## Hitta spelarcell
Det första steget i att flytta spelaren är att hitta vilken cellposition de befinner sig på.

Cellerna i nivån loopas igenom, och om celltypen är en spelare eller en spelare på lagerplats, så skrivs spelarens position ut för närvarande.
Så här ser det ut i konsollfönstret:

```
4 4
```

✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

## Hitta celltyp i riktning mot tangenten som trycks ned
Celltypen för spelarens nuvarande position och celltypen för den intilliggande positionen i riktningen för den nedtryckta piltangenten lagras i variabler och skrivs för närvarande ut.

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

✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

## Skapa en testnivå
En testnivå är gjord för att testa spelarens rörelse.


✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226441985-25fde8b7-f083-443e-bc3c-3e0082023c45.png)


## Flyttar spelaren till tom plats
Om värdet på spelarens nuvarande position är spelare (dvs. inte player_on_storage ) och den intilliggande cellen är tom , så blir spelarens position tom och den intilliggande positionen blir spelare .

✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226442037-607ab9cd-4a59-47de-a13e-6ea0b696a3da.png)

## Flytta spelaren till lagerplats
Om den intilliggande positionen är en lagerplats, blir den nya intilliggande positionen `player_on_storage`.

För närvarande kan spelaren gå vidare till en lagerplats, men inte utanför lagerplatsen.


✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226442060-dddc88af-c52b-4d75-bafc-d202d9069ae1.png)

## Förenkla koden
Den nya intilliggande positionen (antingen player eller player_on_storage ) ställs in baserat på typen av intilliggande , så en ordlista skapas som returnerar nästa intilliggande celltyp när den indexeras av den aktuella intilliggande celltypen.

Den används också för att kontrollera om spelaren kan flytta till den intilliggande positionen genom att kontrollera om den har en nyckel med värdet intilliggande .


✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

## Flytta spelare från lagerplats
Om spelaren är på lagerplats är spelarens nuvarande position inställd på lagerplats.

✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226442123-828097c9-b89f-449a-9de0-e83d8a774464.png)

## Förenkla koden
En ordbok skapas som returnerar nästa celltyp för spelarens tidigare position när den indexeras av den aktuella spelarens celltyp.

✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

## Putta lådan till tom plats
Cellen bortom den intilliggande cellen lagras i en variabel.

player_y + dy + dy kontrolleras för att se om det är större än eller lika med 0 och mindre än len ( level ) , dvs det är inom nivån höjdmässigt, och player_x + dx + dx kontrolleras för att se om det är större än eller lika med 0 och mindre än len ( nivå [ player_y + dy + dy ] ) , dvs det är inom nivån breddmässigt.

(Den intilliggande positionen är inte markerad på samma sätt eftersom det alltid finns en kant av väggar runt varje nivå, så player_y + dy eller player_x + dx kommer aldrig att vara utanför nivån.)

Om den intilliggande cellen är en ruta och den bortom cellen är tom, är den intilliggande positionen inställd på spelare och positionen bortom är satt till låda.

✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226442221-e7c86311-2b78-4175-94f7-29befecbb32e.png)

## Skjuta på lådan till förvaringen
Om den bortomstående positionen är lagring , så ställs bortom positionen till box_on_storage .

✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>


![image](https://user-images.githubusercontent.com/4598641/226442270-45099ac7-095b-4291-a2e4-344aa34e1862.png)


## Förenkla koden
En ordbok skapas som returnerar nästa celltyp när den indexeras av den aktuella celltypen.

✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

## Trycklåda på förvaring
Om den intilliggande cellen är en ruta på lagring, så sätts den intilliggande positionen till box_on_storage .

✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226442358-30a184b9-f44a-4b1f-b418-b73c8b0cd8b9.png)

## Förenkla koden
En ordlista skapas som returnerar nästa intilliggande celltyp när en ruta trycks när den indexeras av den aktuella intilliggande celltypen.

✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

## Laddar nivå från nivålistan
Nivåerna lagras i en lista.

Numret på den aktuella nivån lagras också.

Den aktuella nivån kopieras från listan som innehåller alla nivåer.

Kopieringsmodulen importeras så att copy.deepcopy kan användas .

✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

![image](https://user-images.githubusercontent.com/4598641/226442656-f303feef-223f-4342-a498-17eb88ffb112.png)

## Återställ nivå
När R -tangenten trycks ned återställs nivån.

Koden för att kopiera den aktuella nivån återanvänds, så en funktion görs.


✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

## Nästa och föregående nivå
När N-tangenten trycks in laddas nästa nivå och när p -tangenten trycks in laddas föregående nivå.


✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>


## Slå in nästa och föregående nivå
Om nästa nivå är efter den sista nivån laddas den första nivån.

Om den föregående nivån är före den första nivån laddas den sista nivån.


✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

## Gå till nästa nivå när du är klar
Efter att spelaren har flyttat, går alla celler i nivån igenom, och om ingen av cellerna är lådor (dvs. alla lådor är lagrade), är nivån klar och nästa nivå laddas.

✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

## Fler nivåer

✏️ Uppdatera koden. Vad händer när du ...?

```python
####
```

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
####
```

</details>

Kod: XXXX

# Källor
Engelska originalprojektet: https://simplegametutorials.github.io/pygamezero/sokoban/
