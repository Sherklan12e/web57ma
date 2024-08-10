import {cargarClick} from './login.js';
import {crearToggle} from './toggle.js';

async function iniciar(){
    let contenedorToggle=document.getElementById('contenedorToggle');

    const html = await crearToggle();
    
        if (html) {
            console.log(html); 
            contenedorToggle.innerHTML=html;// Inserta el HTML en el elemento
        }
    
    cargarClick();
    
}
iniciar();

/* contenedorToggle.innerHTML=crearToggle(); */

