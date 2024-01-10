const chai = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
  describe('no rounding', () => {
    it('should return 5', () => {
      chai.expect(calculateNumber('SUM', 1, 4)).to.equal(5);
    });
  });

  describe('first int', () => {
    it('should return 6', () => {
      chai.expect(calculateNumber('SUM', 2.4, 4)).to.equal(6);
    });
  });

  describe('second int', () => {
    it('should return 6', () => {
      chai.expect(calculateNumber('SUM', 4, 2.4)).to.equal(6);
    });
  });

  describe('both ints', () => {
    it('should return 6', () => {
      chai.expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
  });
});
