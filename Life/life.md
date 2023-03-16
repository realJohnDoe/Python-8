# Life
## En handledning för Python och Pygame Zero 1.2

![image](https://user-images.githubusercontent.com/4598641/225728407-f0313924-90f3-4f7e-83ce-43a6303881e7.png)

# Regler
Det finns ett rutnät av celler, där varje enskild cell antingen är levande eller död.

Efter varje tidssteg gäller att:
- Levande celler med exakt två eller tre levande grannar lever vidare.
- Döda celler med exakt tre levande grannar blir levande.

Alla andra celler dör eller förblir döda.

Skapa en första uppsättning med celler, tryck på valfri tangent för att gå framåt i tiden och observera.

## Kontroller
**Vänsterklick**	Gör cellen levande
**Högerklick**	Gör cellen död
**Vilken tangent som helst**	Gå ett steg framåt i tiden

# Översikt
Cellerna i rutnätet lagras som booleska värden: Sant för levande, Falskt för döda.

![image](https://user-images.githubusercontent.com/4598641/225729047-0f4814bc-6527-47b8-b600-dbbf810dd06b.png)

När tiden går framåt skapas ett nytt rutnät. Om cellerna i detta nya rutnät är levande eller döda baseras på det nuvarande rutnätet.

När det nya rutnätet är klart ersätts det nuvarande rutnätet med det nya rutnätet.

# Kodning
## Rita en cell

En cell ritas som en kvadrat.

```python
import pgzrun

def draw():
    screen.fill((255, 255, 255)) # vit färg

    screen.draw.filled_rect(
        Rect(
            (0, 0),
            (4, 4)
        ),
        color=(220, 220, 220)
    )

pgzrun.go()
```

![image](https://user-images.githubusercontent.com/4598641/225729369-04e983ca-eaa8-4009-9b71-fc3d247cf22f.png)


## Rita en rad med celler
En rad med celler ritas, med en pixel mellan varje cell.

```python
import pgzrun

def draw ():
    screen.fill (( 255 , 255 , 255 ))

    for x in range(70): #nyrad
        cell_size = 5 #nyrad
        cell_draw_size = cell_size - 1 #nyrad

        screen.draw.filled_rect(
            Rect(
                (x * cell_size, 0), #ändra
                (cell_draw_size, cell_draw_size) #nyrad
            ),
            color=(220, 220, 220)
        )

pgzrun.go()
```

![image](https://user-images.githubusercontent.com/4598641/225729839-7b0261e5-a2cc-4995-b1b2-d4db4d796737.png)

## Rita alla celler

Vi ritar alla raderna.

✏️ Uppdatera funktionen och testkör din kod.
>Glöm inte att dra in raderna under `for y`.

```python
def draw():
    screen.fill((255, 255, 255))

    for y in range(50): #nyrad
        for x in range(70):
            cell_size = 5
            cell_draw_size = cell_size - 1

            screen.draw.filled_rect(
                Rect(
                    (x * cell_size, y * cell_size), #nyrad
                    (cell_draw_size, cell_draw_size)
                ),
                color=(220, 220, 220)
            )
```

![image](https://user-images.githubusercontent.com/4598641/225730301-6313d4de-4505-417b-8dd3-6c138d1b2ea7.png)

## Markera celler

Cellpositionen som muspekaren är över lagras.

Detta beräknas genom att ta muspositionen och dividera den med cellstorleken och avrunda neråt.

Exempel: om musen har x-koordinat 17 och cellstorleken är 5, dividerar vi 17 med 5 vilket ger 3,4. Vi avrundar neråt och får 3.
Det betyder att musen är över cellen med ett index på 3 på X-axeln .

Cellstorleken behövs för att beräkna detta, så den flyttas till att vara en global variabel.

Vi skriver det värdet på skärmen för att testa.

Vi importerar modulen pygame så att pygame.mouse.get_pos kan användas.

Matematikmodulen importerar vi så att vi kan använda  math.floor.

XXXX



# Källor
Efter originalet på https://simplegametutorials.github.io/pygamezero/life/
