# Repeat ⭐⭐⭐

### En handledning för Python och Pygame Zero 1.2

![image](https://user-images.githubusercontent.com/4598641/225698865-f394ffdb-6b0c-4731-8763-915c93b7b965.png)

### Innehåll
**[Regler för minnesspelet Repeat](#regler-för-minnesspelet-repeat)** &bull;
**[Kodning](#kodning)**
   [Sekvens](#sekvens)
  &bull; [Nuvarande position i sekvensen](#nuvarande-position-i-sekvensen)
  &bull; [Återställ aktuell position](#återställ-aktuell-position)
  &bull; [Lägg till nästa tal att komma ihåg i sekvensen](#lägg-till-nästa-tal-att-komma-ihåg-i-sekvensen)
  &bull; [Startsekvens med ett enda tal](#startsekvens-med-ett-enda-tal)
  &bull; [Återställa spelet](#återställa-spelet)
  &bull; [Rita första rutan](#rita-första-rutan)
  &bull; [Rita alla rutor](#rita-alla-rutor)
  &bull; [Förenkla koden](#förenkla-koden)
  &bull; [Timer](#timer)
  &bull; [Blinkande rutor](#blinkande-rutor)
  &bull; [Blinkande färg](#blinkande-färg)
  &bull; [Se och upprepa](#se-och-upprepa)
  &bull; [Tillfälligt blinkande](#tillfälligt-blinkande)
  &bull; [Game over-läge](#game-over-läge)
  &bull; [Visa text baserat på vilket läge vi är i](#visa-text-baserat-på-vilket-läge-vi-är-i)
&bull;
**[Uppgifter](#uppgifter)** &bull; **[Källor](#källor)**

## Jobba så här
Vägen till ett färdigt projekt är en pusselbit i taget 🧩. Gör därför ett avsnitt i taget uppifrån och ner.
- Få det att fungera innan ni går vidare till nästa avsnitt. 
- Testkör ofta, efter varje avsnitt eller ännu oftare.

Var det något i beskrivningen som var svårt att förstå? Ta med det i redovisningen. 📝

# Regler för minnesspelet Repeat
Se på när en siffersekvens blinkar och försök att komma ihåg ordningen på siffrorna.

Upprepa sekvensen med sifferknapparna.

Om du lyckas upprepa sekvensen läggs ett nytt tal till i slutet. Sen blinkar sekvensen igen.

# Kodning

## Sekvens
Vi skapar sekvenslistan. Till en början innehåller den en testsekvens med siffrorna 1 och 4.

```python
import pgzrun

# Variabler här nedanför
sequence = [4, 3, 1, 2, 2, 3] # Tillfälligt

# Funktioner här nedanför
def draw(): # ritar om skärmen
    screen.fill((0, 0, 0))
    screen.draw.text(', '.join(map(str, sequence)), (0, 0))

# Kod för att starta vår app här nedanför
pgzrun.go() # Ska alltid vara sist i programmet (längst ner)
```

![image](https://user-images.githubusercontent.com/4598641/225699441-a8ba2e0d-516c-42e0-8bbf-c062e783aee5.png)

✏️ Se till att du är inloggad i repl.it. Öppna startprojektet i repl.it: https://replit.com/@RobertStorlind/repeat-starter

Klicka på Fork för att spara en egen kopia. ![image](https://user-images.githubusercontent.com/4598641/225977081-1f9710c5-58cb-4b25-adb9-0f435fd6a1ed.png)


## Nuvarande position i sekvensen
Den aktuella sekvenspositionen börjar vid 1.

Om spelaren trycker på knappen som motsvarar siffran i sekvensen vid den aktuella positionen, ökar vi positionen med 1.

Detta blir fel när den aktuella positionen är större än längden på sekvenslistan. Vi rättar strax den buggen 🐛

✏️ Uppdatera din kod så att den blir som här nedanför och testkör den. Du måste inte mata in kommentarerna &ndash; de förklarar vad koden gör.

Klicka i terminalfönstret. Skriv sen 4 3 1 2 2 3 och se hur skärmen uppdateras. Vad händer om du fortsätter trycka fler siffror?

```python
import pgzrun

sequence = [4, 3, 1, 2, 2, 3] # Tillfälligt
current = 0 #nyrad

def on_key_down(key): # Pygame Zero anropar denna när något händer
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


![image](https://user-images.githubusercontent.com/4598641/225703318-26fb8e5b-9d98-4a9d-b740-fc220f938125.png)

## Återställ aktuell position

När den aktuella positionen överskrider sekvenslängden återställer vi den till 0.

✏️ Uppdatera koden i `on_key_down()` och testkör igen. Vad händer om du skriver många siffror nu?

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

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun

sequence = [4, 3, 1, 2, 2, 3]  # Tillfälligt
current = 0  # nyrad


def on_key_down(key):  # Pygame Zero anropar denna när något händer
    global current  # För att vi ska kunna uppdatera variabeln current som är utanför funktionen

    if key in (keys.K_1, keys.K_2, keys.K_3, keys.K_4):  # siffertangenterna 1, 2, 3, 4
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
            if current == len(sequence):  # nyrad
                current = 0  # nyrad


def draw():
    screen.fill((0, 0, 0))

    screen.draw.text(', '.join(map(str, sequence)), (0, 0))
    screen.draw.text(f"{current + 1}/{len(sequence)}", (0, 20))  # nyrad
    screen.draw.text(
        f"sequence[current]: {sequence[current]}", (0, 40))  # nyrad


pgzrun.go()  # Ska alltid vara sist i programmet (längst ner)
```    

</details>

## Lägg till nästa tal att komma ihåg i sekvensen

När den aktuella positionen återställs läggs ett slumptal mellan 1 och 4 till i sekvensen.

Vi behöver importera modulen `random` så att vi kan få slumptal från `random.randint`.

```python
import random # Lägg till högst upp bland importerna

# Uppdatera funktionen
def on_key_down(key):
    # etc.
            if current == len(sequence):
                current = 0
                sequence.append(random.randint(1, 4)) #nyrad
```
✏️ Uppdatera och testkör koden. 
>Du ser facit överst på skärmen och en ny siffra läggs till varje gång du matat in alla siffrorna i sekvensen.

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import random

sequence = [4, 3, 1, 2, 2, 3]  # Tillfälligt
current = 0  # nyrad


def on_key_down(key):  # Pygame Zero anropar denna när något händer
    global current  # För att vi ska kunna uppdatera variabeln current som är utanför funktionen

    if key in (keys.K_1, keys.K_2, keys.K_3, keys.K_4):  # siffertangenterna 1, 2, 3, 4
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
            if current == len(sequence):  # nyrad
                current = 0  # nyrad
                sequence.append(random.randint(1, 4)) #nyrad


def draw():
    screen.fill((0, 0, 0))

    screen.draw.text(', '.join(map(str, sequence)), (0, 0))
    screen.draw.text(f"{current + 1}/{len(sequence)}", (0, 20))  # nyrad
    screen.draw.text(
        f"sequence[current]: {sequence[current]}", (0, 40))  # nyrad


pgzrun.go()  # Ska alltid vara sist i programmet (längst ner)
```    

</details>

## Startsekvens med ett enda tal

Nu skapar vi en riktig sekvens, till en början med ett enda slumptal.

Eftersom koden för att lägga till ett slumptal till sekvensen återanvänds, gör vi den till en funktion, `add_to_sequence()`.

```python
sequence = [] # Ändra detta högst upp

# Lägg till funktionen
def add_to_sequence():
    sequence.append(random.randint(1, 4))

# etc.

def on_key_down(key):
    # etc.

            if current == len(sequence):
                current = 0
                add_to_sequence() # ersätt raden som var här

add_to_sequence() # lägg till som näst sista rad
pgzrun.go()
```

✏️ Uppdatera koden och testkör den genom att mata in siffror. 
>Glöm inte att klicka i terminalfönstret

<details>
    <summary>Så här kan koden se ut nu:</summary>

```python
import pgzrun
import random

# Globala variabler här nedanför
sequence = [4, 3, 1, 2, 2, 3]  # Tillfälligt
current = 0  # nyrad

# Funktioner här nedanför
def add_to_sequence():
    sequence.append(random.randint(1, 4))

def on_key_down(key):  # Pygame Zero anropar denna när något händer
    global current  # För att vi ska kunna uppdatera variabeln current som är utanför funktionen

    if key in (keys.K_1, keys.K_2, keys.K_3, keys.K_4):  # siffertangenterna 1, 2, 3, 4
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
            if current == len(sequence):  # nyrad
                current = 0  # nyrad
                add_to_sequence()


def draw():
    screen.fill((0, 0, 0))

    screen.draw.text(', '.join(map(str, sequence)), (0, 0))
    screen.draw.text(f"{current + 1}/{len(sequence)}", (0, 20))  # nyrad
    screen.draw.text(
        f"sequence[current]: {sequence[current]}", (0, 40))  # nyrad

# Till slut kod för att starta vår app

add_to_sequence()
pgzrun.go()  # Ska alltid vara sist i programmet (längst ner)
```
</details>
    
## Återställa spelet

Vi skapar en funktion som ställer in spelets startläge.

Denna funktion ska vi anropa innan spelet börjar och också när en felaktig siffertangent trycks ned.

```python
# Funktioner här nedanför
def add_to_sequence():
    sequence.append(random.randint(1, 4))

def reset(): #nyrad
    global sequence #nyrad
    global current #nyrad

    sequence = [] #nyrad
    add_to_sequence() #nyrad
    current = 0 #nyrad

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
# etc.

# Kod för att starta vår app
reset() # ändra
pgzrun.go()  # Ska alltid vara sist i programmet (längst ner)

```
✏️ Uppdatera din kod och testkör.


<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import random

# Globala variabler här nedanför
sequence = [4, 3, 1, 2, 2, 3]  # Tillfälligt
current = 0  # nyrad

# Funktioner här nedanför


def add_to_sequence():
    sequence.append(random.randint(1, 4))


def reset():  # nyrad
    global sequence  # nyrad
    global current  # nyrad

    sequence = []  # nyrad
    add_to_sequence()  # nyrad
    current = 0  # nyrad


def on_key_down(key):  # Pygame Zero anropar denna när något händer
    global current  # För att vi ska kunna uppdatera variabeln current som är utanför funktionen

    if key in (keys.K_1, keys.K_2, keys.K_3, keys.K_4):  # siffertangenterna 1, 2, 3, 4
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
            if current == len(sequence):  # nyrad
                current = 0  # nyrad
                add_to_sequence()
        else:
            reset()


def draw():
    screen.fill((0, 0, 0))

    screen.draw.text(', '.join(map(str, sequence)), (0, 0))
    screen.draw.text(f"{current + 1}/{len(sequence)}", (0, 20))  # nyrad
    screen.draw.text(
        f"sequence[current]: {sequence[current]}", (0, 40))  # nyrad


# Till slut kod för att starta vår app
reset()
pgzrun.go()  # Ska alltid vara sist i programmet (längst ner)
```    

</details>


## Rita första rutan

Den första rutan är mörkröd med en vit siffra.

✏️ Uppdatera funktionen `draw()` och testkör. Ritas rutan med rätt färg?

```python
def draw():
    screen.fill((0, 0, 0))

    square_size = 50 #nyrad

    screen.draw.filled_rect( #nyrad
        Rect(0, 0, square_size, square_size), #nyrad
        color=(50, 0, 0) #nyrad
    ) #nyrad
    screen.draw.text('1', (19, 18)) #nyrad

    screen.draw.text(", ".join(map(str, sequence)), (20, 60)) #ändra
    screen.draw.text(f"{current + 1}/{len(sequence)}", (20, 100))  #ändra
    screen.draw.text(f"sequence[current]: {sequence[current]}", (20, 140))  #ändra
```

![image](https://user-images.githubusercontent.com/4598641/225725617-e4af967f-5de4-4edd-9293-2ba5268b2215.png)

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import random

# Globala variabler här nedanför
sequence = [4, 3, 1, 2, 2, 3]  # Tillfälligt
current = 0  # nyrad

# Funktioner här nedanför


def add_to_sequence():
    sequence.append(random.randint(1, 4))


def reset():  # nyrad
    global sequence  # nyrad
    global current  # nyrad

    sequence = []  # nyrad
    add_to_sequence()  # nyrad
    current = 0  # nyrad


def on_key_down(key):  # Pygame Zero anropar denna när något händer
    global current  # För att vi ska kunna uppdatera variabeln current som är utanför funktionen

    if key in (keys.K_1, keys.K_2, keys.K_3, keys.K_4):  # siffertangenterna 1, 2, 3, 4
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
            if current == len(sequence):  # nyrad
                current = 0  # nyrad
                add_to_sequence()
        else:
            reset()


def draw():
    screen.fill((0, 0, 0))

    square_size = 50  # nyrad

    screen.draw.filled_rect(  # nyrad
        Rect(0, 0, square_size, square_size),  # nyrad
        color=(50, 0, 0)  # nyrad
    )  # nyrad
    screen.draw.text('1', (19, 18))  # nyrad

    screen.draw.text(", ".join(map(str, sequence)), (20, 60))  # ändra
    screen.draw.text(f"{current + 1}/{len(sequence)}", (20, 100))  # ändra
    screen.draw.text(
        f"sequence[current]: {sequence[current]}", (20, 140))  # ändra


# Till slut kod för att starta vår app
reset()
pgzrun.go()  # Ska alltid vara sist i programmet (längst ner)
```    

</details>

## Rita alla rutor
Resten av rutorna kan vi rita på liknande sätt.

✏️ Uppdatera funktionen `draw()` igen och testkör att rutorna har rätt färg för resp. siffra.

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

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import random

# Globala variabler här nedanför
sequence = [4, 3, 1, 2, 2, 3]  # Tillfälligt
current = 0  # nyrad

# Funktioner här nedanför


def add_to_sequence():
    sequence.append(random.randint(1, 4))


def reset():  # nyrad
    global sequence  # nyrad
    global current  # nyrad

    sequence = []  # nyrad
    add_to_sequence()  # nyrad
    current = 0  # nyrad


def on_key_down(key):  # Pygame Zero anropar denna när något händer
    global current  # För att vi ska kunna uppdatera variabeln current som är utanför funktionen

    if key in (keys.K_1, keys.K_2, keys.K_3, keys.K_4):  # siffertangenterna 1, 2, 3, 4
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
            if current == len(sequence):  # nyrad
                current = 0  # nyrad
                add_to_sequence()
        else:
            reset()


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
    screen.draw.text(", ".join(map(str, sequence)), (20, 60))  # ändra
    screen.draw.text(f"{current + 1}/{len(sequence)}", (20, 100))  # ändra
    screen.draw.text(
        f"sequence[current]: {sequence[current]}", (20, 140))  # ändra


# Till slut kod för att starta vår app
reset()
pgzrun.go()  # Ska alltid vara sist i programmet (längst ner)
```    

</details>

## Förenkla koden
Koden för att rita varje ruta är likadan. 
Vi flyttar den koden till funktionen `draw_square()` som vi kan använda flera gånger.

✏️ Uppdatera funktionen `draw()` så att den blir så här. Testkör att det fungerar som innan vi förbättrade koden!

```python
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

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import random

# Globala variabler här nedanför
sequence = [4, 3, 1, 2, 2, 3]  # Tillfälligt
current = 0  # nyrad

# Funktioner här nedanför


def add_to_sequence():
    sequence.append(random.randint(1, 4))


def reset():  # nyrad
    global sequence  # nyrad
    global current  # nyrad

    sequence = []  # nyrad
    add_to_sequence()  # nyrad
    current = 0  # nyrad


def on_key_down(key):  # Pygame Zero anropar denna när något händer
    global current  # För att vi ska kunna uppdatera variabeln current som är utanför funktionen

    if key in (keys.K_1, keys.K_2, keys.K_3, keys.K_4):  # siffertangenterna 1, 2, 3, 4
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
            if current == len(sequence):  # nyrad
                current = 0  # nyrad
                add_to_sequence()
        else:
            reset()


def draw():
    screen.fill((0, 0, 0))

    def draw_square(number, color):  # ändra
        square_size = 50
        screen.draw.filled_rect(
            Rect(square_size * (number - 1), 0,
                 square_size, square_size),  # ändra
            color=color  # ändra
        )
        screen.draw.text(str(number), (square_size *
                         (number - 1) + 21, 18))  # ändra

    draw_square(1, (50, 0, 0))  # nyrad
    draw_square(2, (0, 50, 0))  # nyrad
    draw_square(3, (0, 0, 50))  # nyrad
    draw_square(4, (50, 50, 0))  # nyrad
    screen.draw.text(", ".join(map(str, sequence)), (20, 60))  # ändra
    screen.draw.text(f"{current + 1}/{len(sequence)}", (20, 100))  # ändra
    screen.draw.text(
        f"sequence[current]: {sequence[current]}", (20, 140))  # ändra


# Till slut kod för att starta vår app
reset()
pgzrun.go()  # Ska alltid vara sist i programmet (längst ner)
```    

</details>

## Timer
Siffrorna ska blinka varje sekund.

En timervariabel börjar vid 0 och ökar med `dt` för varje bildruta. 
>Variabeln `dt` talar om hur länge sen det var vi körde `update()` senast.

När timern är 1 eller mer, återställs den till 0.

Till en början skriver vi 'tick' varje gång siffrorna blinkar.

```python3
timer = 0 # lägg till uppe bland variablerna

def reset():
    # etc.
    global timer # lägg till

    # etc.
    timer = 0 #lägg till

# Lägg till den här funktionen
def update(dt): # anropas 60 gånger i sekunden av Pygame
    global timer

    timer += dt
    if timer >= 1:
        timer = 0
        # Temporary
        print("tick")
```
✏️ Uppdatera och testkör koden. Ser du utskriften i terminalfönstret i repl.it?

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import random

# Globala variabler här nedanför
sequence = [4, 3, 1, 2, 2, 3]  # Tillfälligt
current = 0  # nyrad
timer = 0

# Funktioner här nedanför


def add_to_sequence():
    sequence.append(random.randint(1, 4))


def reset():  # nyrad
    global sequence, current, timer

    sequence = []  # nyrad
    add_to_sequence()  # nyrad
    current = 0  # nyrad
    timer = 0


def update(dt):  # anropas 60 gånger i sekunden av Pygame
    global timer

    timer += dt
    if timer >= 1:
        timer = 0
        # Temporary
        print("tick")


def on_key_down(key):  # Pygame Zero anropar denna när något händer
    global current  # För att vi ska kunna uppdatera variabeln current som är utanför funktionen

    if key in (keys.K_1, keys.K_2, keys.K_3, keys.K_4):  # siffertangenterna 1, 2, 3, 4
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
            if current == len(sequence):  # nyrad
                current = 0  # nyrad
                add_to_sequence()
        else:
            reset()


def draw():
    screen.fill((0, 0, 0))

    def draw_square(number, color):  # ändra
        square_size = 50
        screen.draw.filled_rect(
            Rect(square_size * (number - 1), 0,
                 square_size, square_size),  # ändra
            color=color  # ändra
        )
        screen.draw.text(str(number), (square_size *
                         (number - 1) + 21, 18))  # ändra

    draw_square(1, (50, 0, 0))  # nyrad
    draw_square(2, (0, 50, 0))  # nyrad
    draw_square(3, (0, 0, 50))  # nyrad
    draw_square(4, (50, 50, 0))  # nyrad
    screen.draw.text(", ".join(map(str, sequence)), (20, 60))  # ändra
    screen.draw.text(f"{current + 1}/{len(sequence)}", (20, 100))  # ändra
    screen.draw.text(
        f"sequence[current]: {sequence[current]}", (20, 140))  # ändra


# Till slut kod för att starta vår app
reset()
pgzrun.go()  # Ska alltid vara sist i programmet (längst ner)
```    

</details>

## Blinkande rutor
Den aktuella sekvenspositionen återanvänds för att blinka varje ruta i sekvensen.

Timern används för att flytta fram den aktuella sekvenspositionen.

För närvarande ritas kvadraten som motsvarar siffran vid den aktuella sekvenspositionen med sin färg, medan de andra rutorna är ritade i svart.

Testsekvensen från tidigare används igen.

Detta kommer bli fel när `current` är större än längden på `sequence`, alltså listan med siffror.

✏️ Uppdatera och testkör koden. En ruta i taget ska ha färgmarkering. Funkar det?

```python3
def reset():
    # etc.

    sequence = [4, 3, 1, 2, 2, 3] # Tillfälligt

def update(dt):
    global timer, current #ändra

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

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import random

# Globala variabler här nedanför
sequence = [4, 3, 1, 2, 2, 3]  # Tillfälligt
current = 0  # nyrad
timer = 0

# Funktioner här nedanför


def add_to_sequence():
    sequence.append(random.randint(1, 4))


def reset():  # nyrad
    global sequence, current, timer

    sequence = []  # nyrad
    add_to_sequence()  # nyrad
    current = 0  # nyrad
    timer = 0


def update(dt):  # anropas 60 gånger i sekunden av Pygame
    global timer, current

    timer += dt
    if timer >= 1:
        timer = 0


def on_key_down(key):  # Pygame Zero anropar denna när något händer
    global current  # För att vi ska kunna uppdatera variabeln current som är utanför funktionen

    if key in (keys.K_1, keys.K_2, keys.K_3, keys.K_4):  # siffertangenterna 1, 2, 3, 4
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
            if current == len(sequence):  # nyrad
                current = 0  # nyrad
                add_to_sequence()
        else:
            reset()


def draw():
    screen.fill((0, 0, 0))

    def draw_square(number, color):
        if number == sequence[current]:  # nyrad
            square_color = color  # nyrad
        else:  # nyrad
            square_color = (0, 0, 0)  # nyrad

        square_size = 50
        screen.draw.filled_rect(
            Rect(square_size * (number - 1), 0, square_size, square_size),
            color=square_color  # ändra
        )
        screen.draw.text(str(number), (square_size * (number - 1) + 21, 18))

    draw_square(1, (50, 0, 0))  # nyrad
    draw_square(2, (0, 50, 0))  # nyrad
    draw_square(3, (0, 0, 50))  # nyrad
    draw_square(4, (50, 50, 0))  # nyrad
    screen.draw.text(", ".join(map(str, sequence)), (20, 60))  # ändra
    screen.draw.text(f"{current + 1}/{len(sequence)}", (20, 100))  # ändra
    screen.draw.text(
        f"sequence[current]: {sequence[current]}", (20, 140))  # ändra


# Till slut kod för att starta vår app
reset()
pgzrun.go()  # Ska alltid vara sist i programmet (längst ner)
```    

</details>

## Blinkande färg
Vi ger rutorna varsin färg.

✏️ Uppdatera koden så här och testkör igen!

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

![image](https://simplegametutorials.github.io/pygamezero/repeat/7.png)

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import random

# Globala variabler här nedanför
sequence = [4, 3, 1, 2, 2, 3]  # Tillfälligt
current = 0  # nyrad
timer = 0

# Funktioner här nedanför


def add_to_sequence():
    sequence.append(random.randint(1, 4))


def reset():  # nyrad
    global sequence, current, timer

    sequence = []  # nyrad
    add_to_sequence()  # nyrad
    current = 0  # nyrad
    timer = 0


def update(dt):  # anropas 60 gånger i sekunden av Pygame
    global timer, current

    timer += dt
    if timer >= 1:
        timer = 0


def on_key_down(key):  # Pygame Zero anropar denna när något händer
    global current  # För att vi ska kunna uppdatera variabeln current som är utanför funktionen

    if key in (keys.K_1, keys.K_2, keys.K_3, keys.K_4):  # siffertangenterna 1, 2, 3, 4
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
            if current == len(sequence):  # nyrad
                current = 0  # nyrad
                add_to_sequence()
        else:
            reset()


def draw():
    screen.fill((0, 0, 0))

    def draw_square(number, color, color_flashing):  # uppdatera

        if number == sequence[current]:
            square_color = color_flashing  # uppdatera
        else:
            square_color = color  # uppdatera

        square_size = 50
        screen.draw.filled_rect(
            Rect(square_size * (number - 1), 0, square_size, square_size),
            color=square_color
        )
        screen.draw.text(str(number), (square_size * (number - 1) + 21, 18))

    draw_square(1, (50, 0, 0), (255, 0, 0))  # uppdatera
    draw_square(2, (0, 50, 0), (0, 255, 0))  # uppdatera
    draw_square(3, (0, 0, 50), (0, 0, 255))  # uppdatera
    draw_square(4, (50, 50, 0), (255, 255, 0))  # uppdatera
    screen.draw.text(", ".join(map(str, sequence)), (20, 60))  # ändra
    screen.draw.text(f"{current + 1}/{len(sequence)}", (20, 100))  # ändra
    screen.draw.text(
        f"sequence[current]: {sequence[current]}", (20, 140))  # ändra


# Till slut kod för att starta vår app
reset()
pgzrun.go()  # Ska alltid vara sist i programmet (längst ner)
```    

</details>

## Se och upprepa
Vi skapar en variabel som håller reda på om rutorna blinkar, `watch`, eller om spelaren matar in siffror, `repeat`.

Tillståndet börjar som `watch` och ändras till `repeat` efter att den blinkande sekvensen har avslutats.

Koden för att läsa av tangentbordet körs bara när tillståndet är `repeat`.

När spelaren har matat in rätt sekvens, ändras tillståndet tillbaka till `watch`.

✏️ Uppdatera koden och testa igen!

```python
state = 'watch' # lägg till uppe bland variablerna

# etc.

def reset():
    global state
    # etc.
    state = 'watch' # 'watch', 'repeat'

def update(dt):
    global timer, current, state

    if state == 'watch': #nyrad
        timer += dt
        if timer >= 1:
            timer = 0
            current += 1
            if current == len(sequence): #nyrad
                state = 'repeat' #nyrad
                current = 0 #nyrad

def on_key_down(key):
    global current, state #ändra

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

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import random

# Globala variabler här nedanför
sequence = [4, 3, 1, 2, 2, 3]  # Tillfälligt
current = 0  # nyrad
timer = 0
state = 'watch'

# Funktioner här nedanför


def add_to_sequence():
    sequence.append(random.randint(1, 4))


def reset():  # nyrad
    global sequence, current, timer, state

    sequence = []  # nyrad
    add_to_sequence()  # nyrad
    current = 0  # nyrad
    timer = 0
    state = 'watch'

    
def update(dt):  # anropas 60 gånger i sekunden av Pygame
    global timer, current, state

    if state == 'watch':  # nyrad
        timer += dt
        if timer >= 1:
            timer = 0
            current += 1
            if current == len(sequence):  # nyrad
                state = 'repeat'  # nyrad
                current = 0  # nyrad


def on_key_down(key):  # Pygame Zero anropar denna när något händer
    global current, state

    if state == 'repeat':  # nyrad
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
                    state = 'watch'  # nyrad
            else:
                reset()


def draw():
    screen.fill((0, 0, 0))

    def draw_square(number, color, color_flashing):  # uppdatera
        if state == 'watch' and number == sequence[current]:  # ändra
            square_color = color_flashing
        else:
            square_color = color

        square_size = 50
        screen.draw.filled_rect(
            Rect(square_size * (number - 1), 0, square_size, square_size),
            color=square_color
        )
        screen.draw.text(str(number), (square_size * (number - 1) + 21, 18))

    draw_square(1, (50, 0, 0), (255, 0, 0))  # uppdatera
    draw_square(2, (0, 50, 0), (0, 255, 0))  # uppdatera
    draw_square(3, (0, 0, 50), (0, 0, 255))  # uppdatera
    draw_square(4, (50, 50, 0), (255, 255, 0))  # uppdatera
    screen.draw.text(", ".join(map(str, sequence)), (20, 60))  # ändra
    screen.draw.text(f"{current + 1}/{len(sequence)}", (20, 100))  # ändra
    screen.draw.text(
        f"sequence[current]: {sequence[current]}", (20, 140))  # ändra
    screen.draw.text('state: ' + state, (20, 180))  # nyrad


# Till slut kod för att starta vår app
reset()
pgzrun.go()  # Ska alltid vara sist i programmet (längst ner)
```    

</details>

## Tillfälligt blinkande
En boolesk variabel (False/True) används för att hålla reda på om den markerade färgen ska ställas in eller inte.

Från början är variabeln False. Den sätts till True när timern tickar. Nästa gång timern tickar sätts den till False, och så vidare.

Timergränsen ändras till att ticka dubbelt så snabbt.

✏️ Uppdatera din kod och testa igen!

```python
flashing = False # lägg till uppe bland variablerna

def reset():
    # etc.
    global flashing #nyrad

    # etc.
    flashing = False #nyrad

def update(dt):
    global timer, current, state, flashing

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

    screen.draw.text('state: ' + state, (20, 180))
    screen.draw.text(f"flashing: {flashing}", (20, 220)) # nyrad
```

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import random

# Globala variabler här nedanför
sequence = [4, 3, 1, 2, 2, 3]  # Tillfälligt
current = 0  # nyrad
timer = 0
state = 'watch'
flashing = False

# Funktioner här nedanför


def add_to_sequence():
    sequence.append(random.randint(1, 4))


def reset():  # nyrad
    global sequence, current, timer, state, flashing

    sequence = []  # nyrad
    add_to_sequence()  # nyrad
    current = 0  # nyrad
    timer = 0
    state = 'watch'
    flashing = False

    
def update(dt):  # anropas 60 gånger i sekunden av Pygame
    global timer, current, state, flashing

    if state == 'watch':  # nyrad
        timer += dt
        if timer >= 0.5:
            timer = 0
            flashing = not flashing
            if not flashing:
                current += 1
                if current == len(sequence):  # nyrad
                    state = 'repeat'  # nyrad
                    current = 0  # nyrad


def on_key_down(key):  # Pygame Zero anropar denna när något händer
    global current, state

    if state == 'repeat':  # nyrad
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
                    state = 'watch'  # nyrad
            else:
                reset()


def draw():
    screen.fill((0, 0, 0))

    def draw_square(number, color, color_flashing):  # uppdatera
        # ändra
        if state == 'watch' and flashing and number == sequence[current]:
            square_color = color_flashing
        else:
            square_color = color

        square_size = 50
        screen.draw.filled_rect(
            Rect(square_size * (number - 1), 0, square_size, square_size),
            color=square_color
        )
        screen.draw.text(str(number), (square_size * (number - 1) + 21, 18))

    draw_square(1, (50, 0, 0), (255, 0, 0))  # uppdatera
    draw_square(2, (0, 50, 0), (0, 255, 0))  # uppdatera
    draw_square(3, (0, 0, 50), (0, 0, 255))  # uppdatera
    draw_square(4, (50, 50, 0), (255, 255, 0))  # uppdatera
    screen.draw.text(", ".join(map(str, sequence)), (20, 60))  # ändra
    screen.draw.text(f"{current + 1}/{len(sequence)}", (20, 100))  # ändra
    screen.draw.text(
        f"sequence[current]: {sequence[current]}", (20, 140))  # ändra
    screen.draw.text('state: ' + state, (20, 180))  # nyrad
    screen.draw.text(f"flashing: {flashing}", (20, 220))


# Till slut kod för att starta vår app
reset()
pgzrun.go()  # Ska alltid vara sist i programmet (längst ner)
```    

</details>


## Game over-läge

Om spelaren trycker på fel tangent, sätts tillståndet till `gameover`, istället för att återställa spelet meddetsamma. 

När en tangent trycks ned i "gameover"-tillståndet återställs spelet.

✏️ Vi är nästan klara! Uppdatera din kod och testkör igen. Fungerar game over som det ska?

```python
def on_key_down(key):
    global current, state

    if state == 'repeat':
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
                    state = 'watch'  # nyrad
            else: # nyrad
                state = 'gameover' # nyrad
        elif state == 'gameover': # ändra indrag
            reset() # ändra indrag
```        

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import random

# Globala variabler här nedanför
sequence = [4, 3, 1, 2, 2, 3]  # Tillfälligt
current = 0  # nyrad
timer = 0
state = 'watch'
flashing = False

# Funktioner här nedanför


def add_to_sequence():
    sequence.append(random.randint(1, 4))


def reset():  # nyrad
    global sequence, current, timer, state, flashing

    sequence = []  # nyrad
    add_to_sequence()  # nyrad
    current = 0  # nyrad
    timer = 0
    state = 'watch'
    flashing = False


def update(dt):  # anropas 60 gånger i sekunden av Pygame
    global timer, current, state, flashing

    if state == 'watch':  # nyrad
        timer += dt
        if timer >= 0.5:
            timer = 0
            flashing = not flashing
            if not flashing:
                current += 1
                if current == len(sequence):  # nyrad
                    state = 'repeat'  # nyrad
                    current = 0  # nyrad


def on_key_down(key):  # Pygame Zero anropar denna när något händer
    global current, state

    if state == 'repeat':
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
                    state = 'watch'  # nyrad
            else:
                state = 'gameover'
        elif state == 'gameover':  # nyrad
            reset()


def draw():
    screen.fill((0, 0, 0))

    def draw_square(number, color, color_flashing):  # uppdatera
        # ändra
        if state == 'watch' and flashing and number == sequence[current]:
            square_color = color_flashing
        else:
            square_color = color

        square_size = 50
        screen.draw.filled_rect(
            Rect(square_size * (number - 1), 0, square_size, square_size),
            color=square_color
        )
        screen.draw.text(str(number), (square_size * (number - 1) + 21, 18))

    draw_square(1, (50, 0, 0), (255, 0, 0))  # uppdatera
    draw_square(2, (0, 50, 0), (0, 255, 0))  # uppdatera
    draw_square(3, (0, 0, 50), (0, 0, 255))  # uppdatera
    draw_square(4, (50, 50, 0), (255, 255, 0))  # uppdatera
    screen.draw.text(", ".join(map(str, sequence)), (20, 60))  # ändra
    screen.draw.text(f"{current + 1}/{len(sequence)}", (20, 100))  # ändra
    screen.draw.text(
        f"sequence[current]: {sequence[current]}", (20, 140))  # ändra
    screen.draw.text('state: ' + state, (20, 180))  # nyrad
    screen.draw.text(f"flashing: {flashing}", (20, 220))


# Till slut kod för att starta vår app
reset()
pgzrun.go()  # Ska alltid vara sist i programmet (längst ner)
```    

</details>

## Visa text baserat på vilket läge vi är i

Den aktuella sekvenspositionen och längden på sekvensen visas bara när vi är i *upprepa*-läget. 

Ett game over-meddelande visas om spelet är i *gameover*-läget.

✏️ Uppdatera slutet av funktionen `draw()` så att den blir så här. Ta bort raderna som är markerade med "# borttagen". Testkör och se om det stämmer med beskrivningen här uppe!

```python
def draw():
    # etc.
    
    draw_square(1, (50, 0, 0), (255, 0, 0))  # uppdatera
    draw_square(2, (0, 50, 0), (0, 255, 0))  # uppdatera
    draw_square(3, (0, 0, 50), (0, 0, 255))  # uppdatera
    draw_square(4, (50, 50, 0), (255, 255, 0))  # uppdatera
    if state == 'repeat':
        screen.draw.text(f"{current + 1}/{len(sequence)}",
                         (20, 60))
    elif state == 'gameover':
        screen.draw.text("Game over!", (20, 60))
    
    #borttagen: screen.draw.text('sequence[current]: ' + str(sequence[current]), (20, 100))
    #borttagen: screen.draw.text(', '.join(map(str, sequence)), (20, 140))
    #borttagen: screen.draw.text('state: ' + state, (20, 180))
    #borttagen: screen.draw.text('flashing: ' + str(flashing), (20, 220))
```


![image](https://user-images.githubusercontent.com/4598641/225709496-d75bd7ca-c901-420c-9c7d-a381dec241bb.png)

<details>
    <summary>📝 Så här kan koden se ut nu</summary>

```python
import pgzrun
import random

# Globala variabler här nedanför
sequence = [4, 3, 1, 2, 2, 3]  # Tillfälligt
current = 0  # nyrad
timer = 0
state = 'watch'
flashing = False

# Funktioner här nedanför

def add_to_sequence():
    sequence.append(random.randint(1, 4))

def reset():  # nyrad
    global sequence, current, timer, state, flashing

    sequence = []  # nyrad
    add_to_sequence()  # nyrad
    current = 0  # nyrad
    timer = 0
    state = 'watch'
    flashing = False


def update(dt):  # anropas 60 gånger i sekunden av Pygame
    global timer, current, state, flashing

    if state == 'watch':  # nyrad
        timer += dt
        if timer >= 0.5:
            timer = 0
            flashing = not flashing
            if not flashing:
                current += 1
                if current == len(sequence):  # nyrad
                    state = 'repeat'  # nyrad
                    current = 0  # nyrad


def on_key_down(key):  # Pygame Zero anropar denna när något händer
    global current, state

    if state == 'repeat':
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
                    state = 'watch'  # nyrad
            else:
                state = 'gameover'
        elif state == 'gameover':  # nyrad
            reset()


def draw():
    screen.fill((0, 0, 0))

    def draw_square(number, color, color_flashing):  # uppdatera
        # ändra
        if state == 'watch' and flashing and number == sequence[current]:
            square_color = color_flashing
        else:
            square_color = color

        square_size = 50
        screen.draw.filled_rect(
            Rect(square_size * (number - 1), 0, square_size, square_size),
            color=square_color
        )
        screen.draw.text(str(number), (square_size * (number - 1) + 21, 18))

    draw_square(1, (50, 0, 0), (255, 0, 0))  # uppdatera
    draw_square(2, (0, 50, 0), (0, 255, 0))  # uppdatera
    draw_square(3, (0, 0, 50), (0, 0, 255))  # uppdatera
    draw_square(4, (50, 50, 0), (255, 255, 0))  # uppdatera
    if state == 'repeat':
        screen.draw.text(f"{current + 1}/{len(sequence)}",
                         (20, 60))
    elif state == 'gameover':
        screen.draw.text("Game over!", (20, 60))


# Till slut kod för att starta vår app
reset()
pgzrun.go()  # Ska alltid vara sist i programmet (längst ner)
```    

</details>

# Uppgifter

## 1. Utvärdera ert eget arbete!
När ni svarar på detta, tänk er att *ni har tillgång till uppgiften* &ndash; ni behöver alltså inte kunna koden utantill.

A. De här delarna av uppgiften har vi gjort. Vi förstår dem och kan förklara koden för Susanne eller inför klassen.

B. De här delarna av uppgiften har vi gjort *men vi förstår dem inte till 100%*. Ge exempel på något ni inte förstår.

## 2. Pröva att göra några ändringar eller tillägg, t.ex. High Score
- Beskriv kort vad förändringen är och hur den ska fungera.
- Beskriv hur du fick ändra koden för att göra ändringen.
- Om det inte gick att genomföra, förklara med några meningar vad du försökte och vad som hände. Glöm inte kodexempel

### High Score
Lägg till en variabel för High Score. Visa den på skärmen

### Gör spelet snyggare grafiskt
Vad skulle göra spelet ännu bättre grafiskt?

# Källor
Översatt till svenska och anpassad till repl.it baserat på https://simplegametutorials.github.io/pygamezero/repeat/
