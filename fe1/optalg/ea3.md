# terminológia
1. döntési változók
    - x1, x2, ... (változó mennyisége)
2. értelmezési tartomány



# Cél
- profit maximalizálása
- katona eladáas után 3$ -> (3*x1)
- vonat után 2$ -> (2*x2)
- célfüggvény:
    - z=3*x1 + 2*x2 --> kétváltozós lineáris fgv
- korlátozások.
    - összes gyártásra szánt idő
    - 1x1 +1x2 óra fafaragás szükséges ö. 80 óra
    - 2x1+1x2 óra lakkozás-festés ö.100 óra
    - gyártott katonák száma nem lehet több, mint 40 -> x1 <= 40
    - x1,x2 nem negatív egész
        - MAX --> z=3x1+2x2 
            - x1+x2 <= 80
            - 2x1+x2<=100
            - x1 <=40
            - x1,x2>=0
- egyenletrendszer:
    - a döntési változók lineáris fügvvénye 
    - lineáris egyenlőtlenségek a korlátozó feltételek
- ha még egy válotzó (pl kishajó gyártás)
    - --> 3., 4., ... változó
    - komplex gyárban hasonló egyenletrendszer, több változóval
- lineáris programozási feladat, standard formája
- lineáris programozási feladat
    - lineáris célfüggvény minimumást/maximumát
- lehetséges megoldások halmaza
    - összes megoldás (kb végtelen)
- optimális megoldás
    - lehetséges megoldás és maximumon/minimumon van
- LP feladat megoldás
    - x1+x2<=80
        - x1 - 80 <= x2
    - 2*x1+x2<=100
    - x1<=40
- csúcs: két egyenes metszéspontja
- tétel: ha van optimális megoldás, akkor olyan optimális megoldás is van, ami a lehetséges megoldáso tartomány csúcspontja
-     