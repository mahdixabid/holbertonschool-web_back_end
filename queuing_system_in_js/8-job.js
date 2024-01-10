const kue = require("kue");

push_notification_code_3 = kue.createQueue();

async function createPushNotificationsJobs(jobs, queue){
    if ( !Array.isArray(jobs) ) throw new Error('Jobs is not an array');
    jobs.forEach( (msg)=>{
        const job = queue.create('push_notification_code_3', msg).save(err => 
            { if( !err ) console.log( `Notification job created: ${job.id}` ) } );
    });
    
    job.on('complete', (result)=> {console.log(`Notification job ${job.id} completed`)})

    job.on('failed', (errorMessage)=> {console.log(`Notification job ${job.id} failed: ${errorMessage}`)});

    job.on('progress', (progress, data) => {console.log(`Notification job ${job.id} ${progress}% complete`)});
};

export default createPushNotificationsJobs;