
const ModuleFederationPlugin = require('webpack/lib/container/ModuleFederationPlugin');
const path = require('path');

module.exports = {
  output: {
    uniqueName: 'shell',
    publicPath: 'auto',
  },
  plugins: [
    new ModuleFederationPlugin({
      name: 'shell',
      remotes: {
        chat: 'chat@http://localhost:4201/remoteEntry.js',
      },
      shared: {
        '@angular/core': { singleton: true, strictVersion: true },
        '@angular/common': { singleton: true, strictVersion: true },
        '@angular/router': { singleton: true, strictVersion: true },
      },
    }),
  ],
};
