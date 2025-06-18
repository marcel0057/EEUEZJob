/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './core/templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        orange: {
          500: '#F97316',
          600: '#EA580C',
          50: '#FFF7ED',
          100: '#FFEDD5',
        },
        white: '#FFFFFF',
      },
    },
  },
  plugins: [],
}