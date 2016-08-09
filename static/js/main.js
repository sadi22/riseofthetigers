var hidemenu;


$(document).ready(function(){
    $(".tab").click(function(){
        $(this).next('#tabbox').toggle();
        $(".glyphicon", this).toggleClass("glyphicon-plus glyphicon-minus");
        console.log('hello')
    });

    var acc = document.getElementsByClassName("accordion");
    var i;
    
    for (i = 0; i < acc.length; i++) {
        acc[i].onclick = function(){
            this.classList.toggle("active");
            $(".glyphicon", this).toggleClass("glyphicon-plus glyphicon-minus");
            this.nextElementSibling.classList.toggle("show");
      }
    }
    $('#tabs').tab();

    var owl1 = $("#owl-demo1");
    var owl2 = $("#owl-demo2");
    var owl3 = $("#owl-demo3");

    owl1.owlCarousel({
      items : 2, //10 items above 1000px browser width
      itemsDesktop : [1000,5], //5 items between 1000px and 901px
      itemsDesktopSmall : [900,3], // betweem 900px and 601px
      itemsTablet: [600,2], //2 items between 600 and 0
      itemsMobile : false // itemsMobile disabled - inherit from itemsTablet option
  });
    owl2.owlCarousel({
      items : 2, //10 items above 1000px browser width
      itemsDesktop : [1000,5], //5 items between 1000px and 901px
      itemsDesktopSmall : [900,3], // betweem 900px and 601px
      itemsTablet: [600,2], //2 items between 600 and 0
      itemsMobile : false // itemsMobile disabled - inherit from itemsTablet option
  });
   owl3.owlCarousel({
      items : 2, //10 items above 1000px browser width
      itemsDesktop : [1000,5], //5 items between 1000px and 901px
      itemsDesktopSmall : [900,3], // betweem 900px and 601px
      itemsTablet: [600,2], //2 items between 600 and 0
      itemsMobile : false // itemsMobile disabled - inherit from itemsTablet option
  });


    // poll starts

     $('#poll-form').on('submit', function(event){
         var isChecked = jQuery("input[name=choice]:checked").val();
        if(!isChecked)
            {
             alert("Opps! You didn't choose an option")
            }
         else {
            event.preventDefault();
            $("#poll-form").fadeOut();
            $(".result").fadeIn(3000);
            create_post();
        }

    });

    // AJAX for posting
    function create_post() {
        console.log("create post is working!") // sanity check
        var id = $("#hide").val();
        var option = $('input[type="radio"]:checked').val();
        $.ajax({
            url : "create_post/", // the endpoint
            type : "POST", // http method
            data : { the_poll : option, poll_id : id }, // data sent with the post request

            // handle a successful response
            success : function(json) {
                var colors = ["#CCCCCC","#333333","#990099"];

                $.each (json, function (item) {

                    $(".table-striped tbody").prepend("<tr><td class='poll'>"+json[item].choice+"</td>" +
                        "<td colspan='3'><div class='progres-track'><div class='progres-fill'><span>"+json[item].perchent+"%"+"</span></div></div></td>")

                    $('.progres-fill span').each(function(){
                        var percent = $(this).html();
                        var color = '#'+(Math.random()*0xFFFFFF<<0).toString(16)
                        $(this).parent().css({"background-color": color, "width": percent});

                    });
                });


            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };

     var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    
});


/* set Cookie to hide menu */
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires=" + d.toGMTString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
}

/* get Cookie to check hide menu */
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i].trim();
        if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
    }
    return "";
}


(function() {
    var selectors = {
        nav: '[data-phases-nav]',
        tabs: '[data-phases-tabs]',
        active: '.__active'
    };
    var classes = {
        active: '__active'
    };
    $('a', selectors.nav).on('click', function() {
        let $this = $(this)[0];
        $(selectors.active, selectors.nav).removeClass(classes.active);
        $($this).addClass(classes.active);
        $('div', selectors.tabs).removeClass(classes.active);
        $($this.hash, selectors.tabs).addClass(classes.active);
        return false;
    });
}());


