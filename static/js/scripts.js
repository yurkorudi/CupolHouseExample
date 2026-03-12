document.addEventListener('DOMContentLoaded', function() {
    const header = document.getElementById('main-header');
    

    function checkScroll() {
        if (window.scrollY > 300) {
            header.classList.add('visible');
        } else {
            header.classList.remove('visible');
        }
    }
    window.addEventListener('scroll', checkScroll);

    checkScroll();
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 70,
                    behavior: 'smooth'
                });
            }
        });
    });
});