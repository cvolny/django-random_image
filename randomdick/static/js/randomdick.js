function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

(function() {
    console.log(location.pathname);
    $('nav a[href="/' + location.pathname.split("/")[1] + '"]:not(.prev a)').parent().addClass('active');
    var prev = getParameterByName("prev");
    if (prev) {
        $('.prev a').attr('href', function (i, str) {
            return str + prev;
        });
        $('.prev').effect("highlight", {"color": "#d9edf7"}, 1500);
    } else {
        $('.prev').hide();
    }
    var currentUrl = $('#current');
    if (currentUrl.length) {
        var current = currentUrl.attr("href").substr(1);
        $('.needs-prev a').attr('href', function (i, str) {
            return str + '?prev=' + current;
        });

        $(document).bind('keydown keyup', function (e) {
            if ((e.which === 116) || (e.which === 82 && e.ctrlKey)) {
                var url = '/?prev=' + current;
                console.log("override F5, go to '" + url + "'.");
                window.location = url;
                return false;
            }
        });
    }
})();