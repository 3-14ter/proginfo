function selectHouse(elem){
    // elem.id az elemnek az id attribútuma
    localStorage.setItem("house", elem.id);
}

document.addEventListener("DOMContentLoaded", event=>{
    // Létezik-e már a localStorage-ben a house.
    // A tárolót manuálisan is elérhetjük: F12 a böngészőben úgy hogy az index.html van megnyitva.
    // "Tároló" fül majd pedig a "Helyi tároló"-t ha lenyitjuk és kliválasztjuk ami ott van láthatjuk mi van a tárolóban.
    if(localStorage.getItem("house")) {
        // Ha már létezik akkor tűnjön el a másik lehetőség.
        // Előbb viszont írjuk meg a selectHouse függvényt... vagyis én már megírtam így csak nézzünk rá!
        for(let img of document.getElementsByClassName("img-container")[0].children){
            if(img.id!==localStorage.getItem("house")){
                img.remove();
            }
        }
    } else {
        // Ha nem létezik akkor még fenn áll a lehetőség a választásra.
        // Itt lehetne egy tesztet csinálni hogy ki hova tartozik.
        // if(teszteredmeny=="cica"){ selectHouse(document.getElementById("silentpaw")) } else {...}
        // A gyorsaság kedvéért (és az időhiány miatt) most inkább ki lehet választani.
    }
});
