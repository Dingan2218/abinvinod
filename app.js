// ====================================================================
//  Abin Vinod — Portfolio Interactive Logic
// ====================================================================

document.addEventListener('DOMContentLoaded', () => {

  // ======= CUSTOM CURSOR =======
  const cursor = document.getElementById('custom-cursor');
  const cursorDot = document.getElementById('custom-cursor-dot');

  if (cursor && cursorDot) {
    let mouseX = 0, mouseY = 0;
    let cursorX = 0, cursorY = 0;
    let lastX = 0, lastY = 0;
    const flowerEmojis = ['🌸', '🌷', '🌺', '🌻', '🌼', '🏵️', '💮'];

    window.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      cursorDot.style.left = `${mouseX}px`;
      cursorDot.style.top = `${mouseY}px`;

      // Spawn flower trail based on movement distance
      const dist = Math.hypot(mouseX - lastX, mouseY - lastY);
      if (dist > 40) { // Spawn particle every 40 pixels of movement
        spawnTrailFlower(mouseX, mouseY);
        lastX = mouseX;
        lastY = mouseY;
      }
    });

    function spawnTrailFlower(x, y) {
      const flower = document.createElement('div');
      flower.className = 'flower-trail-particle';
      flower.textContent = flowerEmojis[Math.floor(Math.random() * flowerEmojis.length)];
      flower.style.left = `${x}px`;
      flower.style.top = `${y}px`;
      
      // Add slight randomized animation variation
      const randomRotate = (Math.random() - 0.5) * 60;
      flower.style.setProperty('--random-rotate', `${randomRotate}deg`);
      
      document.body.appendChild(flower);
      setTimeout(() => {
        flower.remove();
      }, 1000);
    }

    function animateCursor() {
      cursorX += (mouseX - cursorX) * 0.12;
      cursorY += (mouseY - cursorY) * 0.12;
      cursor.style.left = `${cursorX}px`;
      cursor.style.top = `${cursorY}px`;
      requestAnimationFrame(animateCursor);
    }
    animateCursor();

    // Hover states
    const interactives = document.querySelectorAll('a, button, input, textarea, .magnetic, summary');
    interactives.forEach(el => {
      el.addEventListener('mouseenter', () => cursor.classList.add('hovered'));
      el.addEventListener('mouseleave', () => cursor.classList.remove('hovered'));
    });
  }

  // ======= MAGNETIC BUTTONS =======
  const magneticElements = document.querySelectorAll('.magnetic');
  magneticElements.forEach(el => {
    el.addEventListener('mousemove', (e) => {
      const rect = el.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      el.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
    });
    el.addEventListener('mouseleave', () => {
      el.style.transform = 'translate(0, 0)';
    });
  });

  // ======= SCROLL REVEAL =======
  const revealElements = document.querySelectorAll('.reveal, .reveal-text');
  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        // Stagger animation for grid children
        const delay = entry.target.closest('.services-grid, .testimonials-grid, .results-bar, .blog-grid')
          ? Array.from(entry.target.parentElement.children).indexOf(entry.target) * 100
          : 0;

        setTimeout(() => {
          entry.target.classList.add('active');
        }, delay);

        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });

  revealElements.forEach(el => revealObserver.observe(el));

  // Trigger hero reveals on load
  setTimeout(() => {
    document.querySelectorAll('.hero .reveal-text').forEach((el, i) => {
      setTimeout(() => el.classList.add('active'), i * 120);
    });
  }, 100);

  // ======= CONTACT FORM =======
  const contactForm = document.getElementById('contact-form');
  const formStatus = document.getElementById('form-status');

  if (contactForm && formStatus) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const submitBtn = contactForm.querySelector('button[type="submit"]');
      const originalText = submitBtn.innerHTML;

      submitBtn.disabled = true;
      submitBtn.innerHTML = 'Sending...';
      formStatus.textContent = '';
      formStatus.className = 'form-status';

      setTimeout(() => {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalText;
        if (window.lucide) window.lucide.createIcons();

        formStatus.textContent = '✓ Message sent! I will get back to you within 24 hours.';
        formStatus.classList.add('success');

        contactForm.reset();
      }, 1500);
    });
  }

  // ======= BACK TO TOP =======
  const backToTop = document.getElementById('back-to-top');
  if (backToTop) {
    backToTop.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // ======= POOKIE VIBE TOGGLE (SPARKLES & HEARTS EFFECT) =======
  const vibeToggle = document.getElementById('vibe-toggle');
  if (vibeToggle) {
    const emojis = ['✨', '💖', '🌸', '🧸', '🌟', '🧁', '🍦', '🩰'];
    vibeToggle.addEventListener('click', (e) => {
      // Create 15 cluster particles
      const rect = vibeToggle.getBoundingClientRect();
      const originX = rect.left + rect.width / 2;
      const originY = rect.top + rect.height / 2;

      for (let i = 0; i < 15; i++) {
        createParticle(originX, originY);
      }
    });

    function createParticle(x, y) {
      const particle = document.createElement('div');
      particle.className = 'sparkle-particle';
      particle.textContent = emojis[Math.floor(Math.random() * emojis.length)];
      
      // Calculate random offsets for spray effect
      const offsetX = (Math.random() - 0.5) * 150;
      const offsetY = (Math.random() - 0.5) * 50;
      
      particle.style.left = `${x + offsetX}px`;
      particle.style.top = `${y + offsetY}px`;
      
      // Random animation variations
      particle.style.animationDelay = `${Math.random() * 0.2}s`;
      particle.style.animationDuration = `${1.2 + Math.random() * 0.8}s`;
      
      document.body.appendChild(particle);
      
      // Remove element after animation completes
      setTimeout(() => {
        particle.remove();
      }, 2000);
    }
  }
});

