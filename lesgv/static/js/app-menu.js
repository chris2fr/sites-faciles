function toggleMenu() {
    appMenu.classList.toggle('active');
    overlay.classList.toggle('active');
}

menuBtn.addEventListener('click', toggleMenu);
overlay.addEventListener('click', toggleMenu);