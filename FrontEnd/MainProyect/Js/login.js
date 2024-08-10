/* document.addEventListener('DOMContentLoaded',()=>{ */
  export function cargarClick(){
    const sol = document.getElementById('sun');
    const luna = document.getElementById('mooon');
    /* console.log(sol); */
    let mov_realizado = true;
    
    function movimiento() {
      sol.style.transform = 'translate(60px) rotate(180deg)';
      sol.style.opacity = '0';
      luna.style.opacity = '1';
      luna.style.transform = 'translate(60px) rotate(320deg)';
      mov_realizado = false;
    }
    
    function movimiento_inverso() {
      sol.style.transform = 'translate(0) rotate(-180deg)';
      sol.style.opacity = '1';
      luna.style.opacity = '0';
      luna.style.transform = 'translate(0) rotate(-200deg)';
      mov_realizado = true;
    }
  
    if (sol) {
      sol.addEventListener('click', function() {
        console.log("click object");
        if (mov_realizado) {
          movimiento();
          document.documentElement.classList.toggle('dark');
        } else {
          movimiento_inverso();
          document.documentElement.classList.remove('dark');
        }
      });
    }
    
  }
/* }) */
