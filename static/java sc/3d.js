// elemen
const navs = document.querySelectorAll('.nav-list li');
const cube = document.querySelector('.box');


const resumeLists = document.querySelectorAll('.resume-list');
const resumeBoxes = document.querySelectorAll('.resume-box');

const portfolioLists = document.querySelectorAll('.portfolio-list');
const portfolioBoxes = document.querySelectorAll('.portfolio-box');

// Navbar actions (perbaikan: gunakan idx dan style.transform)
navs.forEach((nav, idx) => {
  nav.addEventListener('click', () => {
    const activeNav = document.querySelector('.nav-list li.active');
    if (activeNav) activeNav.classList.remove('active');
    nav.classList.add('active');

    if (cube) {
      // transisi smooth (opsional)
      cube.style.transition = 'transform 0.7s ease';
      // gunakan template literal dan style.transform
      cube.style.transform = `rotateY(${idx * -90}deg)`;
    }

    
  });
});

// Resume tab switch (sesuaikan nama resumeBoxes)
resumeLists.forEach((list, idx) => {
  list.addEventListener('click', () => {
    const activeList = document.querySelector('.resume-list.active');
    const activeBox = document.querySelector('.resume-box.active');
    if (activeList) activeList.classList.remove('active');
    if (activeBox) activeBox.classList.remove('active');

    list.classList.add('active');
    if (resumeBoxes[idx]) resumeBoxes[idx].classList.add('active');
  });
});

// Portfolio tab switch (sesuaikan nama portfolioBoxes)
portfolioLists.forEach((list, idx) => {
  list.addEventListener('click', () => {
    const activeList = document.querySelector('.portfolio-list.active');
    const activeBox = document.querySelector('.portfolio-box.active');
    if (activeList) activeList.classList.remove('active');
    if (activeBox) activeBox.classList.remove('active');

    list.classList.add('active');
    if (portfolioBoxes[idx]) portfolioBoxes[idx].classList.add('active');
  });
});
