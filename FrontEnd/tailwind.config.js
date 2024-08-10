/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'selector',
  content: ["./MainProyect/**/*.{html, js}"],
  theme: {
    extend: {
      colors: {
        green: "#6C987E",
        white: "#FFFF",
        negro: "#100D14",
        fondoClaro: "#333548",
        darkGrow: "#424457",
        gris: "#D4D4D4",
        negrito: "#1A1520",
        verde: "#668D76",
        grisLetra: "#707070",
        verdeLetra: "#508466",
        verdeClaro: "#96B19A"
      }
    },
  },
  plugins: [],
}

