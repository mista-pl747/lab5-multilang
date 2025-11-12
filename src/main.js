
//console.log("Hello"); // eslint: no-console

function complex(a, b, c, d, e, f, g, h, i, j, k) {
  if (a) if (b) if (c) if (d) if (e)
    if (f) if (g) if (h) if (i) if (j)
      if (k) return true;
  return false;
}

/*// Функція з високою складністю — розбита на частини
function areAllTrue(flags) {
  'use strict';
  return flags.every(flag => Boolean(flag));
}*/

// Приклад використання
//const flags = [true, true, true, true, true, true, true, true, true, true];
//const result = areAllTrue(flags);

//var unused = 42; // no-unused-vars

module.exports = { complex };