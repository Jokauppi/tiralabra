# Toteutusdokumentti

## Ohjelman toteutus

Ohjelma jaettu kolmeen pakettiin `game`, `ai` ja `ui`, jotka jakavat pelitilanteen manipuloinnin ja tarkastelun, pelin algoritmit sekä käyttöliittymän toiminnot erilleen.

Kaikki pelitilanteeseen liittyvä tieto sekä suurin osa sen manipulointiin tarkoitetuista metodeista on sijoitettu game-paketin Board-luokkaan. Keskeisin näistä on move-metodi, jolla suoritetaan perin siirrot. Metodi käsittelee jokaisen rivin tai sarakkeen yksitellen työntämällä tai vetämällä sen numeroita jompaan kumpaan suuntaan yhdistämällä samat numerot ja lopuksi tarkistaa, onko peli voitettu tai hävitty.

ExpectimaxAI-luokka sisältää kokonaan siirtojen valintaan tarvittavan algoritmin sekä sen käyttämät pienet heuristiikkafunktiot.

Käyttöliittymä on jaettu moniin luokkiin, jotka vastaavat käyttöliiittymän eri näkymistä. Suurin osa käyttöliittymästä on toteutettu konsolipohjaisen valikon avulla jota voi käyttää nuolinäppäimillä tai pikanäppäimillä.

Peliä on laajennettu alkuperäisen määritelmän ulkopuolelle sallimalla mielivaltaiset pelilaudan koot, jolloin tavoiteltava numero määräytyy kaavan $2^{⌊\frac{10\cdot n^2}{16}⌋}$ mukaan, jossa $n$ on pelilaudan leveys.

## ALgoritmin toteutus

### Expectimax

Expectimax-algoritmi on variaatio minimax-algoritmista, josta vastustajan minimointiaskel on otettu pois ja tilalla käytetään askelta jossa lasketaa keskiarvo kaikkien siirtojen arvosta niiden todennäköisyyksien avulla. Mikäli tietokone asettaisi numerot aina hankalimpiin paikkoihin, olisi minimax parempi vaihtoehto, mutta koska tietokoneen siirrot ovat täysin sattumanvaraisia, ei minimointiaskeleesta olisi merkittävää hyötyä. Koska kaikki tietokoneen siirrot ovat yhtä todennäköisiä, ei minimax-algoritmille olisi myöskään kovin hyödyllistä tehdä alfa-beta -karsintaa eikä aikavaativuutta näin voisi laskea ja suorituskykyä nostettua.

### Aikavaativuus

Expectimaxin aikavaativuus on 2048-pelissä $\mathcal{O}(b^mn^m)$, jossa $n$ on mahdollisten uusien numeroiden määrä, $b$ mahdollisten siirtojen määrä ja $m$ algoritmissa käytetty hakusyvyys. Pelilaudan koko on myös muutettavissa, jolloin aikavaativuus kasvaa pelilaudan kokoon suhteutettuna $\mathcal{O}(l^2)$, jossa $l$ on pelilaudan leveys.

Testauksen perusteella $b$:n toteutuva arvo on käytännössä 4,0. $n$:n arvo puolestaan riippuu paljolti heuristiikkafunktiosta mutta näyttäisi testauksen perustella totetutuvan arvoon 11,6, kun pelilaudan leveys on 4 (vapaiden ruutujen määrä on voitettavan pelin varrella keskimäärin 5,3 per vuoro ja jokaista ruutua kohden on tarkasteltava numerot 2 ja 4). 

Koska hakusyvyyttä kasvatettaessa yhdellä tarkastellaan lisää joko vain tietokoneen siirtoja tai pelaajan siirtoja, kertaantuu suoritusaika todellisuudessa vuorotellen nelinkertaiseksi tai 11-kertaiseksi. Tietokoneen siirtojen lisääminen todellisuudessa lisää suoritusaikaa vain 8-10 -kertaisesti sillä osa siirroista voidaan karsia pois, mikäli edellisen kerroksen siirto ei tehnyt pelilautaan muutoksia.

### Heuristiikka

Käytetyt heuristiikkafunktiot ovat suhteellisen yksinkertaisia ja ne perustuvat pelilautan arvojen kertomiseen tietyillä painoilla tai pelitilanteeen pistemäärään.

#### Zigzag

Laudan ruutujen painotukset. Funktio suosii suurempia numeroita suurempien painotuksien ruuduissa.
```
╔════╦════╦════╦════╗
║   4║   5║  12║  13║
╠════╬════╬════╬════╣
║   3║   6║  11║  14║
╠════╬════╬════╬════╣
║   2║   7║  10║  15║
╠════╬════╬════╬════╣
║   1║   8║   9║  16║
╚════╩════╩════╩════╝
```
Onnistunein testaamani heuristiikkafunktio matkii tapaa, jolla ihmispelaajatkin usein pelaavat peliä. Funktio pyrki kasaamaan numerot suuruusjärjestykseen jonoon joka kulkee "siksakkia" laudan puolelta toiselle. Näin minimoidaan isompien numeroiden yhdistämiseen tarvittavat siirrot kun tarvittavat numerot on luotu laudalle ja varataan mahdollisimman suuri alue uusien numeroiden muodostamiselle, kun numerot on yhdistetty. Funktio pitää suuret numerot kulmassa ja yhdessä reunassa, jolloin myös maksimoidaan käytettävissä oleva tila pienempien numeroiden yhditämiseen.

