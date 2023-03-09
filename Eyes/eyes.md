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

pgzrun.go() # måste vara sist
```

![image](https://user-images.githubusercontent.com/4598641/223816876-1da49223-c7af-46d5-836c-9b1216eb52d4.png)

# Räkna ut avståndet mellan muspekaren och ögat
Vi lägger till kod så att avståndet mellan ögats mitt och muspekaren visas, räknat i pixlar.

Ögats x- och y-koordinater återanvänder vi från när vi ritar ögat och därför sparar vi koordinaterna i variabler.

Vi importerar modulen `pygame` för att kunna använda funktionen `pygame.mouse.get_pos`.

Funktionen `update()` är tom så länge. Funktionen `draw()` ritar om skärmen vid varje uppdatering.

Koden så här långt &ndash; nya rader är markerade:
```python
import pgzrun
import pygame #nyrad
WIDTH, HEIGHT = 530, 400

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

pgzrun.go() # måste vara sist
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

    distance = math.sqrt(distance_x**2 + distance_y**2) #lägg detta under raden som räknar ut distance_y

    # etc.

    screen.draw.text(f"distance x: {str(distance_x)}\ndistance y: {str(distance_y)}\ndistance: {str(distance)}", (0, 0)) #ändrad
```

# Rörlig pupill

Vi vill att pupillen ska följa muspekaren.

Om muspekaren är innanför ögat är det lätt. Då kan vi sätta pupillen till muspekarens koordinater.

Då kan koden för `draw()` se ut så här. Den övriga koden är oförändrad.

```python
# behåll resten av koden

def draw():
    screen.fill((0, 0, 0))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    eye_x = 200
    eye_y = 200

    distance_x = mouse_x - eye_x
    distance_y = mouse_y - eye_y
    distance = math.sqrt(distance_x**2 + distance_y**2) # Pythagoras
    pupil_x = eye_x + distance_x #nyrad
    pupil_y = eye_y + distance_y #nyrad

    screen.draw.filled_circle((eye_x, eye_y), 50, color=(255, 255, 255))
    screen.draw.filled_circle((pupil_x, pupil_y), 15, color=(0, 0, 100))

# behåll resten av koden
```
Testa koden. Fungerar den bra när muspekaren är innanför ögats cirkel?

# Pupillen ska inte smita när muspekaren är utanför ögat

Hur vet vi att muspekaren är i ögat? Eftersom vi räknat ut avståndet från ögats centrum till muspekaren så kan vi använda ögats radie som en gräns, till exempel 30 pixlar. Vi ska ju plats att rita pupillen också.

Om muspekaren är mer än 30 pixlar från ögats centrum, placerar vi pupillen i kanten av ögat. Se bilden.

![image](https://user-images.githubusercontent.com/4598641/224125785-ee2eedc9-2155-4508-9fc2-d8518bfdfe32.png)

- Den streckade triangeln har hypotenusan 30 pixlar och den är likformig med den större triangeln med muspekaren i ena hörnet.
- Proportionen mellan den större och den streckade triangeln är `distance / 30` när muspekaren är utanför ögat.
- Vi får därför skala `distance_x` och `distance_y` med den skalfaktorn.
- Då kommer vi att kunna rita pupillen så att den alltid hamnar innanför ögats cirkel.

Så här kan `draw()` se ut nu:
```python
# behåll resten av koden

def draw():
    screen.fill((0, 0, 0))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    radius = 30 #nyrad
    eye_x = 200
    eye_y = 200

    distance_x = mouse_x - eye_x
    distance_y = mouse_y - eye_y
    distance = math.sqrt(distance_x**2 + distance_y**2) # Pythagoras
    
    if distance < radius: # innanför ögat
        pupil_x = eye_x + distance_x
        pupil_y = eye_y + distance_y
    else: # utanför ögat
        scale = radius / distance # se bilden
        pupil_x = eye_x + distance_x * scale
        pupil_y = eye_y + distance_y * scale

    screen.draw.filled_circle((eye_x, eye_y), 50, color=(255, 255, 255))
    screen.draw.filled_circle((pupil_x, pupil_y), 15, color=(0, 0, 100))

# behåll resten av koden
```

# Två ögon
Vi vill ha två ögon som följer muspekaren. Därför behöver vi återanvända samma kod.

Vi lägger koden i funktion som har ögats x- och y-koordinat som indata (parametrar).

Så här kan koden se ut nu:

```python
import pgzrun
import pygame
import math

WIDTH, HEIGHT = 530, 400

def update():
    pass

def draw():
    screen.fill((0, 0, 0))

    def draw_eye(eye_x, eye_y): # vi återanvänder denna
        radius = 30
        mouse_x, mouse_y = pygame.mouse.get_pos()

        distance_x = mouse_x - eye_x
        distance_y = mouse_y - eye_y
        distance = math.sqrt(distance_x**2 + distance_y**2)
        if distance < radius:
            pupil_x = eye_x + distance_x
            pupil_y = eye_y + distance_y
        else:
            scale = radius / distance # se bilden
            pupil_x = eye_x + distance_x * scale
            pupil_y = eye_y + distance_y * scale

        screen.draw.filled_circle((eye_x, eye_y), 50, color=(255, 255, 255))
        screen.draw.filled_circle((pupil_x, pupil_y), 15, color=(0, 0, 100))

    draw_eye(200, 200) # första ögat
    draw_eye(330, 200) # andra ögat

pgzrun.go()
```

# Källor

Originalprojekt: https://simplegametutorials.github.io/pygamezero/eyes/
