#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];

  for (const el of list) {
    revList.unshift(el);
  }
  return revList;
};
