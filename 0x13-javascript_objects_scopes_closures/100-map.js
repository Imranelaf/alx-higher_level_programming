#!/usr/bin/node
const list = require('./100-data').list;

console.log(list);
if (Array.isArray(list) && list.every(elem => typeof elem === 'number')) {
  const newList = list.map((value, index) => value * index);
  console.log(newList);
} else {
  console.log(undefined);
}
