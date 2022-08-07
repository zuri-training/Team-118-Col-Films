"use strict";

// querySelectors
const date = document.querySelectorAll("#date");
const menu = document.querySelector(".hamburger--btn");
const overlay = document.querySelector(".overlay");
const sidebar = document.querySelector(".sidebar");
const closeButton = document.querySelector(".close");

// ********** set date ************
// // select span

date.forEach((date) => (date.innerHTML = new Date().getFullYear()));

// ********** menu and close button function ************
menu.addEventListener("click", function (e) {
  e.preventDefault();
  overlay.classList.remove("remove-overlay");
  sidebar.classList.remove("sidebar-close");
});
const closeModal = function () {
  overlay.classList.add("remove-overlay");
  sidebar.classList.add("sidebar-close");
};
closeButton.addEventListener("click", closeModal);
overlay.addEventListener("click", closeModal);

document.addEventListener("keydown", function (e) {
  if (e.key === "Escape" && !sidebar.classList.contains("sidebar-close")) {
    closeModal();
  }
});
