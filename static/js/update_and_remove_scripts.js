// From the lessons from Code Institute.
// Update quantity on click
$('.update-link').click(function(e) {
    let form = $(this).prev('.update-form');
    form.submit();
})

// Remove item and reload on click
$('.remove-item').click(function(e) {
    let csrfToken = "{{ csrf_token }}";
    let itemId = $(this).attr('id').split('remove_')[1];
    let url = `/cart/remove/${itemId}/`;
    let data = {'csrfmiddlewaretoken': csrfToken};

    $.get(url, data)
        .done(function() {
            location.reload();
        });
})
