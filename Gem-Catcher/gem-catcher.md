[Första koden](#första-koden) &bull;
[Funktionen update()](#funktionen-update) &bull;
[Lägga till en ädelsten](#lägga-till-en-ädelsten) &bull;
[Kollision och random()](#kollision-och-random) &bull;
[Räkna poäng](#räkna-poäng) &bull;
[Mus och händelser](#mus-och-händelser) &bull;
[Game Over](#game-over) &bull;
[Utmaningar](#utmaningar)

# Första koden

Öppna startprojektet här i repl.it: FIXA:LÄNK

Skelettet för ett Pygame Zero-program ser ut så här:
```python
import pgzrun

WIDTH = 800
HEIGHT = 600

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

>Frivilligt: Det finns andra bilder om du vill byta. Ladda ner ZIP-arkivet, packa upp och ladda sen upp önskad bild till ditt projekt.
>[Här finns ZIP-arkivet med bilder](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/image_pack.zip).
>**Obs!** Bildens filnamn kan bara innehålla små bokstäver, siffror och understrykning `_`.

Nu ska du lägga till rymdskeppet till ditt Pythonprogram.

```python
import pgzrun

WIDTH = 800
HEIGHT = 600

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

Vi lägger till kod i `update()` så att den kan reagera på tangentnertryckningar, i vårt fall vänster- och högerpil.

```python
import pgzrun

WIDTH = 800
HEIGHT = 600

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

För att sudda skärmen, fyller vi hela skärmen med en färg. Det gör vi i `draw()`-funktionen så här:

```python
screen.fill((80, 0, 70))
```

Det som står inom parenteser, `(80, 0, 70)`, kallas i Python för *tuple*; det fungerar som en lista med värden som inte går att ändra och talar om vilken färgblandning vi vill ha. Det första talet (80) är för färgen rött, det andra (0) för grönt och det tredje (70) är för blått. Det största värdet man kan ha för någon färgkomponent är 255 och det minsta värdet är 0. **Testa olika värden och se vad du får!**

I Chrome kan du öppna en färgväljare genom att trycka tangentkombinationen ctrl+shift+I och sedan klicka på en av de små kvadratikonerna som du kan se i fliken Styles. Se bilden!

![image](https://user-images.githubusercontent.com/4598641/223195080-7bda1b3d-89e9-479a-bebe-936a332b1408.png)

Nu ska ditt program se ut så här:
```
import pgzrun

WIDTH = 800
HEIGHT = 600

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

Lägg nu till en ny *Actor* som representerar ädelstenen:
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

WIDTH = 800
HEIGHT = 600

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

Lägg till det i din kod!

```python
import pgzrun

WIDTH = 800
HEIGHT = 600

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

We also want the gem to go back to the top if it touches the spaceship. 
If you had done Scratch before, you might remember the if touching sprite command. 
In Pygame Zero, we'll use `if gem.colliderect(ship):` or `if ship.colliderect(gem):` &ndash; both works the same.

```python
if gem.colliderect(ship):
    gem.y = 0
```
eller

```python
if ship.colliderect(gem):
    gem.y = 0
```
**Testa det i din kod!**

## Slumptal med `random()`
It's not vey interesting to have the gem fall from the same spot everytime. 
In Introduction to Python, you learned to use the random module.
We'll use it here to randomize the x position of the gem.

Before we can use the random module, we'll need to import it.

```python
import random
```

To assign a random x position, we use

```python
gem.x = random.randint(20, WIDTH - 20)
```
The `random.randint(20, WIDTH - 20)` function will provide a random number between 20 to WIDTH - 20. This should be added whenever we return the gem to the top of the screen.

Your program should look like this now.


```python
import pgzrun

WIDTH = 800
HEIGHT = 600

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

We can track the score easily using a variable. '
Let's add a variable named score and give it the value of 0 at the start of the program.

```python
score = 0
```
Now everytime the spaceship catches the gem, we'll increase score by 1.

```python
if gem.colliderect(ship):
    gem.x = random.randint(20, WIDTH - 20)
    gem.y = 0
    score += 1
```

If you try out this program, you'll get an error:

```python
UnboundLocalError: local variable 'score' referenced before assignment
```

That's because the score variable is declared outside of the update() function, but we are trying to write it from inside the update() function.

In Python, we can read variables that are outside a function (these are called global variables),
but cannot write to them unless we declare them as global inside the function.

```python
global score
```

After this change, your `update()` function should now look like this:
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

To display the score, we will use the `screen.draw.text()` function.

```python
screen.draw.text(f"Score: {score}", (15, 10), color=(255, 255, 255), fontsize=30)
```
The parameters are:

`f"Score: {score}"` : This is the string that we want to draw.

`(15, 10)` : This is the position to draw; x=15 and y=10.

`color=(255, 255, 255)` : This is the color of the text, in this case, it is white

`fontsize=30` : The size of the font.

Like all the other drawing functions, we'll need to put this inside the `draw()` function. After this is done, your program should look like this:

```python
import pgzrun

WIDTH = 800
HEIGHT = 600

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

## Mouse Controls
We can also modify our game to make it work with the mouse. 
Like Scratch, Pygame Zero is events based. 
This means that when certain events occurs (eg. a mouse button is pressed), Pygame Zero will run the corresponding function (eg. `on_mouse_down`).

To detect mouse movement, we can use the `on_mouse_move(pos, rel, buttons)` function. Try adding this to your game:

```
def on_mouse_move(pos, rel, buttons):
    ship.x = pos[0]
```

The purpose of the three parameters are:

`pos` : This provides the position of the mouse. You can get the x position using pos[0] and the y position using pos[1].

`rel` : This provides the change in position since the last mouse move. rel[0] is the change in x position and rel[1] the change in y position.

`buttons` : This provides a list of mouse buttons that are pressed. For example, if you want to check if the left button is pressed:

```python
def on_mouse_move(pos, rel, buttons):
    if mouse.LEFT in buttons:
        print('left click')
```
**This is just an example. Don't add it to your game**

## Other Events
Besides mouse move, there are also other functions that will be run by Pygame Zero when their corresponding events occurs. They are...

`on_mouse_down(pos, buttons)` : Run when a mouse button is pressed.

`on_mouse_up(pos, buttons)` : Run when a mouse button is released.

Parameters:
- `pos` : This provides the position of the mouse. You can get the x position using pos[0] and the y position using pos[1].
- `buttons` : This provides a list of mouse buttons that are pressed.

`on_key_down(key, mod, unicode)` : Run when a keyboard key is pressed.

`on_key_up(key, mod)` : Run when a keyboard key is release.

Parameters:
- key : An integer indicating the key that was pressed. See the Pygame Zero website for a full list of keys.
- mod : A bitmask of modifier keys that were depressed. You can check them as follows:

```python
def on_key_down(key, mod, unicode):
    if mod & keymods.LSHIFT:
        print('Left shift button pressed')
```

`unicode` : Where relevant, the character that was typed. You can check it like this:
```python
def on_key_down(key, mod, unicode):
    if unicode == 'e':
        print('e button pressed')
```


# Game Over
## Gör spelet svårare
Right now the game is too easy.
Not to brag, but I can score over 300 without breaking a sweat.
Let's make it harder by making the gem fall faster the higher your score is.

Look for this line:

```python
gem.y += 4
```
and change it to this:
```python
gem.y += 4 + score / 5
```
This will increase the falling speed as your score goes up. When your score is zero, the gem will fall at speed 4. When your score is 10, the gem will fall at speed 6 (4 + 10 / 5).


## Game Over
It's not much fun to play a game that you cannot lose. 
So let's add in a game over condition. 
If the gem touches the bottom of the screen, we'll end the game.

First, add in a new variable called `game_over` and set it to `False`.

```python
game_over = False
```
Inside the `update()` function, look for these lines:
```python
if gem.y > HEIGHT:
    gem.x = random.randint(20, WIDTH - 20)
    gem.y = 0
```
and change them to these:
```python
if gem.y > HEIGHT:
    game_over = True
```
This will set the `game_over` variable to `True` if the gem touches the bottom of the screen.

You will also need to add global `game_over` to the top of the `update()` function.
Do you remember why? If you can't, refer back to the keeping score page.

Inside the `draw()` function, change these lines:
```python
screen.fill((80, 0, 70))
gem.draw()
ship.draw()
screen.draw.text(f"Score: {score}", (15, 10), color=(255, 255, 255), fontsize=30)
```
into these
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
This will make it draw the game over text when the game_over variable is True, otherwise it will draw the gem and the ship as before.

Your final program should look like this:
```python
import pgzrun

WIDTH = 800
HEIGHT = 600

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

Here are some challenges that you can try to make the game better.

## Challenge 1. Three Lives
Modify the game so that you have 3 lives. The game should only end when all 3 lives are used up.

## Challenge 2. Different Gems
The media pack comes with a few different color gems. Make the gem color change randomly each time it falls from the top.

## Challenge 3. Ship Selection
The media pack comes with a few different types of spaceships. Use input to ask the user which spaceship they want, and let them play the game using the ship they chose.

## Challenge 4. Multiple Gems
Right now, we only have one gem falling at a time. Modify the game to allow multiple gems to fall simultaneously.

## Challenge 5. Multi-Player
Add in a second player and compete to see who can get the higher score!

# Källor/Sources

Det här projektet är översatt och anpassat till repl.it baserat på https://aposteriori.trinket.io/game-development-with-pygame-zero#/gem-catcher/first-program

This project is a translated and adapted to repl.it from https://aposteriori.trinket.io/game-development-with-pygame-zero#/gem-catcher/first-program
