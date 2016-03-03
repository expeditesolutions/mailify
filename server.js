/* eslint no-console: 0 */

const path = require('path');
const express = require('express');
const webpack = require('webpack');
const webpackMiddleware = require('webpack-dev-middleware');
const webpackHotMiddleware = require('webpack-hot-middleware');
const wpConfig = require('./webpack.config.js');

const config = require('./config').config();
const app = express();

if (config.isDeveloping) {
  const compiler = webpack(wpConfig);
  const middleware = webpackMiddleware(compiler, {
    publicPath: wpConfig.output.publicPath,
    contentBase: 'src',
    stats: {
      colors: true,
      hash: false,
      timings: true,
      chunks: false,
      chunkModules: false,
      modules: false
    }
  });

  app.use(middleware);
  app.use(webpackHotMiddleware(compiler));
  app.get('*', function response(req, res) {
    res.write(middleware.fileSystem.readFileSync(path.join(__dirname, 'dist/index.html')));
    res.end();
  });
} else {
  app.use(express.static(__dirname + '/dist'));
  app.get('*', function response(req, res) {
    res.sendFile(path.join(__dirname, 'dist/index.html'));
  });
}

app.listen(config.port, config.ip, function onStart(err) {
  if (err) { console.log(err); }
  console.log('IP : ' + config.ip + ' PORT ' + config.port);
});
