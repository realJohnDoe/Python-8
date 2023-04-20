# `Actor` har många användbara funktioner i Pygame Zero Helper

Det finns en del användbara grafikfunktioner som saknas i vanliga *Pygame Zero*.

Här är en lista med funktionena i *Pygame Zero Helper* och en väldigt kort förklaring av varje.

Kodexempel hittar du på hemsidan  https://www.aposteriori.com.sg/pygame-zero-helper/
och i projekten [Gem Catcher](https://github.com/coderdojolund/Python-8/blob/main/Gem-Catcher/gem-catcher.md) och [Ninja Runner](https://github.com/coderdojolund/Python-8/blob/main/Ninja-Runner/ninja-runner.md).

| Python-funktion för Actor | Kort förklaring |
| ----------------- | --------------- |
| `Actor.flip_x`, `Actor.flip_y` | Spegla Actor horisontellt eller vertikalt |
| `scale` | Sätt skalfaktorn för att göra Actor större eller mindre |
| `move_forward()`, `move_back()`,<br>`move_right()`, `move_left()` | Flytta Actor i en viss riktning | 
| `direction`, `move_in_direction()` | Sätt riktning ocn flytta utan att rotera |
| `distance_to()`, `direction_to()` | Avstånd och riktning till en annan Actor |
| `move_towards()`, `point_towards()` | Gå eller peka mot en annan Actor |
| `get_rect()` | Gör Actor till ett Rect-objekt |
| `images`, `next_image()` | Bestäm klädslar för en Actor och byt till nästa klädsel |
| `fps`, `animate()` | Bestäm hur ofta Actor ska byta klädsel |
| `collidepoint_pixel()`, `collide_pixel()`,<br>`colllidelist_pixel()`, `collidelistall_pixel()` | Upptäck kollisioner exakt men långsamt |
| `obb_collidepoint()`, `obb_collidepoints()` | Upptäck kollisioner ungefär men snabbt |
| `circle_collidepoint()`, `circle_collidepoints()` | Upptäck kollision för runda figurer, ungefär men snabbt |
| `set_fulscreen()`, `set_windowed()`, `toggle_fullscreen()`,<br>`hide_mouse()`, `show_mouse()` | Byt till fullskärm eller fönster. Göm eller visa muspekare |

Gem Catcher hittar du här: https://github.com/coderdojolund/Python-8/blob/main/Ninja-Runner/ninja-runner.md

Ninja Runner hittar du här: https://github.com/coderdojolund/Python-8/blob/main/Ninja-Runner/ninja-runner.md
