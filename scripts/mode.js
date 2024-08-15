document.addEventListener('DOMContentLoaded', () => {
    initializeTheme();
    setAutoThemeSwitch();
});

function initializeTheme() {
    // Check localStorage for user preference
    const theme = localStorage.getItem('theme') || 'light-mode';
    document.body.classList.add(theme);
    
    // Update the icon based on the current theme
    updateThemeIcon(theme);
}

function toggleTheme() {
    const currentTheme = document.body.classList.contains('light-mode') ? 'light-mode' : 'dark-mode';
    const newTheme = currentTheme === 'light-mode' ? 'dark-mode' : 'light-mode';
    
    document.body.classList.remove(currentTheme);
    document.body.classList.add(newTheme);
    
    // Save user preference
    localStorage.setItem('theme', newTheme);
    
    // Update the icon
    updateThemeIcon(newTheme);
}

function updateThemeIcon(theme) {
    const themeToggle = document.getElementById('theme-toggle');
    themeToggle.textContent = theme === 'light-mode' ? '🌙' : '🌞'; // Moon icon for dark mode, Sun icon for light mode
}

function setAutoThemeSwitch() {
    const now = new Date();
    const hours = now.getHours();

    // Set theme based on the current time
    if (hours >= 18 || hours < 6) {
        // It's between 6 PM and 6 AM, set dark mode
        if (!document.body.classList.contains('dark-mode')) {
            toggleTheme();
        }
    }
}
