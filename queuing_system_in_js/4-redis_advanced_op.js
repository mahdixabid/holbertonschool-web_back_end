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

client.hSet('HolbertonSchools', 'Portland', 50, redis.print);
client.hSet('HolbertonSchools', 'Seattle', 80, redis.print);
client.hSet('HolbertonSchools', 'New York', 20, redis.print);
client.hSet('HolbertonSchools', 'Bogota', 20, redis.print);
client.hSet('HolbertonSchools', 'Cali', 40, redis.print);
client.hSet('HolbertonSchools', 'Paris', 2, redis.print);

client.hGetAll('HolbertonSchools', (error, value) => {
    if(error) console.log(value); // nil if not found
});




