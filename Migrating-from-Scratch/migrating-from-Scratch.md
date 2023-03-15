# Att flytta över från Scratch
>Detta är en svensk översättning av Daniel Popes guide, https://pygame-zero.readthedocs.io/en/stable/from-scratch.html, lätt uppdaterad.

Den här handledningen jämför en version av Flappy Bird skriven i Scratch med en skriven i Pygame Zero. Programmen i Scratch och Pygame Zero är förvånansvärt lika.

- Här finns projektet i Scratch 3: https://scratch.mit.edu/projects/820017699
- Här finns versionen i repl.it: https://replit.com/@RobertStorlind/flappy-bird-pope

>Versionen för Pygame Zero (https://github.com/lordmauve/pgzero/blob/stable/examples/flappybird/flappybird.py) finns med i Pygame Zero-projektet.

>Du kan också ladda ner versionen för Scratch 1.4 och versionen för Scratch 3 (https://github.com/lordmauve/pgzero/raw/master/examples/flappybird/Flappy%20Bird.sb3) om du vill provköra.

Versionen för Pygame Zero innehåller logik för poängräkning som vi utelämnar i kodexemplen på den här sidan för att ge en mer rättvis jämförelse.

Pythonkoden som visas här är omflyttad för att göra exemplen tydligare.

# Scenen
Så här ser scenen ut i vårt Scratchprogram:

<img src="https://user-images.githubusercontent.com/4598641/224773342-ab7eb415-b908-42d0-8de4-9b2241e5146b.png" width="400px"/>

Det finns bara tre föremål förutom bakgrunden: fågeln och det övre och undre röret.

Motsvarande kod i Pygame Zero för att sätta upp de här objekten som aktörer, `Actor`, ser ut så här:
```python
bird = Actor('bird1', (75, 200))
pipe_top = Actor('top', anchor=('left', 'bottom'))
pipe_bottom = Actor('bottom', anchor=('left', 'top'))
```

I Pygame Zero ska vi också tänka på att rita de här objekten. I princip ger det oss lite mer flexibilitet hur vi vill rita scenen:

```python
def draw():
    screen.blit('background', (0, 0))
    pipe_top.draw()
    pipe_bottom.draw()
    bird.draw()
```

# Att förflytta rören
Rören åker med konstant fart oberoende av fågeln. När de försvinner ut till vänster på scenen dyker de upp igen till höger och den vertikala placeringen ändras slumpmässigt.

I Scratch kan vi uppnå det genom att skapa två olika skript för det övre och undre röret.

<img src="https://pygame-zero.readthedocs.io/en/stable/_images/flappybird-top-start.png" alt="_images/flappybird-top-start.png"/> <img src="https://pygame-zero.readthedocs.io/en/stable/_images/flappybird-bottom-start.png" alt="_images/flappybird-bottom-start.png"/>

För att summera vad som händer här:
- Villkoret `x position < -240` är sant när ett rör försvinner ut till vänster på skärmen och det är det som ger signalen att återställa rören.
- Variabeln `pipe_height` används för att samordna de två rören. Eftersom avståndet mellan de två rören ska vara samma hela tiden kan vi inte välja höjderna slumpmässigt. Därför har ena röret den här logiken men inte det andra. 
- `set y position to pipe height +/- 230` placerar ett rör så att det är ovanför `pipe_height` och det andra nedanför `pipe_height`.

Den här koden blir mycket enklare i Pygame Zero. Vi kan skriva en enda funktion som uppdaterar båda rören.
I själva verket har jag delat upp det på ett annat sätt för att belysa hur koden för att återställa rören hänger ihop, alltså `reset_pipes()`:

```python
import random

WIDTH = 400
HEIGHT = 708
GAP = 130
SPEED = 3

def reset_pipes():
    pipe_gap_y = random.randint(200, HEIGHT - 200)
    pipe_top.pos = (WIDTH, pipe_gap_y - GAP // 2)
    pipe_bottom.pos = (WIDTH, pipe_gap_y + GAP // 2)

def update_pipes():
    pipe_top.left -= SPEED
    pipe_bottom.left -= SPEED
    if pipe_top.right < 0:
        reset_pipes()
```

En liten skillnad här är att jag kan bryta ut de värden jag vill återanvända som **konstanter**, skrivna med STORA BOKSTÄVER. Det låter mig ändra dem på ett ställe när jag vill finjustera spelet. I koden här uppe t.ex. kan jag göra gapet bredare eller smalare mellan de två rören genom att bara ändra `GAP`.

Den största skillnaden är att det inte finns någon `för alltid`-loop i Pythonkod. 
Det är den stora skillnaden mellan Scratch och de flesta textbaserade programspråk: du måste uppdatera spelet med ett animeringssteg och sen göra `return`.
När du gör `return` från din kod har Pygame Zero möjlighet att hantera indata (tangentbord, mus) eller att rita om skärmen.
Om du kör en oändlig loop (för alltid) kommer spelet att hänga sig, så dina loopar behöver blir klara snabbt.

Pygame Zero anropar funktionen `update()` när den vill att du ska animera ett steg, så vi behöver bara anropa funktionen `update_pipes()`:

```python
def update():
   update_pipes()
```


# Fågeln

Mönstren vi beskrev tidigare hur Scratchlogiken översätts till Python gäller också för fågelns kod.
Den här gången tittar vi först på Pythonkoden.

Koden för att uppdatera fågeln samlar vi funktionen `update_bird()`.
Det första i den här funktionen är lite kod för att flytta fågeln enligt tyngdlagen, gravitationen:

```python
GRAVITY = 0.3

# Fågelns status från början
bird.dead = False
bird.vy = 0

def update_bird():
    uy = bird.vy
    bird.vy += GRAVITY
    bird.y += bird.vy
    bird.x = 75
```

Detta är en enkel gravitationsformel:
- Gravitation betyder konstant **acceleration neråt**.
- Acceleration är förändringen i **hastighet**.
- Hastighet är förändringen i **läge**.

För att hålla reda på detta behöver vi en variabel `bird.vy` som är fågelns hastighet (velocity) i y-led.
Det här är en ny variabel som vi själva definierar, inget som Pygame Zero sköter åt oss.

- Tyngdkraften betyder konstant acceleration nedåt: `GRAVITY`är större än 0.
- Acceleration är förändring i hastighet: `GRAVITY` läggs till fågelns hastighet `bird.vy`
- Hastighet är förändring i position: `bird.vy` läggs till `bird.y`. Vi ökar alltså fågelns y-position med hastigheten i det ögonblicket

Tänk på att fågeln inte rör sig horisontellt! x-koordinaten är 75 under hela matchen.
Vi simulerar rörelse genom att flytta rören mot fågeln.
Det ser ut som om det är en rörlig kamera som följer fågeln. Så det finns inget behov av en `vx`-variabel i det här spelet.

Nästa avsnitt får fågeln att flaxa med vingarna:
```python
if not bird.dead:
    if bird.vy < -3:
        bird.image = 'bird2'
    else:
        bird.image = 'bird1'
```

Detta kontrollerar om fågeln rör sig uppåt eller neråt. 
Vi visar `bird2`-bilden om den rör sig snabbt uppåt och `bird1`-bilden annars.
&ndash;3 prövade vi oss fram till för att få detta att se övertygande ut.

Nästa avsnitt kontrollerar om fågeln har krockat med en vägg:
```python
if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
    bird.dead = True
    bird.image = 'birddead'
```

Om så är fallet sätter vi `bird.dead` till `True`.
Detta är ett booleskt värde, ett sanningsvärde som är antingen True eller False. 
Vi kan använda det för att enkelt kontrollera om fågeln är vid liv.
Om den inte är levande kommer den inte att svara på spelarens input.

Och det sista avsnittet kontrollerar om fågeln har fallit ner från botten eller toppen av spelskärmen. 
Om så är fallet återställer vi fågeln:

```python
if not 0 < bird.y < 720:
    bird.y = 200
    bird.dead = False
    bird.vy = 0
    reset_pipes()
```

Vad gör `reset_pipes()`?
Eftersom jag hade gjort koden för röret som en separat funktion, kan jag lätt anropa den när jag vill återställa väggarna.
I det här fallet gör det spelet bättre eftersom spelaren får en chans att reagera när fågeln flyttar tillbaka till sin startposition.

Vi behöver anropa det här varje gång bilden uppdateras, så vi lägger till det i `update()`:

```python
def update():
   update_pipes()
   update_bird()
```

Den sista delen av fågellogiken är att den måste svara på spelarkontroll.
När vi trycker på en tangent flaxar fågeln uppåt. 
Pygame Zero kommer att anropa funktionen `on_key_down()` när en knapp trycks ner, om du har definierat en funktion med det namnet.

```python
FLAP_VELOCITY = -6.5

def on_key_down():
    if not bird.dead:
        bird.vy = FLAP_VELOCITY
```

Om fågeln inte är död, sätter vi den `vy` (hastigheten) till ett negativt tal: i Pygame Zero betyder det att den börjar röra sig uppåt.

Du kan nog hitta många paralleller mellan Python-koden och den här Scratch-koden:

<img src="https://pygame-zero.readthedocs.io/en/stable/_images/flappybird-bird-start.png"/> <img src="https://pygame-zero.readthedocs.io/en/stable/_images/flappybird-bird-space.png"/>

De största skillnaderna mellan Scratch och Pygame Zero är dessa:
- Du kan inte loopa för evigt i Pygame Zero &ndash; du uppdaterar för en bildruta i taget.
- Koordinatsystemen är olika. I Pygame Zero är skärmens övre vänstra hörn (x, y) = (0, 0). x-axeln går från vänster till höger som innan men y-axeln går nerför skärmen. Det är därför som `GRAVITY` har ett positivt värde och `FLAP_VELOCITY` ett negativt värde i Python-koden.
- `bird.dead` är en logisk variabel så jag kan skriva kod som `if not bird.dead` istället för `dead = 0` som i Scratch.

# Sammanfattning
Många av begreppen i Scratch kan översättas direkt till Pygame Zero.

Här är några jämförelser:

| I Scratch |	I Pygame Zero|
| --- | --- |
| ändra y med 1 (upp)	| `bird.y &ndash;= 1` |
| ändra y med &ndash;1 (ner) |	`bird.y += 1` |
| sätt klädsel till <namn>	| `bird.image = 'name'` | 
| om dead = 0 | 	`if not bird.dead:`| 
| sätt dead till 0	| `bird.dead = False`| 
| om rör vid Top	| `if bird.colliderect(pipe_top)`| 
| när grön flagga klickas på ... för alltid | Lägg koden i funktionen `update()` | 
| När någon tangent trycks ner	| `def on_key_down():`| 
| Välj slumpmässigt a till b	| `import random` för att ladda biblioteket random, sen `random.randint(a, b)` | 
| (0, 0) är mitt på scenen	| (0, 0) är övre vänstra hörnet i fönstret| 

Ibland är koden enklare i Python eftersom den kan läggas upp på ett sätt som gör den lättläst.

Fördelarna med Pygame Zeros aktörer (Actor) gör det också lättare att jobba med koordinater.
Det var lätt att kontrollera om ett rör försvann ut från skärmen genom att ställa frågan
`pipe_top.right < 0` istället för `if x position < -240`.


# Källor
https://pygame-zero.readthedocs.io/en/stable/from-scratch.html
