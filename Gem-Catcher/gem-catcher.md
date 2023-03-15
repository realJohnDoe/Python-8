[Första koden](#första-koden) &bull;
[Funktionen update()](#funktionen-update) &bull;
[Lägga till en ädelsten](#lägga-till-en-ädelsten) &bull;
[Kollision och random()](#kollision-och-random) &bull;
[Räkna poäng](#räkna-poäng) &bull;
[Mus och händelser](#mus-och-händelser) &bull;
[Game Over](#game-over) &bull;
[Utmaningar](#utmaningar)

# Första koden

✏️ Se till att vara inloggad i repl.it. Öppna startprojektet här i repl.it: https://replit.com/@RobertStorlind/gem-catcher-starter

Spara en egen kopia med knappen **Fork**.

Skelettet för ett Pygame Zero-program ser ut så här:
```python
import pgzrun

WIDTH, HEIGHT = 800, 600

pgzrun.go() # Måste vara sista raden
```

Den första raden, `import pgzrun`, hämtar Pygame Zero-modulen och den sista raden, `pgzrun.go()`, är funktionen som startar Pygame Zero. 
I mitten har vi `WIDTH = 800` och `HEIGHT = 600` som sätter spelfönstrets bredd och höjd.

# Figuren (Actor)
Det var inte så spännande, så vi lägger till ett rymdskepp.
För att göra det behöver ha en bild för rymdskeppet.

Du kan använda vilka bilder du vill men för att göra livet enklare för dig, är startprojektet i repl.it förberett med en bild.
Bilden med rymdskeppet behöver ligger i mappen **images** i projektet. 

![image](https://user-images.githubusercontent.com/4598641/222978313-4661f08c-e673-40be-87be-5fa1d8d06de8.png)

>**Frivilligt:** Det finns andra bilder om du vill byta. Ladda ner ZIP-arkivet, packa upp och ladda sen upp önskad bild till ditt projekt.
>Här finns ZIP-arkivet med bilder: https://www.aposteriori.com.sg/wp-content/uploads/2020/02/image_pack.zip.
>**Obs!** Bildens filnamn kan bara innehålla små bokstäver, siffror och understrykning `_`.

✏️ Nu ska du lägga till rymdskeppet till ditt Pythonprogram.

```python
import pgzrun

WIDTH, HEIGHT = 800, 600

ship = Actor('playership1_blue')
ship.x = WIDTH / 2 - 30
ship.y = HEIGHT - 50

def draw():
    ship.draw()

pgzrun.go() # Måste vara sista raden
```

Detta är vad raderna gör:

`ship = Actor('playership1_blue')` : Skapar en ny figur (Actor) med utseende enligt filen *playership1_blue*. Om du använder en annan bildfil behöver du ändra namnet här.

`ship.x = WIDTH / 2 - 30` : Sätter skeppets x-position till att vara ungefär mitt på x-axeln. Pröva att ändra värdet!

`ship.y = HEIGHT - 50` : Sätter skeppets y-position till en bit ovanför undre kanten. Pröva att ändra värdet!

`def draw():` : Detta är en specialfunktion. Vi behöver inte anropa den själva; Pygamze Zero kör den åt oss när det behövs.

`ship.draw()` : Talar om för skeppets Actor att rita sig på skärmen. Koden behöver vara indragen under `def draw():` så att den körs när Pygame Zero anropar funktionen `draw()`.

![image](https://user-images.githubusercontent.com/4598641/222978372-85be8781-e6fe-414e-9fb1-b7847dfc8b5f.png)

# Funktionen update()

Vi la till funktionen `draw()` innan. Det är en speciell funktion som Pygame Zero kör regelbundet för att rita det du ser på skärmen. En annan speciell funktion är `update()`. Pygame Zero anrop regelbundet vår `update()`-funktion för att uppdatera/rita om de olika figurerna i spelet.

✏️ Vi lägger till kod i `update()` så att den kan reagera på tangentnertryckningar, i vårt fall vänster- och högerpil.

```python
import pgzrun

WIDTH, HEIGHT = 800, 600

ship = Actor('playership1_blue')
ship.x = WIDTH / 2 - 30
ship.y = HEIGHT - 50

def update():
    if keyboard.left:
        ship.x -= 5
    if keyboard.right:
        ship.x += 5

def draw():
    ship.draw()

pgzrun.go() # Måste vara sista raden
```

Detta la vi till:
```python
def update():
    if keyboard.left:
        ship.x -= 5
    if keyboard.right:
        ship.x += 5
```
Varje gång Pygame Zero kör vår funktion `update()` kontrollerar den om vänsterpilen är nertryckt.
Om den är det, minskar vi rymdskeppets x-position med 5. Om högerpilen är nertryckt, ökar vi x med 5.

**Testa** programmet med gröna "Run"-knappen i repl.it. Funkar koden som du väntade dig?

## Radera skärmen

Om du testade programmet så här långt, fick du något knasigt i den här stilen:

![image](https://user-images.githubusercontent.com/4598641/222978681-7aa59c8e-4b41-49ae-8415-e5df0db6b51d.png)

Det är för att koden talar om för Pygame Zero att uppdatera skeppets position och rita det på skärmen, men vi bad aldrig om att sudda ut det som redan var ritat på skärmen.

✏️För att sudda skärmen, fyller vi hela skärmen med en färg. Det gör vi i `draw()`-funktionen så här:
```python
screen.fill((80, 0, 70))
```
Det som står inom parenteser, `(80, 0, 70)`, kallas i Python för *tuple*; det fungerar som en lista med värden som inte går att ändra och talar om vilken färgblandning vi vill ha. Det första talet (80) är för färgen rött, det andra (0) för grönt och det tredje (70) är för blått. Det största värdet man kan ha för någon färgkomponent är 255 och det minsta värdet är 0. **Testa olika värden och se vad du får!**

>**Frivilligt:**
>I Chrome kan du öppna en färgväljare genom att trycka tangentkombinationen ctrl+shift+I och sedan klicka på en av de små kvadratikonerna som du kan se i fliken Styles. Se bilden!

![image](https://user-images.githubusercontent.com/4598641/223195080-7bda1b3d-89e9-479a-bebe-936a332b1408.png)

Nu ska ditt program se ut så här:
```
import pgzrun

WIDTH, HEIGHT = 800, 600

ship = Actor('playership1_blue')
ship.x = WIDTH / 2 - 30
ship.y = HEIGHT - 50

def update():
    if keyboard.left:
        ship.x -= 5
    if keyboard.right:
        ship.x += 5

def draw():
    screen.fill((80, 0, 70))
    ship.draw()

pgzrun.go() # Måste vara sista raden
```

# Lägga till en ädelsten

Spelet kan ju inte heta *Gem Catcher* om det inte finns en ädelsten! Det finns redan en i startprojektet i mappen *images*.

![image](https://user-images.githubusercontent.com/4598641/222978860-59fdc056-ee3c-4d15-bca8-09b80051d3c9.png)

✏️ Lägg nu till en ny *Actor* som representerar ädelstenen:
```python
gem = Actor('gemgreen')
gem.x = WIDTH / 2 - 50
gem.y = 0
```
Det här värdet på x placerar den ungefär i mitten horisontellt. Att sätta y till 0 placerar den högst upp i fönstret. Glöm inte att också rita ädelstenen i funktionen `draw()`.

```python
gem.draw()
```

Din kod ska nu se ut så här:

```python
import pgzrun

WIDTH, HEIGHT = 800, 600

ship = Actor('playership1_blue')
ship.x = WIDTH / 2 - 30
ship.y = HEIGHT - 50

gem = Actor('gemgreen')
gem.x = WIDTH / 2 - 50
gem.y = 0

def update():
    if keyboard.left:
        ship.x -= 5
    if keyboard.right:
        ship.x += 5

def draw():
    screen.fill((80, 0, 70))
    gem.draw()
    ship.draw()

pgzrun.go() # Måste vara sista raden
```

## Flytta ädelstenen
Tidigare skrev vi kod i funktionen `update()` för att få skeppet att ändra x-position när vi trycker på vänster- eller högerpil.

Vi låter ädelstenen åka nerför skärmen genom att ändra y-positionen för den.

```python
gem.y += 4
```

Vi vill också att ädelstenen ska återgå till toppen av fönstret när den nått nedre kanten. För att göra det, sätter vi y-positionen till 0 (topp) när den är större än HEIGHT (underkanten).

```python
if gem.y > HEIGHT:
    gem.y = 0
```

✏️ Lägg till det i din kod!

```python
import pgzrun

WIDTH, HEIGHT = 800, 600

ship = Actor('playership1_blue')
ship.x = WIDTH / 2 - 30
ship.y = HEIGHT - 50

gem = Actor('gemgreen')
gem.x = WIDTH / 2 - 50
gem.y = 0

def update():
    if keyboard.left:
        ship.x -= 5
    if keyboard.right:
        ship.x += 5

    gem.y += 4
    if gem.y > HEIGHT:
        gem.y = 0

def draw():
    screen.fill((80, 0, 70))
    gem.draw()
    ship.draw()

pgzrun.go() # Måste vara sista raden
```

# Kollision och random()

## Känna av en kollision

Vi vill också att ädelstenen ska flytta högst upp om den rör rymdskeppet. Om du har använt Scratch tidigare, kanske du har använt blocket "rör vid sprajt".

I PygameZero använder vi antingen `if gem.colliderect(ship):` eller `if ship.colliderect(gem):` &ndash; båda fungerar likadant.

```python
if gem.colliderect(ship):
    gem.y = 0
```
eller

```python
if ship.colliderect(gem):
    gem.y = 0
```
**✏️ Testa det i din kod!**

## Slumptal med `random()`

Det är inte så spännande av låta ädelstenen falla från samma ställe varje gång.
I tidigare Python-projekt har du förmodligen redan använt modulen `random` för slumptal.
Här ska vi använda den för att slumpa fram ädelstenens x-position.

✏️ Innan vi kan använda modulen, behöver vi importera den.
```python
import random
```

✏️ För att ge ädelstenen en slumpmässig x-position använder vi
```python
gem.x = random.randint(20, WIDTH - 20)
```
Anropet `random.randint(20, WIDTH - 20)` ger ett slumptal mellan 20 och WIDTH - 20. Det här behövs varje gång ädelstenen ska börja om högst upp på skärmen.

Nu bör din kod se ut så här:
```python
import pgzrun

WIDTH, HEIGHT = 800, 600

ship = Actor('playership1_blue')
ship.x = WIDTH / 2 - 30
ship.y = HEIGHT - 50

gem = Actor('gemgreen')
gem.x = WIDTH / 2 - 50
gem.y = 0

def update():
    if keyboard.left:
        ship.x -= 5
    if keyboard.right:
        ship.x += 5

    gem.y += 4
    if gem.y > HEIGHT:
        gem.y = 0
    if gem.colliderect(ship):
        gem.x = random.randint(20, WIDTH - 20)
        gem.y = 0

def draw():
    screen.fill((80, 0, 70))
    gem.draw()
    ship.draw()

pgzrun.go() # Måste vara sista raden
```

# Räkna poäng

## En variabel som räknar poäng

Vi kan lätt hålla reda på poängen med en variabel.

✏️ Lägg till en variabel som heter `score` (poäng går också bra) och sätt den till 0 i början av programmet.

```python
score = 0
```
✏️ Nu ökar vi `score` med 1 varje gång rymdskeppet fångar ädelstenen.

```python
if gem.colliderect(ship):
    gem.x = random.randint(20, WIDTH - 20)
    gem.y = 0
    score += 1
```

Om du testkör programmet nu, får du ett fel:

```python
UnboundLocalError: local variable 'score' referenced before assignment
```

Det är för att variabeln `score` är deklarerad utanför funktionen `update()`, men vi försöker ändra värdet inne i funktionen `update()`.

✏️ I Python kan vi *läsa* variabler som finns utanför funktionen &ndash; de kallas globala variabler. Men vi kan inte skriva (ändra) dem om vi inte har deklarerat dem som `global` inuti funktionen.

```python
global score
```

Efter den ändringen, bör din `update()`-funktion se ut så här:
```python
def update():
    global score
    
    if keyboard.left:
        ship.x -= 5
    if keyboard.right:
        ship.x += 5

    gem.y += 4
    if gem.y > HEIGHT:
        gem.y = 0
    if gem.colliderect(ship):
        gem.x = random.randint(20, WIDTH - 20)
        gem.y = 0
        score += 1
```

## Visa poäng

✏️ För att visa poängen använder vi funktionen `screen.draw.text()`.

```python
screen.draw.text(f"Score: {score}", (15, 10), color=(255, 255, 255), fontsize=30)
```
Parametrarna är så här:

`f"Score: {score}"` : Detta är texten (strängen) vi vill skriva.

`(15, 10)` : Detta är koordinaterna där vi vill skriva: x=15 och y=10.

`color=(255, 255, 255)` : Detta är textens färg, vitt i det här fallet.

`fontsize=30` : Textens storlek.

Som med de andra ritfunktionerna, behöver vi lägga detta inuti funktionen `draw()`. När du har gjort det, bör din kod se ut så här:
```python
import pgzrun

WIDTH, HEIGHT = 800, 600

ship = Actor('playership1_blue')
ship.x = WIDTH / 2 - 30
ship.y = HEIGHT - 50

gem = Actor('gemgreen')
gem.x = WIDTH / 2 - 50
gem.y = 0
score = 0

def update():
    global score
    
    if keyboard.left:
        ship.x -= 5
    if keyboard.right:
        ship.x += 5

    gem.y += 4
    if gem.y > HEIGHT:
        gem.y = 0
    if gem.colliderect(ship):
        gem.x = random.randint(20, WIDTH - 20)
        gem.y = 0
        score += 1

def draw():
    screen.fill((80, 0, 70))
    gem.draw()
    ship.draw()
    screen.draw.text(f"Score: {score}", (15, 10), color=(255, 255, 255), fontsize=30)

pgzrun.go() # Måste vara sista raden
```

# Mus och händelser

## Musstyrning
Vi kan också ändra vårt spel så att det fungerar med mus.
Precis som Scratch så är Pygame Zero händelsebaserat.
Det betyder att när en viss händelse inträffar, t.ex. att en musknapp trycks ner, så anropar Pygame Zero motsvarande funktion, t.ex. `on_mouse_down`.

✏️ För att känna av när musen rör sig, kan vi använda funktionen `on_mouse_move(pos, rel, buttons)` function. Pröva att lägga till det här i ditt spel:

```
def on_mouse_move(pos, rel, buttons):
    ship.x = pos[0]
```

Syftet med tre parametrarna är:

`pos` : Ger muspositionen. Du kan få fram x-koordinaten med `pos[0]` och y-koordinaten med `pos[1]`.

`rel` : Ger förändringen i position sedan senaste gången musen förflyttades. `rel[0]` är ändringen i x-led och `rel[1]` förändringen i y-led.

`buttons` : Ger en lista med vilka musknappar som är nertryckta. Om du till exempel vill kolla om vänster musknapp är nertryckt:

```python
def on_mouse_move(pos, rel, buttons):
    if mouse.LEFT in buttons:
        print('left click')
```
**Detta är bara ett exempel. Lägg inte till det i ditt spel just nu**

## Andra händelser

Förutom musrörelser, finns det också andra funktioner som PygameZero kör när motsvarande händelse inträffar. De här händelserna finns:

`on_mouse_down(pos, buttons)` : Körs när en musknapp klickas på.

`on_mouse_up(pos, buttons)` : Körs när man släpper en musknapp.

Parametrar:
- `pos` : Ger musens position. x-koordinaten ges av `pos[0]` och y-koordinaten av `pos[1]`.
- `buttons` : Ger en lista med de musknapper som är nertryckta.

`on_key_down(key, mod, unicode)` : Körs när en tangent trycks ner på tangentbordet.

`on_key_up(key, mod)` : Körs när man släpper en tangent.

Parametrar:
- key : Ett heltal som talar om vilken tangent som trycktes ner. Se Pygame Zeros hemsida för en fullständig lista över tangenter.
- mod : En lista (bitmask) med vilka specialtangenter som trycktes ner. Du kan läsa av dem så här:

```python
def on_key_down(key, mod, unicode):
    if mod & keymods.LSHIFT:
        print('Left shift button pressed')
```

`unicode` : Vilket tecken som skrevs, om något. Du kan läsa av det så här:
```python
def on_key_down(key, mod, unicode):
    if unicode == 'e':
        print('e button pressed')
```


# Game Over
## Gör spelet svårare
Just nu är spelet för lätt.
Utan att skryta kan jag lätt få över 300 poäng utan ansträngning.
Vi gör det svårare genom att låta ädelstenen falla fortare ju högre poängen är.

✏️ Leta upp den här raden:
```python
gem.y += 4
```
och ändra den till
```python
gem.y += 4 + score / 5
```
Detta kommer att öka fallhastigheten när poängen går upp. När du har noll poäng, faller ädelstenen med hastighet 4. När din poäng är 10, kommer ädelstenen att falla med hastigheten 6 (4 + 10 / 5).


## Game Over
Det är inte så värst kul att spela ett spel som man inte kan förlora.
Vi lägger till ett Game Over-läge.
Om ädelstenen rör vi skärmens underkant, avslutas spelet.

✏️ Lägg först till en ny variabel som heter `game_over` och sätt den till `False`.

```python
game_over = False
```
Leta upp de här raderna i funktionen `update()`:
```python
if gem.y > HEIGHT:
    gem.x = random.randint(20, WIDTH - 20)
    gem.y = 0
```
och ändra dem till det här:
```python
if gem.y > HEIGHT:
    game_over = True
```
Detta sätter variabeln `game_over` till `True` om ädelstenen rör skärmens underkant.

Du behöver också lägga till `global game_over` högst upp i funktionen `update()`.
Minns du varför? Om inte, läs på under avsnittet [Räkna poäng](#räkna-poäng).

Inuti funktionen `draw()` ändrar du de här raderna:
```python
screen.fill((80, 0, 70))
gem.draw()
ship.draw()
screen.draw.text(f"Score: {score}", (15, 10), color=(255, 255, 255), fontsize=30)
```
Ändra dem till
```python
screen.fill((80, 0, 70))
if game_over:
    screen.draw.text("Game Over", (360, 300), color=(255, 255, 255), fontsize=60)
    screen.draw.text(f"Final Score: {score}", (360, 350), color=(255, 255, 255), fontsize=60)
else:
    gem.draw()
    ship.draw()
    screen.draw.text(f"Score: {score}", (15, 10), color=(255, 255, 255), fontsize=30)
```
Det gör att Game Over-texten visas när variabeln `game_over` är satt till True; annars kommer ädelstenen och skeppet att ritas som innan.

Till slut bör din kod se ut så här:
```python
import pgzrun

WIDTH, HEIGHT = 800, 600

ship = Actor('playership1_blue')
ship.x = WIDTH / 2 - 30
ship.y = HEIGHT - 50

gem = Actor('gemgreen')
gem.x = WIDTH / 2 - 50
gem.y = 0

score = 0
game_over = False

def on_mouse_move(pos, rel, buttons):
    ship.x = pos[0]
    
def update():
    global score, game_over
    
    if keyboard.left:
        ship.x -= 5
    if keyboard.right:
        ship.x += 5

    gem.y += 4
    if gem.y > HEIGHT:
        gem.y = 0
    if gem.colliderect(ship):
        gem.x = random.randint(20, WIDTH - 20)
        gem.y = 0
        score += 1

def draw():
    screen.fill((80, 0, 70))
    gem.draw()
    ship.draw()
    if game_over:
        screen.draw.text("Game Over", (360, 300), color=(255, 255, 255), fontsize=60)
        screen.draw.text(f"Final Score: {score}", (360, 350), color=(255, 255, 255), fontsize=60)
    else:
        gem.draw()
        ship.draw()
        screen.draw.text(f"Score: {score}", (15, 10), color=(255, 255, 255), fontsize=30)

pgzrun.go() # Måste vara sista raden
```

# Utmaningar

Här är några utmaningar du kan pröva för att göra spelet ännu bättre.

## Utmaning 1. Tre liv
Ändra spelet så att du har tre liv. Spelet ska sluta när spelaren använt alla tre liven.

## Utmaning 2. Olika ädelstenar
Det finns ädelstenar med flera olika färger i mediefilen (ZIP). Gör så att ädelstenar av olika färg kan dyka upp när den ska börja falla uppifrån

## Utmaning 3. Välja skepp

Mediefilen (ZIP) har flera olika slags rymdskepp. Fråga användaren vilket rymdskepp den vill ha när den ska spela.

## Utmaning 4. Flera ädelstenar
Just nu är det bara en fallande ädelsten åt gången. Ändra spelet så att flera kan falla samtidigt.

## Utmanming 5. Multi-player
Lägg till en andra spelare och tävla om vem som får högst poäng!

# Källor/Sources

Det här projektet är översatt och anpassat till repl.it baserat på https://aposteriori.trinket.io/game-development-with-pygame-zero#/gem-catcher/first-program

This project is a translated and adapted to repl.it from https://aposteriori.trinket.io/game-development-with-pygame-zero#/gem-catcher/first-program
