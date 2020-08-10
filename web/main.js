const toggleBtn = document.querySelector('.navbar__togggleBtn');
const menu = document.querySelector('.navbar_menu');

toggleBtn.addEventListener('click', () => {
	menu.classList.toggle('active');
});
