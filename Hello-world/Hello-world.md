# Hello 🌍🌎🌏

## Detta kommer du att göra
- Säga **hej**
- Summor och datum
- Rulla en tärning
- Påbörja en mening
- Kunskapsquiz
- Levla upp ditt projekt
- Nästa steg

# Inledning
Detta är projekt 1 av 6 i kursen *Introduction to Python: Variables, functions, and loops* från Raspberry Pi Foundation[^1].

## Detta kommer du att göra
Ta reda på vad programmeringsspråket Python kan göra, genom att koda ett interaktivt projekt som använder emoji.

> **Emoji** are small colourful images used to add extra meaning to messages. Emoji means ‘picture word’ in Japanese.

Du kommer att:
- Skriva ut text och emoji med `print()` och få `input()` från användaren
- Spara text och tal i **variables**
- Använda **funktioner** för att dela upp din kod i mindre bitar

## Testa!
Du kan testa ett färdigt projekt här: TODO

Startprojekt: https://trinket.io/python/cb3c5d8930

# Säg hej

It’s traditional to write a program to output ‘Hello world!’ when you learn a new programming language.

> FIXA Bildexempel

The line `#!/bin/python3` tells repl.it that you are using Python 3 (the latest version). The import lines tell Python that you are going to use code you didn’t write.

In Python, `print()` outputs text (words or numbers) to the screen.

Lines beginning with `#` are comments, they explain the code to humans and are ignored by Python.

> Find the `# Put code to run below here` line.
> Click below that line. The flashing `|` is the cursor and shows where you will type.
> Type the code to `print()` hello:
> main.py

FIXA: skärmdump

> Test: Click on the Run button to run your code. In Trinket, the output will appear on the right:

FIXA: skärmdump

> Debug: If you get an error then check your code really carefully. In this example, the single quotes around Hello are missing so Python doesn’t know it is supposed to be text.

FIXA: skärmdump

In Python, a variable is used to store text or numbers. Variables make it easier for humans to read code. You can use the same variable in lots of places in your code.

We have included some variables that store emoji characters.

> In your Trinket, click on the emoji.py tab. Find the variable world, which stores the text ‘🌍🌍🌍’.

>You can print() more than one item at a time by including a comma , in between the items. print() will add a space between each item.

>Click on the main.py tab to go back to your print() code.

> Change your code to also print() the contents of the world variable:

> main.py

```python
#Put code to run under here
print(f"Hello {world}")
```

Tip: 'Hello' is a text string because it has single quotes around it, whereas world is a variable so the value stored in it will be printed.


# Källor


[^1]: This is a Swedish translation of the Raspberry Pi Foundation project https://projects.raspberrypi.org/en/projects/hello-world, with minor adaptations.
