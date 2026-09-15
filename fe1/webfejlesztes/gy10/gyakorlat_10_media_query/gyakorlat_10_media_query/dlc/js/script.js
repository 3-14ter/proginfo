// Ez az óraiban is benne van de kell korrekció...
const crest = document.getElementsByClassName('crest')[0];

if(crest){
  crest.addEventListener('mousemove', (e) => {
    const rect = crest.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const centerX = rect.width / 2;
    const centerY = rect.height / 2;

    const rotateX = (y - centerY) / 20;
    const rotateY = (centerX - x) / 20;

    crest.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.15)`;
  });

  crest.addEventListener('mouseleave', () => {
    crest.style.transform = 'rotateX(0) rotateY(0) scale(1)';
  });
}
//...idáig.

/*
 Az előző DLCn szerzett sokk és kétségbeesés után a hogy lehet máshogy által...
 kicsit visszább fogom magam és megnézzük a localStoraget kicsit egyszerűbben.
 Na máris gondunk lesz ugyanis  a "file:///..." megnyitásoknál minden HTML fájlhoz külön helyi tároló tartozik
 míg a localhoston ezt egybe lehetett kezelni.
 
 Most csak annyi lesz hogy ha egy házat választottunk már nem változtathatjuk meg és csak az az opció jelenik meg.
 Lehet a dékánt kérvényezni és megváltoztatni a házat. (a fo    script.js fájlban van ez a logika)

 Note: A böngésző vissza gombjának megnyomása után frissíteni kell az oldalt.

 (Ettől még besettenkedhetünk a másik házba is ha elég ügyesek vagyunk.)

 A ház oldalán megjelölhetjük a kedvenceinket amelyek megmaradnak ha elnavigálunk és vissza.
*/

// nem kedvenc: ☆
// hover: ⭐
// kedvenc: 🌟

let localStorageAsArray=[];

// Ha változtatunk valamit ezt hívhatjuk meg.
function saveLocalStorage(){
  localStorage.setItem("kedvencek", JSON.stringify(localStorageAsArray));
}

function getLocalStorage(){
  return JSON.parse(localStorage.getItem("kedvencek"));
}

function kedvencekhez(nev){
  if(!localStorageAsArray.includes(nev)){
    localStorageAsArray.push(nev);
    saveLocalStorage();
  }
}

function kedvencekbol(nev){
  if(localStorageAsArray.includes(nev)){
    localStorageAsArray.splice(localStorageAsArray.indexOf(nev), 1);
    saveLocalStorage();
  }
}

// A HTML-ben van a jelölőnlégyzet és ahhoz van ez a function kötve.
function csakKedvenc(ison){
  let allatok=document.getElementsByClassName('gallery')[0].querySelectorAll(".star:not(.sel)");
  for(let allat of allatok){
    if(allat.parentElement.querySelector("h2").innerHTML==="Mazsola")continue;
    allat.parentElement.style.display=ison?"none":"block";
  }
}

document.addEventListener("DOMContentLoaded", event=>{
    // Kivesszük a csak kedvencek pipát.
    document.getElementById("csakkedv").checked=false;

    // Ha nem létezik a kedvencek listája akkor hozzuk létre.
    // Előző órán láttuk hogy a localStorage stringeket tárol így az előző óraihoz hasonlóan fogjuk manipulálni.
    if(!localStorage.getItem("kedvencek")){
        localStorage.setItem("kedvencek", "[]");
    }

    localStorageAsArray=getLocalStorage();
    
    // Adjuk hozzá a csillagokat a jobb felső sarokhoz. Ehhez a gallery összes elemén végigmegyünk.
    // Közben figyeljünk oda hogy benne van-e már a kedvencek listájában az adott állat. (igen ez cicára és kutyára is működni fog ráadásul az egész bővíthető más házakkal és állatokkal :D)
    // Tegyük fel hogy minden állatnak más neve van így ez alapján tároljuk le őket.
    let allatok=document.getElementsByClassName('gallery')[0].children;
    for(let allat of allatok){
        let nev=allat.querySelector("h2").innerHTML;
        let kedvenc=localStorageAsArray.includes(nev);
        if(kedvenc) {
          allat.innerHTML+="<span class='star sel'>🌟</span>";
        } else {
          allat.innerHTML+="<span class='star'>☆</span>";
        }
        
    }

    let stars=document.getElementsByClassName("star");

    for(let star of stars){
        star.addEventListener("mouseenter", e=>{
            star.innerHTML="⭐";
        });

        star.addEventListener("mouseleave", e=>{
            star.innerHTML=star.classList.contains("sel")?"🌟":"☆";
        });

        star.addEventListener("click", e=>{
            let nev=star.parentElement.querySelector("h2").innerHTML;
            if(star.classList.contains("sel")){
                star.classList.remove("sel");
                star.innerHTML="☆";
                kedvencekbol(nev);
            } else {
                star.classList.add("sel");
                star.innerHTML="🌟";
                kedvencekhez(nev);
            }

            csakKedvenc(document.getElementById("csakkedv").checked);
        });
    }
});