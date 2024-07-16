// Example JavaScript for closing tasks
document.addEventListener('DOMContentLoaded', function() {
    const closeButtons = document.querySelectorAll('.close-btn');

    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const taskTile = this.closest('.task-tile');
            taskTile.style.display = 'none'; // Or remove() to completely remove from DOM
        });
    });
});
