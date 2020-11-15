document.addEventListener('DOMContentLoaded', function() {
    var link = document.getElementById('trigger');
    // onClick's logic below:
    link.addEventListener('click', function() {
    var images = document.getElementsByTagName('img');
    for (var i = 0, l = images.length; i < l; i++) {
        images[i].src = 'http://placekitten.com/' + images[i].width + '/' + images[i].height;      
    }
    });
});