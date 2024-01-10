const redis = require('redis');
const express = require('express');
const { promisify } = require("util");
const { ClientClosedError } = require('redis');


const listProducts = [{Id: 1, name: 'Suitcase 250', price: 50, stock: 4},
    {Id: 2, name: 'Suitcase 450', price: 100, stock: 10},
    {Id: 3, name: 'Suitcase 650', price: 350, stock: 2},
    {Id: 4, name: 'Suitcase 1050', price: 550, stock: 5}];


function getItemById(id) {
    listProducts.find(element => element.Id === id)};

app.get('/list_products', (req, res) => {
    res.json(listProducts);
    return;
});

const app = express();

host = '127.0.0.1:6379';

const client = redis.createClient(host);
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function reserveStockById(itemId, stock) {
    return setAsync(`item.${itemId}`, stock);
}


async function getCurrentReservedStockById(itemId) {
    return getAsync(`item.${itemId}`);
}


app.get('/list_products/:itemId', (req, res)=>{
    let itemID = Number(req.params.itemId);
    const item = getItemById(itemID);

    if(!item) res.json({"status":"Product not found"});

    const stock = await getCurrentReservedStockById(itemID);
    item.currentQuantity = stock;
    res.json(stock);
});

app.get('/reserve_product/:itemId', (req, res){
    let itemID = Number(req.params.itemId) ;
    const item = getItemById(itemID);

    if (item === null)  res.json({"status":"Product not found"}); 

    let stock = getAsync(`item.${itemID}`);
    
    if(stock < 1) res.json(`{"status":"Not enough stock available","itemId":${itemID}}`);
    else {
        reserveStockById(itemID, stock -1);
        res.json(`{"status":"Reservation confirmed","itemId":${itemID}}`);
    };

});

app.listen(1245, ()=>{
    listProducts.forEach(element => reserveStockById(element.Id, element.stock));
});
