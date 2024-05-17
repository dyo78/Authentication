/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
   
    extend: { colors:{'sky-blue':'#a8c7e6',
    'dim-blue':'#6b88bf',
    'light-blue':'#c8d8f0',
    'skin':'#feeaca'}},
  },
  plugins: [],
}

