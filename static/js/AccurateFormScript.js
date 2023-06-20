function revealOnScroll() {
  const elements = document.getElementsByClassName('revealUp');
  for (let i = 0; i < elements.length; i++) {
    const element = elements[i];
    const windowHeight = window.innerHeight;
    const elementTop = element.getBoundingClientRect().top;

    if (elementTop < windowHeight && elementTop > -element.offsetHeight) {
      element.style.opacity = '1';
      element.style.transform = 'translateY(0)';
    } else {
      element.style.opacity = '0';
      element.style.transform = 'translateY(30px)';
    }
  }
}

function throttle(func, wait) {
  let timeout;
  return function() {
    if (!timeout) {
      timeout = setTimeout(function() {
        func();
        timeout = null;
      }, wait);
    }
  };
}

window.addEventListener('scroll', throttle(revealOnScroll, 200));
window.addEventListener('load', revealOnScroll);
