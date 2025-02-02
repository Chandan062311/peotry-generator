document.addEventListener("DOMContentLoaded", function() {
  // Particle background
  particlesJS("particles-js", {
    particles: {
      number: { value: 80 },
      color: { value: "#ffffff" },
      shape: { type: "circle" },
      opacity: { value: 0.5 },
      size: { value: 3 },
      move: {
        enable: true,
        speed: 2,
        direction: "none",
        random: false,
        straight: false,
        out_mode: "out",
        bounce: false,
      }
    }
  });

  // Form submission animation
  const form = document.getElementById("promptForm");
  const submitBtn = form.querySelector("button[type='submit']");
  
  form.addEventListener("submit", function(e) {
    e.preventDefault();
    
    // Add loading state
    submitBtn.disabled = true;
    submitBtn.innerHTML = `
      <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
      Generating...
    `;

    // Simulate loading (remove in production)
    setTimeout(() => {
      this.submit();
    }, 1000);
  });

  // Typing animation for generated text
  const genText = document.getElementById("genText");
  if (genText) {
    new Typed('#generated-content', {
      strings: [genText.textContent],
      typeSpeed: 30,
      showCursor: false
    });
  }

  // Smooth scroll
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });
});