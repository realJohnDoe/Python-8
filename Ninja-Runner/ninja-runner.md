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

An Infinite Runner (aka Endless Runner) is a game that never ends. The objective is to last as long as possible, and the longer you last, the higher your score.

To make our Infinite Runner, we will be making use of what we have learned from the previous gem catcher game, and adding in...

- Draw
- Animation
- Physics
- List of Actors

## Nytt projekt
Börja med göra en egen kopia av startprojekt i repl.it: FIXA:LÄNK

# Bakgrund
## First Step
Same as before, we start programming our game by...

Importing Pygame Zero
Setting the window's width and height
Running pgzrun.go()
```python
import pgzrun

WIDTH=800
HEIGHT=600

pgzrun.go() # Måste vara sista raden
```
Click File, Save As... then select the ninja_runner folder you have previously created. Give your program a filename (eg. ninja_runner.py) then click Save.

## Draw
We can draw different shapes using the functions under screen.draw. We have previously used screen.draw.text(), but there are many more functions, such as...

- `screen.draw.line()`
- `screen.draw.circle()`
- `screen.draw.filled_circle()`
- `screen.draw.rect()`
- `screen.draw.filled_rect()`
To learn more about these function, you can refer to the Pygame Zero documentations here.

For now, we'll just be using `screen.draw.filled_rect()`. This draws a rectangle to the screen, so we'll need to add it to the draw() function.
```python
import pgzrun

WIDTH=800
HEIGHT=600

def draw():
  screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT - 200), (163, 232, 254))

pgzrun.go() # Måste vara sista raden
```

This is what the new lines do...

`def draw():` : This is the draw function that Pygame Zero will run regularly. Anything that draws to the screen should be inside this function.

`screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT - 200), (163, 232, 254)` : This draws a rectangle on the screen, starting from 0,0 (top left corner) and with a width of 800 and a height of 400. The color consists of 163 red, 232 green, and 254 blue.

**Try: Experiment with different colors and see what you get. Remember that each component of the color must be in the range from 0 to 255.**

## Ground
The previous step drew in the sky. Now let's add a second rectangle to draw the ground.

```python
import pgzrun

WIDTH=800
HEIGHT=600

def draw():
  screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT - 200), (163, 232, 254))
  screen.draw.filled_rect(Rect(0, HEIGHT - 200, WIDTH, 200), (88, 242, 152))

pgzrun.go() # Måste vara sista raden
```
Here's what the new line does...

`screen.draw.filled_rect(Rect(0, HEIGHT - 200, WIDTH, 200), (88, 242, 152))` : This time, we'll start the rectangle at 0,400. This means x=0 and y=400. The screen is 600 pixels tall, and the previous rectangle was 400 pixels tall, so we only need this rectangle to be 200 pixels tall.

Once completed, run your program. Your screen should look like this...

