document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.btn-danger');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const taskName = event.target.closest('.list-group-item').innerText;
            const confirmation = confirm(`Are you sure you want to delete "${taskName}"?`);

            if (!confirmation) {
                event.preventDefault(); // Stop the deletion if the user cancels
            }
        });
    });
});
