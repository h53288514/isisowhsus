const { execFile } = require('child_process');

execFile('./popatlal.sh', (error, stdout, stderr) => {
  if (error) {
    console.error('Error executing script:', error);
    return;
  }
  console.log('stdout:', stdout);
  console.error('stderr:', stderr);
});
