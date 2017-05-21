/**
 * Created by opikovets on 3/10/17.
 */
$(document).ready(function () {

    $(".photo-gallery__photos").justifiedGallery({
        rowHeight : 240,
        margins : 35
    });

    $("a.photo-gallery__photos-item").colorbox({
        rel:'photo-gallery__photos-item',
        slideshow:true
    })

})
