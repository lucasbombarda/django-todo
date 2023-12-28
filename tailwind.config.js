/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}", "./setup/static/**/*.{js}"],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
}

