'use strict';

var speed = 300;
var width = 890;
var currentPos = 0;
var timeoutId = 0;
var path = window.location.pathname.split("/");
var pathLen = path.length;
var reqImg = path[pathLen-1];


var $slider = $('#slider');
var $slideContainer = $slider.find('.slides');
var $slides = $slideContainer.find('.slide');
var $next = $slider.find('.next');
var $prev = $slider.find('.prev');

var endWidth = -(($slides.length-1)*width);
var startWidth = -((reqImg-1)*width);
var currentSlide = reqImg;

function checkLast() {
  if (currentSlide >= $slides.length) {
    currentSlide = 1;
    $slideContainer.css('margin-left', 0);
  }
}

function checkFirst() {
  if (currentSlide <= 1) {
    $slideContainer.animate({'margin-left': endWidth}, 0);
    currentSlide = $slides.length;
  }
}

function nextPic() {
  currentSlide++;
  $slideContainer.animate({'margin-left': '-='+width}, speed, checkLast);
}

function prevPic() {
  checkFirst();
  $slideContainer.animate({'margin-left': '+='+width}, speed);
  currentSlide--;
}

function showNavigators() {
  $next.fadeTo(500, 0.4);
  $prev.fadeTo(500, 0.4);
}

function hideNavigators() {
  $next.fadeOut(300);
  $prev.fadeOut(300);
}

$(function() {
  $next.fadeTo(0, 0.4);
  $prev.fadeTo(0, 0.4);
  $slideContainer.animate({'margin-left': startWidth}, 0)
  $($next.on('click', nextPic));
  $($prev.on('click', prevPic));
  $($slideContainer.on('mouseover', showNavigators));
  $($slider.on('mouseleave', hideNavigators));
});

// var firstPic = document.getElementsByName("current");
// var currentPic = firstPic[0];
// var id = parseInt(currentPic.id);
// var exit = 0;
// while (exit != 1) {
//   currentPic = document.getElementById(id);
//   if (currentPic != null) {
//     currentPic.addEventListener("click", cycleImage);
//     id += 1;
//   } else {
//     exit = 1;
//   }
// }
// id = parseInt(firstPic[0].id);
//
// function cycleImage() {
//   currentPic = document.getElementById(id);
//   currentPic.className = "noscreen";
//   id += 1;
//   var nextPic = document.getElementById(id);
//   if (nextPic != null) {
//     nextPic.className = "";
//     currentPic = nextPic;
//   } else {
//     id = parseInt(firstPic[0].id);
//     nextPic = document.getElementById(id);
//     nextPic.className = "";
//     currentPic = nextPic;
//   }
// }
