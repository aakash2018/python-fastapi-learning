
const ModuleFederationPlugin = require('webpack/lib/container/ModuleFederationPlugin');
const path = require('path');

module.exports = {
  output: {
    uniqueName: 'chat',
    publicPath: 'auto',
  },
  plugins: [
    new ModuleFederationPlugin({
      name: 'chat',
      filename: 'remoteEntry.js',
      exposes: {
        './ChatApp': './src/app/app.component.ts',
      },
      shared: {
        '@angular/core': { singleton: true, strictVersion: true },
        '@angular/common': { singleton: true, strictVersion: true },
        '@angular/router': { singleton: true, strictVersion: true },
      },
    }),
  ],
};
