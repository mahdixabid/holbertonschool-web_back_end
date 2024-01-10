import { createClient } from 'redis';
host = '127.0.0.1:6379';
const client = createClient(host);
client.on('error', (err) => console.log('Redis Client Error', err));
client.connect();
client.on('connect', () => {
    console.log('Redis client connected to the server');
});
client.on('error', (err) => {
    console.log('Redis client not connected to the server: ' + err);
});
