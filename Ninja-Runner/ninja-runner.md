**Navigering:** [Infinite Runner](#infinite-runner) &bull;
[Bakgrund](#bakgrund) &bull;
[Ninjan](#ninjan) &bull;
[Hoppa](#hoppa) &bull;
[Hinder](#hinder) &bull;
[Poängräkning](#poängräkning) &bull;
[Game Over](#game-over) &bull;
[Utmaningar och buggar](#utmaningar-och-buggar) &bull;
[Källor](#källor)

# Infinite Runner

![image](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/google-runner.gif)

Ett spel av typen Infinite/Endless Runner tar aldrig slut. Målet är att överleva så långt som möjligt och ju längre, desto högre poäng får du.

För att göra vårt spel ska vi använda vad vi lärt oss från spelet Gem Catcher och lägga till
- ritning
- animering
- fysik
- listor med figurer (aktörer).

## Nytt projekt
Börja med göra en egen kopia av startprojektet i repl.it: FIXA:LÄNK

# Bakgrund
## Första steget
Precis som i Gem Catcher börjar vi koda vårt spel genom att

- importera Pygame Zero
- sätta grafikfönstrets bredd och höjd
- anropa `pgzrun.go()`
```python
import pgzrun

WIDTH=800
HEIGHT=600

pgzrun.go() # Måste vara sista raden
```
Spara ditt projekt i din egen repl.it.

## Rita
Vi kan rika olika figurer med hjälp av funktionerna i `screen.draw`. Vi har tidigare använt `screen.draw.text()` men det finns många fler funktioner, som till exempel

- `screen.draw.line()`
- `screen.draw.circle()`
- `screen.draw.filled_circle()`
- `screen.draw.rect()`
- `screen.draw.filled_rect()`
För att lära mer om de funktionerna kan du läsa i [dokumentationen för Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/builtins.html#screen).

För tillfället ska vi bara använda `screen.draw.filled_rect()`. Den ritar en rektangel på skärmen, så vi behöver lägga till anropet i funktionen `draw()`.
```python
import pgzrun

WIDTH=800
HEIGHT=600

def draw():
  screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT - 200), (163, 232, 254))

pgzrun.go() # Måste vara sista raden
```

Det här gör de nya raderna:

`def draw():` : Det här är ritfunktionen som Pygame Zero kör med jämna mellanrum. Allt som ritar på skärmen ska vara inuti den här funktionen.

`screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT - 200), (163, 232, 254)` : Detta ritar en rektangel på skärmen med övre vänstra hörnet (0, 0), en bredd på WIDTH (800) och en höjd på HEIGHT - 200 (400). Färgen är en blandning av 163 delar röd, 232 grön och 254 blå.

**Testa att experimentera med olika färger och se vad du får. Kom ihåg att varje färgkomponent ska vara mellan 0 och 255.**

## Marken
Steget innan ritade himlen. Vi lägger till en andra rektangel för att rita marken.

```python
import pgzrun

WIDTH=800
HEIGHT=600

def draw():
  screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT - 200), (163, 232, 254))
  screen.draw.filled_rect(Rect(0, HEIGHT - 200, WIDTH, 200), (88, 242, 152))

pgzrun.go() # Måste vara sista raden
```
Det här gör den nya raden:

`screen.draw.filled_rect(Rect(0, HEIGHT - 200, WIDTH, 200), (88, 242, 152))` : Den här gången börjar rektangeln 200 pixlar ovanför underkanten, alltså x=0 and y=400, om du inte ändrat på WIDTH och HEIGHT vilket du kan vilja göra. Vi har räknat med att marken behöver 200 pixlar.

Mata in detta och kör din kod. Din skärm bör se ut så här:

![image](https://user-images.githubusercontent.com/4598641/223218919-66ee7ecf-043f-4c08-a775-074ff487bb3c.png)

# Ninjan

## Animering
I Scratch kan du animera dina sprajtar genom att ändra klädseln. I Pygame Zero gör vi det genom att byta bild. Ett sätt att göra det på är så här:

```python
def update():
    if runner.image == 'run__000':
      runner.image == 'run__001'
    elif runner.image == 'run__001':
      runner.image == 'run__002'
    elif runner.image == 'run__002':
      runner.image == 'run__000'
```

Detta kollar vad den aktuella bilden är och byter till nästa. Det fungerar men är mer besvärligt än i Scratch. Som hjälp kan vi använda modulen [Pygame Zero Helper](https://www.aposteriori.com.sg/pygame-zero-helper), som redan är med i startprojektet.

## Modulen Pygame Zero Helper

```python
import pgzrun
from pgzhelper import *

WIDTH=800
HEIGHT=600

def draw():
  screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT - 200), (163, 232, 254))
  screen.draw.filled_rect(Rect(0, HEIGHT - 200, WIDTH, 200), (88, 242, 152))

pgzrun.go() # Måste vara sista raden
```

Sparar och kör din kod för att se att allt fungerar som det ska.

## Ninjabilder
Det finns redan ett antal ninjabilder förberedda i startprojektet. De ligger i mappen *images*.

![image](https://user-images.githubusercontent.com/4598641/223219964-a4109c3b-04be-4793-a600-dba2c386f297.png)

**Andra sätt: Det finns flera uppsättningar av bilder med springande figurer du kan använda. Testa 'dino', 'knight' eller 'zombies'.**

## Programmera ninjan

Vi lägger till ninjan i vårt spel så här:

```python
runner = Actor('run__000')
run_images = ['run__000', 'run__001', 'run__002', 'run__003', 'run__004', 'run__005', 'run__006', 'run__007', 'run__008', 'run__009']
runner.images = run_images
```

Det här gör de olika raderna:

`runner = Actor('run__000')` : This creates a new Actor using the first run image. It's the same as what we have done in our gem catcher game.

`run_images = ['run__000', 'run__001', 'run__002', 'run__003', 'run__004', 'run__005', 'run__006', 'run__007', 'run__008', 'run__009']` : This creates a new list in the variable run_images. The list is filled with the names of the run images. If you are not using the ninja, you will need to change these names.

`runner.images = run_images` : This tells our Actor to use the images in run_images for its animation.

We'll also need to add runner.draw() into the draw() function. Once completed, your program should look like this...

```python
import pgzrun
from pgzhelper import *

WIDTH=800
HEIGHT=600

runner = Actor('run__000')
run_images = ['run__000', 'run__001', 'run__002', 'run__003', 'run__004', 'run__005', 'run__006', 'run__007', 'run__008', 'run__009']
runner.images = run_images

def draw():
  screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT - 200), (163, 232, 254))
  screen.draw.filled_rect(Rect(0, HEIGHT - 200, WIDTH, 200), (88, 242, 152))
  runner.draw()

pgzrun.go() # Måste vara sista raden
```

Det ska få ninjan att synas på skärmen, men den springer inte än! Lägg till det i `update`-funktionen så här:

```python
def update():
  runner.next_image()
```
Detta talar om för Pygame Zero att byta till nästa bild varje gång den uppdaterar. Med detta ska du nu ha en springande ninja!

### Justera placeringen

Du kan justera ninjas placering med `runner.x` och `runner.y`. Pröva detta:

```python
runner.x = 100
runner.y = HEIGHT - 200
```
**Pröva att justera ninjans position genom att ändra `runner.x` och `runner.y` tills hon är där du vill.**

# Hoppa

## Fysik

Vilken av de här ser mest realistisk ut?

![image](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/jump.gif)

I verkliga livet påverkas föremål av gravitationen. För att få vår ninja att hoppa realistiskt, behöver vi simulera gravitationens effekter i vårt spel.

Vi börjar med att lägga till variabler för `velocity_y` och `gravity`, alltså hastigheten i y-led och gravitationen.

```python
velocity_y = 0
gravity = 1
```

Förklaring av kodraderna:

`velocity_y = 0` : Håller reda på hur snabbt ninjan ska röra sig uppåt eller neråt. Hastigheten börjar med 0 eftersom ninjan inte hoppar än.

`gravity = 1` : Gravitationen påverkar hastigheten. Vi kan ändra detta senare och se effekten av det, men just nu låter vi värdet vara 1. 

I `update()` ska vi sen ändra hastigheten när uppåtpilen trycks ner.

```python
def update():
  global velocity_y
  runner.next_image()

  if keyboard.up:
    velocity_y = -15

  runner.y += velocity_y
```

Det här gör raderna:

`global velocity_y` : Vi behöver använda `global` om vi ändrar på en variabel som finns utanför funktionen.

`if keyboard.up:` : När tangenten med uppåtpil trycks ner &ldots;

`velocity_y = -15` : Sätt hastigheten upp/ner till &ndash;15. Ett negativt värde betyder att den rör sig uppåt.

`runner.y += velocity_y` :  Ändra vår ninjas position baserat på hastigheten. Operatorn `+=` betyder att vi ökar `runner.y` med värdet i `velocity_y`.

# Tips
```python
a += 1      # Den här raden gör samma sak som ...
a = a + 1   # ... den här raden.
```

Testa det! Om du programmerat rätt, bör ninjan flyga upp i himlen när du trycker uppåtpil. Det är för att vi inte har lagt till någon gravitation än!

## Gravitation
Graviationen ändrar ninjans hastighet. 
Under raden `runner.y += velocity_y` lägger vi till gravitionen med `velocity_y += gravity`.

Nu ramlar vår ninja rakt ner! Vi har inte talat om för ninjan när den ska sluta falla! Vi lägger till det nu:

```python
if runner.y > HEIGHT - 200:
  velocity_y = 0
  runner.y = HEIGHT - 200
```
Här bestämmer vi att `HEIGHT - 200` är där marken börjar och om ninjan är på en y-koordinat som är större än `HEIGHT - 200` så sätter vi hennes `velocity_y` till 0 och y-koordinaten till `HEIGHT - 200`. Detta hindrar att hon faller igenom marken.

Ditt program bör nu se ut så här:
```python
import pgzrun
from pgzhelper import *

WIDTH=800
HEIGHT=600

runner = Actor('run__000')
run_images = ['run__000', 'run__001', 'run__002', 'run__003', 'run__004', 'run__005', 'run__006', 'run__007', 'run__008', 'run__009']
runner.images = run_images
runner.x = 100
runner.y = HEIGHT - 200

velocity_y = 0
gravity = 1

def update():
  global velocity_y
  runner.next_image()

  if keyboard.up:
    velocity_y = -15

  runner.y += velocity_y
  velocity_y += gravity
  if runner.y > HEIGHT - 200:
    velocity_y = 0
    runner.y = HEIGHT - 200

def draw():
  screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT - 200), (163, 232, 254))
  screen.draw.filled_rect(Rect(0, HEIGHT - 200, WIDTH, 200), (88, 242, 152))
  runner.draw()

pgzrun.go() # Måste vara sista raden
```

# Hinder
## En lista med figurer

I vårt Gem Catcher-spel har vi bara en ädelsten i taget och den flyttar sig till toppen av skärmen varje gång vi fångar den.
I vårt ninjaspel kommer vi att flera hinder på skärmen samtidigt.
För att klara det behöver vi använda **listor**.

![image](https://user-images.githubusercontent.com/4598641/223222660-26ee39e0-5420-47ba-8ef9-d4cb855636fe.png)

Först skapar vi en tom lista som heter `obstacles` och en heltalsvariabel `obstacles_timeout`.

```python
obstacles = []
obstacles_timeout = 0
```
I vår funktion `update()` ska vi räkna upp `timeout` med 1 varje gång.
```python
obstacles_timeout += 1
```
Och om `timeout` är större än 50 lägger vi till ett hinder och sätter `timeout` till 0.

```python
if obstacles_timeout > 50:
  actor = Actor('cactus')
  actor.x = WIDTH + 50
  actor.y = HEIGHT - 170
  obstacles.append(actor)
  obstacles_timeout = 0
```

Det enda nya här är `obstacles.append(actor)`. Det lägger till figuren `actor` i hinderlistan, `obstacles`.

**VIKTIGT: Du behöver ha bilden med kaktusen i mappen images. Om du vill använda en annan bild, glöm inte att byta bildnamnet i koden också.**

För att få hindren att röra sig över skärmen:
```python
for actor in obstacles:
  actor.x -= 8
```
Detta går igenom hela listan `obstacles` och minskar x-koordinaten för varje hinder. Att minska *x* gör att hindret rör sig åt vänster.

Till slut behöver vi rita hindren på skärmen. Lägg till det här i `draw()`-funktionen:
```python
for actor in obstacles:
  actor.draw()
```

Nu ska ditt program se ut ungefär så här:

```python
import pgzrun
from pgzhelper import *

WIDTH=800
HEIGHT=600

runner = Actor('run__000')
run_images = ['run__000', 'run__001', 'run__002', 'run__003', 'run__004', 'run__005', 'run__006', 'run__007', 'run__008', 'run__009']
runner.images = run_images
runner.x = 100
runner.y = HEIGHT - 200

velocity_y = 0
gravity = 1

obstacles = []
obstacles_timeout = 0

def update():
  global velocity_y, obstacles_timeout
  runner.next_image()

  obstacles_timeout += 1
  if obstacles_timeout > 50:
    actor = Actor('cactus')
    actor.x = 850
    actor.y = 430
    obstacles.append(actor)
    obstacles_timeout = 0

  for actor in obstacles:
    actor.x -= 8

  if keyboard.up:
    velocity_y = -15

  runner.y += velocity_y
  velocity_y += gravity
  if runner.y > HEIGHT - 200:
    velocity_y = 0
    runner.y = HEIGHT - 200

def draw():
  screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT - 200), (163, 232, 254))
  screen.draw.filled_rect(Rect(0, HEIGHT - 200, WIDTH, 200), (88, 242, 152))
  runner.draw()
  for actor in obstacles:
    actor.draw()

pgzrun.go() # Måste vara sista raden
```

# Poängräkning

## Poängen

Precis som i Gem Catcher, använder vi en variabel `score` för att hållra reda på vår poängställning.

```python
score = 0
```
Vi ökar poängen varje gång ett hinder försvinner ut åt vänster. Ändra det här inuti `update()`, från
```python
  for actor in obstacles:
    actor.x -= 8
```
... till detta: .
```python
  for actor in obstacles:
    actor.x -= 8
    if actor.x < -50:
      obstacles.remove(actor)
      score += 1
```
Detta är vad raderna betyder:

`if actor.x < -50` : När x-koordinaten är mindre än &ndash;50 är figuren förmodligen utanför skärmen. Då kommer vi att ...

`obstacles.remove(actor)` : ta bort figuren från listan `obstacles` och sen

`score += 1` : öka poängen med 1. Kom ihåg att deklarera `score` som global variabel!

## Rita hinder och skriva ut poängen
Hindren ritas inte om vi glömmer att göra det i `draw()`. Så vi lägger till detta:
```python
for actor in obstacles:
  actor.draw()
```
Det går igenom listan med hinder och ritar dem ett i taget.

Vi behöver också visa poängen på skärmen så här:

```python
screen.draw.text(f"Score: {score}", (15, 10), color=(0,0,0), fontsize=30)
```
Ändra gärna färg, placering eller teckenstorleken.


# Game Over
Just nu gör spelet inget även om vår ninja krockar med kaktusen. Vi lägger till ett game over-läge. Om ninjan rör något av hindren så avslutar vi spelet.

Först lägger vi till en variabel `game_over` och sätter den till `False` i början.

```python
game_over = False
```
Inuti funktionen `update()` ska vi upptäckte om vår ninja har krockat med något av hindren. Om hon gjorde det så sätter vi `game_over` till `True`.

```python
if runner.collidelist(obstacles) != -1:
  game_over = True
```
**Viktigt: kom ihåg att deklarera `game_over` som global i funktionen `update()`.

Frågan `runner.collidelist(obstacles)` kollar om ninjan har krockat med något av hindren i listan `obstacles`.
Om hon inte gjorde det, ger funktionen `collidelist` värdet &ndash;1.

Sen behöver vi skriva texten "Game over" inuti `draw()` genom att ändra från
```python
  runner.draw()
  for actor in obstacles:
    actor.draw()
  screen.draw.text(f"Score: {score}", (15, 10), color=(0,0,0), fontsize=30)
.. till
```python
if game_over:
  screen.draw.text('Game Over', centerx=WIDTH/2, centery=HEIGHT - 330, color=(255, 255, 255), fontsize=60)
  screen.draw.text(f"Score: {score}", centerx=WIDTH/2, centery=330, color=(255, 255, 255), fontsize=60)
else:
  runner.draw()
  for actor in obstacles:
    actor.draw()
  screen.draw.text(f"Score: {score}", (15, 10), color=(0, 0, 0), fontsize=30)
```

Ditt spel bör se ut så här till slut:

```python
import pgzrun
from pgzhelper import *

WIDTH=800
HEIGHT=600

runner = Actor('run__000')
run_images = ['run__000', 'run__001', 'run__002', 'run__003', 'run__004', 'run__005', 'run__006', 'run__007', 'run__008', 'run__009']
runner.images = run_images
runner.x = 100
runner.y = HEIGHT - 200

velocity_y = 0
gravity = 1

obstacles = []
obstacles_timeout = 0

score = 0
game_over = False

def update():
  global velocity_y, obstacles_timeout, score, game_over
  runner.next_image()

  obstacles_timeout += 1
  if obstacles_timeout > 50:
    actor = Actor('cactus')
    actor.x = WIDTH + 50
    actor.y = HEIGHT - 170
    obstacles.append(actor)
    obstacles_timeout = 0

  for actor in obstacles:
    actor.x -= 8
    if actor.x < -50:
      obstacles.remove(actor)
      score += 1

  if keyboard.up:
    velocity_y = -15

  runner.y += velocity_y
  velocity_y += gravity
  if runner.y > HEIGHT - 200:
    velocity_y = 0
    runner.y = HEIGHT - 200

  if runner.collidelist(obstacles) != -1:
    game_over = True

def draw():
  screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT - 200), (163, 232, 254))
  screen.draw.filled_rect(Rect(0, HEIGHT - 200, WIDTH, 200), (88, 242, 152))
  if game_over:
    screen.draw.text('Game Over', centerx=WIDTH/2, centery=HEIGHT - 330, color=(255, 255, 255), fontsize=60)
    screen.draw.text(f"Score: {score}", centerx=WIDTH/2, centery=330, color=(255, 255, 255), fontsize=60)
  else:
    runner.draw()
    for actor in obstacles:
      actor.draw()
    screen.draw.text(f"Score: {score}", (15, 10), color=(0, 0, 0), fontsize=30)

pgzrun.go() # Måste vara sista raden
```

# Utmaningar och buggar
## Fixa buggar!
It is common for programs to have bugs. I've deliberately left a few bugs in our ninja runner game. Have you spotted any? Try fixing them!

Bug Fix 1. Game Over Score
Play the game, let your ninja touch a cactus, then watch the score carefully after game over... Did you see the score continue to increase? That happens because after game over, we are still adding cactuses to the obstacles list. Can you fix this?

Bug Fix 2. Multi-Jumps
Try quickly pressing the jump button multiple times. Did your ninja jump out of the screen? Our ninja should only be able to jump when she is on the ground, and not when she is in the air. Can you fix this?

## Challenges!
Here are some challenges to make the game better.

### Challenge 1. Gliding Ninja
Can you change the ninja image to a gliding ninja whenever she jumps? If you are using a different character, most of them will have a jumping image that you can use.

![image](https://user-images.githubusercontent.com/4598641/223225545-64334e74-b6e3-4511-8f25-8128512012d8.png)
![image](https://user-images.githubusercontent.com/4598641/223225411-f124b452-0956-44a9-bbe2-1e9936c87552.png)
![image](https://user-images.githubusercontent.com/4598641/223225445-7663895c-45e2-4237-95c4-7dfaef60d46f.png)


### Challenge 2. Different obstacles
The only obstacle we have now is the cactus. Can you make the program randomly select a different type of obstacle each time?

![image](https://user-images.githubusercontent.com/4598641/223225610-600aa71d-9f7d-4d51-bc0d-745b8442470b.png)
![image](https://user-images.githubusercontent.com/4598641/223225631-7523def5-ca93-4bb9-a7d1-df6ad8b6e06c.png)
![image](https://user-images.githubusercontent.com/4598641/223225654-7930549a-1186-4d7e-8ae7-572e8670cd5d.png)

### Challenge 3. Spacing out
In the current game, the obstacles always appear at the same distance away from each other. Can you randomize this, so that sometimes the obstacles will be closer and at other times further apart.

# Källor
Projektet är en översättning och anpassning till repl.it av originalet på https://aposteriori.trinket.io/game-development-with-pygame-zero#/ninja-runner/infinite-runner

This is a Swedish translation and repl.it adaptation of https://aposteriori.trinket.io/game-development-with-pygame-zero#/ninja-runner/infinite-runner
