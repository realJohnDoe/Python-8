# Repeat

### En handledning för Python och Pygame Zero 1.2

![image](https://user-images.githubusercontent.com/4598641/225698865-f394ffdb-6b0c-4731-8763-915c93b7b965.png)

# Regler
Se när en talsekvens blinkar.

Upprepa sekvensen med sifferknapparna.

Om du lyckas upprepa sekvensen läggs ett nytt tal till och sekvensen blinkar igen.

# Kodning

## Sekvens
Vi skapar sekvenslistan. Till en början innehåller den en testsekvens med siffror mellan 1 och 4.

```python
import pgzrun

sequence = [4, 3, 1, 2, 2, 3] # Tillfälligt

def draw():
    screen.fill((0, 0, 0))
    screen.draw.text(', '.join(map(str, sequence)), (0, 0))

pgzrun.go() # Ska alltid vara sist i programmet (längst ner)
```

![image](https://user-images.githubusercontent.com/4598641/225699441-a8ba2e0d-516c-42e0-8bbf-c062e783aee5.png)

✏️ Mata in och testkör koden i ett nytt projekt i repl.it.

## Nuvarande position i sekvensen
Den aktuella sekvenspositionen börjar vid 1.

Om spelaren trycker på knappen som motsvarar siffran i sekvensen vid den aktuella positionen, ökar vi positionen med 1.

Detta blir fel när den aktuella positionen är längre än längden på sekvenslistan.

```python
import pgzrun

sequence = [4, 3, 1, 2, 2, 3] # Tillfälligt
current = 0 #nyrad

def on_key_down(key):
    global current # För att vi ska kunna uppdatera variabeln current som är utanför funktionen
    
    if key in (keys.K_1, keys.K_2, keys.K_3, keys.K_4): # siffertangenterna 1, 2, 3, 4
        if key == keys.K_1:
            number = 1
        elif key == keys.K_2:
            number = 2
        elif key == keys.K_3:
            number = 3
        elif key == keys.K_4:
            number = 4
        
        if number == sequence[current]:
            current += 1

def draw():
    screen.fill((0, 0, 0))

    screen.draw.text(', '.join(map(str, sequence)), (0, 0))
    screen.draw.text(f"{current + 1}/{len(sequence)}", (0, 20)) #nyrad
    screen.draw.text(f"sequence[current]: {sequence[current]}", (0, 40)) #nyrad

pgzrun.go() # Ska alltid vara sist i programmet (längst ner)
```

✏️ Uppdatera din kod så att den blir som här ovanför och testkör den. Du måste inte mata in kommentarerna &ndash; de förklarar vad koden gör.
Klicka i terminalfönstret. Sedan kan du trycka på siffertangenterna 1 till 4 för att testa.

![image](https://user-images.githubusercontent.com/4598641/225703318-26fb8e5b-9d98-4a9d-b740-fc220f938125.png)

## Återställ aktuell position

När den aktuella positionen överskrider sekvenslängden återställs vi den till 0.

✏️ Uppdatera koden i on_key_down() och testkör igen.

```python
def on_key_down(key):
    global current

    if key in (keys.K_1, keys.K_2, keys.K_3, keys.K_4):
        # etc. som innan

        if number == sequence[current]:
            current += 1
            if current == len(sequence): #nyrad
                current = 0 #nyrad
```

## Lägg till nästa tal att komma ihåg i sekvensen

När den aktuella positionen återställs läggs ett slumptal mellan 1 och 4 till i sekvensen.

Vi behöver importera random så att vi kan få slumptal från `random.randint`.

```python
import random # Lägg till högst upp bland importerna

# Uppdatera funktionen
def on_key_down(key):
    # etc.
            if current == len(sequence):
                current = 0
                sequence.append(random.randint(1, 4))
```
✏️ Uppdatera och testkör koden.

<details>
    <summary>📝 Så här ser hela koden ut nu XXXX</summary>

</details>

## Startsekvens med ett enda tal

Nu skapar vi en riktig sekvens, till en början med ett enda slumptal.

Eftersom koden för att lägga till ett slumptal till sekvensen återanvänds, gör vi den till en funktion, `add_to_sequence()`.

```python
sequence = [] # Lägg detta högt upp vid de andra variablerna

def add_to_sequence():
    sequence.append(random.randint(1, 4))

add_to_sequence()

# etc.

def on_key_down(key):
    # etc.

            if current == len(sequence):
                current = 0
                add_to_sequence() #nyrad
```

✏️ Uppdatera koden och testkör den.

<details>
    <summary>Så här bör koden se ut nu:</summary>

```python
import pgzrun
import random

sequence = []

def add_to_sequence():
    sequence.append(random.randint(1, 4))

add_to_sequence()

current = 0

def on_key_down(key):
    global current

    if key in (keys.K_1, keys.K_2, keys.K_3, keys.K_4):
        if key == keys.K_1:
            number = 1
        elif key == keys.K_2:
            number = 2
        elif key == keys.K_3:
            number = 3
        elif key == keys.K_4:
            number = 4

        if number == sequence[current]:
            current += 1
            if current == len(sequence):
                current = 0
                add_to_sequence()

def draw():
    screen.fill((0, 0, 0))

    screen.draw.text(', '.join(map(str, sequence)), (0, 0))
    screen.draw.text(f"{current + 1}/{len(sequence)}", (0, 20))
    screen.draw.text(f"sequence[current]: {sequence[current]}", (0, 40))
    
pgzrun.go()
```
</details>
    
## Återställa spelet

Vi skapar en funktion som ställer in spelets startläge.

Denna funktion anropas innan spelet börjar och när en felaktig siffertangent trycks ned.

```python
def add_to_sequence():
    sequence.append(random.randint(1, 4))

def reset(): #nyrad
    global sequence #nyrad
    global current #nyrad

    sequence = [] #nyrad
    add_to_sequence() #nyrad
    current = 0 #nyrad

reset() #nyrad

def on_key_down(key):
    global current

    if key in (keys.K_1, keys.K_2, keys.K_3, keys.K_4):

        # etc.

        if number == sequence[current]:
            current += 1
            if current == len(sequence):
                current = 0
                add_to_sequence()
        else: #nyrad
            reset() #nyrad
```
✏️ Uppdatera din kod och testkör.


## Rita första kvadraten

Den första rutan är ritad med en mörkröd ruta och en vit siffra.

```python
def draw():
    screen.fill((0, 0, 0))

    square_size = 50 #nyrad

    screen.draw.filled_rect( #nyrad
        Rect(0, 0, square_size, square_size), #nyrad
        color=(50, 0, 0) #nyrad
    ) #nyrad
    screen.draw.text('1', (19, 18)) #nyrad

    screen.draw.text(str(current + 1) + '/' + str(len(sequence)), (20, 60)) #uppdatera
    screen.draw.text('sequence[current]: ' + str(sequence[current]), (20, 100)) #uppdatera
    screen.draw.text(', '.join(map(str, sequence)), (20, 140)) #uppdatera
```

![image](https://user-images.githubusercontent.com/4598641/225725617-e4af967f-5de4-4edd-9293-2ba5268b2215.png)

## Rita alla rutor
Resten av rutorna är ritade på liknande sätt.

```python
def draw():
    screen.fill((0, 0, 0))

    square_size = 50

    screen.draw.filled_rect(
        Rect(0, 0, square_size, square_size),
        color=(50, 0, 0)
    )
    screen.draw.text('1', (19, 18))

    # Lägg till nya rader
    screen.draw.filled_rect(
        Rect(square_size, 0, square_size, square_size),
        color=(0, 50, 0)
    )
    screen.draw.text('2', (square_size + 21, 18))

    screen.draw.filled_rect(
        Rect(square_size * 2, 0, square_size, square_size),
        color=(0, 0, 50)
    )
    screen.draw.text('3', (square_size * 2 + 21, 18))

    screen.draw.filled_rect(
        Rect(square_size * 3, 0, square_size, square_size),
        color=(50, 50, 0)
    )
    screen.draw.text('4', (square_size * 3 + 21, 18))

    # etc.
```

![image](https://user-images.githubusercontent.com/4598641/225706773-2c9ffb3d-555c-4df1-b3f4-35a19c6e385e.png)

## Förenkla koden
Koden för att rita varje ruta är likadan. Vi gör den till en funktion som vi kan använda flera gånger.
```python3
def draw():
    screen.fill((0, 0, 0))

    def draw_square(number, color): #ändra
        square_size = 50
        screen.draw.filled_rect(
            Rect(square_size * (number - 1), 0, square_size, square_size), #ändra
            color=color #ändra
        )
        screen.draw.text(str(number), (square_size * (number - 1) + 21, 18)) #ändra

    draw_square(1, (50, 0, 0)) #nyrad
    draw_square(2, (0, 50, 0)) #nyrad 
    draw_square(3, (0, 0, 50)) #nyrad
    draw_square(4, (50, 50, 0)) #nyrad

    # etc.
```

## Timer
Siffrorna blinkar varje sekund.

En timervariabel börjar vid 0 och ökar med `dt` för varje bildruta.

När timern är på eller över 1 återställs den till 0.

Till en början skriver vi 'tick' varje gång siffrorna blinkar.

```python3
def reset():
    # etc.
    global timer

    # etc.
    timer = 0

def update(dt):
    global timer

    timer += dt
    if timer >= 1:
        timer = 0
        # Temporary
        print('tick')
```
✏️ Uppdatera och testkör koden.

## Blinkande rutor
Den aktuella sekvenspositionen återanvänds för att blinka varje ruta i sekvensen.

Timern används för att flytta fram den aktuella sekvenspositionen.

För närvarande ritas kvadraten som motsvarar siffran vid den aktuella sekvenspositionen med sin färg, medan de andra rutorna är ritade i svart.

Testsekvensen från tidigare används igen.

Detta kommer bli fel när `current` är större än längden av `sequence`.

```python3
def reset():
    # etc.

    sequence = [4, 3, 1, 2, 2, 3] # Tillfälligt

def update(dt):
    global timer
    global current #nyrad

    timer += dt
    if timer >= 1:
        timer = 0
        current += 1 #nyrad

def draw():
    screen.fill((0, 0, 0))

    def draw_square(number, color):
        if number == sequence[current]: #nyrad
            square_color = color #nyrad
        else: #nyrad
            square_color = (0, 0, 0) #nyrad

        square_size = 50
        screen.draw.filled_rect(
            Rect(square_size * (number - 1), 0, square_size, square_size),
            color=square_color #ändra
        )
        screen.draw.text(str(number), (square_size * (number - 1) + 21, 18))

    # etc.
```

![image](https://user-images.githubusercontent.com/4598641/225707453-d0919991-6a40-4803-b883-5e25e8a65d25.png)

## Blinkande färg
Vi ger rutorna varsin färg.

```python3
def draw():
    screen.fill((0, 0, 0))

    def draw_square(number, color, color_flashing): #uppdatera

        if number == sequence[current]:
            square_color = color_flashing #uppdatera
        else:
            square_color = color #uppdatera

        square_size = 50
        screen.draw.filled_rect(
            Rect(square_size * (number - 1), 0, square_size, square_size),
            color=square_color
        )
        screen.draw.text(str(number), (square_size * (number - 1) + 21, 18))

    draw_square(1, (50, 0, 0), (255, 0, 0)) #uppdatera
    draw_square(2, (0, 50, 0), (0, 255, 0)) #uppdatera
    draw_square(3, (0, 0, 50), (0, 0, 255)) #uppdatera
    draw_square(4, (50, 50, 0), (255, 255, 0)) #uppdatera

    # etc.
```

https://simplegametutorials.github.io/pygamezero/repeat/7.png

## Titta och upprepa
En variabel skapas som indikerar om rutorna blinkar, `watch`, eller om spelaren matar in siffror, `repeat`.

Tillståndet börjar som `watch` och ändras till `repeat` efter att den blinkande sekvensen har avslutats.

Koden för att läsa av tangentbordet körs bara när tillståndet är `repeat`.

När sekvensen väl har angetts, ändras tillståndet tillbaka till `watch`.

```python3
def reset():
    global state

    # etc.

    state = 'watch' # 'watch', 'repeat'

def update(dt):
    global timer
    global current
    global state

    if state == 'watch': #nyrad
        timer += dt
        if timer >= 1:
            timer = 0
            current += 1
            if current == len(sequence): #nyrad
                state = 'repeat' #nyrad
                current = 0 #nyrad

def on_key_down(key):
    global current
    global state #nyrad

    if state == 'repeat': #nyrad
        if key in (keys.K_1, keys.K_2, keys.K_3, keys.K_4):

            if key == keys.K_1:
                number = 1
            elif key == keys.K_2:
                number = 2
            elif key == keys.K_3:
                number = 3
            elif key == keys.K_4:
                number = 4

            if number == sequence[current]:
                current += 1
                if current == len(sequence):
                    current = 0
                    add_to_sequence()
                    state = 'watch' #nyrad
            else:
                reset()

def draw():
    screen.fill((0, 0, 0))

    def draw_square(number, color, color_flashing):

        if state == 'watch' and number == sequence[current]: #ändra
            square_color = color_flashing
        else:
            square_color = color

    # etc.

    screen.draw.text('state: ' + state, (20, 180)) #nyrad
```

![image](https://user-images.githubusercontent.com/4598641/225708386-2c6b9be1-c195-4ef3-98a5-a2300828e5b5.png)

## Tillfälligt blinkande
En boolesk variabel (False/True) används för att indikera om den markerade färgen ska ställas in eller inte.

Från början är variabeln False. Den sätts till True när timern tickar. Nästa gång timern tickar sätts den till False, och så vidare.

Timergränsen ändras till att ticka dubbelt så snabbt.

```python3
def reset():
    # etc.
    global flashing #nyrad

    # etc.
    flashing = False #nyrad

def update(dt):
    global timer
    global current
    global state
    global flashing #nyrad

    if state == 'watch':
        timer += dt
        if timer >= 0.5: #ändra
            timer = 0
            flashing = not flashing #nyrad
            if not flashing: #nyrad
                current += 1
                if current == len(sequence):
                    state = 'repeat'
                    current = 0

def draw():
    screen.fill((0, 0, 0))

    def draw_square(number, color, color_flashing):

        if state == 'watch' and flashing and number == sequence[current]: #ändra
            square_color = color_flashing
        else:
            square_color = color

    # etc.

    screen.draw.text('flashing: ' + str(flashing), (20, 220)) #ändra
```


## Game over-läge

Om du trycker på fel tangent sätts tillståndet till `gameover`, istället för att återställa spelet meddetsamma. 
När en tangent trycks ned i "gameover"-tillståndet återställs spelet.

```python
def on_key_down(key):
    global current
    global state

    if state == 'repeat':
        if key in (keys.K_1, keys.K_2, keys.K_3, keys.K_4):
            # etc.

            if number == sequence[current]:
                # etc.
            else:
                state = 'gameover' nyrad
    elif state == 'gameover': nyrad
        reset()
```        
       
## Visa text baserat på tillstånd
Den aktuella sekvenspositionen och längden på sekvensen visas bara när vi är i "upprepa"-läget. 
Ett game over-meddelande visas om spelet är i "gameover"-läget.

```python
def draw():
    # etc.

    if state == 'repeat': #nyrad
        screen.draw.text(str(current + 1) + '/' + str(len(sequence)), (20, 60))
    elif state == 'gameover': #nyrad
        screen.draw.text('Game over!', (20, 60)) #nyrad

    #borttagen: screen.draw.text('sequence[current]: ' + str(sequence[current]), (20, 100))
    #borttagen: screen.draw.text(', '.join(map(str, sequence)), (20, 140))
    #borttagen: screen.draw.text('state: ' + state, (20, 180))
    #borttagen: screen.draw.text('flashing: ' + str(flashing), (20, 220))
```


![image](https://user-images.githubusercontent.com/4598641/225709496-d75bd7ca-c901-420c-9c7d-a381dec241bb.png)



# Källor
Översatt till svenska och anpassad till repl.it baserat på https://simplegametutorials.github.io/pygamezero/repeat/