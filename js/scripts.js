document.addEventListener("DOMContentLoaded", function () {
    loadContent('home'); // Load the home content by default
});

function loadContent(page) {
    const contentDiv = document.getElementById('content');

    fetch(`${page}.html`)
        .then(response => response.text())
        .then(data => {
            contentDiv.innerHTML = data;
            loadCSS(page);
        })
        .catch(error => {
            contentDiv.innerHTML = '<p>Error loading content. Please try again later.</p>';
            console.error('Error loading content:', error);
        });
}

function loadCSS(page) {
    const head = document.head;
    const existingLink = document.querySelector(`link[href^="css/${page}.css"]`);
    if (existingLink) {
        return;
    }

    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = `css/${page}.css`;

    head.appendChild(link);
}

function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
}