![image](https://user-images.githubusercontent.com/4598641/223218919-66ee7ecf-043f-4c08-a775-074ff487bb3c.png)

# Ninjan

## Animering
In Scratch, you can make your sprites animate by changing its costumes. In Pygame Zero, we do the same by changing the images. One way to do this is...

```python
def update():
    if runner.image == 'run__000':
      runner.image == 'run__001'
    elif runner.image == 'run__001':
      runner.image == 'run__002'
    elif runner.image == 'run__002':
      runner.image == 'run__000'
```

This checks what is the current image and switches to the next one. It works, but it's a lot more troublesome than Scratch. To help with this, we can use the Pygame Zero Helper module.

## Pygame Zero Helper

First, download it from here.

Next, open up the downloaded zip file and copy the pgzhelper.py file that's inside. Paste it into your ninja_runner folder.

Finally, we need to load the pgyhelper.py module. Add from pgzhelper import * to your Python game file. It should now look like this...

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

Save and run it, just to make sure that everything is done correctly.

## Ninjabilder
Before we can start programming our ninja, we need to put the ninja images in the images folder.

![image](https://user-images.githubusercontent.com/4598641/223219964-a4109c3b-04be-4793-a600-dba2c386f297.png)

Go to the image_pack that you have downloaded previously, and look for the ninja folder. Inside, you can find many run images, ranging from run__000 to run__009. Copy all of the run images from the ninja folder and paste them into your own images folder.

**Options: There are many other sets of running images that you can use. Try dino, knight, or zombies.**

## Programmera ninjan

We'll add in the ninja into our game using...

```python
runner = Actor('run__000')
run_images = ['run__000', 'run__001', 'run__002', 'run__003', 'run__004', 'run__005', 'run__006', 'run__007', 'run__008', 'run__009']
runner.images = run_images
```

This is what each line does...

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

That should display your ninja on screen, but it's not running yet! Add in the update function like this...

```python
def update():
  runner.next_image()
```
This tells Pygame Zero to switch to the next image everytime it updates. With this, you should now have a running ninja!

### Justera placeringen

You can adjust the position of the ninja using runner.x and runner.y. Try the following...

```python
runner.x = 100
runner.y = HEIGHT - 200
```
Try: Adjust the position of the ninja by changing runner.x and runner.y until you have her at the position you want.


# Hoppa

## Fysik

Which of these look more realistic?

![image](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/jump.gif)

In real life, objects are affected by gravity. To make our ninja jump realistically, we'll need to simulate the effects of gravity in our game.

Let's start by adding in a variable for velocity_y and gravity.

```python
velocity_y = 0
gravity = 1
```

Explanation for each line...

`velocity_y = 0` : This represents how fast our ninja should be moving in the up/down direction. It starts at zero, as our ninja isn't jumping yet.

`gravity = 1` : Gravity will change our velocity. We can change this later and see its effects, but leave it at 1 for now.

Next, in update() we are going to change the velocity when the up arrow is pressed.

```python
def update():
  global velocity_y
  runner.next_image()

  if keyboard.up:
    velocity_y = -15

  runner.y += velocity_y
```
This is what each line does...

`global velocity_y` : We need to use global if we change a variable that comes from outside of a function.

`if keyboard.up:` : When the up arrow is pressed...

`velocity_y = -15` : Set the up/down velocity to -15. A negative number means it's going upwards.

`runner.y += velocity_y` : Change our ninja's position using the velocity. The += means to add velocity_y to runner.y.

# Tips
```python
a += 1      # This line is the same as...
a = a + 1   # ...this line.
```

Try it out! If you programmed it correctly, the ninja should fly up into the sky when you press up. That's because we haven't added gravity yet!

## Gravity
Gravity will change our velocity. Under the runner.y += velocity_y line, let's add it in velocity_y += gravity.

Now our ninja falls straight down! We haven't tell our ninja when to stop falling yet! Let's add that in next...

```python
if runner.y > HEIGHT - 200:
  velocity_y = 0
  runner.y = HEIGHT - 200
```
Here we are treating `y = 400` as the "ground", and if the ninja is at a y position that's greater than 400, we will set her velocity_y to 0 and her y position to 400. This will prevent her from falling through the ground.

Your program should now look like this...

```python
import pgzrun
from pgzhelper import *

WIDTH=800
HEIGHT=600

runner = Actor('run__000')
run_images = ['run__000', 'run__001', 'run__002', 'run__003', 'run__004', 'run__005', 'run__006', 'run__007', 'run__008', 'run__009']
runner.images = run_images
runner.x = 100
runner.y = 400

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

In our gem catcher game, we only have a single gem at a time and it returns to the top everytime we catch it. In our ninja runner game, we are going to have multiple obstacles appear on screen at the same time. To do so, we are going to make use of **lists**.

![image](https://user-images.githubusercontent.com/4598641/223222660-26ee39e0-5420-47ba-8ef9-d4cb855636fe.png)

First, let's add an empty list called obstacles and a integer variable `obstacles_timeout`

```python
obstacles = []
obstacles_timeout = 0
```
Now in our `update()` function, we are going to increase out timeout by 1 each time.

```python
obstacles_timeout += 1
```
Next, if the timeout is greater than 50, we'll add in an obstacle and reset the timeout to zero.

```python
if obstacles_timeout > 50:
  actor = Actor('cactus')
  actor.x = WIDTH + 50
  actor.y = HEIGHT - 170
  obstacles.append(actor)
  obstacles_timeout = 0
```

The only thing new here is `obstacles.append(actor)`. This adds `actor` to the `obstacles` list.

**IMPORTANT: You'll need to move the cactus image into your images folder first! If you decide to use a different image, change the image name accordingly.**

Now to make the obstacles move across the screen...

```python
for actor in obstacles:
  actor.x -= 8
```
This will go through the entire obstacles list and reduce the *x* position for obstacle. Reducing x will make the obstacle move to the left.

Finally, we need to draw the obstacles on screen. In the `draw()` function, add...

```python
for actor in obstacles:
  actor.draw()
```
Your program should now look like this...

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
  if runner.y > 400:
    velocity_y = 0
    runner.y = 400

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

Just like in the gem catcher program, we'll use a variable named score to keep track of our score.

```python
score = 0
```
We'll increase our score each time the obstacle disappears off the left side of the screen. Inside update(), let's change this...
```python
  for actor in obstacles:
    actor.x -= 8
```
...into this...
```python
  for actor in obstacles:
    actor.x -= 8
    if actor.x < -50:
      obstacles.remove(actor)
      score += 1
```
This is what each line means...

`if actor.x < -50` : When the x position is less than -50, the actor is most probably outside of the screen. So we will...

`obstacles.remove(actor)` : Remove the actor from the obstacles list...

`score += 1` : ...and increase score by 1. Remember to declare score as a global!.

## Drawing Obstacles and Score
The obstacles won't appear on screen if we don't draw it inside the `draw()` function. So let's add in...

```python
for actor in obstacles:
  actor.draw()
```
This will go through the list of obstacles and draw each one.

We should also display the score on screen using...

```python
screen.draw.text(f"Score: {score}", (15, 10), color=(0,0,0), fontsize=30)
```
Feel free to change the color, position, or fontsize.



# Game Over
Right now, the game does nothing even if our ninja crashes into the cactus. Let's add in a game over condition. If the ninja touches any of the obstacles, we'll end the game.

First, we'll add in a variable called `game_over` and set it to `False` at the start.

```python
game_over = False
```
Inside the update() function, we'll detect if our runner collided with any of the obstacles. If she did, we'll set game_over to True.

```python
if runner.collidelist(obstacles) != -1:
  game_over = True
```
Important: Remember to declare game_over as a global in the update() function.

The runner.collidelist(obstacles) checks if the runner collided with any of the actors in the obstacles list. If she didn't, the collidelist function will give us the value -1.

Next, we'll need to draw the game over text inside draw() by changing this...
```python
  runner.draw()
  for actor in obstacles:
    actor.draw()
  screen.draw.text(f"Score: {score}", (15, 10), color=(0,0,0), fontsize=30)
...into this...
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

Your final game should look like this...

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
