process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.setEncoding('utf8');

let inputData = '';

process.stdin.on('data', (chunk) => {
  inputData += chunk;
});

process.stdin.on('end', () => {
  const name = inputData.trim();
  if (name) {
    process.stdout.write(`Your name is: ${name}\n`);
  }
  process.stdout.write('This important software is now closing\n');
});

if (process.stdin.isTTY) {
  process.stdin.on('data', (chunk) => {
    const name = chunk.trim();
    process.stdout.write(`Your name is: ${name}\n`);
  });
}
