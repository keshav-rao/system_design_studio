/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        background: '#0B0F17',
        surface: '#151D2A',
        surfaceLight: '#1E293B',
        accent: '#3B82F6',
        accentHover: '#2563EB',
      }
    },
  },
  plugins: [],
}
