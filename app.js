// ====================================================================
//  Abin Vinod — Portfolio Interactive Logic
// ====================================================================

// Register Service Worker for Resilient Offline Fallback
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    const isSubDir = window.location.pathname.includes('/blog/') || 
                     window.location.pathname.includes('/best_digital_marketer_kerala/') || 
                     window.location.pathname.includes('/best_seo-expert-kerala/') ||
                     window.location.href.includes('/blog/') ||
                     window.location.href.includes('/best_digital_marketer_kerala/') ||
                     window.location.href.includes('/best_seo-expert-kerala/');
    const swPath = isSubDir ? '../sw.js' : './sw.js';
    navigator.serviceWorker.register(swPath)
      .then(reg => console.log('Service Worker registered successfully:', reg.scope))
      .catch(err => console.error('Service Worker registration failed:', err));
  });
}

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
      if (dist > 15) { // Spawn particle every 15 pixels of movement
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
      // Create 35 cluster particles for a rich burst effect
      const rect = vibeToggle.getBoundingClientRect();
      const originX = rect.left + rect.width / 2;
      const originY = rect.top + rect.height / 2;

      for (let i = 0; i < 35; i++) {
        createParticle(originX, originY);
      }
    });

    function createParticle(x, y) {
      const particle = document.createElement('div');
      particle.className = 'sparkle-particle';
      particle.innerHTML = flowerIllustrations[Math.floor(Math.random() * flowerIllustrations.length)];
      
      // Calculate wider random offsets for spray scatter effect
      const offsetX = (Math.random() - 0.5) * 250;
      const offsetY = (Math.random() - 0.5) * 80;
      
      particle.style.left = `${x + offsetX}px`;
      particle.style.top = `${y + offsetY}px`;
      
      // Set longer animation variations so flowers fall all the way down
      particle.style.animationDelay = `${Math.random() * 0.4}s`;
      particle.style.animationDuration = `${2.5 + Math.random() * 1.5}s`;
      
      document.body.appendChild(particle);
      
      // Clean up after the fall animation finishes
      setTimeout(() => {
        particle.remove();
      }, 5000);
    }
  }

  // ======= CINE-DECK CAROUSEL, DECRYPT & PARALLAX =======
  const deck = document.getElementById('cine-deck');
  const character = document.getElementById('deck-character');
  const bgTitle = document.getElementById('deck-bg-title');
  const slides = document.querySelectorAll('.deck-slide');
  const categoryPills = document.querySelectorAll('.category-pill');
  const prevBtn = document.getElementById('deck-prev');
  const nextBtn = document.getElementById('deck-next');
  const currentPageInd = document.getElementById('deck-current-page');
  
  if (deck) {
    let currentIdx = 0;
    const totalSlides = slides.length;
    const bgTitleTexts = ['SEO EXPERT', 'ADS EXPERT', 'GROWTH LEAD'];

    // Scramble / Decrypt text transition
    function scrambleText(element, targetText) {
      if (!element) return;
      const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#%*?@';
      let frame = 0;
      const queue = [];
      
      const currentText = element.textContent || '';
      const maxLength = Math.max(currentText.length, targetText.length);
      
      for (let i = 0; i < maxLength; i++) {
        const from = currentText[i] || '';
        const to = targetText[i] || '';
        const start = Math.floor(Math.random() * 15);
        const end = start + Math.floor(Math.random() * 15) + 5;
        queue.push({ from, to, start, end, char: '' });
      }
      
      function update() {
        let output = '';
        let complete = 0;
        
        for (let i = 0; i < queue.length; i++) {
          let { from, to, start, end, char } = queue[i];
          if (frame >= end) {
            complete++;
            output += to;
          } else if (frame >= start) {
            if (!char || Math.random() < 0.3) {
              char = chars[Math.floor(Math.random() * chars.length)];
              queue[i].char = char;
            }
            output += `<span style="color: var(--accent-cyan); font-family: monospace; font-weight: 700;">${char}</span>`;
          } else {
            output += from;
          }
        }
        
        element.innerHTML = output;
        if (complete === queue.length) {
          element.textContent = targetText;
        } else {
          frame++;
          requestAnimationFrame(update);
        }
      }
      update();
    }

    // Slide switching
    function showSlide(index) {
      if (index < 0) index = totalSlides - 1;
      if (index >= totalSlides) index = 0;
      
      currentIdx = index;
      
      // Update active slide
      slides.forEach((slide, idx) => {
        slide.classList.toggle('active', idx === currentIdx);
      });
      
      // Update category pill active state
      categoryPills.forEach((pill, idx) => {
        pill.classList.toggle('active', idx === currentIdx);
      });

      // Update page indicators
      if (currentPageInd) {
        currentPageInd.textContent = String(currentIdx + 1).padStart(2, '0');
      }

      // Trigger text decrypt on current slide title
      const activeTitle = slides[currentIdx].querySelector('.deck-title');
      if (activeTitle) {
        const targetText = activeTitle.getAttribute('data-text') || activeTitle.textContent;
        scrambleText(activeTitle, targetText);
      }

      // Transition background huge title with blur-out and scramble
      if (bgTitle) {
        bgTitle.classList.add('blur-out');
        setTimeout(() => {
          bgTitle.textContent = bgTitleTexts[currentIdx];
          bgTitle.classList.remove('blur-out');
          scrambleText(bgTitle, bgTitleTexts[currentIdx]);
        }, 300);
      }

      // Add a pop scale effect to the center character graphic on switch
      if (character) {
        character.style.transform = 'translate3d(0, 0, 50px) scale(0.95)';
        character.style.filter = 'drop-shadow(0 25px 50px rgba(255, 117, 151, 0.55)) brightness(1.2)';
        setTimeout(() => {
          character.style.transform = 'translate3d(0, 0, 0) scale(1)';
          character.style.filter = 'drop-shadow(0 25px 50px rgba(255, 117, 151, 0.35))';
        }, 400);
      }
    }

    // Event bindings for controls
    if (prevBtn) prevBtn.addEventListener('click', () => showSlide(currentIdx - 1));
    if (nextBtn) nextBtn.addEventListener('click', () => showSlide(currentIdx + 1));
    
    categoryPills.forEach((pill) => {
      pill.addEventListener('click', () => {
        const index = parseInt(pill.getAttribute('data-index'), 10);
        showSlide(index);
      });
    });

    // 3D Parallax Tilt Effect
    deck.addEventListener('mousemove', (e) => {
      const rect = deck.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      
      // Update CSS variables for spotlight glow gradient
      deck.style.setProperty('--mouse-x', `${(x / rect.width) * 100}%`);
      deck.style.setProperty('--mouse-y', `${(y / rect.height) * 100}%`);
      
      // Calculate tilt values (max 6deg)
      const rotateX = -((y - rect.height / 2) / (rect.height / 2)) * 5;
      const rotateY = ((x - rect.width / 2) / (rect.width / 2)) * 5;
      
      deck.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
      
      // Deep 3D shift for character illustration
      if (character) {
        const charX = ((x - rect.width / 2) / (rect.width / 2)) * 25;
        const charY = ((y - rect.height / 2) / (rect.height / 2)) * 20;
        character.style.transform = `translate3d(${charX}px, ${charY}px, 60px) scale(1.02)`;
        character.style.filter = 'drop-shadow(0 30px 60px rgba(255, 117, 151, 0.45))';
      }
    });

    deck.addEventListener('mouseleave', () => {
      deck.style.transform = 'rotateX(0deg) rotateY(0deg)';
      if (character) {
        character.style.transform = 'translate3d(0, 0, 0) scale(1)';
        character.style.filter = 'drop-shadow(0 25px 50px rgba(255, 117, 151, 0.35))';
      }
    });

    // Run initial scramble on page load
    setTimeout(() => {
      const activeTitle = slides[0].querySelector('.deck-title');
      if (activeTitle) scrambleText(activeTitle, activeTitle.getAttribute('data-text'));
      if (bgTitle) scrambleText(bgTitle, bgTitleTexts[0]);
    }, 800);
  }

  // ======= LIVE FOOTER CLOCK (IST Time Zone) =======
  const footerTime = document.getElementById('footer-local-time');
  if (footerTime) {
    const updateTime = () => {
      const options = {
        timeZone: 'Asia/Kolkata',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false
      };
      const formatter = new Intl.DateTimeFormat('en-US', options);
      footerTime.textContent = `${formatter.format(new Date())} IST (GMT+5:30)`;
    };
    updateTime();
    setInterval(updateTime, 1000);
  }

  // ======= INTERACTIVE FOOTER CANVAS CONSTELLATION =======
  const footerCanvas = document.getElementById('footer-interactive-canvas');
  if (footerCanvas) {
    const ctx = footerCanvas.getContext('2d');
    let particles = [];
    const maxParticles = 65;
    const connectionDist = 110;
    
    let mouse = { x: null, y: null, active: false };
    
    const resizeCanvas = () => {
      const rect = footerCanvas.parentElement.getBoundingClientRect();
      footerCanvas.width = rect.width;
      footerCanvas.height = rect.height;
    };
    
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();
    
    const footer = footerCanvas.parentElement;
    const hudCoords = document.getElementById('hud-coordinates');
    footer.addEventListener('mousemove', (e) => {
      const rect = footer.getBoundingClientRect();
      mouse.x = e.clientX - rect.left;
      mouse.y = e.clientY - rect.top;
      mouse.active = true;
      if (hudCoords) {
        hudCoords.textContent = `X: ${mouse.x.toFixed(0)} / Y: ${mouse.y.toFixed(0)}`;
      }
    });
    
    footer.addEventListener('mouseleave', () => {
      mouse.active = false;
      if (hudCoords) {
        hudCoords.textContent = 'X: 0.00 / Y: 0.00';
      }
    });
    
    class Particle {
      constructor() {
        this.x = Math.random() * footerCanvas.width;
        this.y = Math.random() * footerCanvas.height;
        this.vx = (Math.random() - 0.5) * 0.5;
        this.vy = (Math.random() - 0.5) * 0.5;
        this.radius = Math.random() * 2 + 1;
        this.alpha = Math.random() * 0.5 + 0.2;
      }
      
      update() {
        this.x += this.vx;
        this.y += this.vy;
        
        if (this.x < 0 || this.x > footerCanvas.width) this.vx *= -1;
        if (this.y < 0 || this.y > footerCanvas.height) this.vy *= -1;
        
        if (mouse.active) {
          const dx = mouse.x - this.x;
          const dy = mouse.y - this.y;
          const dist = Math.hypot(dx, dy);
          if (dist < 100) {
            const force = (100 - dist) / 100;
            this.x -= (dx / dist) * force * 1.5;
            this.y -= (dy / dist) * force * 1.5;
          }
        }
      }
      
      draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(255, 117, 151, ${this.alpha})`;
        ctx.fill();
      }
    }
    
    const initParticles = () => {
      particles = [];
      for (let i = 0; i < maxParticles; i++) {
        particles.push(new Particle());
      }
    };
    initParticles();
    
    const animate = () => {
      ctx.clearRect(0, 0, footerCanvas.width, footerCanvas.height);
      
      particles.forEach(p => {
        p.update();
        p.draw();
      });
      
      for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
          const dx = particles[i].x - particles[j].x;
          const dy = particles[i].y - particles[j].y;
          const dist = Math.hypot(dx, dy);
          
          if (dist < connectionDist) {
            const alpha = (1 - (dist / connectionDist)) * 0.15;
            ctx.beginPath();
            ctx.moveTo(particles[i].x, particles[i].y);
            ctx.lineTo(particles[j].x, particles[j].y);
            ctx.strokeStyle = `rgba(255, 117, 151, ${alpha})`;
            ctx.lineWidth = 0.8;
            ctx.stroke();
          }
        }
        
        if (mouse.active) {
          const dx = particles[i].x - mouse.x;
          const dy = particles[i].y - mouse.y;
          const dist = Math.hypot(dx, dy);
          if (dist < 130) {
            const alpha = (1 - (dist / 130)) * 0.22;
            ctx.beginPath();
            ctx.moveTo(particles[i].x, particles[i].y);
            ctx.lineTo(mouse.x, mouse.y);
            ctx.strokeStyle = `rgba(255, 117, 151, ${alpha})`;
            ctx.lineWidth = 1;
            ctx.stroke();
          }
        }
      }
      
      requestAnimationFrame(animate);
    };
    animate();
    
    window.addEventListener('resize', () => {
      initParticles();
    });
  }

  // ======= HUD SCROLL PROGRESS & KINETIC PARALLAX MARQUEES =======
  const hudScroll = document.getElementById('hud-scroll-depth');
  const marqueeLeft = document.getElementById('marquee-left');
  const marqueeRight = document.getElementById('marquee-right');
  
  window.addEventListener('scroll', () => {
    const winHeight = window.innerHeight;
    const docHeight = document.documentElement.scrollHeight;
    const scrollPos = window.scrollY;
    const scrollPercent = Math.min(100, Math.max(0, Math.ceil((scrollPos / (docHeight - winHeight)) * 100)));
    
    if (hudScroll) {
      hudScroll.textContent = `PROGRESS: ${scrollPercent}%`;
    }
    
    if (marqueeLeft && marqueeRight) {
      marqueeLeft.style.transform = `translate3d(${scrollPercent * 0.1}vw, 0, 0)`;
      marqueeRight.style.transform = `translate3d(-${scrollPercent * 0.1}vw, 0, 0)`;
    }
  });

  // ======= INTERACTIVE WARPED GRID CANVAS =======
  const gridCanvas = document.getElementById('grid-interactive-canvas');
  if (gridCanvas) {
    const ctx = gridCanvas.getContext('2d');
    let width = window.innerWidth;
    let height = window.innerHeight;
    
    gridCanvas.width = width;
    gridCanvas.height = height;
    
    let mouseX = -1000;
    let mouseY = -1000;
    let targetMouseX = -1000;
    let targetMouseY = -1000;
    
    window.addEventListener('mousemove', (e) => {
      targetMouseX = e.clientX;
      targetMouseY = e.clientY;
    });
    
    document.addEventListener('mouseleave', () => {
      targetMouseX = -1000;
      targetMouseY = -1000;
    });
    
    window.addEventListener('resize', () => {
      width = window.innerWidth;
      height = window.innerHeight;
      gridCanvas.width = width;
      gridCanvas.height = height;
    });
    
    const gridSize = 80;
    const warpRadius = 150;
    const warpStrength = 36;
    const step = 8;
    
    function drawGrid() {
      ctx.clearRect(0, 0, width, height);
      
      // Interpolate mouse coordinates for fluid movement
      if (targetMouseX < 0) {
        mouseX += (targetMouseX - mouseX) * 0.1;
        mouseY += (targetMouseY - mouseY) * 0.1;
      } else {
        mouseX += (targetMouseX - mouseX) * 0.15;
        mouseY += (targetMouseY - mouseY) * 0.15;
      }
      
      ctx.lineWidth = 1;
      ctx.strokeStyle = 'rgba(255, 117, 151, 0.04)';
      
      // 1. Draw Vertical Lines
      const startX = Math.floor(-gridSize);
      const endX = Math.floor(width + gridSize);
      for (let x = startX - (startX % gridSize); x < endX; x += gridSize) {
        ctx.beginPath();
        if (Math.abs(x - mouseX) < warpRadius && mouseX > -500) {
          let drawing = false;
          for (let y = 0; y <= height + step; y += step) {
            let px = x;
            let py = y;
            const dx = px - mouseX;
            const dy = py - mouseY;
            const dist = Math.hypot(dx, dy);
            
            if (dist < warpRadius) {
              const factor = Math.sin((1 - dist / warpRadius) * Math.PI / 2);
              const push = factor * warpStrength;
              px += (dx / (dist || 1)) * push;
              py += (dy / (dist || 1)) * push;
            }
            
            if (!drawing) {
              ctx.moveTo(px, py);
              drawing = true;
            } else {
              ctx.lineTo(px, py);
            }
          }
        } else {
          ctx.moveTo(x, 0);
          ctx.lineTo(x, height);
        }
        ctx.stroke();
      }
      
      // 2. Draw Horizontal Lines
      const startY = Math.floor(-gridSize);
      const endY = Math.floor(height + gridSize);
      for (let y = startY - (startY % gridSize); y < endY; y += gridSize) {
        ctx.beginPath();
        if (Math.abs(y - mouseY) < warpRadius && mouseY > -500) {
          let drawing = false;
          for (let x = 0; x <= width + step; x += step) {
            let px = x;
            let py = y;
            const dx = px - mouseX;
            const dy = py - mouseY;
            const dist = Math.hypot(dx, dy);
            
            if (dist < warpRadius) {
              const factor = Math.sin((1 - dist / warpRadius) * Math.PI / 2);
              const push = factor * warpStrength;
              px += (dx / (dist || 1)) * push;
              py += (dy / (dist || 1)) * push;
            }
            
            if (!drawing) {
              ctx.moveTo(px, py);
              drawing = true;
            } else {
              ctx.lineTo(px, py);
            }
          }
        } else {
          ctx.moveTo(0, y);
          ctx.lineTo(width, y);
        }
        ctx.stroke();
      }
      
      // 3. Hovering wrap highlight (glass sphere effect)
      if (mouseX > -500 && mouseX < width + 500) {
        const glowRad = warpRadius;
        const grad = ctx.createRadialGradient(mouseX, mouseY, 0, mouseX, mouseY, glowRad);
        grad.addColorStop(0, 'rgba(255, 117, 151, 0.05)');
        grad.addColorStop(0.5, 'rgba(255, 117, 151, 0.015)');
        grad.addColorStop(1, 'rgba(255, 117, 151, 0)');
        
        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.arc(mouseX, mouseY, glowRad, 0, Math.PI * 2);
        ctx.fill();
        
        ctx.strokeStyle = 'rgba(255, 117, 151, 0.07)';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.arc(mouseX, mouseY, warpRadius * 0.45, 0, Math.PI * 2);
        ctx.stroke();
      }
      
      requestAnimationFrame(drawGrid);
    }
    
    drawGrid();
  }
});
