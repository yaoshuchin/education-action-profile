const filterButtons = document.querySelectorAll('[data-filter]');
const photoCards = document.querySelectorAll('.photo-grid figure');

function applyFilter(filter) {
  photoCards.forEach((card) => {
    const matches = filter === 'all' || card.dataset.category === filter;
    card.classList.toggle('is-hidden', !matches);
  });
  filterButtons.forEach((button) => {
    const active = button.dataset.filter === filter;
    button.classList.toggle('active', active);
    button.setAttribute('aria-pressed', String(active));
  });
}

filterButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const filter = button.dataset.filter;
    history.replaceState(null, '', filter === 'all' ? 'photos.html' : `photos.html#${filter}`);
    applyFilter(filter);
  });
});

const requestedFilter = window.location.hash.slice(1);
const validFilters = ['sport', 'international', 'care', 'school'];
applyFilter(validFilters.includes(requestedFilter) ? requestedFilter : 'all');
