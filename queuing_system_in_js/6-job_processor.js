const kue = require("kue");
const q = kue.createQueue();

async function sendNotification(phoneNumber, message){
     console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

q.process('push_notification_code', (job, done)=>{
    sendNotification(job.phoneNumber, job.message);
    done();
}
);
