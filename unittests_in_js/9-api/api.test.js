const request = require('request');
const chai = require('chai');

describe('basic integration testing', () => {
  describe('gET /', () => {
    it('endpoint: GET /', () => new Promise((done) => {
      const call = {
        url: 'http://localhost:7865',
        method: 'GET',
      };
      request(call, (error, response, body) => {
        chai.expect(response.statusCode).to.equal(200);
        chai.expect(body).to.equal('Welcome to the payment system');
        done();
      });
    }));
  });
});

describe('regex integration testing', () => {
  describe('gET /cart/:id', () => {
    it('endpoint: GET /cart/:id', () => new Promise((done) => {
      const call = {
        url: 'http://localhost:7865/cart/12',
        method: 'GET',
      };
      request(call, (error, response, body) => {
        chai.expect(response.statusCode).to.equal(200);
        chai.expect(body).to.equal('Payment methods for cart 12');
        done();
      });
    }));
  });
  describe('gET /cart/:isNaN', () => {
    it('gET /cart/:isNaN 404', () => new Promise((done) => {
      const call = {
        url: 'http://localhost:7865/cart/anything',
        method: 'GET',
      };
      request(call, (error, response, body) => {
        chai.expect(response.statusCode).to.equal(404);
        done();
      });
    }));
  });
});
