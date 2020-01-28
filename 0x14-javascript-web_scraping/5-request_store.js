#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request.get(process.argv[2], function (error, request, data) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], data, 'utf-8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
