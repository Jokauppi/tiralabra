# Käyttöohje

## Projektin asentaminen ja käynnistäminen

> Projektin paketinhallinnassa käytetään _Poetry_:ä, joka on oltava asennettuna ohjelman käynnistämiseksi.

> Projektin käyttöliittymäkirjaston vuoksi ohjelma on käynnistettävissä vain linux- tai mac-pohjaisissa järjestelmissä (ml. WSL).

Tarvittavat kirjastot asennetaan ensin projektin hakemistossa komennolla `poetry install`

Ohjelman voi tämän jälkeen käynnistää komennolla `poetry run python3 src/`

> Pelin pelilautan koon voi määrittää asettamalla ympäristömuuttujan BOARD_SIZE johonkin positiiviseen lukuarvoon esim. `BOARD_SIZE=5 poetry run python3 src/`.
> Huomaa kuitenkin, että osa heuristiikka-algoritmeista ei toimi eri laudan koolla (zigzag ja edge)

## Testit ja tyylin tarkistus

Ohjelman testit on mahdollista ajaa komennolla `poetry run pytest`

Ohjelman koodin tyyli on mahdollista tarkistaa komennolla `poetry run pylint src/`

## Käyttöliittymä

Ohjelma koostuu pääosin valikoista, joita voi navigoida nuolinäppäimillä ja enterillä tai hakasuluissa näkyvillä pikanäppäimillä
```
2048-AI
> [a] Algorithm play
  [h] Human play
  [q] Quit
```
Peliä on mahdollista kokeilla ja pelata itse kohdasta `Human play`.
Kohdassa `Algorithm play` on mahdollista tarkastella peliä algoritmin pelaamana joko siirto siirrolta visuaalisesti tai koostettuna tilastona useiden pelien pohjalta.

### Visuaalinen näkymä
```
Seed: 2035629
╔════╦════╦════╦════╗
║    ║   4║    ║    ║
╠════╬════╬════╬════╣
║    ║   8║   2║    ║
╠════╬════╬════╬════╣
║   2║   2║   8║    ║
╠════╬════╬════╬════╣
║   4║   8║   2║2048║
╚════╩════╩════╩════╝
Score: 20164
Board won!
```

### Tilastonäkymä
```
Chosen algorithm: ExpectimaxAI
Chosen Heuristics: zigzag
Set algorithm search depth [empty = 4]: 3
Amount of games:10

SUMMARY
=========
Wins: 7
Games played: 10
Win%: 70.0
Max score: 60756
Avg score: 32390.4
Avg time per move: 0:00:00.005568 (h:min:s)
Avg time to victory: 0:00:05.672163 (h:min:s)
Max highest number: 4096
Median highest number: 2048

HIGHEST NUMBERS OCCURRENCES
=========
512:   *
1024:  **
2048:  *****
4096:  **
```

## Peli

Pelin tavoitteena on saada pelilaudalle numero 2048 siirtämällä laudalla olevia numeroita pelilaudan reunoihin ja yhdistelemällä vierekkäisiä samoja numeroita kahden potensseiksi. Siirtoja voi tehdä `Human play`-näkymässä WASD-näppäimillä.

```
╔════╦════╦════╦════╗
║    ║   2║   8║   2║
╠════╬════╬════╬════╣
║    ║    ║   8║  32║
╠════╬════╬════╬════╣
║    ║    ║  64║   2║
╠════╬════╬════╬════╣
║   2║    ║    ║   4║
╚════╩════╩════╩════╝
Score: 460
> [w] ↑
  [s] ↓
  [a] ←
  [d] →
  [q] Quit game
```
Esimerkki kaksi numeroa yhdistävästä siirrosta:
```
╔════╦════╦════╦════╗
║    ║    ║    ║   2║
╠════╬════╬════╬════╣
║    ║    ║    ║   2║
╠════╬════╬════╬════╣
║    ║    ║    ║    ║
╠════╬════╬════╬════╣
║    ║    ║    ║    ║
╚════╩════╩════╩════╝
Siirto ylös ↑
╔════╦════╦════╦════╗
║    ║    ║    ║   4║
╠════╬════╬════╬════╣
║   2║    ║    ║    ║
╠════╬════╬════╬════╣
║    ║    ║    ║    ║
╠════╬════╬════╬════╣
║    ║    ║    ║    ║
╚════╩════╩════╩════╝
```
Esimerkki voittavasta siirrosta:
```
╔════╦════╦════╦════╗
║    ║   4║    ║    ║
╠════╬════╬════╬════╣
║    ║   8║   2║    ║
╠════╬════╬════╬════╣
║   2║   2║   8║1024║
╠════╬════╬════╬════╣
║   4║   8║   2║1024║
╚════╩════╩════╩════╝
Siirto alas ↓
╔════╦════╦════╦════╗
║    ║   4║    ║   2║
╠════╬════╬════╬════╣
║    ║   8║   2║    ║
╠════╬════╬════╬════╣
║   2║   2║   8║    ║
╠════╬════╬════╬════╣
║   4║   8║   2║2048║
╚════╩════╩════╩════╝
```
