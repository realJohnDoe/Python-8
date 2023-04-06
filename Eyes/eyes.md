# Ögon

![image](https://user-images.githubusercontent.com/4598641/223815678-2c97174e-578c-4df4-9f8a-d8764f0b2424.png)

Vi vill göra en animering där ögonen följer muspekaren.

## Innehåll
[Rita ett öga](#rita-ett-öga)
&bull; [Räkna ut avståndet mellan muspekaren och ögat](#räkna-ut-avståndet-mellan-muspekaren-och-ögat)
&bull; [Räkna ut avståndet mellan muspekaren och ögat](#räkna-ut-avståndet-mellan-muspekaren-och-ögat)
&bull; [Rörlig pupill](#rörlig-pupill)
&bull; [Pupillen ska inte smita när muspekaren är utanför ögat](#pupillen-ska-inte-smita-när-muspekaren-är-utanför-ögat)
&bull; [Två ögon](#två-ögon)
&bull; [Utmaningar](#utmaningar)
&bull; [Källor](#källor)

# Rita ett öga
Ögat ritas med en vit cirkel och en lite mindre, mörkblå cirkel för pupillen.
>Vi använder `screen` från Pygame Zero för att rita.

![image](https://user-images.githubusercontent.com/4598641/223816876-1da49223-c7af-46d5-836c-9b1216eb52d4.png)

Koden så här långt:
```python
import pgzrun
WIDTH, HEIGHT = 530, 400

def draw():
    screen.fill((0, 0, 0))

    screen.draw.filled_circle((200, 200), 50, color=(255, 255, 255))
    screen.draw.filled_circle((200, 200), 15, color=(0, 0, 100))

pgzrun.go() # måste vara sist
```

✏️ Se till att du är inloggad i repl.it. Gör en kopia av startprojektet https://replit.com/@RobertStorlind/eyes-starter
med knappen "Fork". Testkör!

# Räkna ut avståndet mellan muspekaren och ögat
Vi lägger till kod så att avståndet mellan ögats mitt och muspekaren visas, räknat i pixlar.

- Ögats x- och y-koordinater återanvänder vi från när vi ritar ögat och därför sparar vi koordinaterna i variabler.
- Vi importerar modulen `pygame` för att kunna använda funktionen `pygame.mouse.get_pos`.
- Funktionen `update()` är tom så länge. Funktionen `draw()` ritar om skärmen vid varje uppdatering.

✏️ **Mata in** och testkör koden!

Koden så här långt &ndash; nya rader är markerade:

```python
import pgzrun
import pygame #nyrad 👀
WIDTH, HEIGHT = 530, 400

def update():
    pass

def draw():
    screen.fill((0, 0, 0))

    mouse_x, mouse_y = pygame.mouse.get_pos() #nyrad 👀
    eye_x = 200 #nyrad 👀
    eye_y = 200 #nyrad 👀

    distance_x = mouse_x - eye_x #nyrad 👀
    distance_y = mouse_y - eye_y #nyrad 👀

    screen.draw.filled_circle((eye_x, eye_y), 50, color=(255, 255, 255)) #lite ändrad 👀
    screen.draw.filled_circle((200, 200), 15, color=(0, 0, 100))

    screen.draw.text(f"distance x: {distance_x}\ndistance y: {distance_y}", (0, 0)) #nyrad 👀

pgzrun.go() # måste vara sist
```


![image](https://user-images.githubusercontent.com/4598641/223817639-1363643f-481d-44e3-979b-d0b48eb0c9da.png)


# Räkna ut avståndet mellan muspekaren och ögat
Avståndet, `distance`, kan vi räkna ut med Pythagoras sats. Se figuren.

![image](https://user-images.githubusercontent.com/4598641/224125785-ee2eedc9-2155-4508-9fc2-d8518bfdfe32.png)

Avståndet i pixlar är roten ur (antalet pixlar i X-led i kvadrat + antalet pixlar i Y-led i kvadrat).
- Operatorn `**2` är upphöjt till 2, alltså kvadraten
- Vi importerar mattemodulen `math` för att räkna roten ur med `math.sqrt()`.

```python
import pgzrun
import pygame
import math  # nyrad 👀

WIDTH, HEIGHT = 530, 400

def update():
    pass

def draw():
    screen.fill((0, 0, 0))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    eye_x = 200
    eye_y = 200

    distance_x = mouse_x - eye_x
    distance_y = mouse_y - eye_y
    distance = math.sqrt(distance_x**2 + distance_y**2)  # nyrad 👀

    screen.draw.filled_circle(
        (eye_x, eye_y), 50, color=(255, 255, 255))
    screen.draw.filled_circle((200, 200), 15, color=(0, 0, 100))

    screen.draw.text(
        f"distance x: {distance_x}\ndistance y: {distance_y}\ndistance: {distance}", (0, 0))  # ändrad 👀

pgzrun.go()  # måste vara sist
```

:pencil2: **Uppdatera** och testkör koden!


# Rörlig pupill

Vi vill att pupillen ska följa muspekaren.

Om muspekaren är innanför ögat är det lätt. Då kan vi sätta pupillen till muspekarens koordinater.

Då kan koden för `draw()` se ut så här. Den övriga koden är samma som innan.

```python
# behåll resten av koden

def draw(): #funktionen är uppdaterad 👀
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
:pencil2: **Uppdatera och testa** din kod. Fungerar den bra när muspekaren är innanför ögats cirkel?

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun
import pygame
import math  

WIDTH, HEIGHT = 530, 400


def update():
    pass


def draw(): #funktionen är uppdaterad 👀
    screen.fill((0, 0, 0))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    eye_x = 200
    eye_y = 200

    distance_x = mouse_x - eye_x
    distance_y = mouse_y - eye_y
    distance = math.sqrt(distance_x**2 + distance_y**2) # Pythagoras
    pupil_x = eye_x + distance_x #nyrad 👀
    pupil_y = eye_y + distance_y #nyrad 👀

    screen.draw.filled_circle((eye_x, eye_y), 50, color=(255, 255, 255))
    screen.draw.filled_circle((pupil_x, pupil_y), 15, color=(0, 0, 100))


pgzrun.go()  # måste vara sist
```
    
</details>

# Pupillen ska inte smita när muspekaren är utanför ögat

🤔 Hur vet vi att muspekaren är i ögat? Eftersom vi räknat ut avståndet från ögats centrum till muspekaren så kan vi använda ögats radie som en gräns, till exempel 30 pixlar. Vi ska ju plats att rita pupillen också.

Om muspekaren är mer än 30 pixlar från ögats centrum, placerar vi pupillen i kanten av ögat. Se bilden.

![image](https://user-images.githubusercontent.com/4598641/224125785-ee2eedc9-2155-4508-9fc2-d8518bfdfe32.png)

- Den streckade triangeln har hypotenusan 30 pixlar och den är likformig med den större triangeln med muspekaren i ena hörnet.
- Proportionen mellan den större och den streckade triangeln är `30 / distance` när muspekaren är utanför ögat.
- Vi får därför skala `distance_x` och `distance_y` med den skalfaktorn när vi ska räkna ut pupillens x- och y-koordinater.
- Då kommer vi att kunna rita pupillen så att den alltid hamnar innanför ögats cirkel.

Så här kan `draw()` se ut nu:

```python
# behåll resten av koden

def draw(): #uppdaterad 👀
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
:pencil2: **Uppdatera och testa koden.** Fungerar den bra när muspekaren är innanför ögats cirkel?

<details>
  <summary>📝 Så här ser hela koden ut nu</summary>
  
```python
import pgzrun
import pygame
import math

WIDTH, HEIGHT = 530, 400


def update():
    pass


def draw():  # uppdaterad 👀
    screen.fill((0, 0, 0))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    radius = 30  # nyrad
    eye_x = 200
    eye_y = 200

    distance_x = mouse_x - eye_x
    distance_y = mouse_y - eye_y
    distance = math.sqrt(distance_x**2 + distance_y**2)  # Pythagoras

    if distance < radius:  # innanför ögat
        pupil_x = eye_x + distance_x
        pupil_y = eye_y + distance_y
    else:  # utanför ögat
        scale = radius / distance  # se bilden
        pupil_x = eye_x + distance_x * scale
        pupil_y = eye_y + distance_y * scale

    screen.draw.filled_circle((eye_x, eye_y), 50, color=(255, 255, 255))
    screen.draw.filled_circle((pupil_x, pupil_y), 15, color=(0, 0, 100))


pgzrun.go()  # måste vara sist
```
    
</details>

# Två ögon
Vi vill ha två ögon som följer muspekaren. Vi kan återanvända samma kod. Därför lägger vi ögats kod
i funktionen `draw_eye` som har ögats x- och y-koordinat som indata/parametrar.

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

    def draw_eye(eye_x, eye_y): # vi återanvänder denna 👀 
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

    draw_eye(200, 200) # första ögat 👀
    draw_eye(330, 200) # andra ögat 👀

pgzrun.go()
```
:pencil2: **Uppdatera och testa koden.** Fungerar den bra när muspekaren är innanför ögats cirkel?

# Utmaningar
Kan du göra det ännu mer spännande? Kan du förbättra koden?

* Uträkningen av scale går att göra om så att vi får ännu färre kodrader. Kan du komma på hur?[^1]                          
* Kan du få ögonen att byta färg, försvinna eller röra sig?
* Kan du lägga in någon annan slags figur och få ögonen att följa den figuren istället för muspekaren?

# Mer om Pygame Zero 

screen.draw()

screen.fill()

pygame.mouse.get_pos()

# Källor

Detta är en anpassning till repl.it av originalprojektet https://simplegametutorials.github.io/pygamezero/eyes/

[1]: Vad kan du sätta `scale` till när `distance < radius`?

                            
