const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, datatext) => {
      if (err) {
        reject(Error('Cannot load the database'));
      } else {
        const lines = datatext.split(/\r?\n/);
        const data = [];
        for (const i of lines) {
          if (i !== '') {
            data.push(i.split(','));
          }
        }
        const first_name = data[0].indexOf('firstname');
        const field = data[0].indexOf('field');
        const dict = {};
        for (const line of data) {
          if (data.indexOf(line) !== 0) {
            if (line[field] in dict) {
              dict[line[field]].push(line[first_name]);
            } else {
              dict[line[field]] = [];
              dict[line[field]].push(line[first_name]);
            }
          }
        }
        console.log(`Number of students: ${data.length - 1}`);
        for (const [key, value] of Object.entries(dict)) {
          console.log(
            `Number of students in ${key}: ${value.length}. List: ${value.join(', ')}`
          );
        }
        resolve(dict);
      }
    });
  });
}
module.exports = countStudents;
