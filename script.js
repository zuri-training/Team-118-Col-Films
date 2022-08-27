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

// ********** icon buttons ************
const like = document.getElementById("like");
const dislike = document.getElementById("dislike");
const save = document.getElementById("bookmark");

like.addEventListener("click", function (e) {
  const likeButton = e.currentTarget;
  const disl = e.currentTarget.nextElementSibling;
  if (disl) {
    console.log(disl.children);
  }
  if (!likeButton.classList.contains("btn-like")) {
    likeButton.classList.add("btn-like");
    like.innerHTML = '<i class="fa-solid fa-thumbs-up"></i>';
    dislike.innerHTML = '<i class="fa-regular fa-thumbs-down"></i>';
  } else if (likeButton.classList.contains("btn-like")) {
    like.innerHTML = '<i class="fa-regular fa-thumbs-up"></i>';
    likeButton.classList.remove("btn-like");

    // dislike.innerHTML = '<i class="fa-solid fa-thumbs-down"></i>';
  }

  if (!disl.classList.contains("btn-dislike")) {
    dislike.classList.add("btn-dislike");
    like.innerHTML = '<i class="fa-regular fa-thumbs-up"></i>';
    dislike.innerHTML = '<i class="fa-solid fa-thumbs-down"></i>';
  } else if (dislike.classList.contains("btn-dislike")) {
    dislike.innerHTML = '<i class="fa-regular fa-thumbs-down"></i>';
    dislike.classList.remove("btn-like");
  }
});
