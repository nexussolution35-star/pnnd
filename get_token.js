// Register/login a surge account directly via POST /token (basic auth),
// using the proxy-compatible axios (>=1.16.1). Prints the token.
const axios = require("/opt/node22/lib/node_modules/surge/node_modules/axios");

const email = process.argv[2];
const pass = process.argv[3];

axios({
  url: "https://surge.surge.sh/token",
  method: "POST",
  auth: { username: email, password: pass },
})
  .then(function (r) {
    console.log("TOKEN " + r.data.token);
  })
  .catch(function (e) {
    if (e.response) {
      console.error("HTTP " + e.response.status + " " + JSON.stringify(e.response.data));
    } else {
      console.error("ERR " + e.message);
    }
    process.exit(1);
  });
