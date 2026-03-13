const { defineConfig } = require("cypress");

module.exports = defineConfig({
  reporter: "mochawesome",
  reporterOptions: {
    reportDir: "reporte",
    overwrite: false,
    html: true,
    json: true
  },

  e2e: {
    baseUrl: "https://petstore.swagger.io/v2"
  }
});