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


# Källor

Originalprojekt: https://simplegametutorials.github.io/pygamezero/eyes/
