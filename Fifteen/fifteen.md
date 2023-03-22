# Fifteen ⭐⭐⭐

## En handledning för Python och Pygame Zero 1.2

![image](https://user-images.githubusercontent.com/4598641/226436083-7b0b90b9-9c13-4b83-bfd8-3534ac8291c0.png)

# Regler

Det finns en tavla med 15 bitar och ett tomt utrymme. 
Flytta runt pjäserna tills de är i nummerordning genom att använda piltangenterna för att flytta pjäserna till det tomma utrymmet.

## Kontroller

**Piltangenter**	Flytta pjäs

# Översikt
Bitarna lagras som ett rutnät med siffror.

Siffran 16 representerar det tomma utrymmet.

![image](https://user-images.githubusercontent.com/4598641/226436258-85719c97-8e01-4aca-85b0-82d3cc184876.png)

De andra siffrorna byts ut med det tomma utrymmet när en piltangent trycks ned.

I början av spelet är rutnätet initialt i sorterad ordning, och slumpmässiga drag görs för att blanda det. (Om pjäspositionerna istället var helt slumpmässiga kan det resultera i en olöslig bräda.)

Efter att en pjäs har flyttats, går pjäserna igenom, och om de alla har sina initiala sorterade värden är spelet över.

# Kodning

## Rita bitarna

Bitarna är ritade som rutor.

För nu ritas en bit där det tomma utrymmet ska vara.

✏️ Se till att du är inloggad i repl.it. Öppna startprojektet https://replit.com/@RobertStorlind/fifteen-starter och spara en egen kopia med knappen "Fork".
Testkör!

![image](https://user-images.githubusercontent.com/4598641/226436463-1d10dd82-ed1c-429b-b0bc-e855b4969551.png)

## Rita siffrorna

Stycknumren dras ovanpå pjäserna.

Ett styckenummer beräknas genom att addera Y-positionen (dvs. radnummer) multiplicerat med antalet pjäser i en rad till X-positionen plus 1.

Till exempel, på den första raden är Y-positionen 0, så ingenting läggs till varje X-position, så den första siffran på den första raden är 1.
På den andra raden läggs 4 till varje X-position, så den första nummer på andra raden är 5.

![image](https://user-images.githubusercontent.com/4598641/226436562-731e3960-4198-4bef-8635-e239557be6c9.png)

## Skapa rutnätet
Ett rutnät skapas med varje pjäs nummer lagrat på sin plats på rutnätet, och detta nummer dras.

Antalet bitar på X- och Y-axlarna återanvänds från att rita bitarna, så de görs till variabler.


## Rita inte det tomma utrymmet
Antalet pjäser på varje axel multiplicerat tillsammans ger det totala antalet pjäser (dvs. 4 gånger 4 betyder 16 pjäser), och en pjäs dras endast om det inte är detta nummer.

![image](https://user-images.githubusercontent.com/4598641/226437183-8e41b05e-77bc-488b-b400-4785be077050.png)

## Hitta position för tomt utrymme
Det första steget i att flytta en bit är att hitta positionen för det tomma utrymmet.

När en tangent trycks in, slingras rutnätet, och om en bit är lika med antalet bitar på varje axel multiplicerat med varandra (dvs det är det tomma utrymmet), så skrivs dess position för närvarande ut.

```
tom x: 3, tom y: 3
```

## Flytta bitar ner
Om Y-positionen för det tomma utrymmet är större än 0, betyder det att det finns en pjäs ovanför det tomma utrymmet, så det är möjligt att flytta en pjäs nedåt.

Det tomma utrymmet ändras till styckenumret ovanför utrymmet, och stycket ovanför utrymmet ändras till utrymmesnumret.

För nu flyttar vilken tangent som helst en bit ner.

![image](https://user-images.githubusercontent.com/4598641/226437400-e5f88975-05ce-4b80-80ca-50862059eb21.png)

## Flytta upp bitar
Om Y-positionen för det tomma utrymmet är mindre än antalet rader i rutnätet, betyder det att det finns en bit under det tomma utrymmet,
så att det är möjligt att flytta pjäsen uppåt.

Y-positionen för den bit som det tomma utrymmet byter med görs till en variabel. 
När upp-tangenten trycks in ställs den till positionen under det tomma utrymmet (dvs plus 1 på Y-axeln).

## Flytta bitar åt vänster och höger
X-positionen för den bit som det tomma utrymmet byter med görs till en variabel, och den ändras när vänster- eller högerpilen trycks ned.

![image](https://user-images.githubusercontent.com/4598641/226437516-322ed925-e617-41a9-94a7-fc3e9329aeeb.png)



## Blanda
I början av spelet görs ett antal slumpmässiga drag för att blanda brädet.

Ett slumptal mellan 1 och 4 genereras och ett drag görs i en av de fyra rörelseriktningarna baserat på detta nummer.

Slumpmodulen importeras så att random.randint kan användas.

![image](https://user-images.githubusercontent.com/4598641/226437586-c1a482c0-b465-4214-822a-68f8b2530839.png)

## Förenkla kod
Den enda skillnaden mellan blandningskoden och den tangentbordskontrollerade koden är hur riktningen för förflyttningen bestäms,
så en funktion görs med riktningen som parameter.

## Gör den nedre högra positionen tom
Så att det tomma utrymmet alltid börjar i det nedre högra hörnet, flyttas bitarna åt vänster och uppåt flera gånger. 
Antalet pjäser på en axel minus 1 är det maximala antalet drag det skulle ta för att flytta utrymmet från ena sidan till den andra.

![image](https://user-images.githubusercontent.com/4598641/226437694-caf5182b-39da-41bf-95d7-4ef3c098baf8.png)


## Återställa spelet
En funktion skapas som ställer in spelets initiala tillstånd.

Denna funktion anropas innan spelet börjar och när r- tangenten trycks ned.

## Kontrollera om komplett
Efter att ett drag har gjorts, slingras pjäserna igenom, och om ingen av pjäserna inte är lika med numret som de fick från början 
(dvs de är alla i sina sorterade positioner), återställs spelet.

## Förenkla kod
Koden för att beräkna startvärdet för en bit återanvänds, så den görs till en funktion.


## Blanda igen om det är klart efter att du har blandat
Om bitarna fortfarande är i sin ursprungliga ordning efter att de har blandats, sker blandningsprocessen igen.

Koden för att kontrollera om bitarna är i sin ursprungliga ordning återanvänds, så den görs till en funktion.



# Källor

Översatt och bearbetat för repl.it baserat på originalet: https://simplegametutorials.github.io/pygamezero/fifteen/
