#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const json = JSON.parse(body);
  const completedByUserId = json.reduce((acc, el) => {
    if (el.completed) {
      acc[el.userId] = (acc[el.userId] || 0) + 1;
    }
    return acc;
  }, {});
  console.log(completedByUserId);
});
