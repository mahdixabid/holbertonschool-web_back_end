export default function getFullResponseFromAPI(success) {
    return new Promise((resolve, reject) => {
    if (success){
        return resolve({ status: 200, body: 'Success' });
    }
    else {
        return reject(new Error('The fake API is not working currently'));
    }
});
}
