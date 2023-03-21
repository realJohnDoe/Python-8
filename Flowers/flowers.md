# Flowers ⭐⭐⭐
## En handledning för Python och Pygame Zero 1.2

[flowers.zip](https://simplegametutorials.github.io/pygamezero/flowers/flowers.zip)

![image](https://user-images.githubusercontent.com/4598641/226450608-0fb4fbf9-c465-4d93-8acd-c3f38ac4225d.png)

# Regler
Spelet börjar med ett rutnät av täckta celler. Under några av cellerna finns blommor. Spelet är över när en blomma avslöjas.

Vänsterklick på en cell avslöjar den. Om ingen av de intilliggande cellerna innehåller blommor, avtäcks de också och för de avslöjade cellerna, om ingen av deras intilliggande celler innehåller blommor, avslöjas de också, och så vidare.

Att högerklicka på en cell växlar mellan en flagga, ett frågetecken eller ingenting. Flaggor förhindrar att en cell avslöjas med ett vänsterklick. Frågetecken är  markeringar som inte påverkar vad som händer när cellen klickas.

Spelet är klart när alla celler utan blommor har avslöjats.

## Kontroller

**Vänsterklick**	Avslöja en cell
**Högerklicka** Växla en dold cell mellan att ha en flagga, ett frågetecken eller ingenting.

# Översikt

Cellerna representeras av ordböcker som innehåller ett booleskt värde som anger om den innehåller en blomma eller inte, och ett strängvärde som anger i vilket av fyra tillstånd cellen är: täckt, täckt med en flagga, täckt med ett frågetecken eller avslöjad.

De celler som har blommor är slumpmässigt valda. Den första cellen som klickas utesluts från de möjliga alternativen.

När en cell klickas läggs dess position till i listan "avtäck stack".

Medan det finns något kvar i avtäckningsstacken...

- En position tas bort från slutet av stapeln.
- Denna position är inställd på avslöjad .
- Om det inte finns några blommor som omger denna position läggs de omgivande täckta och frågemarkerade positionerna (dvs. inte de avtäckta och flaggade positionerna) till avtäckningsstacken.

Cellerna ritas genom att sätta ihop följande bilder:

![image](https://user-images.githubusercontent.com/4598641/226450949-d9e02014-22b1-4aac-84ed-d00dfe9f782b.png)

# Kodning
## Rita brickor
Den täckta cellbilden ritas för varje cell.

Du kan komma åt bildfilerna som används i den här handledningen genom att ladda ner och packa upp .zip-filen som länkas till högst upp på den här sidan.

![image](https://user-images.githubusercontent.com/4598641/226451206-410b436d-e044-4c2f-876e-f5109dc96310.png)

## Markera celler
Cellpositionen under musen uppdateras varje bildruta.

Detta behöver cellstorleken, så det flyttas till att vara globalt.

För närvarande är denna position ritad som text.

pygame - modulen importeras så att pygame.mouse.get_pos kan användas.

Matematikmodulen är importerad så att math.floor kan användas .

![image](https://user-images.githubusercontent.com/4598641/226451267-d9515e88-2fc0-4a97-828d-6781174e029a.png)

## Håller vald cell inom rutnätet
Om muspositionen är större än rutnätets X- eller Y-cellantal (dvs. den är till höger eller längst ned i rutnätet), ställs den valda positionen in på den sista cellen på den axeln.

Rutnätets X- och Y-cellantal återanvänds från att rita cellerna, så variabler görs för dem.

![image](https://user-images.githubusercontent.com/4598641/226451363-15f4d3b2-c3f1-4187-9d11-949fd2691b7d.png)


## Markera celler
Den markerade cellen är en ritad med den markerade bilden.

![image](https://user-images.githubusercontent.com/4598641/226451429-c6b5e111-f945-47a4-bfe6-5005c372f603.png)

## Ändra cellbild när vänster musknapp är nere
När vänster musknapp är nere, ritas den markerade cellen som en avslöjad cell.


![image](https://user-images.githubusercontent.com/4598641/226451476-56697739-2fbd-436c-8baa-06d9e22be4ad.png)


## Rita blommor
Ett rutnät skapas för att lagra tillståndet för cellerna.

Varje cell kommer att representeras av en ordbok som lagrar två värden: om den har en blomma och om den är avslöjad/flaggad/frågemarkerad/ingenting.

För närvarande kommer det bara att lagra blomvärdet.

Om en cells "blomma" -nyckel är sann, för närvarande ritas blombilden över cellbilden.

![image](https://user-images.githubusercontent.com/4598641/226451517-df57e52b-abe0-4c91-b75c-fd350bc0ef44.png)

## Förenkla kod
Koden för att rita celler och rita blomman är densamma förutom bilden att rita, så en funktion skapas med bilden och X- och Y-värdena som parametrar.

## Växla blommor
För teständamål, högerklickar du på en cell för att växla dess blomma.


## Visar det omgivande antalet blommor
För att hitta det omgivande antalet blommor, slingras varje position i de 8 riktningarna runt varje cell. Om någon av dessa positioner är inuti rutnätet och cellen vid positionen har en blomma, läggs 1 till det omgivande antalet blommor.

Om det omgivande antalet blommor är större än 0, så ritas, för närvarande, lämplig nummerbild över cellen.

![image](https://user-images.githubusercontent.com/4598641/226451615-217a10c0-cf61-41f0-80fd-df17ef8c238e.png)

## Slumpmässig placering av blommor
En lista skapas som innehåller varje X- och Y-position i rutnätet.

Slumpmässiga positioner tas upprepade gånger bort från den här listan och cellerna på dessa positioner är inställda på att ha en blomma.

![image](https://user-images.githubusercontent.com/4598641/226451656-7aac2925-cd35-488f-a397-0a2efc8d269b.png)

## Återställa spelet
En funktion skapas som ställer in spelets initiala tillstånd.

Denna funktion anropas innan spelet börjar och när någon knapp trycks ned.

Att avslöja celler
Cellerna får en ny nyckel för cellens tillstånd. För närvarande är detta bara om cellen är täckt eller avtäckt.

För närvarande, när en cell vänsterklickas är dess tillstånd inställt på " avtäckt" .

Om en cells tillstånd är "avtäckt" ritas den avtäckta bilden istället för den täckta bilden.


![image](https://user-images.githubusercontent.com/4598641/226451742-496e7414-d3d4-4be4-b251-df824a393c09.png)




## Översvämningsfyllning: avtäck stapeln
En lista över cellpositioner skapas, och så småningom kommer alla cellpositioner som ska avslöjas att läggas till i denna lista.

För närvarande kommer denna "avtäckstapel" bara att innehålla den valda positionen, så den kommer bara att avslöja den valda cellen som tidigare.

Medan det finns positioner i avtäckningsstacken, tas en position bort från den och cellen vid denna position på rutnätet avtäcks.


## Översvämningspåfyllning: lägga till i högen
Varje position i de 8 riktningarna runt varje cell slingras igenom, och om positionen är inuti rutnätet och den är täckt, så läggs den till i avtäckningsstacken.

Detta resulterar i att alla celler blir avslöjade.

![image](https://user-images.githubusercontent.com/4598641/226451814-b25ebd8c-a36b-445d-9512-a291112a56f4.png)

## Översvämningsfyllning: med omgivande blommängd
De omgivande cellerna i en position som tagits bort från avtäckningsstacken läggs bara till stapeln om ingen av de omgivande cellerna har blommor.

Att hitta antalet omgivande blommor återanvänds från att rita det, så en funktion skapas.

![image](https://user-images.githubusercontent.com/4598641/226451877-3422c1a8-a0ff-49d3-8df1-f46e50c52424.png)


## Rita flaggor och frågetecken
En cells tillstånd kan också vara en flagga eller ett frågetecken.

Om en cells tillstånd är en flagga/frågetecken, ritas flaggan/frågeteckenbilden över cellen.

För att testa detta ändras tillståndet för två celler till att ha en flagga och ett frågetecken.


![image](https://user-images.githubusercontent.com/4598641/226451916-0675c6bd-8039-4926-b164-3cf556ff3a08.png)


## Cykelflaggor och frågetecken
Att högerklicka på en cell växlar dess tillstånd genom att det inte finns någonting, en flagga och ett frågetecken.

## Förhindra att flaggor avslöjas
Om en cell har en flagga kan den inte avslöjas med ett vänsterklick.

## Frågetecken slutar inte fyllas
Positioner läggs till i avtäckningsstacken om cellens tillstånd är täckt eller ett frågetecken (men inte en flagga).

## Ändra cellbild när vänster musknapp är nere över flaggan
Om vänster musknapp är nere när musen är på en cell med en flagga, så ritas cellen med den täckta bilden.

## Spelet slut
Om en blomma avslöjas är spelet över.

En variabel görs för att lagra om spelet är över eller inte.

För närvarande gör det ingenting att klicka på celler om spelet är över.

## Spelet vunnit
Om det inte finns några celler som är täckta och inte har en blomma, är spelet vunnet.

## Nytt spel vid nästa klick
Om spelet är över och en musknapp klickas, återställs spelet.

## Markera inte när spelet är över
När spelet är över markerar musen inte längre celler.



## Göm blommor tills spelet är över
Blommorna dras inte förrän spelet är över.



![image](https://user-images.githubusercontent.com/4598641/226452171-3df8c25a-b72c-4d16-9ff4-c654bb0e6db3.png)


## Dölj nummer för täckta celler
Om en cell inte avtäcks, visas inte dess omgivande blommängd.

![image](https://user-images.githubusercontent.com/4598641/226452196-f8755175-df82-4650-be3a-73491516082d.png)


## Förhindrar att du klickar på blomman vid det första klicket
För att det första klicket inte ska avslöja en blomma, flyttas koden för att placera blommor så att den körs när vänster musknapp klickas, och cellen under muspekaren läggs inte till de möjliga blompositionerna.

En variabel skapas för att lagra om ett klick är det första klicket i spelet.














# Källor
https://simplegametutorials.github.io/pygamezero/flowers/
