const links = {
  primary: 'https://is.gd/5AKOTT',
  backup: 'https://yaoshuchin.github.io/education-action-profile/',
};

document.querySelectorAll('[data-copy]').forEach((button) => {
  button.addEventListener('click', async () => {
    const value = links[button.dataset.copy];
    await navigator.clipboard.writeText(value);
    const original = button.textContent;
    button.textContent = '已複製';
    button.classList.add('copied');
    setTimeout(() => {
      button.textContent = original;
      button.classList.remove('copied');
    }, 1400);
  });
});
