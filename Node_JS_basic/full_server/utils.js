import fs from 'fs';

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      reject(err);
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

    resolve(fields);
  });
});

export default readDatabase;
