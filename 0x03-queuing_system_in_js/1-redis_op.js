// redis-node script 

import { createClient, print } from 'redis';

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server: ERROR_MESSAGE', err));
client.on('connect', () => console.log('Redis client connected to the server'));

await client.connect();

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        if (err) {
            console.error(err);
        } else {
            console.log(reply);
        }
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
