// Basic JavaScript for expense tracker
document.addEventListener('DOMContentLoaded', function() {
    console.log('Expense tracker loaded');
    
    // Add any interactive functionality here
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this expense?')) {
                e.preventDefault();
            }
        });
    });
});
