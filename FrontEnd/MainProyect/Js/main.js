import {cargarClick} from './login.js';
import { crearToggle } from './toggle.js';

document.addEventListener('DOMContentLoaded', () => {
    const HEADER = document.getElementById('header');
    const PRODUCTOS = document.querySelectorAll('.producto');
    const ASIDE = document.getElementById('aside')
    
/*  function crearNav(){ */
    fetch('./layout/Navbar.html')  // Ajusta la ruta según la estructura de tus directorios
    .then(response => response.text())
    .then(async html => {
        /* console.log(html); */
        HEADER.innerHTML = html;
        document.getElementById('toggle').innerHTML = await crearToggle('prueba');
        cargarClick();  // Llama a cargarClick después de que se haya asignado el HTML
    })
/* } */
    fetch('./layout/producto.html')
    .then(response => response.text())
    .then(html => {
        PRODUCTOS.forEach(element => {
            element.innerHTML = html;
        }); 
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
    
    fetch('./layout/Aside.html')
    .then(response => response.text())
    .then(html => {
        ASIDE.innerHTML = html;
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
    
});