#### Corner

```
╔════╦════╦════╦════╗
║   0║   1║   2║   3║
╠════╬════╬════╬════╣
║   1║   2║   3║   4║
╠════╬════╬════╬════╣
║   2║   3║   4║   5║
╠════╬════╬════╬════╣
║   3║   4║   5║   6║
╚════╩════╩════╩════╝
```
Toiseksi onnistunein heuristiikkafunktio pyrkii kasaamaan suurimman numerot yhteen kulmaan. Funktio toimii lähes kuten zigzag mutta joutuu usein tekemään ylimääräisiä siirtoja poispäin kulmasta yhdistääkseen numeroita ja luodakseen uusia suotuisiin paikkoihin. Suuria numeroita päätyy myös kauaksi toisistaan vasempaan alakulmaan ja oikeaan yläkulmaan jolloin kyseisiä numeroita on haasteellista yhdistää ja tila loppuu pienemmiltä numeroilta kesken.

#### Score

Pelissä saa pisteitä yhtistämällä kaksi numeroa, jolloin pisteitä kertyy ydistetyn numeron verran. Täysin pelin pisteytykseen perustuva heuristiikkafunktio on nopeampi suorittaa, mutta ei huomioi mitenkään numeroiden asettelua. Tämän seurauksena suuret numerot päätyvät usein laudan keskelle ja useimmin yhdistettävät pienemmät numerot päätyvät laudan eri puolille hankaliin paikkoihin ja tila loppuu kesken.

#### Edge

```
╔════╦════╦════╦════╗
║ 100║  10║  10║ 100║
╠════╬════╬════╬════╣
║  10║   1║   1║  10║
╠════╬════╬════╬════╣
║  10║   1║   1║  10║
╠════╬════╬════╬════╣
║ 100║  10║  10║ 100║
╚════╩════╩════╩════╝
```
Tämä funktio suosii erityisesti kulmia ja reunoja mutta kaikkia kulmia keskenään yhtä paljon. Tämä johtaa siihen, että siirtoja tapahtuu paljon puolelta toiselle ja suuret numerot päätyvät vahvasta painotuksesta huolimatta usein keskelle seuraa sama ongelma kuin pistepohjaisessa funktiossa.

### Satunnaisalgoritmi

Ennen expectimax-algoritmin toteuttamista loin lähinnä varhaista testaamista varten yksinkertaisen "algoritmin", joka generoi pelille satunnaisia siirtoja. Satunnaisalgoritmin todennäköisyys läpäistä peli on luonnollisesti häviävän pieni, mutta satunnaisalgoritmi toimii hyvänä vertailukohtana varsinkin expectimax-algroitmille toteutetuille huonommille heuristiikkafunktiolle ja algoritmin pienemmille hakusyvyyksille. Satunnaisalgoritmin saavuttama maksimilukujen mediaani on 128. Toiseksi yleisin luku on 64, mutta myös lukuun 256 se pääsee kiitettävän usein. Tätä suurempia lukuja on käytännössä mahdotonta saavuttaa kannettavan tietokoneen testauskapasiteetilla järkevällä aikaskaalalla.

## Työn kehityskohteet
Algoritmin onnistumisprosentin kannalta eniten kehitettävää olisi ollut heuristiikka. Lukemieni lähteiden perusteella hyvällä heuristiikkafunktiolla olisi ilman muutoksia itse expectimax-algoritmiin mahdollista päästä huomattavasti suurempiin lukuihin ja voittaa peli käytännössä 100 % ajasta.

Itse expectimax-algoritmin nopeudessa ja pelilaudan manipulointiin liittyvissä metodeissa olisi ollut varaa parantaa suorituskykyä jonkin verran, sillä joillain toteutuksilla on saavutettu sama siirtojen nopeus yhden tai kaksi tasoa suuremmalla hakusyvyydellä

Olisi ollut mielenkiintoista myös tehdä toteutus minimax-algoritmista ja verrata sen toimintaa expectimaxiin.

## Lähteet

Stackoverflow [https://stackoverflow.com/questions/22342854/](https://stackoverflow.com/questions/22342854/what-is-the-optimal-algorithm-for-the-game-2048/22498940#22498940)
Wikipedia, Expectiminimax, luettu 22.12.22 [https://en.wikipedia.org/wiki/Expectiminimax](https://en.wikipedia.org/wiki/Expectiminimax)