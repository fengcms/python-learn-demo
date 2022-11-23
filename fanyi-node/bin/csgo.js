#!/usr/bin/env node
const clipboard = require('node-clipboardy')

const str = 'sv_cheats 1; sv_infinite_ammo 1;god; noclip;'
console.log(str)
clipboard.writeSync(str)
