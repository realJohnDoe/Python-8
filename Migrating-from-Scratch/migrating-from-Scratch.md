# Att flytta över från Scratch
>Detta är en svensk översättning av Daniel Popes guide, https://pygame-zero.readthedocs.io/en/stable/from-scratch.html

Den här handledningen jämför en version av Flappy Bird skriven i Scratch med en skriven i Pygame Zero. Programmen i Scratch och Pygame Zero är förvånansvärt lika.

[Versionen för Pygame Zero](https://github.com/lordmauve/pgzero/blob/stable/examples/flappybird/flappybird.py) finns med i Pygame Zero-projektet.

Du kan också ladda ner versionen för Scratch 1.4 och [versionen för Scratch 3](https://github.com/lordmauve/pgzero/raw/master/examples/flappybird/Flappy%20Bird.sb3) från den här länken.

Versionen för Pygame Zero innehåller logik för poängräkning som vi utelämnar i kodexemplenm på den här sidan för att ge en mer rättvis jämförelse.

Pythonkoden som visas här är omflyttad för att göra exemplen tydligare.

# Scenen
Så här ser scenen ut i vårt Scratchprogram:

<img src="https://pygame-zero.readthedocs.io/en/stable/_images/flappybird-stage.png" />

Det finns bara tre objekt förutom bakgrunden: fågeln och det övre och undre röret.

Detta motsvarar Pygame Zero-koden för att sätta upp de här objekten som aktörer, `Actor`:
```python
bird = Actor('bird1', (75, 200))
pipe_top = Actor('top', anchor=('left', 'bottom'))
pipe_bottom = Actor('bottom', anchor=('left', 'top'))
```

I Pygame Zero ska vi också tänka på att rita de här objekten. I princip ger det oss lite mer flexibilitet hur vi vill rita scenen:

```python
def draw():
    screen.blit('background', (0, 0))
    pipe_top.draw()
    pipe_bottom.draw()
    bird.draw()
```

# Att förflytta rören
Rören åker med konstant fart oberoende av fågeln. När de försvinner ut till vänster på scenen dyker de upp igen till höger och den vertikala placeringen ändras slumpmässigt.

I Scratch kan vi uppnå det genom att skapa två olika skript för det övre och undre röret.

<img src="https://pygame-zero.readthedocs.io/en/stable/_images/flappybird-top-start.png" alt="_images/flappybird-top-start.png"/> <img src="https://pygame-zero.readthedocs.io/en/stable/_images/flappybird-bottom-start.png" alt="_images/flappybird-bottom-start.png"/>

För att summera vad som händer här:
- Villkort `x position < -240` är sant när ett rör försvinner ut till vänster på skärmen och det är det som signalen att återställa rören.
- Variabeln `pipe_height` används för att samordna de två rören. Eftersom avståndet mellan de två rören ska vara samma hela tiden kan vi inte välja höjderna slumpmässigt. Därför har ena röret den här logiken men inte det andra. 
- `set y position to pipe height +/- 230` placerar ett rör så att det är ovanför `pipe_height` och det andra nedanför `pipe_height`.

Den här koden blir mycket enklare i Pygame Zero. We kan skriva en enda funktion som uppdaterar båda rören. I själva verket har jag delat upp det på ett annat sätt för att belysa hur koden för att återställa rören hänger ihop, alltså `reset_pipes()`:

```python
import random

WIDTH = 400
HEIGHT = 708
GAP = 130
SPEED = 3

def reset_pipes():
    pipe_gap_y = random.randint(200, HEIGHT - 200)
    pipe_top.pos = (WIDTH, pipe_gap_y - GAP // 2)
    pipe_bottom.pos = (WIDTH, pipe_gap_y + GAP // 2)

def update_pipes():
    pipe_top.left -= SPEED
    pipe_bottom.left -= SPEED
    if pipe_top.right < 0:
        reset_pipes()
```

En liten skillnad här är att jag kan bryta ut de värden jag vill återanvända som **konstanter**, skrivna med STORA BOKSTÄVER. Det låter mig ändra dem på ett ställe när jag vill finjustera spelet. I koden här uppe t.ex. kan jag göra gapet bredare eller smalare mellan de två rören genom att bara ändra `GAP`.

Den största skillnaden är att det inte finns någon `för alltid`-loop i Pythonkod. Det är den stora skillnaden mellan Scratch och de flesta textbaserade programspråk: du måste uppdatera spelet med ett animeringssteg och sen gör `return`. När du gör `return` från din kod har Pygame Zero möjlighet att hantera indata (tangentbord, mus) eller att rita om skärmen. Om du kör en oändlig loop (för alltid) kommer spelet att hänga sig så dina loopar behöver blir klara snabbt.

Pygame Zero anropar funktionen `update()` när den vill att du ska animeringen ett steg, så vi behöver bara anropa funktionen `update_walls()`:

```python
def update():
   update_walls()
```


# The Bird

The patterns described above for how Scratch logic translates to Python code also apply for the bird logic. Let’s look at the Python code first this time.

The code to update the bird is organised into a function called `update_bird()`.
The first thing this function contains is some code to move the bird according to gravity:

```python
GRAVITY = 0.3

# Initial state of the bird
bird.dead = False
bird.vy = 0

def update_bird():
    uy = bird.vy
    bird.vy += GRAVITY
    bird.y += bird.vy
    bird.x = 75
```

This is a simple gravity formula:

- Gravity means constant **acceleration downwards**.
- Acceleration is change in **velocity**.
- Velocity is change in **position**.

To represent this we need to track a variable `bird.vy`, which is the bird’s velocity in the y direction. 
This is a new variable that we are defining, not something that Pygame Zero provides for us.

- Gravity means constant acceleration downwards: `GRAVITY` is greater than 0.
- Acceleration is change in velocity: `GRAVITY` gets added to `bird.vy`
- Velocity is change in position: `bird.vy` gets added to `bird.y`

Note that the bird does not move horizontally! Its x position stays at 75 through the whole game.
We simulate movement by moving the pipes towards it. This looks as though it’s a moving camera following the bird. 
So there’s no need for a `vx` variable in this game.

The next section makes the bird flap its wings:
```python
if not bird.dead:
    if bird.vy < -3:
        bird.image = 'bird2'
    else:
        bird.image = 'bird1'
```

This checks if the bird is moving upwards or downwards. 
We show the `bird2` image if it is moving upwards fast and the `bird1` image otherwise.
(&ndash;3 was picked by trial and error to make this look convincing).

The next section checks if the bird has collided with a wall:

```python
if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
    bird.dead = True
    bird.image = 'birddead'
```

If so we set `bird.dead` to `True`.
This is a boolean value meaning it is either `True` or `False`.
We can use this to easily check if the bird is alive. If it isn’t alive it won’t respond to player input.

And the final section checks if the bird has fallen off the bottom (or the top) of the game screen. If so it resets the bird:

```python
if not 0 < bird.y < 720:
    bird.y = 200
    bird.dead = False
    bird.vy = 0
    reset_pipes()
```

What’s `reset_pipes()` doing there? Because I’d organised my pipes code to be a separate function, I can just call it whenever I want to reset my walls. In this case it makes it a better game because it gives the player a chance to react when the bird moves back to its start position.

Again, this needs to be called every frame, so we add it to `update()`:

```python
def update():
   update_walls()
   update_bird()
```

The final part of the bird logic is that it has to respond to player control. When we press a key, the bird flaps upwards. Pygame Zero will call an `on_key_down()` function &ndash; if you’ve defined one &ndash; whenever a key is pressed:

```python
FLAP_VELOCITY = -6.5

def on_key_down():
    if not bird.dead:
        bird.vy = FLAP_VELOCITY
```

Here, if the bird is not dead, we set its `vy` to a negative number: in Pygame Zero this means it starts moving upwards.

You should be able to find a lot of parallels between the Python code and this Scratch code:

<img src="https://pygame-zero.readthedocs.io/en/stable/_images/flappybird-bird-start.png"/> <img src="https://pygame-zero.readthedocs.io/en/stable/_images/flappybird-bird-space.png"/>

The biggest differences between Scratch and Pygame Zero are these:

- You cannot loop forever in Pygame Zero &ndash; just update for one frame and then return.
- The coordinates are different. In Pygame Zero, the top left of the screen is (x, y = (0, 0). The x direction goes from left to right as before, but y goes down the screen! This is why `GRAVITY` is a positive number and `FLAP_VELOCITY` is a negative number in Python.
- `bird.dead` is a bool, so I can write code like `if not bird.dead` instead of `dead = 0` as in Scratch.

# Summary
Many of the concepts available in Scratch can be translated directly into Pygame Zero.

Here are some comparisons:

| In Scratch |	In Pygame Zero|
| --- | --- |
| change y by 1 (up)	| bird.y &ndash;= 1|
| change y by -1 (down) |	bird.y += 1 |
| set costume to <name>	| bird.image = 'name'| 
| if dead = 0| 	if not bird.dead:| 
| set dead to 0	| bird.dead = False| 
| if touching Top?	| if bird.colliderect(pipe_top)| 
| When Flag clicked… forever | 	Put code into the update() function. | 
| When [any] key pressed	| def on_key_down():| 
| pick random a to b	| import random to load the random module, then random.randint(a, b)| 
| (0, 0) is the centre of the stage	| (0, 0) is the top-left of the window| 

In some cases, the code is simpler in Python because it can be organised in a way that helps it make sense when you read it.

The power of Pygame Zero’s actors also makes the coordinate manipulation easier. 
We used the anchor position to position the pipes, and we were able to see if a pipe was off-screen by checking
`pipe_top.right < 0` rather than `if x position < -240`.



# Källor
https://pygame-zero.readthedocs.io/en/stable/from-scratch.html
