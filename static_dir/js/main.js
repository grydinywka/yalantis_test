function autoHeight() {
    $('#content').css('min-height', 0);
    var h = $(document).outerHeight() - $('#header').outerHeight() - $('#footer').outerHeight();
    $('#content').css('min-height', h);
}

$(window).resize(function() {
    autoHeight();
});

$(document).ready(function() {
    autoHeight();
});

