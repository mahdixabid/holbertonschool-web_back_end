const request = require('request');
const chai = require('chai');

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
  it('endpoint: GET /cart/:isNaN', () => new Promise((done) => {
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

describe('gET /available_payments', () => {
  it('endpoint: GET /available_payments', () => new Promise((done) => {
    const call = {
      url: 'http://localhost:7865/available_payments',
      method: 'GET',
    };
    request(call, (error, response, body) => {
      chai.expect(response.statusCode).to.equal(200);
      chai.expect(body).to.equal(
        '{"payment_methods":{"credit_cards":true,"paypal":false}}',
      );
      done();
    });
  }));
});

describe('pOST /login', () => {
  it('pOST /login', () => new Promise((done) => {
    const call = {
      url: 'http://localhost:7865/login',
      method: 'POST',
      json: {
        userName: 'Marty',
      },
    };
    request(call, (error, response, body) => {
      chai.expect(response.statusCode).to.equal(200);
      chai.expect(body).to.equal('Welcome Marty');
      done();
    });
  }));
});
