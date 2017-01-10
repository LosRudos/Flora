'use strict';

var $hjem = $("li[title='hjem']");
var $pl = $("li[title='pl']");
var $fln = $("li[title='fln']");
var $fll = $("li[title='fll']");
var $ko = $("li[title='ko']");

var path = window.location.pathname.split("/");
var currentPath = path[2];

if (currentPath) {
  switch (currentPath) {
    case "planteliste":
      $pl.attr("id", "active");
      break;
    case "familieliste":
      $fln.attr("id", "active");
      break;
    case "famile_latin":
      $fll.attr("id", "active");
      break;
    case "kontakt":
      $ko.attr("id", "active");
      break;
  }
} else {
  $hjem.attr("id", "active")
}
