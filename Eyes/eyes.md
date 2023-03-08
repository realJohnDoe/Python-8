# Ögon

![image](https://user-images.githubusercontent.com/4598641/223815678-2c97174e-578c-4df4-9f8a-d8764f0b2424.png)

Ögonen följer muspekaren.

# Rita ett öga
Ögat ritas med en vit cirkel och en lite mindre mörkblå cirkel för pupillen.

Koden så här långt:
```python
import pgzrun
WIDTH, HEIGHT = 800, 600

def draw():
    screen.fill((0, 0, 0))

    screen.draw.filled_circle((200, 200), 50, color=(255, 255, 255))
    screen.draw.filled_circle((200, 200), 15, color=(0, 0, 100))

pgzrun.go()
```

![image](https://user-images.githubusercontent.com/4598641/223816876-1da49223-c7af-46d5-836c-9b1216eb52d4.png)

# Räkna ut avståndet mellan muspekaren och ögat
Avståndet mellan ögats mitt och muspekaren visas.
Ögats x- och y-koordinater återanvänder vi från när vi ritar ögat och därför sparar vi koordinaterna i variabler.

Vi importerar modulen `pygame` för att kunna använda funktionen `pygame.mouse.get_pos.

Funktionen `update()` är tom så länge. Funktionen `draw()` ritar om skärmen vid varje uppdatering.

Koden så här långt &ndash; nya rader är markerade:
```python
import pgzrun
import pygame #nyrad
WIDTH, HEIGHT = 800, 600

def update():
    pass

def draw():
    screen.fill((0, 0, 0))

    mouse_x, mouse_y = pygame.mouse.get_pos() #nyrad

    eye_x = 200 #nyrad
    eye_y = 200 #nyrad

    distance_x = mouse_x - eye_x #nyrad
    distance_y = mouse_y - eye_y #nyrad

    screen.draw.filled_circle((eye_x, eye_y), 50, color=(255, 255, 255)) #lite ändrad
    screen.draw.filled_circle((200, 200), 15, color=(0, 0, 100))

    screen.draw.text(f"distance x: {str(distance_x)}\ndistance y: {str(distance_y)}", (0, 0)) #nyrad

pgzrun.go()
```

![image](https://user-images.githubusercontent.com/4598641/223817639-1363643f-481d-44e3-979b-d0b48eb0c9da.png)

# Räkna ut avståndet mellan muspekaren och ögat
Avståndet kan vi räkna ut med Pythagoras sats. Se figuren.

Avståndet i pixlar är roten ur (antalet pixlar i X-led i kvadrat + antalet pixlar i Y-led i kvadrat).

Vi importerar mattemodulen `math` för att räkna roten ur med `math.sqrt()`.

```python
import math #lägg detta överst

def draw():
    # Ändra i draw. Behåll oförändrade rader!

    distance = math.sqrt(distance_x**2 + distance_y**2) #ändra den här raden

    # etc.

    screen.draw.text(f"distance x: {str(distance_x)}\ndistance y: {str(distance_y)}\ndistance: {str(distance)}", (0, 0)) #ändrad
```

# Rörlig pupill

Vi vill att pupillen ska följa muspekaren.

Om muspekaren är innanför ögat är det lätt. Då kan vi sätta pupillen till muspekarens koordinater.
Hur vet vi att muspekaren är i ögat? Eftersom vi räknat ut avståndet från ögats centrum till muspekaren så kan vi använda ögats radie som en gräns, till exempel 30 pixlar.

Då kan koden för `draw()` se ut så här:

```python
# behåll resten av koden

def draw():
    screen.fill((0, 0, 0))

    def draw_eye(eye_x, eye_y):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        distance_x = mouse_x - eye_x
        distance_y = mouse_y - eye_y
        distance = math.sqrt(distance_x**2 + distance_y**2) # Pythagoras
        pupil_x = eye_x + distance_x
        pupil_y = eye_y + distance_y

        screen.draw.filled_circle((eye_x, eye_y), 50, color=(255, 255, 255))
        screen.draw.filled_circle((pupil_x, pupil_y), 15, color=(0, 0, 100))

# behåll resten av koden
```

Om muspekaren är mer än 30 pixlar från ögats centrum, placerar vi pupillen i kanten av ögat.

BILDILLUSTRATION HÄR: likformig triangel innanför ögat som skalas proportionellt i X- och Y-led med avståndsfaktorn. Då hamnar pupillen alltid innanför cirkeln.

**Kodexempel här**

# Maximala avståndet pupillen kan röra sig
**Kodexempel här**

# Två ögon
The code is made into a function which takes an eye's X and Y positions.
**Kodexempel här**

```python
import pgzrun
import pygame
import math

def update():
    pass

def draw():
    screen.fill((0, 0, 0))

    def draw_eye(eye_x, eye_y):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        distance_x = mouse_x - eye_x
        distance_y = mouse_y - eye_y
        distance = math.sqrt(distance_x**2 + distance_y**2) # Pythagoras
        if distance < 30:
            pupil_x = eye_x + distance_x
            pupil_y = eye_y + distance_y
        else:
            pupil_x = eye_x + 30 * distance_x / distance
            pupil_y = eye_y + 30 * distance_y / distance

        screen.draw.filled_circle((eye_x, eye_y), 50, color=(255, 255, 255))
        screen.draw.filled_circle((pupil_x, pupil_y), 15, color=(0, 0, 100))

    draw_eye(200, 200)
    draw_eye(330, 200)

WIDTH = 530
HEIGHT = 400
pgzrun.go()
```

# Källor

Originalprojekt: https://simplegametutorials.github.io/pygamezero/eyes/
