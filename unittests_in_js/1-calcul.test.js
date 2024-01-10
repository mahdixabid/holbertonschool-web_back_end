const assert = require('assert').strict;
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  describe('round not used', () => {
    it('should return 5', () => {
      assert.equal(calculateNumber('SUM', 1, 4), 5);
    });
  });

  describe('round first int', () => {
    it('should return 6', () => {
      assert.equal(calculateNumber('SUM', 2.4, 4), 6);
    });
  });

  describe('round second int', () => {
    it('should return 6', () => {
      assert.equal(calculateNumber('SUM', 4, 2.4), 6);
    });
  });

  describe('both ints', () => {
    it('should return 6', () => {
      assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
    });
  });
});
