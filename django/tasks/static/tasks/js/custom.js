$( document ).ready(function() {
    // autosize textareas
    autosize($('textarea'));

    // change placeholders for empty fields
    $( 'div.form-group-formset.empty'  ).find( "textarea[id*='body'], input[id*='title']"  ).attr("placeholder", "Add new");
})


