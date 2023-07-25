#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: node script.js <file path> <string to write>');
  process.exit(1);
}

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFile(filePath, contentToWrite, 'utf8', (err) => {
  if (err) {
    console.error('Error:', err);
  } else {
    console.log('Content written to the file successfully!');
  }
});
