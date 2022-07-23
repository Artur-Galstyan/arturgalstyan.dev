module.exports = {
  mode: 'jit',
  content: [
    "./index/templates/**/*.{html,js}",
    "./blog/templates/**/*.{html,js}",
    "./demos/templates/**/*.{html,js}",
    './templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}