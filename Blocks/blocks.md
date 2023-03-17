# Blocks
## En handledning för Python och Pygame Zero 1.2

![image](https://user-images.githubusercontent.com/4598641/226001268-afea64f1-d51c-48e0-b4b8-0bff27a3e893.png)

# Regler

Det finns sju typer av bitar. Varje bit innehåller fyra block.

![image](https://user-images.githubusercontent.com/4598641/226001342-33230a9a-d8a3-4218-9a37-3cc579827ad0.png)

Bitar faller från toppen av spelområdet. Spelaren kan flytta pjäserna åt vänster och höger och rotera dem. När en bit kommer till vila, faller nästa bit.

Typen av nästa pjäs som kommer att falla visas ovanför spelområdet.

![image](https://user-images.githubusercontent.com/4598641/226001405-e8e90545-4b84-4dc6-87a5-374f584ade98.png)

När en obruten rad av block bildas, försvinner raden och alla block ovanför flyttas ner en rad.

Spelet slutar när en pjäs har hamnat i vila och nästa pjäs skulle omedelbart överlappa ett tidigare fallet block.

## Kontroller

**Vänsterpil**	Flytta vänster ⬅️<br>
**Högerpil**	Flytta höger ➡️<br>
**z**	Rotera moturs 🔄<br>
**x**	Rotera medurs 🔃<br>
**c**	Släpp ⏬


# Översikt
Ett rutnät lagrar de orörliga blocken som redan har fallit.

Tillståndet för ett block kan antingen vara tomt eller fyllt med ett block av en viss färg.

Strängen ' ' (ett mellanslag) betyder ett tomt block, och strängarna 'i' , 'j' , 'l' , 'o' , 's' , 't' och 'z' representerar block med olika färger.

![image](https://user-images.githubusercontent.com/4598641/226003821-3a435de3-4843-421e-ab20-477e93bf3fe8.png)

Alla olika typer av bitar lagras med sina roterade varianter.

![image](https://user-images.githubusercontent.com/4598641/226003959-15932dfd-3435-47dd-b1f2-78b050e562fb.png)

# Källor

Översatt och bearbetat för repl.it baserat på originalet: https://simplegametutorials.github.io/pygamezero/blocks/
