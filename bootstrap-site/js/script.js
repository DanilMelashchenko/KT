const galleryButtons = document.querySelectorAll('.gallery-button');
const galleryImages = document.querySelectorAll('.gallery-image');

galleryButtons.forEach(button => {
    button.addEventListener('click', () => {
    const filter = button.getAttribute('data-filter');
    galleryImages.forEach(img => {
        if (filter === 'all' || img.classList.contains(filter)) {
        img.style.display = 'block';
        } else {
        img.style.display = 'none';
        }
    });
});
});

const contactForm = document.querySelector('#contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
    e.preventDefault();
    alert('Повідомлення надіслано!');
    contactForm.reset();
    });
}

const navLinks = document.querySelectorAll('nav a');
navLinks.forEach(link => {
  link.addEventListener('click', function (e) {
    const target = this.getAttribute('href');
    if (target.startsWith('#')) return;
    window.location.href = target;
  });
});
