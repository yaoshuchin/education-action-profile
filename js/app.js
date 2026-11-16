const body = document.body;
const menu = document.querySelector('.menu');
const nav = document.querySelector('.nav');
const savedTheme = localStorage.getItem('education-theme');
const savedSize = localStorage.getItem('education-size');
if (savedTheme) body.dataset.theme = savedTheme;
if (savedSize) body.dataset.size = savedSize;

function syncButtons(selector, attribute, value) {
  document.querySelectorAll(selector).forEach((button) => {
    button.setAttribute('aria-pressed', String(button.dataset[attribute] === value));
  });
}

menu?.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  menu.setAttribute('aria-expanded', String(open));
});

document.querySelectorAll('[data-size]').forEach((button) => {
  button.addEventListener('click', () => {
    body.dataset.size = button.dataset.size;
    localStorage.setItem('education-size', body.dataset.size);
    syncButtons('[data-size]', 'size', body.dataset.size);
  });
});

document.querySelectorAll('[data-theme]').forEach((button) => {
  button.addEventListener('click', () => {
    body.dataset.theme = button.dataset.theme;
    localStorage.setItem('education-theme', body.dataset.theme);
    syncButtons('[data-theme]', 'theme', body.dataset.theme);
  });
});

syncButtons('[data-size]', 'size', body.dataset.size);
syncButtons('[data-theme]', 'theme', body.dataset.theme);
