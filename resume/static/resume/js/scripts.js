// import mixitup from 'mixitup';

var navbar = document.querySelector('#main-nav');
var div = document.querySelector('#intro');
var mailme = document.querySelector('.mail-me');


const faders = document.querySelectorAll('.fade-in');
const sliders = document.querySelectorAll('.slide-in-left');
const slide = document.querySelector('.slide-in-right');
const bounceIn = document.querySelector('.mail-me');
const options = {};
const options2 = {};

const navObserver = new IntersectionObserver(function (entries, observer) {

    entries.forEach(entry => {
        if (!entry.isIntersecting) {
            navbar.classList.add('nav-scrolled');
        }
    });

}, options);

const navObserver2 = new IntersectionObserver(function (entries, observer) {

    entries.forEach(entry => {
        if (entry.isIntersecting) {
            navbar.classList.remove('nav-scrolled');

        }
    });

}, options2);
navObserver.observe(navbar);
navObserver2.observe(div);


$(document).ready(function () {
    var scrolllink = $('.scroll');

    scrolllink.click(function (e) {
        e.preventDefault();
        $('body,html').animate({
            scrollTop: $(this.hash).offset().top
        }, 500)
    })


    $(window).scroll(function () {
        // Active link switch
        var scrollbarLocation = $(this).scrollTop();
        scrolllink.each(function () {
            var sectionOffset = $(this.hash).offset().top-20;

            if (sectionOffset <= scrollbarLocation) {
                $(this).addClass('active');
                $(this).siblings().removeClass('active');
            }
        })
    })

    var anchortags = document.querySelectorAll('.project-nav-link')
    anchortags.forEach(tag => {
        $(tag).click(function () {
            $(this).addClass('activated-link');
            $(this).siblings().removeClass('activated-link');
        })
    })


    // var mixer = mixitup('.projects-display');
    
})

const appearOptions = {
    threshold: 0,
    rootMargin: '0px 0px -300px 0px'
};

const appearOnScroll = new IntersectionObserver(
    function (
        entries,
        appearOnScroll
    ) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            }
            else {
                entry.target.classList.add('appear');
                appearOnScroll.unobserve(entry.target);
            }
        })
    }
    , appearOptions);

faders.forEach(fader => {
    appearOnScroll.observe(fader);
})

sliders.forEach(slider => {
    appearOnScroll.observe(slider);

})


const appearOnScrollwithPercentage = new IntersectionObserver(
    function (
        entries,
        appearOnScrollwithPercentage
    ) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            }
            else {
                entry.target.classList.add('appear');
                appearOnScrollwithPercentage.unobserve(entry.target);
                x();
            }
        })
    }
    , appearOptions);


appearOnScrollwithPercentage.observe(slide);

const addbounce = new IntersectionObserver(
    function (
        entries,
        addbounce
    ) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            }
            else {
                entry.target.classList.add('bounceIn');
                addbounce.unobserve(entry.target);
            }
        })
    }
    , appearOptions);


addbounce.observe(bounceIn);

function x() {
    $('.percentage').css({
        transform: 'scaleX(1)',
    })
}

new WOW().init()

var projectNavbarlinks = document.querySelectorAll('.project-nav-link');

function animateProjects(links) {
    links.forEach( link => {
        $(link).click( () => {
            console.log(link);
        } );
    } )
}

animateProjects(projectNavbarlinks);