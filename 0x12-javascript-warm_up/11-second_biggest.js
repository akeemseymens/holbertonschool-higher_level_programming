#!/usr/bin/node

let arr = [];
if (process.argv.length <= 3) {
  console.log(0);
} else {
  arr = (process.argv.slice(2));
  const secLrg = arr.sort(function (a, b) { return a - b; })[arr.length - 2];
  console.log(secLrg);
}
