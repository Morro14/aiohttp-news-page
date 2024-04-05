const chat = document.getElementById("chat");
const socket = new WebSocket("http://localhost:8080/ws");
const header = document.getElementById("header-text");

header.innerHTML = "Live News Update (no connection)";

socket.onopen = function (e) {
  console.log("Connected");
  const header = document.getElementById("header-text");
  header.innerHTML = "Live News Update (connected)";
  text = document.createElement("p");
  const msg = document.createElement("div");
  text.innerHTML = "Connected. Waiting for news";
  msg.appendChild(text);
  chat.appendChild(msg);
  socket.send("user connected");
};

socket.onmessage = function (event) {
  const msg = document.createElement("div");

  const data = JSON.parse(event.data);
  if (data.news) {
    data.news.forEach((n) => {
      title = document.createElement("h4");
      title.innerHTML = n.title;
      text = document.createElement("p");
      text.innerHTML = n.text;
      msg.appendChild(title);
      msg.appendChild(text);
    });
  }
  chat.appendChild(msg);
};

socket.onclose = function (event) {
  const msg = document.createElement("div");
  text.innerHTML = "disconnected";
  header.innerHTML = "Live News Update (no connection)";
  msg.appendChild(text);
  chat.appendChild(msg);
  console.log(`Disconnected. Code: ${event.code}`);
};

socket.onerror = function (error) {
  console.log("Error");
  const header = document.getElementById("header-text");
  header.innerHTML = "Live News Update (no connection)";
};
