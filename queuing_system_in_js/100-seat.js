const kue = require("kue");
const redis = require('redis');
const { promisify } = require("util");

const express = require('express');

client = redis.createClient(6379, '127.0.0.1');
const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

setAsync('available_seats', 50);

let reservationEnabled = true;

function reverseSeat(number) {
    return setAsync('available_seats', number);
}

function getCurrentAvailableSeats() {
    let r = getAsync('available_seats');
    return r;
} 

queue = kue.createQueue();

const app = express();

app.get('available_seats', (req, res)=> {
    let v = Asyncget('available_seats');
    return res.json(`{"numberOfAvailableSeats":"${v}"}`);
});

app.get('/reserve_seat', (req, res)=>{
    if(!reservationEnabled) {res.json({ "status": "Reservation are blocked" });}
    let job = queue.create('reserve_seat', )
        .save(err =>{ if(!err) res.json({ "status": "Reservation in process" });});
    
        job.on('complete', result=>{ console.log(`Seat reservation job ${job.id} completed`)});
        job.on('failed', errorMessage=>
        {console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
                                    });

app.get('/process', async (req, res)=>{
    await queue.process('reserve_seat', (job, done)=>{
        res.json({ "status": "Queue processing" })
        let count =  getCurrentAvailableSeats();
        if(count === 0) reservationEnabled = false; 
        if(count >= 0 ) return done();
        return done(new Error('Not enough seats available'));

    });
});

});


