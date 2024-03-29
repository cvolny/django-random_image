(function() {
    var PREVIOUS_COOKIE_NAME = $('body').data("previous-name");
    // style active links and their parents
    var active = $('nav a[href="/' + location.pathname.split("/")[1] + '"]');
    active.addClass('active');
    active.parent().addClass('active');

    // get the permalink, override F5 to go to index
    var currents = $("#current");
    if (currents.length) {
        var permalink = currents.first().attr("href");
        document.cookie = PREVIOUS_COOKIE_NAME + "=" + permalink.substring(1);

        $(document).bind('keydown', function (e) {
            if ((e.which === 116) || (e.which === 82 && e.ctrlKey)) {
                var index = permalink.substring(0, permalink.lastIndexOf("/"));
                console.log("override F5, go to '" + index + "'.");
                window.location = index;
                return false;
            }
        });
    }

    // highlight info
    $('.highlight.info').effect('highlight', {color: '#ddf'}, 1000);

    // enable default colorbox support
    $('.colorbox').colorbox();
})();