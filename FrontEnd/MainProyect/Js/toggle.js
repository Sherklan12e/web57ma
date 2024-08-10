export async function crearToggle(page) {
    try {
        const response = await fetch(page == 'prueba'
            ?'./layout/darkmode.html':'./layout/darkmode.html'); // Ajusta la ruta según la estructura de tus directorios
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const html = await response.text();
        console.log(html); // Verifica que obtuviste el HTML
        return html; // Retorna el HTML
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
        return null; // Retorna null en caso de error
    }
}