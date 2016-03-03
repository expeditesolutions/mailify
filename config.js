
const path =  require('path');
const rootPath = path.normalize(__dirname + '/..');
const env = process.env.NODE_ENV || 'development';

const config = {
  development : {
    ip : '127.0.0.1',
    port : 5000,
    root : rootPath
  },
  production : {
    ip : process.env.OPENSHIFT_NODEJS_IP,
    port : process.env.OPENSHIFT_NODEJS_PORT,
    root : rootPath
  }
};

module.exports.config = function () {
  return config[env];
};

module.exports.isDeveloping = process.env.NODE_ENV !== 'production';