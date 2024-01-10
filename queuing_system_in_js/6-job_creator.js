const kue = require("kue");
const push_notification_code = kue.createQueue();
job_data = {
    phoneNumber: string,
    message: string,
  };
let job = push_notification_code.create('message', job_data).save(function(err){
    if( !err ) console.log('Notification job created: \n' + job.id);
 });
job.on('complete', (result)=> {
    console.log('Notification job completed');
}).on('failed', (errorMessage)=>{ console.log('Notification job failed')});
  