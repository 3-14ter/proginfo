/* Órai stuff begin */
let isOpen = false;
let jobPanel = document.getElementById("job-panel");
let catPanel = document.getElementById("cat-panel");
let tourPanel = document.getElementById("tour-panel");


function showPanel(which) {

    if (which == "job" && !isOpen) {
        jobPanel.style.display = "block";
        isOpen = true;
        jobPanel.classList.add("active");
    }

    if (which == 'cat' && !isOpen) {
        catPanel.style.display = "block";
        isOpen = true;
    }

    if (which === "tour" && !isOpen) {
        tourPanel.style.display = "block";
        isOpen = true;
    }

}

let closeButtons = document.getElementsByClassName('close-button');

for (let btn of closeButtons) {
    btn.addEventListener("click", function() {
        isOpen = false;
        jobPanel.classList.remove("active");
        jobPanel.style.display = 'none';
        catPanel.style.display = 'none';
        tourPanel.style.display = 'none';
    });
}

/* Órai stuff end */



/*
 Ebben a DLC-ben végre elérkeztünk az űrlapokhoz.
 Megnézzük hogynan lehet űrlapmezőket ((tiszta Sci-fi)) lekérni és az értékükkel adatot feldolgozni.
 Van egy kis CSS DLC is ami amúgy.
*/


// Konvertáló függvény.
// A kódot eldarabolja #RRGGBB -> [RR,GG,BB] majd átváltja tízes számrendszerbe (parseInt második paramétere hogy hanyas számrendszerből kódolsz 10-esre).
function szinkodToRGB(kod){
    return [kod.substring(1,3),kod.substring(3,5),kod.substring(5,7)].map(v=>parseInt(v,16));
    // Igen tudom hogy a darabolást is lehetne kompaktabban de legalább így olvashatóbb.
}

// Visszakonvertáló függvény. (opcionális de itt van)
// A toString paramétere hogy 10-es számrendszerből hanyasra váltsa.
// A reduce segítségével rakjuk össze a kódot. (ezt most kicsit hosszú lenne elmagyarázni)
// A padStart 2 karakter hosszúra egészíti ki a szöveget "0"-ákkal az elején.
function RGBToSzinkod(rgb){
    return "#"+rgb.reduce((prev, curr)=>prev+curr.toString(16).padStart(2, "0"), "");
}

// Random szín.
function randomSzin(){
    return RGBToSzinkod([Math.random(), Math.random(), Math.random()].map(v=>Math.floor(256*v)));
}

document.addEventListener("DOMContentLoaded", (event) => {
    // Az űrlap validálásához a validateFrom függvényt hívjuk meg a form onsubmit-jében.
    // onsubmit="return validateFrom1(this);"
    // A return ha igaz akkor elküldi a formot azaz nem volt hiba.
    // Ha false akkor pedig megakadályozzuk az elküldést.

    // Adjunk meg a macskák színére random értékeket.
    let szin=document.getElementsByName("macskolor")[0];
    let szinmegint=document.getElementsByName("macskolormegint")[0];
    szin.value=randomSzin();
    szinmegint.value=randomSzin();

    // Úti cél: fold:🌍, hold:🌕, mars:🛸, titok:🌌
    let uticel=document.getElementsByName("uticel")[0];
    uticel.addEventListener("change", function(){
        let uticel_out=document.getElementById("uticel");
        switch (uticel.value){
            case "fold":
                uticel_out.innerHTML="🌍";
                break;
            case "hold":
                uticel_out.innerHTML="🌕";
                break;
            case "mars":
                uticel_out.innerHTML="🛸";
                break;
            case "titok":
                uticel_out.innerHTML="🌌";
                break;
            default:
                uticel_out.innerHTML="";
        }
    });

    // utasszam
    let utasszam=document.getElementsByName("utasszam")[0];
    let emberek=document.getElementById("emberek");
    utasszam.addEventListener("change", function(evt){
        let utasok_szama=evt.target.value;
        // A repeat megismétli a stringet egymás után annyiszor amennyit a paraméterében megadunk.
        emberek.innerHTML="👤".repeat(utasok_szama);
    });

    // Kezdő dátum beállítása
    let indulas=document.getElementsByName("indulas-datum")[0];
    indulas.min=new Date().toISOString().slice(0, 10);

    let felkeszultseg=document.getElementsByName("felkeszultseg")[0];
    // Az intervallumnál írjuk ki mellé mi az aktuális érték. Ezt akkor írjuk ki ha változik az értéke. Ez lesz a "change" event.
    // Ha még dinamikusabban szeretnénk látni a változást próbáld meg a "mousemove" eventet (cseréld ki az első paraméterben lévő change-t) és töltsd újra az oldalt!
    felkeszultseg.addEventListener("change", e=>{
        document.getElementById("val").innerHTML=(felkeszultseg.value*10)+"%";
    });
});

function validateFrom(from){
    let ok=true; // Minden rendben van-e. Ezt adjuk vissza.
    // Ellenőrizzük hogy a macska színe megyezik-e a megerősítéssel. Ha közel van jelezzük hogy közel járunk.

    let szin=document.getElementsByName("macskolor")[0];
    let szinmegint=document.getElementsByName("macskolormegint")[0];

    if(szin.value!==szinmegint.value){
        alert("Sajnos nem egyezik meg a két szín.");
        ok=false;
        // Na de közel vagyunk-e.
        // Az RGB csatornák közötti eltérést fogjuk nézni.
        // R1,G1,B1 mint szin és R2,G2,B2 mint szinmegint csatornái.
        // Azt mondjuk 2 szín közel van ha maximum 8 az eltérés minden csatornán.
        // A szín formátuma: #RRGGBB RR,GG,BB hexben (16-os számrendszerben).

        // teszt
        console.log(szinkodToRGB(szin.value));
        console.log(RGBToSzinkod(szinkodToRGB(szin.value)));

        let egyik=szinkodToRGB(szin.value),
            masik=szinkodToRGB(szinmegint.value);

        let sokakulonbseg=false;
        for (let i = 0; i < 3; i++) {
            // Math.abs az abszolútérték. Egyéb dolog is van a Math-ban ami hasznos. Pl sqrt a négyzetgyök de az most nekünk nem kell.
            if(Math.abs(egyik[i]-masik[i])>8){
                sokakulonbseg=true;
                break;
            }
        }

        // Az előzőt egy sorban is lehet persze:
        let sokakulonbseg_alt=egyik.reduce((prev, curr, index)=>prev||(Math.abs(curr-masik[index])>8), false);
        console.log("Okos vagyok: "+(sokakulonbseg===sokakulonbseg_alt));

        // Ha nem sok a különbség írjuk ki hogy majdnem sikerült.
        if(!sokakulonbseg){
            alert("De majdnem megvan.");
        }
    }
    return ok;
}