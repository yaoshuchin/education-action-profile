const body = document.body;
const menuToggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.main-nav');

menuToggle?.addEventListener('click', () => {
  const isOpen = nav.classList.toggle('open');
  menuToggle.setAttribute('aria-expanded', String(isOpen));
});

document.querySelectorAll('.main-nav a').forEach((link) => {
  link.addEventListener('click', () => {
    nav.classList.remove('open');
    menuToggle?.setAttribute('aria-expanded', 'false');
  });
});

const savedTheme = localStorage.getItem('education-theme');
const savedSize = localStorage.getItem('education-size');
if (savedTheme) body.dataset.theme = savedTheme;
if (savedSize) body.dataset.size = savedSize;

function updateSelected(selector, attribute, value) {
  document.querySelectorAll(selector).forEach((button) => {
    button.classList.toggle('selected', button.getAttribute(attribute) === value);
  });
}

document.querySelectorAll('[data-theme-choice]').forEach((button) => {
  button.addEventListener('click', () => {
    const theme = button.dataset.themeChoice;
    body.dataset.theme = theme;
    localStorage.setItem('education-theme', theme);
    updateSelected('[data-theme-choice]', 'data-theme-choice', theme);
  });
});

document.querySelectorAll('[data-size-choice]').forEach((button) => {
  button.addEventListener('click', () => {
    const size = button.dataset.sizeChoice;
    body.dataset.size = size;
    localStorage.setItem('education-size', size);
    updateSelected('[data-size-choice]', 'data-size-choice', size);
  });
});

updateSelected('[data-theme-choice]', 'data-theme-choice', body.dataset.theme);
updateSelected('[data-size-choice]', 'data-size-choice', body.dataset.size);
