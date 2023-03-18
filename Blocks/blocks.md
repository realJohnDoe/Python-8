# Blocks
## En handledning för Python och Pygame Zero 1.2

![image](https://user-images.githubusercontent.com/4598641/226001268-afea64f1-d51c-48e0-b4b8-0bff27a3e893.png)

# Regler

Det finns sju typer av bitar. Varje bit innehåller fyra rutor.

![image](https://user-images.githubusercontent.com/4598641/226001342-33230a9a-d8a3-4218-9a37-3cc579827ad0.png)

Bitar faller från toppen av spelplanen. Spelaren kan flytta bitar åt vänster och höger och rotera dem. När en bit landar, faller nästa bit.

Hur nästa bit ser ut visas ovanför spelplanen som en hjälp till spelaren.

![image](https://user-images.githubusercontent.com/4598641/226001405-e8e90545-4b84-4dc6-87a5-374f584ade98.png)

När en obruten rad av rutor bildas, försvinner raden och alla rutor ovanför flyttas ner en rad.

Spelet slutar när en bit har hamnat i vila och nästa bit skulle omedelbart överlappa en tidigare nerfallen bit.

## Kontroller

**Vänsterpil**	Flytta vänster ⬅️<br>
**Högerpil**	Flytta höger ➡️<br>
**Z**	Rotera moturs 🔄<br>
**X**	Rotera medurs 🔃<br>
**C**	Släpp ⏬


# Översikt
Ett rutnät lagrar de orörliga rutorna från nerfallna bitar.

En ruta är antingen tom eller fylld med en viss färg.

- Tecknet `' '` är ett mellanslag och betyder en tom ruta.
- Tecknen  `'i'`, `'j'`, `'l'`, `'o'`, `'s'`, `'t'` och `'z'` betyder rutor med olika färger.

![image](https://user-images.githubusercontent.com/4598641/226003821-3a435de3-4843-421e-ab20-477e93bf3fe8.png)

Alla olika typer av bitar lagras med sina roterade varianter.

![image](https://user-images.githubusercontent.com/4598641/226003959-15932dfd-3435-47dd-b1f2-78b050e562fb.png)

Den fallande biten lagras som 
- ett tal som representerar vilken typ av bit det är,
- ett tal som representerar vilken rotation den befinner sig i
- och så X- och Y-koordinaten för biten på spelplanen.

En ny bit skapas längst upp på skärmen, om den inte skulle överlappa ett orörligt block, i vilket fall spelet är över.

Spelaren kan flytta biten åt vänster och höger, om inte den nya positionen överlappar ett orörligt block eller är utanför spelplanen.

Efter en liten fördröjning flyttas biten nedåt. Om den nya positionen överlappar ett orörligt block eller är utanför spelplanen så landar biten.

När någon av rotationsknapparna trycks, ändrar biten sin rotation, om inte den rotationen överlappar ett orörligt block eller är utanför spelplanen.

När släppknappen trycks in, flyttas biten neråt så långt det går utan att den överlappar ett orörligt block är vara utanför spelplanen. Sen landar biten.

När en bit landar, läggs bitens block till de orörliga blocken och nästa bit skapas.

En sekvens av en av var och en av de sju bitarna i en slumpmässig ordning skapas, och nästa bit tas från denna sekvens. 
När alla bitar har tagits, skapas en ny slumpmässig ordning.

# Kodning

## Rita rutnätet med block
En ruta ritas för varje block i spelplanen.

Kod:XXXX

![image](https://user-images.githubusercontent.com/4598641/226004861-bb0676e3-8ace-444f-af72-a4c3859483b0.png)

## Lagring av orörliga block

Rutnätet för de orörliga blocken skapas och varje block sätts till ett mellanslag, `' '`. Det representerar ett tomt block.

Bredden och höjden på rutnätet i block återanvänds från ritning av blocken, så vi gör bredden och höjden till variabler.

Kod:XXXX

## Sätt färgen på blocken

När block ritas, ställs färgen in baserat på vilken typ av block det är.

För att kunna testa det, sätter vi en några block i det orörliga nätet till att ha olika typ.

Kod:XXXX

![image](https://user-images.githubusercontent.com/4598641/226006718-62e1013b-99f3-427b-b095-4cda85184e19.png)

## Lagring av bitarnas utseende
Varje rotation av en biten är en 4x4-kvadrat av tecken.

```python
[
    [' ', ' ', ' ', ' '],
    ['i', 'i', 'i', 'i'],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
]
```

Varje bit lagras som en lista av de olika rotationerna.

```python
[ # en lista
    [ # ett element i listan = en rotation av biten
        [' ', ' ', ' ', ' '],
        ['i', 'i', 'i', 'i'],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
    ],
    [
        [' ', 'i', ' ', ' '],
        [' ', 'i', ' ', ' '],
        [' ', 'i', ' ', ' '],
        [' ', 'i', ' ', ' '],
    ],
]
```

Alla de olika bitarna och deras rotationer sparas som en lista.

```python
piece_structures = [
    [ # en lista av bitar
        [ # bit 1, rotation nr 1
            [' ', ' ', ' ', ' '],
            ['i', 'i', 'i', 'i'],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [ # bit 1, rotation nr 2
            [' ', 'i', ' ', ' '],
            [' ', 'i', ' ', ' '],
            [' ', 'i', ' ', ' '],
            [' ', 'i', ' ', ' '],
        ],
    ],
    [ # nästa bit
        [ # bit 2, rotation nr 1 -- den har bara en!
            [' ', ' ', ' ', ' '],
            [' ', 'o', 'o', ' '],
            [' ', 'o', 'o', ' '],
            [' ', ' ', ' ', ' '],
        ],
    ],
    [ # nästa bit
        [ # bit 3, rotation nr 1
            [' ', ' ', ' ', ' '],
            ['j', 'j', 'j', ' '],
            [' ', ' ', 'j', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [ # bit 3, rotation nr 2
            [' ', 'j', ' ', ' '],
            [' ', 'j', ' ', ' '],
            ['j', 'j', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [ # bit 3, rotation nr 3
            ['j', ' ', ' ', ' '],
            ['j', 'j', 'j', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [ # bit 3, rotation nr 4
            [' ', 'j', 'j', ' '],
            [' ', 'j', ' ', ' '],
            [' ', 'j', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
    ],
    [
        [
            [' ', ' ', ' ', ' '],
            ['l', 'l', 'l', ' '],
            ['l', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            [' ', 'l', ' ', ' '],
            [' ', 'l', ' ', ' '],
            [' ', 'l', 'l', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            [' ', ' ', 'l', ' '],
            ['l', 'l', 'l', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            ['l', 'l', ' ', ' '],
            [' ', 'l', ' ', ' '],
            [' ', 'l', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
    ],
    [
        [
            [' ', ' ', ' ', ' '],
            ['t', 't', 't', ' '],
            [' ', 't', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            [' ', 't', ' ', ' '],
            [' ', 't', 't', ' '],
            [' ', 't', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            [' ', 't', ' ', ' '],
            ['t', 't', 't', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            [' ', 't', ' ', ' '],
            ['t', 't', ' ', ' '],
            [' ', 't', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
    ],
    [
        [
            [' ', ' ', ' ', ' '],
            [' ', 's', 's', ' '],
            ['s', 's', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            ['s', ' ', ' ', ' '],
            ['s', 's', ' ', ' '],
            [' ', 's', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
    ],
    [
        [
            [' ', ' ', ' ', ' '],
            ['z', 'z', ' ', ' '],
            [' ', 'z', 'z', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            [' ', 'z', ' ', ' '],
            ['z', 'z', ' ', ' '],
            ['z', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
    ],
]
```


## Lagra biten som faller just nu

Biten som faller just nu representeras av
- dels ett tal som anger vilken typ av bit det är &ndash; vi behöver använda det för att indexera i listan över med olika bitar
- dels ett tal som anger vilken rotation biten har &ndash; vi behöver det för att indexera i listan med rotationer.

Kod:XXXX

## Rita blocket

Biten ritas genom att loopa genom dess struktur och &ndash; om rutan är fylld &ndash; så ritar vi en fyrkant med den färg som bestäms av blocktypen.

Kod:XXXX

![image](https://user-images.githubusercontent.com/4598641/226010899-049e0b7e-591d-4d0b-b296-7fb35778e094.png)


## Förenkla koden

Koden för att rita ett orörligt block och för att rita ett block av den fallande biten är samma. Därför gör vi en funktion för det.

Kod:XXXX

## Rotation
När vi trycker på X, ökas bitens rotationsnummer med 1 och biten roteras medurs.

>Om rotationstalet är större än antalet möjliga rotationer minus 1 sätts rotationstalet till 0. Vi går alltså tillbaks till bitens första rotation.

På samma sätt när vi trycker på Z så minskas rotationstalet med 1 och biten roterar moturs.

>Om rotationstalet är mindre än 0, sätts rotationstalet till antalet rotationer minus 1, alltså bitens sista rotation.
>
Kod:XXXX

![image](https://user-images.githubusercontent.com/4598641/226011415-59b9b18c-2496-4af0-a39c-f854ef940d2e.png)


## Testa block

För att göra det lätt att testa, låter vi upp- och och neråtpil byta mellan olika bitar.

Kod:XXXX

![image](https://user-images.githubusercontent.com/4598641/226011550-d53162ca-1eaf-4674-b2dc-71eefe2fed7d.png)


## Placera nästa bit

Bitens position i spelplanen lagras och biten ritas på den positionen.

Kod:XXXX

![image](https://user-images.githubusercontent.com/4598641/226011946-ae6035af-d12b-4390-bfe8-2a1a3019655b.png)



## Flytta blocket
Vänster- och högerpilarna subtraherar eller adderar 1 till bitens X-koordinat.

Kod:XXXX

![image](https://user-images.githubusercontent.com/4598641/226012210-eff3bfe9-dcb6-4579-be14-4eb21ec43338.png)


## Timer

Bitar kommer att falla med 0.5 s mellanrum.

En timervariabel börjar vid 0 och ökar med `dt` för varje bildruta.
>`dt` talar om hur lång tid det har gått sedan vi senast ritade på skärmen.

När timern har passerat 0.5, återställs den till 0.

För att se hur det fungerar skriver vi just nu ut 'tick' ut varje gång biten faller.

Kod:XXXX

## Fallande block
Timern används för att öka bitens Y-position var 0.5:e sekund.

Kod:XXXX

![image](https://user-images.githubusercontent.com/4598641/226012579-0a5bce97-00a6-4f54-ba96-95cc123f9a4c.png)


## Begränsa rörelsefriheten

För att förhindra att biten hamnar till vänster eller höger om spelplanen när den flyttas eller roteras, 
kontrollerar vi vart och ett av dess block för att se om de är inom spelplanen innan biten flyttas eller roteras.

Eftersom den här kontrollen kommer att göras på flera ställen, gör vi en funktion med den koden.
Funktionen ska kontrollera bitens position och rotation och returnera True om biten kan röra sig eller rotera, annars False.

Till att börja med kommer denna funktion alltid att returnera True, så att vi alltid kan flytta och rotera medan vi testar.

Vi ändrar koden från omedelbart ställa in positioner/rotationer.
Istället skapar vi variabler för de ändrade värdena.
Om kontrollfunktionen returnerar True ställs den faktiska positionen/rotationen till de ändrade värdena, annars inte.

Kod:XXXX

## Kontrollera vänsterkanten
Om något block inte är tomt och X-positionen är mindre än 0, returnerar funktionen False. Det är när blocket är utanför spelplanens vänstra sida.

Kod:XXXX

## Förenkla koden
Storleken på varje bit i X- och Y-led återanvänds från att rita bitarna, så vi gör variabler för det.

## Kontrollera högerkanten

Om något blocks X-position är större än eller lika med spelplanens bredd hamnar det utanför spelplanens högra sida.
Då returnerar funktionen också False.

Kod:XXXX

## Kontrollera underkanten
Om något blocks Y-position är större än eller lika med höjden på spelplanen är det nedanför botten av spelplanen.
Då returnerar funktionen också False.


Kod:XXXX

## Kontrollera orörliga block
Om det finns ett orörligt block vid något blocks position, returnerar funktionen också False .

För att testa detta lägger vi in ett orörligt block.

Kod:XXXX

![image](https://user-images.githubusercontent.com/4598641/226013942-ae181f75-53b1-4b7c-8156-ba22cf2ecc9c.png)

## Förenkla koden
De beräknade blockpositionerna som ska testas behövs på fler ställen. Vi sparar dem i variabler.

Kod:XXXX

## Släppa ner ett block

När C-tangenten trycks, ökas bitens Y-position med 1 så länge som biten får plats.

Kod:XXXX

## Återställa blocket

Om timern tickar och biten inte kan röra sig neråt, återställs biten till sin ursprungliga position och rotation, och sin ursprungliga typ. 
Vi ska ändra det sen.

Kod:XXXX

## Förenkla koden

Biten sätts till sitt ursprungliga tillstånd på två ställen. Vi gör en funktion för det.

Kod:XXXX

## Håll reda på kommande block
De kommande bitarna lagrar vi som en lista som innehåller numren som representerar bittyper i slumpmässig ordning.

Vi gör en lista med talen från 0 till `len(piece_structures) - 1`. 
Sedan slumpar vi ordningen på den listan med `random.shuffle`.

För att testa, skapar vi  en ny sekvens när S-tangenten trycks ned och skriver ut sekvensen.

Slumpmodulen importeras vi så att vi kan använda `random.shuffle`.

Kod:XXXX

```python
[3, 2, 4, 1, 0, 5, 6]
```

## Nästa block från listan
När en ny bit skapas tar den bort det sista talet från listan och använder det för att bestämma typen av bit.

När listan med blocknummer är tom skapas en ny sådan lista.

Kod:XXXX

## Lägg till orörliga block
När en bit har landat läggs bitens block till de orörliga blocken.

Bitens block gås igenom och om ett block inte är tomt, sätter vi det orörliga blocket på den positionen till värdet som vi hämtar från biten.

Kod:XXXX

## Ny bit direkt efter släpp
När en bit släpps ner, sätter vi timern så att den löper ut direkt.
Då kommer nästa bit att skapas direkt istället för att vänta på timern.

Timergränsen återanvänds, så vi gör den till en variabel.

Kod:XXXX

## Hitta fyllda rader
Varje rad av de orörliga blocken loopas igenom. Om ingen av kolumnerna i raden är ett tomt block så är raden fylld.

För att göra det lättare att testa, skrivs de fullständiga radnumren ut just nu.

Kod:XXXX

## Ta bort fyllda rader
Om raden är fylld, loopar vi igenom raderna ända till näst översta raden.

Varje block i raden loopas igenom och ställs in på värdet för blocket ovanför det.
Eftersom det inte finns något ovanför den översta raden behöver den inte loopas igenom.

Den översta raden kommer då att vara helt tom.

Kod:XXXX

## Slut på spelet

Om en nyskapad bit är i en orörlig position är spelet över.

Vi gör en funktion som ställer in spelets startläge.
Den anropas innan spelet börjar och när spelet är över.

Kod:XXXX

## Förskjutning av spelplanen
Spelplanen ritas 2 block från vänster på skärmen och 5 block från toppen av skärmen.

Kod:XXXX

![image](https://user-images.githubusercontent.com/4598641/226016663-cb1d5333-1bd0-4943-91e7-8d22d195f2ef.png)

## Rita nästa block

Den sista biten i sekvensen, alltså nästa bit som faller, ritas med sin första rotationsstil.
Den är förskjuten rutor från vänster och en ruta uppifrån.

Kod:XXXX

![image](https://user-images.githubusercontent.com/4598641/226016912-b2e1d0a6-fbf5-41b8-b808-9fdacaea6fb0.png)



# Källor

Översatt och bearbetat för repl.it baserat på originalet: https://simplegametutorials.github.io/pygamezero/blocks/