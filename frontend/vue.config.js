// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })

const path = require("path");
const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
    transpileDependencies: [
        'vuetify'
    ],
    assetsDir: "static",
    outputDir: path.resolve(__dirname, "../dist"),
})
