// Ez egy egy soros komment.

/* Több
    soros
komment.

*/

// Konzolba írás. (Autómatikusan hozzáírja a sortörést (\n).)
console.log("Hello Web!"); //A böngészőben nyisd meg az index.html-t majd nyomj egy F12-t és kattints a console-ra.

function load() {
    console.log("Az oldal betöltött.");
    document.getElementById("cim").innerHTML+=" DLC"; //id alapján kiválasztás és a tartalom módosítása

    // A következő kódrészt akkor olvasd el, ha végigértél ezen a függvény (load) utáni részen.
    // Itt class alapján kiválasztjuk az elemeket, majd a ponthatároknál kiíratjuk, hogy a hallgató teljesítette-e a kurzust.
    let intervallumok=document.getElementsByClassName("pont-intervallum");
    for (let i = 0; i < intervallumok.length; i++) {
        if (i === 4) {
            intervallumok[i].innerHTML+=" Megbuktál :(";
            continue;
        }
        intervallumok[i].innerHTML+=" Átmentél :)";
    }
} 

// Van szkriptnyelvek kurzus ahol részletesebben megtalálhatóak a JS alapok.

// Típusok
// number
let szam=42;
console.log("A szám típusa: '"+typeof szam+"'.");

// string
let szoveg="Az élet értelme: ";

// boolean (true | false)
let esik=false;

// tömb: Több elemet el lehet benne tárolni. Különböző típusúakat is.
let gyumolcsok=["alma", "szőlő", "körte", "szilva"];
console.log(szam);
console.log(szoveg + szam) //nem kell konverzió

// Vezérlési szerkezetek
// Feltételes elágazás
if(esik){
    console.log("Esik az 🌧️.")
} else {
    console.log("Nem esik az 🌧️.")
}

if(szam<6) {
    console.log("A "+szam+" kisebb mint 6.");
} else if(szam>=9) {
    console.log("A "+szam+" legalább 9.");
} else {
    console.log("A "+szam+" elvileg 6 és 9 között van. A kétszerese: "+(szam*2)+".");
}

// Ciklusok
console.log("Italok:")
for(let i=0;i<gyumolcsok.length;i++) {
    console.log("- "+gyumolcsok[i]+" üdítő")
}

//Ugyanez while ciklussal visszafelé
console.log("Italok visszafelé:")
let j=gyumolcsok.length;
while(j--){
    console.log("- "+gyumolcsok[j]+" üdítő")
}

// Most vissza lehet menni a load() függvényhez!
//Egyelőre ennyi volt a DLC demo része. Innentől a Cáospace felületéről tölthetik le a további DLC-ket.