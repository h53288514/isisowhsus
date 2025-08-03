const { exec } = require("child_process");

async function runPythonScript() {
  try {
    exec("python popatlal.py", (error, stdout, stderr) => {
      if (error) {
        console.log(`error: ${error.message}`);
        return;
      }
      if (stderr) {
        console.log(`stderr: ${stderr}`);
        return;
      }
      console.log(`stdout: ${stdout}`);
    });
  } catch (err) {
    console.error("Unexpected error:", err);
  }
}

runPythonScript();
