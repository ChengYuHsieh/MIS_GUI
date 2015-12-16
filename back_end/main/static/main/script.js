
$('#buttonId').click(function() {
    $.ajax({
        url: 'database',
        method: 'GET',
        success: function (data) {        
            alert(data);
        }
    });
});