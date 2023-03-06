[Infinite Runner](#infinite-runner) &bull;
[Bakgrund](#bakgrund) &bull;
[Ninja](#ninja) &bull;
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

pgzrun.go() # Must be last line
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
  screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254))

pgzrun.go() # Must be last line
```

This is what the new lines do...

`def draw():` : This is the draw function that Pygame Zero will run regularly. Anything that draws to the screen should be inside this function.

`screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254)` : This draws a rectangle on the screen, starting from 0,0 (top left corner) and with a width of 800 and a height of 400. The color consists of 163 red, 232 green, and 254 blue.

**Try: Experiment with different colors and see what you get. Remember that each component of the color must be in the range from 0 to 255.**

## Ground
The previous step drew in the sky. Now let's add a second rectangle to draw the ground.

```python
import pgzrun

WIDTH=800
HEIGHT=600

def draw():
  screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254))
  screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))

pgzrun.go() # Must be last line
```
Here's what the new line does...

`screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))` : This time, we'll start the rectangle at 0,400. This means x=0 and y=400. The screen is 600 pixels tall, and the previous rectangle was 400 pixels tall, so we only need this rectangle to be 200 pixels tall.

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
  screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254))
  screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))

pgzrun.go() # Must be last line
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
  screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254))
  screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
  runner.draw()

pgzrun.go() # Must be last line
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
runner.y = 400
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
if runner.y > 400:
  velocity_y = 0
  runner.y = 400
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
  if runner.y > 400:
    velocity_y = 0
    runner.y = 400

def draw():
  screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254))
  screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
  runner.draw()

pgzrun.go() # Must be last line
```

# Hinder
# Poängräkning
# Game Over
# Utmaningar och buggar

# Källor
Projektet är en översättning och anpassning till repl.it av originalet på https://aposteriori.trinket.io/game-development-with-pygame-zero#/ninja-runner/infinite-runner

This is a Swedish translation and repl.it adaptation of https://aposteriori.trinket.io/game-development-with-pygame-zero#/ninja-runner/infinite-runner
