var path = require('path');
var webpack = require('webpack');

module.exports = {
  entry: './main.js',
  output: {
    path: __dirname + '/mwtracker/static',
      filename: 'bundle.js',
      libraryTarget: 'var',
      library: 'main'
  },
  module: {
    rules: [
      {
        test: /.jsx?$/,
        exclude: /node_modules/,
        use: 'babel-loader'
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      }
    ]
  },
};

