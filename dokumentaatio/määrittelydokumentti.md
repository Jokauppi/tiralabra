# Määrittelydokumentti

Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti
Koodin kieli: englanti
Dokumentaation kieli: suomi

## Ohjelmointikielet

Projektin ohjelmointikieli:
- Python

Osaamani kielet:
- Python
- JavaScript/TypeScript
- (Java)

## Ongelma

Tavoitteena on tekoälyn luominen 2048-peliin, joka mahdollisimman suurella todennäköisyydellä ja kiitettävällä suoritusajalla pystyy muodostamaan $2048$ ruudun $4\times4$ ruudukossa ja $2^{⌊\frac{10\cdot n^2}{16}⌋}$ ruudun $n\times n$ ruudukossa.

## Algoritmi

Tavoitteena on määrittää eri pelitilanteille erilaisia arvoja erilaisilla heuristiikkafunktioilla ja käyttää näitä apuna [expectimax](https://en.wikipedia.org/wiki/Expectiminimax)-algoritmissa.
Expectimax on minimax-algoritmin variaatio joka soveltuu paremmin peleihin, joissa tietokoneen tekemä siirto perustuu puhtaasti sattumaan. Siinä ei siis suoriteta vastustajan minimointivaihetta, vaan ainoastaan pelaajan maksimointivaihe. Minimointivaiheen tilalla on pelitilanteiden arvojen tasoitus niiden todennäköisyyksien mukaan. 

## Syöte

Algoritmin syötteenä on pelilaudan tilanne, jonka pohjalta algoritmi tutkii tulevia siirtoja.

## Aika- ja tilavaativuudet

Expectimaxin aikavaativuus on parhaimmassa tapauksessa $\mathcal{O}(b^m)$, kun kaikki tietokoneen siirrot tiedetään ja huonoimmassa $\mathcal{O}(b^mn^m)$, jossa $n$ on mahdollisten uusien numeroiden määrä, $b$ mahdollisten siirtojen määrä ja $m$ algoritmissa käytetty hakusyvyys. Koska algoritmin toteutuksessa pelille kaikki tietokoneen siirrot ovat mahdollisia, on toteutuksen noudatettava huonointa tapausta. Pelilaudan koko on myös määritettävissä, jolloin aikavaativuus laudan koon suhteen on $\mathcal{O}(n^2)$, jossa n on laudan leveys.

## Lähteet

[https://en.wikipedia.org/wiki/Expectiminimax](https://en.wikipedia.org/wiki/Expectiminimax)
[https://stackoverflow.com/questions/22342854/](https://stackoverflow.com/questions/22342854/what-is-the-optimal-algorithm-for-the-game-2048/22498940#22498940)