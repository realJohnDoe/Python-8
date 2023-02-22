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
- Spara text och tal i **variabler**
- Använda **funktioner** för att dela upp din kod i mindre bitar

## Testa!
Du kan testa ett färdigt projekt här: TODO

# Säg hej

It’s traditional to write a program to output ‘Hello world!’ when you learn a new programming language.

:pencil2: Öppna startprojektet i en ny flik i webbläsaren genom att högerklicka eller långklicka här: https://trinket.io/python/cb3c5d8930
![image](https://user-images.githubusercontent.com/4598641/219971993-cc7b2b07-d871-4bff-b6e3-6b234e0b1d43.png)

The line `#!/bin/python3` tells repl.it that you are using Python 3 (the latest version). The import lines tell Python that you are going to use code you didn’t write.

In Python, `print()` outputs text (words or numbers) to the screen.

Lines beginning with `#` are comments, they explain the code to humans and are ignored by Python.

:pencil2:
- Find the `# Put code to run below here` line.<br>
- Click below that line. The flashing `|` is the cursor and shows where you will type.<br>
- Type the code to `print()` hello:<br>

**main.py**
 
![image](https://user-images.githubusercontent.com/4598641/219972382-af779079-2354-4e10-aad4-0b1e1b8b7738.png)

> Test: Click on the Run button to run your code. In Trinket, the output will appear on the right:

![image](https://user-images.githubusercontent.com/4598641/220738163-1e3ba089-ba30-4492-9fe9-23cc645a244d.png)

> Debug: If you get an error then check your code really carefully. In this example, the single quotes around Hello are missing so Python doesn’t know it is supposed to be text.

![image](https://user-images.githubusercontent.com/4598641/220738431-406b3a27-805b-4fcc-82d7-e4e0ba9f5d9b.png)

In Python, a variable is used to store text or numbers. Variables make it easier for humans to read code. You can use the same variable in lots of places in your code.
Du kan också vara misstänksam när den oranga understrykningen visas.

We have included some variables that store emoji characters.

>In your Trinket, click on the emoji.py tab. Find the variable world, which stores the text ‘🌍🌍🌍’.<br>
>You can print() more than one item at a time by including a comma , in between the items. print() will add a space between each item.<br>
>Click on the main.py tab to go back to your print() code.<br>
>Change your code to also print() the contents of the world variable:

**main.py**

```python
#Put code to run under here
print(f"Hello {world}")
```

Tips: Hej är en textsträng. Klamrarna runt {world} betyder att vi vill skriva ut variabelns värde, ’🌍🌍🌍’
Tip: 'Hello' is a text string because it has single quotes around it, whereas world is a variable so the value stored in it will be printed.
![image](https://user-images.githubusercontent.com/4598641/220739447-a48012ec-df89-4ee7-9db6-526bfb291139.png)

![image](https://user-images.githubusercontent.com/4598641/220739616-55e9dca1-4bf7-420a-95da-0fd2f12d8116.png)

![image](https://user-images.githubusercontent.com/4598641/220739775-da61c759-eae4-42cd-9f96-5b13c3f7ce3b.png)


# Källor

[^1]: This is a Swedish translation of the Raspberry Pi Foundation project https://projects.raspberrypi.org/en/projects/hello-world, with minor adaptations.
