// script to create and connect to the Redis server 

import { createClient } from 'redis';

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server: ERROR_MESSAGE', err));
client.on('connect', () => console.log('Redis client connected to the server'));

await client.connect();
