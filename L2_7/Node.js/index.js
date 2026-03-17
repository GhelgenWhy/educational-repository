const axios = require("axios");
async function fetchUserData() {
  try {
    console.log("sending request...");
    const response = await axios.get(
      "https://jsonplaceholder.typicode.com/users/7",
    );
    console.log("\ndata received");
    console.log(`name: ${response.data.name}`);
    console.log(`email: ${response.data.email}`);
    console.log(`city: ${response.data.address.city}`);
    console.log("--------------------------------\n");
  } catch (error) {
    console.error("error:");
    if (error.response) {
      console.error(`status: ${error.response.status}`);
    } else if (error.request) {
      console.error("Server died");
    } else {
      console.error(error.message);
    }
  }
}
fetchUserData();
