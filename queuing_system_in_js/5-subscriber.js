const redis = require("redis");
host = '127.0.0.1:6379';
const client = redis.createClient(host);
client.on('error', (err) => console.log('Redis Client Error', err));
client.connect();
client.on('connect', () => {
    console.log('Redis client connected to the server');
});
client.on('error', (err) => {
    console.log('Redis client not connected to the server: ' + err);
});

client.subscribe('holberton school channel');

client.on('message', (channel, message)=> {
    if (channel === 'holberton school channel') console.log(message); 
    if (message === 'KILL_SERVER')
    {
        client.unsubscribe(channel);
        client.quit();
    }
});


