var readline = require('readline');
var fs = require('fs');
var os = require('os');

var fReadName = './before.txt';
var fWriteName = './after.txt';

var fRead = fs.createReadStream(fReadName);
var fWrite = fs.createWriteStream(fWriteName);

var objReadline = readline.createInterface({
  input: fRead,
});

var index = 1;
objReadline.on('line', (line) => {
  var pattern = /[0-9]/;
  if (!line.match(pattern)) {
    line = line.replace(pattern, index);
    index++;
  }

  fWrite.write(line + os.EOL);
});

objReadline.on('close', () => {
  console.log('completed！');
});
