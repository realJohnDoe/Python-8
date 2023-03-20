# Snake ⭐⭐⭐
En handledning för Python och Pygame Zero 1.2

![image](https://user-images.githubusercontent.com/4598641/226439115-c9800ff9-c916-406c-9efb-39407658988a.png)

# Regler
Att äta mat gör att ormen växer. När maten är uppäten flyttas den till en annan slumpmässig position.

Ormen kommer att svepa runt till andra sidan av skärmen när den går av kanten.

Spelet är över när ormen kraschar in i sig själv.

## Kontroller
**Piltangenter**	Byt riktning

# Översikt
Ormen representeras av en sekvens av X- och Y-positioner.

Maten representeras av en enda X- och Y-position.

När ormen rör sig, tas det sista föremålet i sekvensen (dvs. dess gamla svansposition) bort, och ett föremål läggs till framtill (dvs. dess nya huvudposition) i den riktning som ormen går.

![image](https://user-images.githubusercontent.com/4598641/226439258-020b4582-5409-448b-99e6-55cf6a4bbcdc.png)

![image](https://user-images.githubusercontent.com/4598641/226439284-599e5e4f-6987-4eea-8b79-f39d5a2d850a.png)

Om den nya huvudpositionen är i samma position som matens position tas inte ormens svans bort, och maten flyttas till en slumpmässig position som inte upptas av ormen.

![image](https://user-images.githubusercontent.com/4598641/226439323-b54bc813-62f2-49d5-ac3b-1002ba0de713.png)

Om den nya huvudpositionen är i samma position som någon av ormens andra segment, är spelet över.

# Kodning
## Rita bakgrunden
Spelområdet är 20 celler brett och 15 celler högt, och varje cell har en sidolängd på 15 pixlar.

En rektangel ritas för bakgrunden.

![image](https://user-images.githubusercontent.com/4598641/226439410-a04eb468-d4cf-4b10-9916-02534cea3a3d.png)

## Rita ormen
Ormens segment lagras som X- och Y-positioner och ritas som rutor.

![image](https://user-images.githubusercontent.com/4598641/226439469-a0bf9621-d2ff-4b38-810e-9a1be63b3324.png)

## Timer
Ormen kommer att röra sig en gång var 0,15:e sekund.

En timervariabel börjar vid 0 och ökar med dt för varje bildruta.

När timern är på eller över 0,15 återställs den till 0.

För närvarande skrivs 'tick' ut varje gång ormen ska röra sig.

## Flytta ormen rätt
Nästa position för ormens huvud beräknas genom att lägga till 1 till den nuvarande X-positionen för ormens huvud (dvs. det första elementet i segmentlistan). Detta nya segment läggs till i början av segmentlistan.

Det sista elementet i segmentlistan (ormens svans) tas bort.

Segmentlistan ändras i uppdateringsfunktionen , så den flyttas till att vara global.

![image](https://user-images.githubusercontent.com/4598641/226439549-4395b5df-c7f0-4a1f-9a91-921994eb1365.png)

## Flytta ormen i alla fyra riktningar
Ormens nuvarande riktning lagras i en variabel och ändras med hjälp av piltangenterna.

Ormens nästa huvudposition ställs in utifrån denna riktning.

![image](https://user-images.githubusercontent.com/4598641/226439597-2d0fded6-4174-4bbb-8dc1-9f3499761701.png)

## Förhindrar att röra sig rakt bakåt
Ormen ska inte kunna röra sig i motsatt riktning som den för närvarande går i (t.ex. när den går åt höger ska den inte direkt gå åt vänster), så detta kontrolleras innan riktningen ställs in.


## Använder riktningskö
För närvarande kan ormen fortfarande gå bakåt om en annan riktning och sedan den motsatta riktningen trycks in inom en enda bock på timern. Till exempel, om ormen flyttade höger på den sista bocken, och sedan spelaren trycker ner och sedan vänster före nästa bock, kommer ormen att flytta åt vänster på nästa bock.

Dessutom kan spelaren vilja ge flera anvisningar inom en enda bock. I exemplet ovan kan spelaren ha velat att ormen skulle flytta ner för nästa bock, och sedan lämnat på bocken efter.

En vägbeskrivningskö skapas. Det första objektet i kön är riktningen som ormen kommer att röra sig vid nästa bock.

Om vägbeskrivningskön har mer än en post tas den första posten bort från den vid varje bock.

När en knapp trycks ned läggs riktningen till i slutet av vägbeskrivningskön.

Den sista posten i riktningskön (dvs. den senast tryckta riktningen) kontrolleras för att se om den inte är i motsatt riktning mot den nya riktningen innan den nya riktningen läggs till i riktningskön.

![image](https://user-images.githubusercontent.com/4598641/226439688-1765d719-ee76-4b94-be2f-d8760ced80d7.png)

## Förhindrar att lägga till samma riktning två gånger
Om den sista riktningen är i samma riktning som den nya riktningen läggs den nya riktningen inte till i riktningskön.

## Slår sig runt skärmen
Om nästa position skulle vara utanför nätet, lindas den runt till positionen på andra sidan.

Rutnätets X/Y-antal återanvänds från att rita bakgrunden, så de flyttas till att vara globala.

![image](https://user-images.githubusercontent.com/4598641/226439789-ce8299ae-1e6c-449b-9dc0-6c64b6124c6f.png)


## Rita mat
Maten lagras som ett par av X- och Y-värden och ritas som en kvadrat.

Slumpmodulen importeras så att random.randint kan användas .

![image](https://user-images.githubusercontent.com/4598641/226439842-6fae488e-e72d-494c-bad4-9204c860144a.png)

## Förenkla kod
Koden för att rita en orms segment och rita maten är densamma förutom färgen, så en funktion görs med färgen som parameter.


## Äter mat
Om ormens nya huvudposition är densamma som matens position tas inte ormens svans bort, och maten får en ny slumpmässig position.

## Förenkla kod
Koden för att ställa in maten till en slumpmässig position återanvänds, så en funktion görs.

## Flytta mat till lediga positioner
Istället för att flytta maten till valfri slumpmässig position, flyttas den till en position som ormen inte upptar.

Alla positioner i rutnätet loopas igenom, och för varje rutnätsposition slingras alla segment av ormen, och om inga segment av ormen är i samma position som rutnätspositionen läggs rutnätspositionen till till en lista över möjliga matpositioner. Nästa matposition väljs slumpmässigt från denna lista.


## Spelet slut
Ormens segment slingras igenom, och om någon av dem förutom det sista är i samma position som ormens nya huvudposition, så har ormen kraschat in i sig själv.

Det sista segmentet är inte markerat eftersom det kommer att tas bort inom samma bock.

För närvarande skrivs 'kollision' ut när ormen kraschar in i sig själv.

## Återställa spelet
En funktion skapas som ställer in spelets initiala tillstånd.

Denna funktion anropas innan spelet börjar och när ormen kraschar.

## Pausar efter att ormen har kraschat
En variabel används för att lagra om ormen är vid liv eller inte, och den är inställd på False när ormen har kraschat.

Om ormen är död, väntar timern i 2 sekunder innan den ringer återställning .

## Ändra ormens färg när den är död
Ormens färg ändras beroende på om den är vid liv eller inte.

![image](https://user-images.githubusercontent.com/4598641/226440133-a580b309-3b49-400d-ab5b-97c545c75ecd.png)


# Källor

https://simplegametutorials.github.io/pygamezero/snake/
