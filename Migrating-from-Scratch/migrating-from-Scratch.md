# Migrating from Scratch
>Detta är en svensk översättning av Daniel Popes guide, https://pygame-zero.readthedocs.io/en/stable/from-scratch.html


This tutorial will compare an implementation of Flappy Bird written in Scratch with one written in Pygame Zero. The Scratch and Pygame Zero programs are similar to a remarkable extent.

The Pygame Zero version can be found in Pygame Zero repository.

You can also download the Scratch 1.4 version and Scratch 3 version from the repository.

The Pygame Zero version includes scoring logic, which is omitted in the code examples on this page to make it a closer comparison.

The Python code shown below is re-arranged for clarity within the examples.

The stage
Here’s how the stage is laid out in our Scratch program:

<img src="https://pygame-zero.readthedocs.io/en/stable/_images/flappybird-stage.png" />

There are just three objects, aside from the background: the bird, and the top and bottom pipes.

This corresponds to the Pygame Zero code setting these objects up as Actors:

```python
bird = Actor('bird1', (75, 200))
pipe_top = Actor('top', anchor=('left', 'bottom'))
pipe_bottom = Actor('bottom', anchor=('left', 'top'))
```

In Pygame Zero we also have to ensure we draw these objects. In principle this gives a little more flexibility about how to draw the scene:

```python
def draw():
    screen.blit('background', (0, 0))
    pipe_top.draw()
    pipe_bottom.draw()
    bird.draw()
```

# Källor
https://pygame-zero.readthedocs.io/en/stable/from-scratch.html
