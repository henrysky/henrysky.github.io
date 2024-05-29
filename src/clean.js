const sh = require('shelljs');
const upath = require('upath');

const destPath1 = upath.resolve(upath.dirname(__filename), '../static');
const destPath2 = upath.resolve(upath.dirname(__filename), '../public');

sh.rm('-rf', `${destPath1}`)
sh.rm('-rf', `${destPath2}`)
