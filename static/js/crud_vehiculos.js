// TOOLTIP PARA LOS CHECKBOXES
$(document).ready(function(){
	// Activate tooltip
	$('[data-toggle="tooltip"]').tooltip();
	
	// Select/Deselect checkboxes
	var checkbox = $('table tbody input[type="checkbox"]');
	$("#selectAll").click(function(){
		if(this.checked){
			checkbox.each(function(){
				this.checked = true;                        
			});
		} else{
			checkbox.each(function(){
				this.checked = false;                        
			});
		} 
	});
	checkbox.click(function(){
		if(!this.checked){
			$("#selectAll").prop("checked", false);
		}
	});
});

// Modal AGREGAR VEHICULO
$(document).ready(function() {
    // Trigger the modal
    $('#addVehiculoModal').on('show.bs.modal', function (event) {
        // Clear form fields
        $('#addVehiculoForm')[0].reset();
    });

    // Handle form submission
    $('#addVehiculoForm').submit(function(event) {
        event.preventDefault();
        // Send form data to Django backend using AJAX
        $.ajax({
            type: 'POST',
            url: '/add_vehiculo/', // Replace with your actual URL
            data: $(this).serialize(),
            success: function(response) {
                // Handle successful response, e.g., update the table
                console.log(response);
                // Close the modal and reload the page or update the table
                $('#addVehiculoModal').modal('hide');
                location.reload();
            },
            error: function(error) {
                // Handle errors
                console.error(error);
                // Display error message to the user
            }
        });
    });
});

// PAGINADOR
$(document).ready(function() {
    // Assuming you have a function to fetch data from the server
    function fetchData(page) {
        $.ajax({
            url: '/your_url_to_fetch_data/',
            data: { page: page },
            success: function(data) {
                // Update the table with the fetched data
                $('#table-body').html(data);
                // Update pagination links based on the total number of pages
                updatePagination(data.total_pages);
            }
        });
    }

    function updatePagination(totalPages) {
        // ... (Logic to update pagination links based on totalPages)
    }

    // Handle pagination clicks
    $('.pagination li a').click(function(e) {
        e.preventDefault();
        var page = $(this).text();
        fetchData(page);
    });
});