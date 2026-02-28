// ===== Landing page: animated stat counters =====
document.addEventListener("DOMContentLoaded", () => {

  // Count-up animation for hero stats
  const stats = document.querySelectorAll(".stat span");
  stats.forEach(stat => {
    const raw = stat.textContent.replace(/\D/g, "");
    const target = parseInt(raw);
    if (isNaN(target)) return;
    let current = 0;
    const step = Math.ceil(target / 50);
    stat.textContent = "0";
    const interval = setInterval(() => {
      current = Math.min(current + step, target);
      stat.textContent = current + "+";
      if (current >= target) clearInterval(interval);
    }, 25);
  });

  // Scroll-reveal for cards
  const revealEls = document.querySelectorAll(".card, .feat-card");
  if (revealEls.length === 0) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.style.opacity = "1";
          entry.target.style.transform = "translateY(0)";
        }, i * 80);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  revealEls.forEach(el => {
    el.style.opacity = "0";
    el.style.transform = "translateY(24px)";
    el.style.transition = "opacity 0.5s ease, transform 0.5s ease, border-color 0.3s ease, box-shadow 0.3s ease";
    observer.observe(el);
  });

});