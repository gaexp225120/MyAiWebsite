$('.myLinkToTop').click(function () {
    $(' body').animate({scrollTop:$(document).height()}, 'slow');
    return false;
});

$('.myMenuLink').click(function () {
    $(' body').animate({scrollTop:0}, 'slow');
    return false;
});