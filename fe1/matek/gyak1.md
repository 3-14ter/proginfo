# 1. óra
- Kőműves Emese
- komuvesemeseon@gmail.com

- követelmények:
    - hiányzás: 
        - 3 igazolatlan hiányzás MAX 
        - utána igazolás kell
        - hiányzások után sikertelenn tárgy
    - előadás: kellene
- Gyakorlat jegy:
    - megajánlott jegy félév végén
    - 1-es gyak esetén: gyak uv (utóvizsga) -> szóban vizsgázni kell, nem lehet megajánlottként elfogadtatni
- E-tesztek
    - 6 db
    - 4 pontosak
    - min 10 sum
    - napi 1x kitölthető
    - időtúllépés 0p
    - nem pótolható
    - regisztrálni kell (neptun kód, email)
-ZH-k
    - 6. hét (okt. 13)
    - 13. hét (dec. 1)
    - 2x36 pont
- előadás:
    - plusz pontok
- gyakorlat röpdoga:
    - minden gyak elején (x11)
    - max 1 szorgalmi pont / óra
        - kockák
- javítások:
    - gyak uv
    - e-teszt miniimumok megvannak (10p):
        - 1 ZH javítás/pótlási lehetőség
        - megajánlottnak számít
    - e-teszt minimum nincs meg:
        - elégtelen ag gyakorlat -> gyak uv kell
    - ez így szopó
ponthatárok:
    -
# Óra
- gak színtéren feladatsor linkek megvannak
## Ítélet kalkulus
- Alapja az ítélet -> olyan állítás/kij. mondat, ami vagy igaz, vagy hamis, egyszerre mind2 NEM lehet
- Logikai érték/ igazságérték:
    - igaz, vagy hamis (boolean)
- A és B ítéletek
    - negáció
        - ítélet elé
    - ÉS / konjunkció
        - A ^ B
    - VAGY / negáció
        - A ˇ B
    - implikáció
        - A -> B
    - ekvivalencia
        - A <-> B
- A és B:
    - ezek prímítéletek (tovább nem bontható)
- ítélet:
    - A 
    - B
    - A^B
    - stb...
    - negáció is 
- formula:
    - ítéletek összekapcsolása
    - maguk az ítéletek is
- igazságábra

## Feladatok
- 1. 
    - A: süt a nap
    - B: kimegyek az uszodába
    - C hamburgert ebédelek
        - Kimegyek az uszodába vagy hamburgert ebédelek: B ˇ C
        - Nem süt a Nap: negált A
        - Ha kimegyek az uszodába, hamburgert ebédelek B -> C
- 1.4a formalizációa
    - A: ezt a mindatot jól formalizálom
    - B: gyakveznek jó kedve van
    - C: kapok egy pirospontot
    - D: örülhetek
- 1.4b
    - A: megyek boltba
    - B: esik az eső
    - C: van nálam esernyő
    - A -> (neg. B ˇ(B^C) )
- 1.4c
    - Pontosan akkor érem el az zht, ha nem esik több hó, vagy ha eltakarítják
    - A: elérem a zh-t
    - B: több hó esik
    - C: eltakarítják
    - A <-> (negB v (B^C))
- 1.4d
    - Ki kell találnom még formalizálandó feladatokat, vagy kirugnak és mehetek utcát seperni
    - A v (B^C)
- 1.5a ítéletformalizáció
    - Ha micimackó mézet akar enni de a méz a fán van akkor a mézszerzés akkor sikeres ha malacka nem fél a méhektől és tigris fel tud mászni a fára 
    - A: micimackó mézet akar enni
    - B: méz a fán van
    - C: mézszerzés sikeres
    - D: malacka fél a méhektől
    - E: Tigris fel tud mászni a fára
    - (A ^ B) -> C <-> ((negD) v E)
    - A i, B h, C i, neg(D) h, E i

- részformulák
    - nagyobb formula részei
    - minden formula amiből a fő formula összetevődik, részformulának számít

- 1.6b (igazságtábla)
    - ((neg(A))->(A^B))^C  <-> (A<->C)A
 

- ekvivalencia:
    - F és G formulák ekvivalensek, ha F <-> G minden esetben igaz



# 2. Hét

Ismert ekvivalenciák:
1. Implikációt ki tudjuk fejeznidiszjunkcióval és negációval: A->B --- (nA)vB
2. Negáció alaptulajdonság:  n(nA) --- A
3. De Morgan azonosság: 
    - n(AvB) --- (nA)^(nB)
    - n(A^B) --- (nA)v(nB)
4. v és ˇalaptuulajdonságai (néhány)
    - kommutatív
    - asszociatív
5. -> és <-> tulajdonságai
    - A<->B --- (A->B)^(B->A)

## Feladat

### 1.8
- n(A->B) --- n((nA)vB) --- (n(nA))^(nB) --- A^(nB)

### 1.9
- klóz: olyan formula melyben a változók és a váétozók negáltjai diszjunkciójával szerepelnek és legfeljebb egyszer
    - pl: _v_v_ viszont nA^BvC nem klót -> csak BvC
- konjunktív normál forma:
    - olyan formula ami több klózból épül föl, konjunkciócal elválasztva
    - F K1^K2...^Kx
    - pl: (AvB)^(AvC)
- taljes konjunktív normálforma
    - mindek kólzjában szerepel az összes prímítélet egyetlen egyszer
    - A1,...,An náltozók, K1^...^Kn <- knf, és a1,...An ítéletváltozók mindegyike negálva vagy negálatlanul szerepel az összes K1,...,Kn-ben
    - pl: (AvBvC)^(Av(nB)vC)
- F1 = knf
- F2 = egyesevel, nem knf
- F3 = tknf
- F4 = tknf
- F6 = külön klózok

### 1.10
- Av(nB) -> (C<->B)

| A | B | C | nB | Av(nB) | C <-> B | Av(nB) -> (C<->B) |
|i|
|i|
|i|
|i|
|h|
|h|
|h|
|h|

## Predikátum kalulus
- univerzális kvantor $\forall$: minden
- egszisztenciális kvantor $\exists$: létezik, van olyan
- predikátorjel: pl nagyobb N(x,y):x>y
    - N(3,2) - igaz
- Predikátum:
    - olyan kifejezés amelybe alkalmas objektumokat behelyettesítve ítéletet kapunk
    - pl: P(x): x piros --> P(alma) = alma piros

### 2.1
- P(x) x páros szám, O(x,y): x osztója y-nak, o(a,b)=a+b, s(a,b)=a*B
- a) P(7): 7 páros szám - nem
- d) ($\exists$)(P(x)O(x,6))  létezik olyan száma, ami páros és oosztója 6-nak
- f) ($\forall$ x)($\forall$ y)(P(o(x,y)) <-> P(s(x,y))) - Két egész szám összege páro pontosan akkor, ha szorzatuk is páros - nuh uh

### 2.2
- 