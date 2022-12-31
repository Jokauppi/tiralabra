# Testausdokumentti

## Testauksen toteutus

Testaus toteuttettiin yksikkö- ja integraationtesteinä pytest-kirjastolla. Testikattavuus ladattiin Github Actionsin avulla Codecoviin.

Peliluokkien testaus tapahtui lähinnä yksikkötestauksena, kun taas algoritmin testauksessa käytettiin hyväksi peliluokkia ja testit olivat käytäännössä integraatiotestausta.

Expectimax-algoritmin yksikkötestaus on haastavaa sillä pelissä on paljon satunnaisuutta ja samaan lopputulokseen voidaan päästä useaa eri reittiä. Tämän seurauksena algoritmi hylkää usein siirtoja, jotka ihminen tekisi vaistonvaraisesti, ja tekee siirron aivan toiseen suuntaan tiedolla että samaan tai lähes samaan tilanteeseen päädytään kuitenkin myöhemmässä siirrossa. Algoritmissa ei siis usein ole ns. oikeita siirtoja ja testaus perustuu lähinnä suurpiisteiseempiin tavoitteisiin.

Käyttöliittymä jätettiin testaamatta ohjelmallisesti ja testaus suoritettiin manuaalisesti. Projektissa oli aluksi valmius tehdä käyttöliittymätestausta mut se jätettiin pois sen työläyden ja pienen hyödyn vuoksi.

### Testien syötteet

Testeissä käytettiin syötteinä lautojen tai rivien pelitiloja. Algoritmin testauksessa pyrittiin räätälöimään syötteitä korostamaan jonkin tietyn tavoitteen saavuttamista esim. häviön välttämistä.

## Testikattavuus

Ohjelman peli- ja algoritmiluokille saatiin laaja testauskattavuus. Peliluokkien pienepien funktioden testaus tapahtui lähinnä algoritmin integraatiotastauksen kautta.

|Module|statements|missing|excluded|branches|partial|coverage|
|---|---|---|---|---|---|---|
|src/ai/__init__.py 	    |0 	|0 	|0 	|0 	|0 	|100%|
|src/ai/expectimax_ai.py 	|72 |2 	|0 	|30 |1 	|97%|
|src/ai/random_ai.py 	    |7 	|0 	|0 	|0 	|0 	|100%|
|src/game/__init__.py 	    |0 	|0 	|0 	|0 	|0 	|100%|
|src/game/board.py 	        |109|3 	|0 	|36 |0 	|98%|
|src/game/board_utils.py 	|73 |1 	|33 |26 |1 	|98%|
|Total 	                    |261|6 	|33 |92 |2 	|98%|

## Algoritmin suorituskykytestaus

Algoritmin suorituskykytestausta tehtiin ohjelmaan rakennetulla `benchmark`-toiminnolla joka suoritti useita pelejä ja koosti tilaston pelatuista peleistä. Toiminnolla mitattiin mm. voittoprosenttia, mediaani- ja maksiminumeroita, siirtoon ja peliin kulunutta aikaa sekä eri maksiminumeroide esiintymiskertoja.

Esimerkki testausdatasta valinnoilla Expectimax, Zigzag ja syvyys 3:

```
SUMMARY
=========
Wins: 171
Games played: 300
Win%: 56.99999999999999
Max score: 74968
Avg score: 26569.72
Avg time per move: 0:00:00.005722 (h:min:s)
Avg time to victory: 0:00:06.264535 (h:min:s)
Max highest number: 4096
Median highest number: 2048

HIGHEST NUMBERS OCCURRENCES
=========
256:   *
512:   ***********************
1024:  *********************************************************************************************************
2048:  ********************************************************************************************************************************************
4096:  *******************************
```

### Syvyys

Syvyydellä oli merkittävä vaikutus algoritmin käyttämään keskimääräisiin siirto- ja voittoaikoihin. Voittoprosenttia syvyyden kasvattaminen nosti reilusti mutta vähenevin tuloksin. Syvyyden 5 voittoprosentti on epävarma sillä otos on pieni, kuitenkin yli 90 %.

|Algorimi ja heuristiikka|Syvyys|aika/siirto (ms)|aika alusta voittoon (s)|voitto%|
|---|---|---|---|---|
|Expectimax + Zigzag|3|5,7|6,2|57,0|
|Expectimax + Zigzag|4|34,3|41|81,7|
|Expectimax + Zigzag|5|221,1|343|~95|

### Heuristiikka
Heuristiikalla ei ollut yhtä suurta vaikutusta siirto- tai voittoaikoihin, mutta vaikutus voittoprosenttiin oli merkittävä.

|Algorimi ja heuristiikka|Syvyys|aika/siirto (ms)|aika alusta voittoon (s)|voitto%|
|---|---|---|---|---|
|Expectimax + Zigzag|3|5,7|6,2|57,0|
|Expectimax + Corner|3|5,6|6,9|38,3|
|Expectimax + Score|3|4,8|4,2|1,7|
|Expectimax + Edge|3|4,6|-|0|