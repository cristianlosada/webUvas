var btnAbrirpopup = document.getElementById('btnAbrirpopup'),
    overlay = document.getElementById('overlay'),
    popup = document.getElementById('popup'),
    cerrarpopup = document.getElementById('cerrar-popup');

btnAbrirpopup.addEventListener('click', function(){

    overlay.classList.add('action');
    popup.classList.add('action');

});



cerrarpopup.addEventListener('click', function(){

    overlay.classList.remove('action');
    popup.classList.remove('action');

});
