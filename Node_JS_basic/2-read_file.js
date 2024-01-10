const fs = require('fs');

const countStudents = (path) => {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const students = data.split('\n').slice(1);
    const cs = [];
    const swe = [];
    for (const student of students) {
      if (student.split(',')[3] === 'CS') {
        cs.push(student.split(',')[0]);
      } else {
        swe.push(student.split(',')[0]);
      }
    }
    console.log(`Number of students: ${students.length}`);
    console.log(`Number of students in CS: ${cs.length}. List: ${cs.join(', ')}`);
    console.log(`Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`);
  } catch (err) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
