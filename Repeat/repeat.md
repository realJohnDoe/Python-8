# Repeat

![image](https://user-images.githubusercontent.com/4598641/225698865-f394ffdb-6b0c-4731-8763-915c93b7b965.png)

# Regler
Se när en nummersekvens blinkar.

Upprepa sekvensen med sifferknapparna.

Om du lyckas upprepa sekvensen läggs ett nytt nummer till och sekvensen blinkar igen.

# Kodning

## Sekvens
Sekvenslistan skapas. Till en början innehåller den en testsekvens med siffror mellan 1 och 4.

```python
import pgzrun

sequence = [4, 3, 1, 2, 2, 3] # Tillfälligt

def draw():
    screen.fill((0, 0, 0))
    screen.draw.text(', '.join(map(str, sequence)), (0, 0))

pgzrun.go() # Ska alltid vara sist i programmet (längst ner)
```

![image](https://user-images.githubusercontent.com/4598641/225699441-a8ba2e0d-516c-42e0-8bbf-c062e783aee5.png)

✏️ Mata in och testkör koden i ett nytt projekt i repl.it.

## Nuvarande position i sekvensen
Den aktuella sekvenspositionen börjar vid 1.

Om siffran i sekvensen vid den aktuella positionen trycks in, läggs 1 till den aktuella positionen.

Detta blir fel när den aktuella positionen är längre än längden på sekvenslistan.

```python
import pgzrun

sequence = [4, 3, 1, 2, 2, 3] # Tillfälligt
current = 0

def on_key_down(key):
    global current # För att vi ska kunna uppdatera variabeln current som är utanför funktionen
    
    if key in (keys.K_1, keys.K_2, keys.K_3, keys.K_4): # siffertangenterna 1, 2, 3, 4
        if key == keys.K_1:
            number = 1
        elif key == keys.K_2:
            number = 2
        elif key == keys.K_3:
            number = 3
        elif key == keys.K_4:
            number = 4
        
        if number == sequence[current]:
            current += 1

def draw():
    screen.fill((0, 0, 0))

    screen.draw.text(', '.join(map(str, sequence)), (0, 0))
    screen.draw.text(f"{current + 1}/{len(sequence)}", (0, 20))
    screen.draw.text(f"sequence[current]: {sequence[current]}", (0, 40))

pgzrun.go() # Ska alltid vara sist i programmet (längst ner)
```

✏️ Uppdatera din kod så att den blir som här och testkör den. Du måste inte mata in kommentarerna &ndash; de förklarar vad koden gör.
Klicka i terminalfönstret. Sedan kan du trycka på siffertangenterna 1 till 4 för att testa.

![image](https://user-images.githubusercontent.com/4598641/225703318-26fb8e5b-9d98-4a9d-b740-fc220f938125.png)


# Källor
Översatt till svenska och anpassad till repl.it baserat på https://simplegametutorials.github.io/pygamezero/repeat/
