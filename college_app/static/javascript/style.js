document.addEventListener("DOMContentLoaded", () => {
    // Add hover effect to buttons
    const buttons = document.querySelectorAll('.button');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', () => {
            button.style.transform = 'scale(1.05)';
            button.style.transition = 'all 0.2s ease';
            button.style.backgroundColor = '#476086ff';  // hover color
        });

        button.addEventListener('mouseleave', () => {
            button.style.transform = 'scale(1)';
            button.style.backgroundColor = '';  // revert to original (defined in CSS)
        });
    });

    
});
