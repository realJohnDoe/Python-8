# Snake ⭐⭐⭐
## En handledning för Python och Pygame Zero 1.2
![image](https://user-images.githubusercontent.com/4598641/226440407-e4b478ca-f453-48b3-a640-38e4858d1c56.png)

# Regler
Skjut alla lådorna på förvaringsplatserna.

Lådor kan endast flyttas om det finns ett ledigt utrymme bortom den (inte en vägg eller annan låda).

## Teckenförklaring

![image](https://user-images.githubusercontent.com/4598641/226440572-913c4152-7a92-415b-82c2-ebf0f5817183.png)
Spelare<br>
![image](https://user-images.githubusercontent.com/4598641/226440611-a41f140d-f21d-4e68-a216-17f9fe4ef197.png)
Spelare på lagring<br>
![image](https://user-images.githubusercontent.com/4598641/226440626-7c18df09-a547-48eb-ab11-13b1e372e626.png)
Låda<br>
![image](https://user-images.githubusercontent.com/4598641/226440685-78b3e349-3357-44c4-abc7-5fffb41ff9b6.png)
Box på förvaring<br>
![image](https://user-images.githubusercontent.com/4598641/226440711-2682f8f3-d36c-448d-a9c4-7f37e79a1840.png)
Lagring<br>
![image](https://user-images.githubusercontent.com/4598641/226440721-3dafc158-56c0-4038-8c98-8dd8bb8b512a.png)
Vägg

## Kontroller
Piltangenter	Flytta
r	Återställ nivån
n	Nästa nivå
sid	Tidigare nivå

# Översikt
De olika tillstånden en cell kan vara i representeras av följande strängar:

'@'	Spelare
'+'	Spelare på lagring
'$'	Låda
'*'	Box på förvaring
'.'	Lagring
'#'	Vägg

Varje spelnivå (level) lagras som ett rutnät av dessa strängar.




# Källor
https://simplegametutorials.github.io/pygamezero/sokoban/
