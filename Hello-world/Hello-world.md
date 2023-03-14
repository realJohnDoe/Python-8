# Hello 🌍🌎🌏

## Detta kommer du att göra
- [Säga hej](#säg-hej)
- [Summor och datum](#summor-och-datum)
- [Kasta en tärning](#kasta-en-tärning)
- [Påbörja en mening](#påbörja-en-mening)
- [Kunskapsquiz](#kunskapsquiz)
- [Levla upp ditt projekt](#levla-upp-ditt-projekt)

# Inledning
Detta är projekt nr 1 ur kursen *Introduction to Python: Variables, functions, and loops* från Raspberry Pi Foundation[^1].

## Detta kommer du att göra
Ta reda på vad programmeringsspråket Python kan göra, genom att koda ett interaktivt projekt som använder emoji.

> **Emoji** är små färgglada bilder som ger extra innebörd till en text. Emoji betyder 'bild-tecken' på japanska.

Du kommer att:
- Skriva ut text och emoji med `print()` och få `input()` från användaren
- Spara text och tal i **variabler**
- Använda **funktioner** för att dela upp din kod i mindre bitar

# Säg hej

Det är en tradition att skriva ett program som säger "Hej världen" när man lär sig ett nytt programspråk.

![image](https://user-images.githubusercontent.com/4598641/220739775-da61c759-eae4-42cd-9f96-5b13c3f7ce3b.png)

:pencil2: Se till att du är inloggad i repl.it.

Öppna startprojektet i en ny flik i webbläsaren genom att högerklicka eller långklicka här: 
https://replit.com/@RobertStorlind/Hello-Starter

Spara en egen kopia av startprojektet med knappen
![image](https://user-images.githubusercontent.com/4598641/225108391-32f24ead-3eb1-4ffb-ad3a-9c18ce5849bb.png)

---

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

🧪 **Testa din kod:** klicka på knappen knappen Run högst upp i repl.it-fönstret så visas resultatet till höger:

![image](https://user-images.githubusercontent.com/4598641/220738163-1e3ba089-ba30-4492-9fe9-23cc645a244d.png)

🤔 **Leta fel:** om du får en felutskrift, kontrollera din kod noga. I exemplet här under, fattas citattecknen runt hej och Python förstår då inte vad som menas. Du kan också vara extra misstänksam när den oranga understrykningen visas.

![image](https://user-images.githubusercontent.com/4598641/220738431-406b3a27-805b-4fcc-82d7-e4e0ba9f5d9b.png)

I Python används variabler för att spara text eller tal. Variabler gör det lättare för människor att läsa koden. Du kan använda samma variabel på många ställen i din kod.

Vi har förberett några variabler som innehåller emoji-tecken.

:pencil2:
- I repl.it kan du klicka till vänster på fliken `emoji.py`. Hitta variabeln *world*, som innehåller texten ‘🌍🌍🌍’.<br>
- Du kan skriva ut mer än en sak i taget genom att lägga till det innanför citattecknen. Lägg till mellanslag där det behövs.
- Klicka på fliken `main.py` för att komma tillbaks till din kod.<br>
- Ändra din kod så att den också skriver ut variabeln *world*.
- Lägg till ett **f** före citattecknet så vet Python att du vill använda variabler i din sträng.

**main.py**

```python
# Skriv koden som ska köras här nedanför
print(f"Hej {world}")
```

**Tips:** Hej är en textsträng. Klamrarna runt {world} betyder att vi vill skriva ut variabelns värde, ’🌍🌍🌍’.
![image](https://user-images.githubusercontent.com/4598641/220739447-a48012ec-df89-4ee7-9db6-526bfb291139.png)

![image](https://user-images.githubusercontent.com/4598641/220739616-55e9dca1-4bf7-420a-95da-0fd2f12d8116.png)

:pencil2:
Lägg till en ny rad för att skriva mer text och emoji:

**main.py**
```python
print(f"Hello {world}")
print(f"Welcome to {python}") # Lägg till den här raden
```

**Tips:** Koden du behöver skriva in är markerad. Koden utan markering hjälper dig att hitta var den nya koden ska hamna.

🧪 **Testa:** Klicka på Run.

![image](https://user-images.githubusercontent.com/4598641/220739775-da61c759-eae4-42cd-9f96-5b13c3f7ce3b.png)

🤔 **Leta fel:** Kontrollera noga parenteser, citattecken och stavning. Python är väldigt petigt.

💾 Om du har ett konto på repl.it, kan du klicka på Remix och spara en egen kopia av projektet i din repl.it.

# Summor och datum

Python är bra på tal och datum.

![image](https://user-images.githubusercontent.com/4598641/225109246-7ddecc59-4ac9-4b3d-91a8-9f393704e4f3.png)

I Python använder du matematiska symboler för uträkningar:

| Symbol | Räknesätt |
| ------ | --------- |
| `+`    | addition  |
| `-`    | subtraktion |
| `*`	   | multiplikation |
| `/`	   | division |
| `**`   | upphöjt till |

Lägg till två `print()`-rader till i din kod där den ena är en räkneuppgift för Python.

**main.py**
```python
print(f"Hello {world}")
print(f"Welcome to {python}")
print(f"{python} is very good at {sums}")
print(230 * 5782 ** 2 / 23781)
```

🧪 **Testa:** Kör din kod. Räknade Python rätt på uppgiften? Skojar bara! Python gör de svåra uträkningarna så slipper du.

>Den japanska datalogen Emma Haruka Iwao använde en dator för räkna ut värdet på pi (π) med 31 biljoner siffror. Svaret är så långt att det skulle ta över 300 000 år bara att säga det!

:pencil2: Pröva att ändra uträkningen som Python gör till något krångligare!

Du kan också använda parenteser om du vill ändra prioritetsordningen för uträkningen:

```python
print( (2 + 4) * (5 + 3) )
```

🧪 **Testa:** Kör din kod och låt Python räkna ut svaret åt dig.

🤔 **Leta fel:** Kontrollera att din uträkning har vänster- och högerparenteser på rätt plats. Om du använder extra parenteser för att ändra ordningen, kontrollera att du har matchande vänster- och högerparenteser.

Om du ber Python att göra en riktigt stor uträkning kan det hända att svaret tar flera rader i terminalfönstret.

**Tips:** Klicka på de tre prickarna uppe till höger för att få fram menyn. Där kan du välja Maximize för att få ett stort terminalfönster.

![image](https://user-images.githubusercontent.com/4598641/225109587-2e6252e3-7762-4564-901f-f1fc582312db.png)

För att gå ur helskärmsläge, välj Restore i menyn med tre prickar.

![image](https://user-images.githubusercontent.com/4598641/225109859-abe76664-aed9-48fe-b74e-6180e5ea99d7.png)

Raden `from datetime import *` överst i fliken `main.py` hämtar ett bibliotek med användbara funktioner för att hämta datum och tid.

>En av de bästa sakerna med Python är alla kodbibliotek som man kan använda. Ett Pythonbibliotek låter dig lätt använda kod som andra har skrivit. Det finns bibliotek för att rita diagram och grafer, göra konst, göra uträkningar och mycket annat.

✏️ Lägg till en rad i din kod som skriver lite mer text och emoji-variablerna `calendar` och `clock`.

Hämta aktuellt datum och aktuell tid med funktionen `now()` i **datetime**-biblioteket.

**main.py**
```
print(f"{python} är mycket bra på {sums}")
print(230 * 5782 ** 2 / 23781) # Skriv resultatet av uträkningen
print(f"{calendar} {clock} är {datetime.now()}") # Skriv med emoji
```

**Tips:** du behöver inte mata in kommentarerna; de är till för att du ska förstå koden. Det räcker att skriva det som står före `#`.

🧪 **Testa:** kör din kod några gånger för att se att tiden uppdateras.

🤔 **Leta fel:** Kolla att du har en punkt (.) mellan `datetime` och `now`. Kolla noga att skiljetecknen är rätt.

💾 **Spara** ditt projekt!

# Kasta en tärning
Python kan generera slumptal som man kan ha till en digital tärning.

![image](https://user-images.githubusercontent.com/4598641/225118079-4ccafd48-d670-46b2-bbcb-72d69cbbe417.png)

I Python **kallar du på**, anropar, en **funktion** för att göra något. Du har redan använt funktionen `print()` för att skriva ut text.

Du kan **definiera** en ny funktion för att gruppera ihop kod &ndash; du ger koden ett namn och kan sen använda den flera gånger.

✏️ Funktioner måste definieras innan du kan anropa dem. Leta upp kommentaren (#) högt upp i fliken main.py med texten "# Definiera funktioner här nedanför"

Definiera en ny funktion som heter `roll_dice()` som använder funktionen `randint()` från biblioteket `random` för att generera ett slumpmässigt heltal mellan 1 och 6 och skriva ut talet på skärmen. *int* är en förkortning av *integer*, som betyder heltal på engelska

**main.py**
```python
# Definiera funktioner här nedanför

def roll_dice(): # Glöm inte kolon i slutet av den här raden
  print(f"{python} kan kasta {dice}")
  print(f"Du rullade {randint(1, 6)}")
```

Raderna under `def roll_dice():` är indragna. För att göra indrag kan du använda Tab-tangenten på tangentbordet; den finns oftast ovanför Caps Lock till vänster. Indraget talar om för Python att raderna med indrag hör till funktionen.

**Tips:** Understrykningen `_` används mellan ord i variabler och funktionsnamn i Python för att göra dem mer lättlästa. Man kan inte ha mellanslag i variabel- och funktionsnamn.

🧪 **Testa:** Om kör du din kod nu med Run, kommer den inte att rulla någon tärning. Det är för att du har definierat funktionen `roll_dice()` men inte anropat den än.

✏️ För att använda en funktion behöver du anropa den i koden. Gå till slutet av din kod och lägg till ett anrop till funktionen `roll_dice()`.

**main.py**
```python
print(f"{calendar} {clock} är {datetime.now()}")

roll_dice() # Anropa funktionen
```

🧪 **Testa:** Kör ditt projekt flera gånger för att se det slumpmässiga tärningskastet varje gång.

🤔 **Leta fel:** Kolla att du har en understrykning `_` mellan `roll` och `dice` i funktionsnamnet. Kolla att du har ett kolon (:) i slutet på raden.

🤔 **Leta fel:** Kolla att raderna under `def roll_dice()` är indragna. Det är lätt att det blir fel i Python, så kolla noga.

![image](https://user-images.githubusercontent.com/4598641/221656767-bfb7b85f-cb00-4915-8712-e22f5f6918b9.png)

>Slumptal har vi nytta av inom kryptografi, datavetenskap och för att göra spel och datorkonst mer omväxlande. Datorer genererar slumptal med en algoritm. För att få äkta slumptal behövs en oförutsägbar källa från omgivningen utanför datorn.

Variabeln `fire` innehåller emojin 🔥. Koden `print(fire * 3)` skriver ut tre eld-emoji: ’🔥🔥🔥’. Du behöver skriva ut samma antal emoji som tärningskastet.

<details>
  <summary>🔥🤔 Vad händer om du skriver `print(fire * randint(1, 6))`?</summary>
  
  Då får du ett nytt slumptal som oftast inte är samma som det första du fick.
</details>

Hmm, hur kan du göra så att du använder samma slumptal?

✏️ Ändra din kod så att den sparar värdet från `randint()` i variabeln `roll` och sen använder den variabeln för att skriva ut tärningskastet med rätt antal 🔥-emoji.

**main.py**
```python
# Definiera funktioner här nedanför

def roll_dice():
  print(f"{python} kan kasta {dice}")
  roll = randint(1, 6) # Generera ett slumptal mellan 1 och 6
  print(f"Du kastade {roll}") # Skriv ut variabelns värde
  print(fire * roll) # Upprepa eld-emojin så det stämmer med tärningskastet
```

Du kan använda en stjärna eller ett hjärta istället för eld om du så vill.

Symbolen `*` betyder multiplikation så `fire * roll` multiplicerar texten i eld-variabeln (’🔥’) med talet i variabeln `roll`.

🧪 **Testa:** Testa ditt projekt några gånger. Övertyga dig om hur koden fungerar.

**Tips:** Variabler är bra när du behöver samma värde flera gånger i din kod. Att ge variabler bra namn gör också din kod lättare att förstå.
>Att sätta bra namn på saker är en av de svåraste sakerna när man programmerar.

✏️ Uppgradera din tärning så att användaren kan välja det högsta värdet (antalet sidor).

>Många spel använder tärningar med många sidor. I verkligheten består tärningar av regelbundna geometriska figurer. Vanliga tärning är D6, D12 och D20. På datorn kan du generera slumptal som motsvarar en tärning med vilket antal sidor som helst.

✏️ Funktionen `input()` frågar användare och skickar sen tillbaks svaret.

Lägg till kod för att 
1. fråga användaren om största talet på hens tärning och 
2. spara sen resultatet i varabeln `max` och 
3. skriv ut det i terminalfönstret:

**main.py**
```python
# Definiera funktioner här nedanför

def roll_dice():
  print(f"{python} kan kasta {dice}")
  max = input('Hur många sidor?:') # Vänta på inmatning från användaren
  print(f"Det är en D{max}") # Använd värdet som matades in
  roll = randint(1, 6)
  print(f"Du kastade {roll}")
  print(fire * roll)
```

Ändra din `roll`-variabel så att koden använder `max` som största värdet i `randint` när vi genererar ett slumptal.

När du får input from användaren behandlar Python det som text. Men funktionen `randint` behöver ett heltal (integer). 
Funktionen `int` omvandlar användarens input till ett heltal.

```python
# Definiera funktioner här nedanför

def roll_dice():
  print(f"{python} kan kasta {dice}")
  max = input('Hur många sidor?:') # Vänta på inmatning från användaren
  print(f"Det är en D{max}") # Använd värdet som matades in
  roll = randint(1, int(max)) # randint behöver ett heltal max
  print(f"Du kastade {roll}")
  print(fire * roll)
```  

🧪 **Testa:** Kör ditt projekt. När programmet når raden med input, kommer det att använda på att du matar in ett svar innan det fortsätter.
Försök igen med ett annat tal.

💾 **Spara** ditt projekt!

# Påbörja en mening

Skriv ut fler meningar med ditt projekt.

![image](https://user-images.githubusercontent.com/4598641/221963087-1528815a-192f-44bd-9823-f544900070a9.png)

Lägg till fler rader till din kod. Här är några förslag på början till meningar:

**main.py**
```python
print(f"Jag {heart} ...")
print(f"... gör mig {happy}")
print(f"Jag skulle vilja göra ... med {python}")
```

**Tips:** lägg till mellanslag där det behövs.

>Den gula hjärt-emojin används ofta för att visa vänskap och lycka.

:pencil2:
Vilket meddelande skulle du skicka till en kompis för att pigga upp? Vilken emoji skulle du välja?

Klicka på fliken `emoji.py` tab i repl.it och se vilka emoji-variabler du kan använda. Klicka dig tillbaks till fliken `main.py` för att lägga till i din kod.

Du kan lägga till fler emoji-variabler i `emoji.py`. [Använd den här listan med emoji](https://unicode.org/emoji/charts/full-emoji-list.html) för att hitta de du vill ha.

💾 **Spara** ditt projekt!

# Kunskapsquiz

# Levla upp ditt projekt
Lägg till mer i ditt projekt. Det finns flera emoji att välja bland.

![image](https://user-images.githubusercontent.com/4598641/221965063-6e7cf08d-814e-413e-82ca-701908bfa9ab.png)

Du kan:
- Använda `print` med olika text och emoji.
- Använda `input` för att läsa in värden från användaren och spara dem som variabler och sen göra uträkningar med variablerna
- Skriva fler funktioner för att dela upp din kod
- Använda `#` för att kommentera koden

Klicka på fliken `emoji.py` för att se emoji-variablerna du kan använda. Klicka tillbaks till fliken `main.py` för att lägga till mer kod.

Här är ett exempel på en funktion som frågar om hobby:
**main.py**
```python
# Definiera funktioner här nedanför
def hobbies():
  hobby = input('Vad gillar du?')
  print(f"Det låter {fun}")
  print(f"Du kan göra ett {python}-projekt om {hobby}")
```

**Tips:** Kom ihåg att du behöver anropa en funktion som du har definierat.

Du kan använda `input` för att ditt projekt ska vänta tills du trycker på Enter innan det fortsätter köra.

**main.py**
```python
roll_dice()

input() # Vänta på att användaren trycker på Enter

hobbies()
```

💾 **Spara** ditt projekt!


# Källor

[^1]: This is a Swedish translation of the Raspberry Pi Foundation project https://projects.raspberrypi.org/en/projects/hello-world, with minor adaptations.
