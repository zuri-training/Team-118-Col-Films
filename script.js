"use strict";

// ********** set date ************
// // select span
const date = (document.querySelectorAll("#date"));

date.forEach(date => date.innerHTML =
  new Date().getFullYear())

