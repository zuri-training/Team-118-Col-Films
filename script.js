"use strict";

// querySelectors
const date = document.querySelectorAll("#date");
const menu = document.querySelector(".hamburger--btn");
const overlay = document.querySelector(".overlay");
const sidebar = document.querySelector(".sidebar");
const closeButton = document.querySelector(".close");
const profileButton = document.querySelectorAll(".arrow");
const userSidebar = document.querySelectorAll(".user-sidebar");
const arrowButtonOne = document.querySelectorAll(".arrow-button");

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

// ********** profile button ************
profileButton.forEach((button) =>
  button.addEventListener("click", function (e) {
    const arrowButton = e.currentTarget;
    if (arrowButton.classList.contains("down-button")) {
      userSidebar.forEach((btn) => btn.classList.remove("user-sidebar-toggle"));

      arrowButtonOne.forEach((btn) =>
        btn.setAttribute("src", "./Images/icon-arrow-up.svg")
      );
      arrowButton.classList.remove("down-button");
    } else {
      userSidebar.forEach((btn) => btn.classList.add("user-sidebar-toggle"));

      arrowButtonOne.forEach((btn) =>
        btn.setAttribute("src", "./Images/icon-arrow-down.svg")
      );

      arrowButton.classList.add("down-button");
    }
  })
);
