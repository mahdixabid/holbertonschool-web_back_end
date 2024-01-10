import {createPushNotificationsJobs } from './8-job';
queue = require('kue').createQueue();

import expect from 'chai';

test_jobs = [{phoneNumber: '+54', message: 'argentina'}, 
                {phoneNumber: '+44', message: 'England'}, {phoneNumber: '+385', message: 'Croatia'}, 
                {phoneNumber: '+31', message: 'Netherlands'}
            ];
before(function() {
    queue.testMode.enter();
  });

afterEach(function() {
    queue.testMode.clear();
  });

after(function() {
    queue.testMode.exit()
  });

describe('createPushNotificationsJobs', ()=>{
    it('sends messages ', ()=>{
        createPushNotificationsJobs(test_jobs, queue);
        expect(queue.testMode.jobs.length).to.equal(4);
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.eql({phoneNumber: '+54', message: 'argentina'});
        createPushNotificationsJobs(test_jobs, queue);
        expect(queue.testMode.length).to.equal(8);
    });
} );

it('Invalid Data', ()=> {
    expect( ()=> {createPushNotificationsJobs('', queue).to.throw(Error);});
    expect( ()=> {createPushNotificationsJobs('{}', queue).to.throw(Error);});
    expect( ()=> {createPushNotificationsJobs([{phoneNumber: '+32'}], queue).to.throw(Error);});
    expect( ()=> {createPushNotificationsJobs('NaN', queue).to.throw(Error);});
})

