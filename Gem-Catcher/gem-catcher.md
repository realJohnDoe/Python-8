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

# Skådespelaren
Now that wasn't very interesting, so let us add in a spaceship. 
To do so, we need to first provide an image for the spaceship. 
You can use any images you want, but to make it easy for you, I have prepared a zip file containing a variety of images.
[Download it here.](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/image_pack.zip)

Remember the images folder I told you to create inside your project folder? 
That's where your spaceship image need to go. Open the zip file, choose a suitable image, and copy it into the images folder. 
I'm using this image...

![image](https://user-images.githubusercontent.com/4598641/222978313-4661f08c-e673-40be-87be-5fa1d8d06de8.png)

IMPORTANT: Your image filename must only contain lowercase letters, numbers and underscores.

Once that is done, you can add the spaceship to your Python program...

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

This is what each line does:

`ship = Actor('playership1_blue')` : Create a new Actor using the playership1_blue image file. If you are using a different file, you'll need to change this.

`ship.x = WIDTH / 2 - 30` : Set the x position of the ship to 370. Try changing this!

`ship.y = HEIGHT - 50` : Set the y position of the ship to 550. Try changing this!

`def draw():` : This is a special function. We don't need to run it ourselves; Pygame Zero will run it for us regularly.

`ship.draw()` : This tells the ship Actor to draw itself on the screen. It needs to be indented under def draw():, so that it will run whenever Pygame Zero run the draw() function.

![image](https://user-images.githubusercontent.com/4598641/222978372-85be8781-e6fe-414e-9fb1-b7847dfc8b5f.png)

# Funktionen update()

Earlier, we created the `draw()` function. This is a special function that Pygame Zero runs regularly to draw what you see on the screen. Another special function is `update()`. Pygame Zero will regularly run our `update()` function to update the position of the various actors in the game.

Let's add in the `update()` function and program it to react to keypresses.

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

This is what we added ...
```python
def update():
    if keyboard.left:
        ship.x -= 5
    if keyboard.right:
        ship.x += 5
```
Whenever Pygame Zero runs our `update()` function, we will check if the left key is pressed. 
If it is, we'll reduce the x position by 5.
If the right key is pressed, we'll increase the x position by 5.

Try out the program! Write it in IDLE and run it using F5 or Run -> Run Module. Did that work the way you expected?

## Clearing Screen
If you tried the previous program, you should have gotten something funky like this ...

![image](https://user-images.githubusercontent.com/4598641/222978681-7aa59c8e-4b41-49ae-8415-e5df0db6b51d.png)

That's because we told Pygame Zero to update the ship's position and draw it to screen, but we didn't tell it to erase what was drawn before!

To erase the screen, we'll fill the entire screen with a single color. We'll do this in the `draw()` function, using

```python
screen.fill((80, 0, 70))
```

The `(80, 0, 70)` is a tuple (a tuple is like a list, but it cannot be changed) representing the color. The first number (80) is for red, the second number (0) is for green, and the last number (70) is for blue. The largest allowable value for each color is 255 and the smallest is 0. **Try different numbers and see what color you get!**

Your progam should now look like this: 
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

The game won't be called "Gem Catcher" without a gem! We can add in a gem the same way we added the spaceship.

First, add a gem image to the **images** folder. I'm using this one:

![image](https://user-images.githubusercontent.com/4598641/222978860-59fdc056-ee3c-4d15-bca8-09b80051d3c9.png)

Next, add a new gem **Actor**
```python
gem = Actor('gemgreen')
gem.x = WIDTH / 2 - 50
gem.y = 0
```
Setting x this way will place it roughly in the middle horizontally, while setting y to 0 will place it at the top. Don't forget to also draw the gem in the draw() function.

```python
gem.draw()
```
Your program should now look like this:

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
Previously, we have written code in the `update()` function to make the ship move by changing its x position when the left or right key is pressed. For the gem, we'll make it move continuously downwards by changing the y position.

```python
gem.y += 4
```

We also want the gem to return to the top when it reaches the bottom. To do that, we'll set the y position to 0 (top), when it exceeds HEIGHT (bottom most position).

```python
if gem.y > HEIGHT:
    gem.y = 0
```

Add that into your program!

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