jQuery(document).ready(function() {

    'use strict';

    /* Contact us Form Submit */
    $('#contactsubmit').bind('click', function() {
        $.ajax({
            url: 'contact.php',
            type: 'POST',
            data: $('#contactform').serialize(),
            success: function(data) {
                if (data == 'Sent Success') {
                    $('#formmsg').addClass('mag-alert-scc').show().find('span.error').html('Thank you for contact us');
                } else {
                    $('#formmsg').addClass('mag-alert-dngr').show().find('span.error').html(data);
                }
            }
        });
        return false;
    });
    /* Toggle scroll menu */
    $('#hidemenu').bind('click', function() {
        var nav = $('.main-menu');
        nav.removeClass("f-nav");
        $(this).hide();
        hidemenu = true;
        setCookie('hidemenu', 'hide', 10);
    });

    $('#showmenu').bind('click', function() {
        var nav = $('.main-menu');
        nav.addClass("f-nav");
        $(this).show();
        hidemenu = false;
        setCookie('hidemenu', 'hide', -10);
    });

    /* Toolbar Menu */
    $('#main-menu-items').smartmenus();

    /* Home Big Boxs Hover caption JS */
    $('.boxgrid.caption').hover(function() {
        $(".cover", this).stop().animate({
            top: '70px'
        }, {
            queue: false,
            duration: 183
        });
    }, function() {
        $(".cover", this).stop().animate({
            top: '142px'
        }, {
            queue: false,
            duration: 153
        });
    });

    $('.boxgrid2.caption').hover(function() {
        $(".cover", this).stop().animate({
            top: '270px'
        }, {
            queue: false,
            duration: 183
        });
    }, function() {
        $(".cover", this).stop().animate({
            top: '366px'
        }, {
            queue: false,
            duration: 153
        });
    });

    $('.boxgrid3.caption').hover(function() {
        $(".cover", this).stop().animate({
            top: '145px'
        }, {
            queue: false,
            duration: 183
        });
    }, function() {
        $(".cover", this).stop().animate({
            top: '202px'
        }, {
            queue: false,
            duration: 153
        });
    });

    /* News ticker JQ */
    $('.newsticker').newsTicker({
        row_height: 40,
        max_rows: 1,
        speed: 500,
        pauseOnHover: 1,
        prevButton: $('#tkr-prev'),
        nextButton: $('#tkr-nxt'),
        stopButton: $('#tkr-stop')
    });

    /* Flickr Feed */
    $('#basicuse').jflickrfeed({
        limit: 9,
        qstrings: {
            id: '80919450@N00'
        },
        itemTemplate: '<a href="{{image_b}}"><img src="{{image_m}}" alt="{{title}}" /></a>'
    });

    /* Right Side Calender */
    var cal = CALENDAR();

    cal.init();


    /* Tooltips */
    $('.mag-info a').tooltip();

    /* Selectors */
    $('select.cust-slctr').customSelect();

});

/* ===== Sliders ===== */

$(window).load(function() {
    $('.flexslider.hm-slider').flexslider({
        animation: 'fade',
        controlNav: false,
        prevText: "",
        nextText: ""

    });

    $('.flexslider.sm-sldr').flexslider({
        animation: 'slide',
        controlNav: false,
        slideshowSpeed: 2000,
        animationSpeed: 2500,
        prevText: "",
        nextText: ""
    });

    $('.flexslider.news-sldr').flexslider({
        animation: 'slide',
        controlNav: false,
        pauseText: '',
        itemWidth: 183,
        itemMargin: 0,
        slideshowSpeed: 4000,
        animationSpeed: 2500,
        prevText: "",
        nextText: ""

    });

    $('.flexslider.img-sm-gal').flexslider({
        animation: 'slide',
        controlNav: true,
        directionNav: false,
        pauseText: '',
        itemWidth: 79,
        itemMargin: 15,
        slideshowSpeed: 6000,
        animationSpeed: 2500,
        slideshow: false,
        prevText: "",
        nextText: ""

    });


    $('.flexslider.vid-thmb').flexslider({
        animation: 'fade',
        controlNav: false,
        itemWidth: 166,
        itemMargin: 10,
        slideshowSpeed: 4000,
        animationSpeed: 2500,
        prevText: "",
        nextText: ""

    });


});


/* This is for the Fixed Menu on scroll */
var nav = $('.main-menu');

$(window).scroll(function() {
    var hidecookie = getCookie('hidemenu');
    if ($(this).scrollTop() > 160 && hidemenu != true && hidecookie != 'hide') {
        nav.addClass("f-nav");
        $('#hidemenu').show();
    } else {
        nav.removeClass("f-nav");
        $('#hidemenu').hide();
    }
});



