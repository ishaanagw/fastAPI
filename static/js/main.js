function toggleTheme() {
    const body = document.body;
    const button = document.querySelector(".toggle-btn");

    body.classList.toggle("dark");

    if (body.classList.contains("dark")) {
        localStorage.setItem("theme", "dark");
        button.textContent = "☀";
    } else {
        localStorage.setItem("theme", "light");
        button.textContent = "🌙";
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const savedTheme = localStorage.getItem("theme");
    const button = document.querySelector(".toggle-btn");

    if (savedTheme === "dark") {
        document.body.classList.add("dark");
        button.textContent = "☀";
    }
});