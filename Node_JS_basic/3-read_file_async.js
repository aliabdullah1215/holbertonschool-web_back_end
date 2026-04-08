const fs = require('fs');

function countStudents(path) {
    return new Promise((resolve, reject) => {
        // قراءة الملف بشكل غير متزامن
        fs.readFile(path, 'utf8', (err, data) => {
            if (err) {
                reject(new Error('Cannot load the database'));
                return;
            }

            // تقسيم الملف إلى أسطر وتجاهل الأسطر الفارغة
            const lines = data.split('\n').filter(line => line.trim() !== '');
            
            // إزالة رأس العمود (first line)
            const students = lines.slice(1);
            
            if (students.length === 0) {
                console.log('Number of students: 0');
                resolve();
                return;
            }

            console.log(`Number of students: ${students.length}`);

            // تجميع الطلاب حسب المجال
            const fields = {};
            
            for (const student of students) {
                const [firstname, , , field] = student.split(',');
                
                if (!fields[field]) {
                    fields[field] = [];
                }
                fields[field].push(firstname);
            }

            // طباعة كل مجال
            for (const [field, names] of Object.entries(fields)) {
                console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
            }

            resolve();
        });
    });
}

module.exports = countStudents;
