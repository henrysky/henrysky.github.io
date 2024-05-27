'use strict';
const fs = require('fs');
const upath = require('upath');
const sh = require('shelljs');

module.exports = function renderScripts() {
    const sourcePath = upath.resolve(upath.dirname(__filename), '../src/js');
    const destPath = upath.resolve(upath.dirname(__filename), '../static/js');
    sh.cp('-R', sourcePath, destPath)

    const sourcePathScriptsJS = upath.resolve(upath.dirname(__filename), '../node_modules/bootstrap/dist/js/bootstrap.min.js');
    const destPathScriptsJS = upath.resolve(upath.dirname(__filename), '../static/js');
    sh.cp(sourcePathScriptsJS, destPathScriptsJS)
};