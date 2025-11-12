const { complex } = require('../src/main');

test('complex function is defined', () => {
  expect(typeof complex).toBe('function');
});

test('all true → returns true', () => {
  expect(complex(1,1,1,1,1,1,1,1,1,1)).toBe(true);
});

test('first false → early return false', () => {
  expect(complex(0,1,1,1,1,1,1,1,1,1)).toBe(false);
});

test('last false → returns false', () => {
  expect(complex(1,1,1,1,1,1,1,1,1,0)).toBe(false);
});