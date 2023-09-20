const lightbox = GLightbox();
const owl = $('.owl-carousel');
owl.on("initialized.owl.carousel changed.owl.carousel", function(e) {
    if (!e.namespace) {
      return;
    }
    $("#counter").text(
      e.relatedTarget.relative(e.item.index) + 1 + " / " + e.item.count
    );
  })
.owlCarousel({
    loop:true,
    margin:10,
    lazyLoad: true,
    nav:true,
    dots: false,
    singleImage: true,
    autoHeight: false,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:1
        }
    },
    onInitialized: function(event) {
        let counterDiv = document.createElement('div');
        counterDiv.setAttribute('id', 'counter');
        counterDiv.setAttribute('class', 'text-sm text-white px-4 leading-9');
        counterDiv.textContent = `${event.relatedTarget.relative(event.item.index)+1} / ${event.item.count}`;
        let nextButton = document.querySelector('.owl-next');
        nextButton.parentNode.insertBefore(counterDiv, nextButton.nextSibling);

        $('.owl-carousel').find('.owl-item').attr('aria-selected','false');
        $('.owl-carousel').find('.owl-item.active').attr('aria-selected','true'); // let screen readers know an item is active

        // apply meta info to next and previous buttons and make them focusable
        $('.owl-carousel').find('.owl-prev').attr('role','button').attr('title','Previous');
        $('.owl-carousel').find('.owl-next').attr('role','button').attr('title','Next');
        $('.owl-carousel, .owl-prev, .owl-next').attr('tabindex','0');

        // add instructions to keyboard users that are only visible when the carousel is focused
        $('.owl-carousel').find('.owl-stage-outer').append('<p class="alert alert-success show-on-focus">Use left and right arrow keys to navigate.</p>');

        // listen for keyboard input
        $(document).on('keydown', function(e){

            var $focusedElement = $(document.activeElement),
                singleOwl = $(".owl-carousel").data('owlCarousel'),
                type = e.which == 39? 'next': null,
                type = e.which == 37? 'prev': type,
                type = e.which == 13? 'enter':type;

            // if the carousel is focused, use left and right arrow keys to navigate
            if($focusedElement.attr('class') === 'owl-carousel'){

                if (type == 'next') {
                    singleOwl.next();
                } else if (type == 'prev') {
                    singleOwl.prev();
                }

                // if the prev and next buttons are focused, catch "Enter" and navigate in the right direction
            } else if (type == 'enter') {
                if ($focusedElement.hasClass('owl-next')) {
                    singleOwl.next();
                } else if ($focusedElement.hasClass('owl-prev')) {
                    singleOwl.prev();
                }
            }
        });
    },
    // let screen readers know which slide is active after navigation or reinit
    onChange : function() {
        $('.owl-carousel').find('.owl-item').attr('aria-selected','false');
        $('.owl-carousel').find('.owl-item.active').attr('aria-selected','true');
    }
});