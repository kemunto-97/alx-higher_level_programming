#!/usr/bin/node

const fs = require('fs');
fs.writeFile(process.argv[2], 'Python is Cool!', 'utf8', function (err, data) {
    if (err) throw err;
  console.log('Saved!');
});
