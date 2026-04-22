const BASE = "http://127.0.0.1:8000/api/v1";
let token = localStorage.getItem("token") || "";

let loading = false;

// Auto login
if (token) {
  showDashboard();
}

function showDashboard() {
  document.getElementById("auth").style.display = "none";
  document.getElementById("dashboard").style.display = "block";
  loadTasks();
}

// ---------------- AUTH ----------------

async function register() {
  try {
    const res = await fetch(`${BASE}/auth/register`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        email: email.value,
        username: username.value,
        password: password.value
      })
    });

    if (!res.ok) throw new Error("Registration failed");

    alert("Registered!");
  } catch (err) {
    alert(err.message);
  }
}

async function login() {
  try {
    const res = await fetch(`${BASE}/auth/login`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        email: email.value,
        password: password.value
      })
    });

    const data = await res.json();

    if (!res.ok) throw new Error(data.detail || "Login failed");

    token = data.access_token;
    localStorage.setItem("token", token);

    showDashboard();
  } catch (err) {
    alert(err.message);
  }
}

// ---------------- TASKS ----------------

async function createTask() {
  if (!token) return alert("Login first");

  try {
    await fetch(`${BASE}/tasks/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
      },
      body: JSON.stringify({
        title: title.value,
        description: desc.value
      })
    });

    title.value = "";
    desc.value = "";

    loadTasks();
  } catch (err) {
    alert("Failed to create task");
  }
}

async function loadTasks() {
  if (!token) return;
  if (loading) return;

  loading = true;

  try {
    const res = await fetch(`${BASE}/tasks/`, {
      headers: {"Authorization": "Bearer " + token}
    });

    if (!res.ok) {
      if (res.status === 401) {
        alert("Session expired. Login again.");
        localStorage.removeItem("token");
        location.reload();
      }
      throw new Error("Failed to fetch tasks");
    }

    const data = await res.json();

    tasks.innerHTML = "";

    data.forEach(t => {
      const li = document.createElement("li");
      li.innerHTML = `
        ${t.title} - ${t.description}
        <button onclick="deleteTask(${t.id})">❌</button>
      `;
      tasks.appendChild(li);
    });

  } catch (err) {
    console.error(err);
  }

  loading = false;
}

async function deleteTask(id) {
  if (!token) return;

  try {
    await fetch(`${BASE}/tasks/${id}`, {
      method: "DELETE",
      headers: {"Authorization": "Bearer " + token}
    });

    loadTasks();
  } catch (err) {
    alert("Delete failed");
  }
}