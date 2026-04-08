const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split(/\r?\n/).filter((line) => line.trim() !== '');
      const students = lines.slice(1);
      const fields = {};

      for (const line of students) {
        const parts = line.split(',');
        const firstname = parts[0];
        const field = parts[3];

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstname);
      }

      console.log(`Number of students: ${students.length}`);

      Object.keys(fields).forEach((field) => {
        const list = fields[field].join(', ');
        console.log(
          `Number of students in ${field}: ${fields[field].length}. List: ${list}`
        );
      });

      resolve();
    });
  });
}

module.exports = countStudents;
