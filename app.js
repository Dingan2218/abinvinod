// ====================================================================
//  Abin Vinod — Portfolio Interactive Logic
// ====================================================================

document.addEventListener('DOMContentLoaded', () => {

  // Detect if page is located in the blog directory to adjust relative path
  const isBlog = window.location.pathname.includes('/blog/') || window.location.href.includes('/blog/');
  const basePath = isBlog ? '../assets/' : './assets/';

  // ======= CUSTOM CURSOR =======
  const cursor = document.getElementById('custom-cursor');
  const cursorDot = document.getElementById('custom-cursor-dot');

  if (cursor && cursorDot) {
    let mouseX = 0, mouseY = 0;
    let cursorX = 0, cursorY = 0;
    let lastX = 0, lastY = 0;

    // Cute multi-colored vector flower illustrations
    const flowerIllustrations = [
      // Sakura / Cherry Blossom Illustration (Soft pinks)
      `<svg viewBox="0 0 100 100" style="width: 22px; height: 22px; display: block;"><path d="M50,50 Q35,20 50,5 Q65,20 50,50 Z" fill="#ffb7c5" /><path d="M50,50 Q20,35 5,50 Q20,65 50,50 Z" fill="#ffa5ba" /><path d="M50,50 Q65,80 50,95 Q35,80 50,50 Z" fill="#ffb7c5" /><path d="M50,50 Q80,65 95,50 Q80,35 50,50 Z" fill="#ffa5ba" /><circle cx="50" cy="50" r="14" fill="#fff" opacity="0.3"/><circle cx="50" cy="50" r="8" fill="#ffd15c"/></svg>`,
      // Daisy / Sunflower Cartoon Illustration (Warm yellows)
      `<svg viewBox="0 0 100 100" style="width: 22px; height: 22px; display: block;"><g fill="#ffe082"><circle cx="50" cy="20" r="15"/><circle cx="50" cy="80" r="15"/><circle cx="20" cy="50" r="15"/><circle cx="80" cy="50" r="15"/><circle cx="29" cy="29" r="15"/><circle cx="71" cy="71" r="15"/><circle cx="29" cy="71" r="15"/><circle cx="71" cy="29" r="15"/></g><circle cx="50" cy="50" r="22" fill="#ffb300"/><circle cx="50" cy="50" r="15" fill="#f57c00"/></svg>`,
      // Cute Tulip Illustration (Pastel red/pink)
      `<svg viewBox="0 0 100 100" style="width: 22px; height: 22px; display: block;"><path d="M30,70 C30,40 40,30 50,30 C60,30 70,40 70,70 C70,85 30,85 30,70 Z" fill="#ff8a80"/><path d="M40,70 C40,45 45,35 50,35 C55,35 60,45 60,70 C60,80 40,80 40,70 Z" fill="#ff5252"/><path d="M50,70 C50,50 50,40 50,40 C50,40 50,50 50,70 Z" stroke="#d32f2f" stroke-width="2"/><path d="M20,60 C35,60 45,45 50,30 C45,45 30,50 20,60 Z" fill="#ff8a80"/><path d="M80,60 C65,60 55,45 50,30 C55,45 70,50 80,60 Z" fill="#ff8a80"/></svg>`
    ];

    window.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      cursorDot.style.left = `${mouseX}px`;
      cursorDot.style.top = `${mouseY}px`;

      // Spawn flower trail based on movement distance
      const dist = Math.hypot(mouseX - lastX, mouseY - lastY);
      if (dist > 40) {
        spawnTrailFlower(mouseX, mouseY);
        lastX = mouseX;
        lastY = mouseY;
      }
    });

    function spawnTrailFlower(x, y) {
      const flower = document.createElement('div');
      flower.className = 'flower-trail-particle';
      flower.innerHTML = flowerIllustrations[Math.floor(Math.random() * flowerIllustrations.length)];
      flower.style.left = `${x}px`;
      flower.style.top = `${y}px`;
      
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
    const flowerIllustrations = [
      // Sakura / Cherry Blossom Illustration (Soft pinks)
      `<svg viewBox="0 0 100 100" style="width: 28px; height: 28px; display: block;"><path d="M50,50 Q35,20 50,5 Q65,20 50,50 Z" fill="#ffb7c5" /><path d="M50,50 Q20,35 5,50 Q20,65 50,50 Z" fill="#ffa5ba" /><path d="M50,50 Q65,80 50,95 Q35,80 50,50 Z" fill="#ffb7c5" /><path d="M50,50 Q80,65 95,50 Q80,35 50,50 Z" fill="#ffa5ba" /><circle cx="50" cy="50" r="14" fill="#fff" opacity="0.3"/><circle cx="50" cy="50" r="8" fill="#ffd15c"/></svg>`,
      // Daisy / Sunflower Cartoon Illustration (Warm yellows)
      `<svg viewBox="0 0 100 100" style="width: 28px; height: 28px; display: block;"><g fill="#ffe082"><circle cx="50" cy="20" r="15"/><circle cx="50" cy="80" r="15"/><circle cx="20" cy="50" r="15"/><circle cx="80" cy="50" r="15"/><circle cx="29" cy="29" r="15"/><circle cx="71" cy="71" r="15"/><circle cx="29" cy="71" r="15"/><circle cx="71" cy="29" r="15"/></g><circle cx="50" cy="50" r="22" fill="#ffb300"/><circle cx="50" cy="50" r="15" fill="#f57c00"/></svg>`,
      // Cute Tulip Illustration (Pastel red/pink)
      `<svg viewBox="0 0 100 100" style="width: 28px; height: 28px; display: block;"><path d="M30,70 C30,40 40,30 50,30 C60,30 70,40 70,70 C70,85 30,85 30,70 Z" fill="#ff8a80"/><path d="M40,70 C40,45 45,35 50,35 C55,35 60,45 60,70 C60,80 40,80 40,70 Z" fill="#ff5252"/><path d="M50,70 C50,50 50,40 50,40 C50,40 50,50 50,70 Z" stroke="#d32f2f" stroke-width="2"/><path d="M20,60 C35,60 45,45 50,30 C45,45 30,50 20,60 Z" fill="#ff8a80"/><path d="M80,60 C65,60 55,45 50,30 C55,45 70,50 80,60 Z" fill="#ff8a80"/></svg>`
    ];

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
      particle.innerHTML = flowerIllustrations[Math.floor(Math.random() * flowerIllustrations.length)];
      
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

