# Hello 🌍🌎🌏

## Detta kommer du att göra
- [Säga hej](#säg-hej)
- [Summor och datum](#summor-och-datum)
- Rulla en tärning
- Påbörja en mening
- Kunskapsquiz
- Levla upp ditt projekt
- Nästa steg

# Inledning
Detta är projekt 1 av 6 i kursen *Introduction to Python: Variables, functions, and loops* från Raspberry Pi Foundation[^1].

## Detta kommer du att göra
Ta reda på vad programmeringsspråket Python kan göra, genom att koda ett interaktivt projekt som använder emoji.

> **Emoji** är små färgglada bilder som ger extra innebörd till en text. Emoji betyder 'bild-tecken' på japanska.

Du kommer att:
- Skriva ut text och emoji med `print()` och få `input()` från användaren
- Spara text och tal i **variabler**
- Använda **funktioner** för att dela upp din kod i mindre bitar

## Testa!
Du kan testa ett färdigt projekt här: TODO

# Säg hej

Det är en tradition att skriva ett program som säger "Hej världen" när man lär sig ett nytt programspråk.

:pencil2: Öppna startprojektet i en ny flik i webbläsaren genom att högerklicka eller långklicka här: https://trinket.io/python/cb3c5d8930
![image](https://user-images.githubusercontent.com/4598641/219971993-cc7b2b07-d871-4bff-b6e3-6b234e0b1d43.png)

Raden `#!/bin/python3` berättar för repl.it att du använder Python 3, senaste versionen av Python.
Raderna med `import` berättar för Python att du ska använda kod som du inte skrivit själv.

I Python används `print()` för att skriva ut text (ord eller siffror) på skärmen. 

Rader som börjar med `#` är kommentarer. De förklarar koden för människor och ignoreras av Python.

:pencil2:
- Hitta kodraden `# Skriv koden som ska köras här nedanför`<br>
- Klicka på raden under. Det blinkande strecket `|` är markören och visar var du skriver just nu.<br>
- Mata in koden för att skriva **hej**<br>

**main.py**
 
![image](https://user-images.githubusercontent.com/4598641/219972382-af779079-2354-4e10-aad4-0b1e1b8b7738.png)

> Testa din kod: klicka på knappen knappen Run högst upp i repl.it-fönstret så visas resultatet till höger:

![image](https://user-images.githubusercontent.com/4598641/220738163-1e3ba089-ba30-4492-9fe9-23cc645a244d.png)

> Leta fel: om du får en felutskrift, kontrollera din kod noga. I exemplet här under, fattas citattecknen runt hej och Python förstår då inte vad som menas. Du kan också vara misstänksam när den oranga understrykningen visas.

![image](https://user-images.githubusercontent.com/4598641/220738431-406b3a27-805b-4fcc-82d7-e4e0ba9f5d9b.png)

I Python används variabler för att spara text eller tal. Variabler gör det lättare för människor att läsa koden. Du kan använda samma variabel på många ställen i din kod.

Vi har förberett några variabler som innehåller emoji-tecken.

:pencil2:
>I repl.it kan du klicka till vänster på fliken `emoji.py`. Hitta variabeln *world*, som innehåller texten ‘🌍🌍🌍’.<br>
>Du kan skriva ut mer än en sak i taget genom att lägga till det innanför citattecknen. Lägg till mellanslag där det behövs.
>Klicka på fliken `main.py` för att komma tillbaks till din kod.<br>
>Ändra din kod så att den också skriver ut variabeln *world*.
>Lägg till ett **f** före citattecknet så vet Python att du vill använda variabler i din sträng.

**main.py**

```python
# Skriv koden som ska köras här nedanför
print(f"Hej {world}")
```

Tips: Hej är en textsträng. Klamrarna runt {world} betyder att vi vill skriva ut variabelns värde, ’🌍🌍🌍’.
![image](https://user-images.githubusercontent.com/4598641/220739447-a48012ec-df89-4ee7-9db6-526bfb291139.png)

![image](https://user-images.githubusercontent.com/4598641/220739616-55e9dca1-4bf7-420a-95da-0fd2f12d8116.png)

:pencil2:
Lägg till en ny rad för att skriva ut en till text och emoji:

**main.py**

![image](https://user-images.githubusercontent.com/4598641/221403615-05239dfc-f84e-4dbb-bb03-f2e88f2d9006.png)

Tips: Koden du behöver skriva in är markerad. Koden utan markering hjälper dig att hitta var den nya koden ska hamna.

Testa: Klicka på Run.

![image](https://user-images.githubusercontent.com/4598641/220739775-da61c759-eae4-42cd-9f96-5b13c3f7ce3b.png)

Felsök: Kontrollera noga parenteser, citattecken och stavning. Python är väldigt petigt.

Om du har ett konto på repl.it, kan du klicka på Remix och spara en egen kopia av projektet i din repl.it.

# Summor och datum

Python is great at working with numbers and dates.
![image](https://user-images.githubusercontent.com/4598641/221425501-a8fa5bed-d694-4529-a28b-8ad465316482.png)

The output area with five printed lines showing new sum and current date outputs.

In Python you can use maths operators to do sums:

| Symbol | Räknesätt |
| ------------- | ------------- |
| `+` | addition  |
| `-` | subtraktion |
| `*`	| multiplikation |
| `/`	| division |
| `**` | upphöjt till |

Add another two print() lines to your code including a sum for Python to work out:

**main.py**
```python
print('Hello', world)
print('Welcome to', python)
print(python, 'is very good at', sums)
print(230 * 5782 ** 2 / 23781)
```

Test: Run your code. Did Python calculate the sum correctly? Only joking! Python does the hard maths for you so you don’t need to work it out.

>Japanese computer scientist Emma Haruka Iwao used a computer to calculate the value of Pi (π) to 31 trillion digits. That answer is so long that it would >take over 300,000 years just to say it!


Try changing the sum that Python does to a complicated one!

You can also use brackets if you want to control the order that Python calculates the sum: 

```print( (2 + 4) * (5 + 3) )
```

Test: Run your code and get Python to calculate your sum.

Debug: Make sure your sum has a left and right round bracket around it ( 2 * 45 ). If you use extra brackets to control the order, make you have a right bracket to match every left bracket.


If you have asked Python to calculate a really big sum, you might find the answer goes across multiple lines in the output area.

Tip: Click on the hamburger menu (the icon with three lines) in the top-left of your Trinket editor. Then click on the Fullscreen button to view your project in fullscreen mode.

![image](https://user-images.githubusercontent.com/4598641/221425982-34cc44ef-02fe-4d99-ba27-1787921c3b3d.png)

The Trinket editor with left-hand side menu expanded, via the hamburger menu, to show the fullscreen option.

To exit fullscreen mode, click on the Fullscreen button again or press Esc on your keyboard.

The line `from datetime import *` at the top of the main.py tab includes a library with helpful functions for getting the current date and time.

>One of the great things about Python is all the libraries of code that are available to use. A Python library allows you to easily use code that other people have written. There are libraries for drawing charts and graphs, making art, doing calculations, and lots more.


Add another line to your code to print some more text and the emoji variables calendar and clock.

Get the current date and time by using the now() function from the datetime library:

**main.py**
```
print(python, 'is very good at', sums)
print(230 * 5782 ** 2 / 23781) #Print the result of the sum
print('The', calendar, clock, 'is', datetime.now()) #Print with emoji
```

Tip: You don’t need to type the comments, they are just there to help you understand the code. Just type the part before the #.


Test: Run your code a couple of times to see the date and time update.

Debug: Check that you have a fullstop . between datetime and now. Check all the punctuation carefully.

💾 **Spara** ditt projekt!

# Källor

[^1]: This is a Swedish translation of the Raspberry Pi Foundation project https://projects.raspberrypi.org/en/projects/hello-world, with minor adaptations.
