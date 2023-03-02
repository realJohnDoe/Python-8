# Hur många dagar fyller du?

Har du fyllt 5000 dagar? Vilket datum fyller eller fyllde du 5555 dagar?

**Uppgift:** Gör ett program som räknar ut hur många dagar det är mellan två datum. Använd det för att räkna ut hur många **dagar** du fyller idag!

**Idé:** vi låter programmet räkna ut hur många dagar det har gått sen ett visst startdatum, t.ex. 1 januari 2000. Den dagen kallar vi dag 1.
Hur kan du använda den informationen för att räkna ut hur många dagar du fyller idag?

![image](https://user-images.githubusercontent.com/4598641/222534676-a6a5c5ce-12de-4a9d-be65-2ee80d426993.png)

## STEG 1
Vi börjar med hur det ska se ut när vi kör programmet.
- Programmet ska fråga efter ett startdatum, alltså år, månad, dag. Det kan t.ex. vara användarens födelsedatum
- Sen ska det fråga efter ett slutdatum, alltså år, månad, dag. Det kan t.ex. vara dagens datum
- Programmet ska skriva `Det är 5432 dagar mellan datumen` (t.ex.) och sen avsluta

✏️ Mata in den här koden i ett nytt Pythonprojekt i repl.it.

**main.py**
```python
### Skriv vanliga funktioner här under
def dagnummer(år, månad, dag):
  return 0
  
#### Skriv testfunktioner här under
def testa():
  print("Vi testar")
  
### Skriv kod som pratar med användaren här under
def fråga_datum(rubrik):
  print(rubrik)
  år = int(input('År, fyra siffror: '))
  månad = int(input('Månad, 1--12: '))
  dag = int(input('Dag, 1--31: '))
  return (år, månad, dag)

def fråga_och_svara():
  print('Hur många dagar är det?')
  (från_år, från_månad, från_dag) = fråga_datum('Från vilket datum?')
  (till_år, till_månad, till_dag) = fråga_datum('Till vilket datum?')
  
  dagar = dagnummer(till_år, till_månad, till_dag) - dagnummer(från_år, från_månad, från_dag)
  
  print(f"Det är {dagar} dagar mellan datumen")

### Här börjar appen köra
fråga_och_svara()
```

✏️ Testa koden med gröna knappen Run i repl.it. Vad tror du att resultatet kommer att bli?

## STEG 2

OK, nu har vi en idé hur det kan se ut. Nu behövs det kod för att räkna dagar. 
Funktionen `dagnummer` är ett skelett som behöver fyllas i.

Det finns flera sätt att göra det på. Vi gör det i små steg.

När man skriver en app kan man testa den på olika sätt. Ett sätt är att mata in olika värden i terminalfönstret. Ibland är det lättare och snabbare att skriva testkod. Det ska vi göra nu.

✏️ Ändra appen så att det längst ner blir så här. Du kan stänga av frågorna så länge så här och anropa funktionen `testa` istället:

```
### Här börjar appen köra
testa()
#fråga_och_svara()
```

Vad händer om du kör appen nu?

## STEG 3
Vi vill att funktionen `dagnummer` ska ge oss antalet dagar från den 1 januari 2000, som vi kan kalla dag 1.

Lägg till ett test i funktionen `testa()`:
```python
#### Skriv testkod här under
def testa():
  print("Vi testar")
  d = dagnummer(2000, 1, 1)
  if d != 1: print(f"Dagnumret blev {d}")
```
✏️ Vad tror du resultatet blir? Kör koden i repl.it. Blev det som du tänkte dig?

Lägg till ett testfall längst ner i `testa()`:
```python
#### Skriv testkod här under
def testa():
  print("Vi testar")
  d = dagnummer(2000, 1, 1)
  if d != 1: print(f"Dagnumret blev {d}")
  d = dagnummer(2000, 1, 31)
  if d != 31: print(f"Dagnumret blev {d}")
  print("Slut på tester")
```
✏️ Vad tror du resultatet blir nu? Kör koden i repl.it. Blev det som du tänkte dig?

Finns det ett enkelt sätt att ändra funktionen `dagnummer` så att våra tester fungerar?[^1]


```python
# Först behöver vi veta om det är skottår
# "%" ger resten vid division och kallas "modulo" eller bara "mod"
def skottdag(år): # 1 om skottår, annars 0
  if år % 400 == 0: return 1
  if år % 100 == 0: return 0
  if år % 4 == 0: return 1
  return 0

# Hur många dagar in på året är vi?
def dagnummer_på_året(år, månad, dag): # år med fyra siffror, månad 1 till 12, dag 1
  dagnr = dag
  if månad > 1: 
    dagnr += 31 # plussa på antalet dagar i januari 
  if månad > 2:
    dagnr += 28 + skottdag(år) # februari är krångligast
  if månad > 3: 
    dagnr += 31 # antalet dagar i mars
  # ATT FIXA: ta hand om resten av månaderna med "if"
  # Du behöver lägga till en if-sats för varje månad > 4, 5, 6, 7, 8, 9, 10 och 11,
  # alltså totalt åtta if-satser till
return dagnr
```

Provkör din kod
```python
# Är det skottår i år?
print("2023? ja, skottår" if skottdag(2023) == 1 else "2023? nej, inte skottår")
# Testa din funktion dagnummer_på_året med några exempel du är säker på
# Glöm inte att klicka på pilen för att uppdatera
print(dagnummer_på_året(2023, 1, 1)) # bör vara 1
print(dagnummer_på_året(2023, 2, 1)) # bör vara 32 
print(dagnummer_på_året(2023, 12, 31)) # bör vara 365
```

## STEG 2
Säg att det är den 1 maj 2023 idag.
För att räkna ut hur många dagar det har gått sen 1 januari 2000 är det praktiskt att ha en funktion som ger oss antalet dagar för åren
2000, 2001, ... till och med 2022. Vi kallar den funktionen antal_dagar_före.

Sen kan vi använda funktionen dagnummer_på_året för år 2023 för att få fram ett exakt svar.

Testkör först de två rutorna. Gör sen klart funktionen antal_dagar_före. Här är en början:

```python
def antal_dagar_före(år):
  # Hur många dagar hade åren från 2000 ända fram till 31 december det givna året?
  dagar = 365 * (år - 2000)
  # ATT FIXA: Gör klart så att skottår räknas rätt! Använd funktionen skottdag t.ex. 
  return dagar
```

### Testa din funktion här! 
```python
print(antal_dagar_före(2000))
print(antal_dagar_före(2001))
print(antal_dagar_före(2002))
print(antal_dagar_före(2021))
```

## STEG 3
Gör nu färdigt programmet genom att 1) läsa in två olika datum från och till, 2) beräkna skillnaden i dagnummer mellan datumen och 3) skriva ut svaret.

Hur många dagar är du?

```python
från_år = int(input("Från år: "))
från_månad = int(input("Från månad, 1 till 12: "))
från_dag = int(input("Från dag, 1 till 31: "))

# ATT FIXA: Gör klart enligt tipsen för steg 3 och skriv ut antalet dagar mellan de två datumen
```

## STEG 4
Kan du göra så att koden klarar datum på 1900-talet också? Idag klarar den inte ens generationen av millennials :)

Ändra koden i rutorna ovanför och glöm inte att klicka på pilen till vänster för att köra när du ändrat.


# Hjälp på traven
[¹]: `return dag` istället för `return 0`
