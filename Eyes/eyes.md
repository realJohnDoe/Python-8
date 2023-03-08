# Ögon

![image](https://user-images.githubusercontent.com/4598641/223815678-2c97174e-578c-4df4-9f8a-d8764f0b2424.png)

Ögonen följer muspekaren.

# Rita ett öga
The eye is drawn with a white circle and a smaller dark blue circle for the pupil.

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
The distance between the center of the eye and the mouse cursor is displayed.

The X and Y positions of the eye are reused from drawing the eye, so variables are made for them.

The pygame module is imported so that pygame.mouse.get_pos can be used.

An empty update function is created so that the draw function will update on every frame.

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
The distance in a straight line is calculated using the Pythagorean theorem.

The square root of the distance on the X axis squared plus the distance on the Y axis squared is the distance in a straight line.

The math module is imported so that math.sqrt can be used.

```python
import math #lägg detta överst

def draw():
    # Ändra i draw. Behåll oförändrade rader!

    distance = math.sqrt(distance_x**2 + distance_y**2) #ändra den här raden

    # etc.

    screen.draw.text(f"distance x: {str(distance_x)}\ndistance y: {str(distance_y)}\ndistance: {str(distance)}", (0, 0)) #ändrad
```

# Så här ser slutversionen ut, utan trig-funktioner

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
        distance = math.sqrt(distance_x**2 + distance_y**2)
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
