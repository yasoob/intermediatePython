$(document).ready(function () {
    var height = $("div.wy-menu").height();
    var onMobile = $(".wy-nav-side").hasClass("shift");
    $("#expand-nav").click(function () {
        if (!onMobile){
            $("div.wy-menu").toggleClass("menu-toggle");
            if (!$("div.wy-menu").hasClass("menu-toggle")){
                $("div.wy-menu").animate({ height: 0 }, 200);
            } else{
                $("div.wy-menu").animate({ height: height }, 200);
            }
        }
    });

    if ($('.wy-nav-side').height() > $(window).height()){
        $(".wy-nav-side").addClass("shift");
    }

    $(".close-btn").click(function () {
        $("#mc_embed_signup").hide();

        // Updating cookies will help prevent this from showing up again soon
        // http://www.quirksmode.org/js/cookies.html
        var date = new Date();
        var days = 10;
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        document.cookie =
            "hidesubscribe=true; expires=" + date.toGMTString() + "; path=/";
    });

    if (document.cookie.indexOf("hidesubscribe") != -1) {
        $("#mc_embed_signup").hide();
    }
});  

