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


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    let v = client.get(schoolName);
    console.log = v;
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');


