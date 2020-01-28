#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (err, res) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(`code: ${res.statusCode}`);
});
