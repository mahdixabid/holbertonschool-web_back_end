const redis = require("redis");
host = '127.0.0.1:6379';
const client = redis.createClient(host);
client.on('error', (err) => console.log('Redis Client Error', err));
client.connect();
client.on('ready', () => {
    console.log('Redis client connected to the server');
});
client.on('error', (err) => {
    console.log('Redis client not connected to the server: ' + err);
});

async function publishMessage(message, time){
    await new Promise(() => setTimeout( ()=> {
    console.log('About to send ' + message);
    client.publish('holberton school channel', message); //client.xAdd()
    }, time));

};

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);

