# Hur många dagar fyller du idag?
Har du fyllt 5000 dagar? Vilket datum fyller eller fyllde du 5555 dagar?

**Uppgift:** Gör ett program som räknar ut hur många dagar det är mellan två datum. Använd det för att räkna ut hur många **dagar** du fyller idag!

Idé: låt programmet räkna ut hur många dagar det har gått sen ett visst startdatum, t.ex. 1 januari 2000, som vi kan ge dagnumret 1. Hur kan du använda den informationen för att räkna ut hur många dagar du fyller idag?

## STEG 1
Testkör först koden i de två rutorna nedanför. Gör sen klart där det står "# ATT FIXA"

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
