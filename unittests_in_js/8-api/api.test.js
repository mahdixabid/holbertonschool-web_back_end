const request = require('request');
const chai = require('chai');

describe('basic integration testing', () => {
  describe('gET /', () => {
    it('endpoint GET /', () => new Promise((done) => {
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
