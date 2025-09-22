// ===================================
// MAHARASHTRA IT WEBSITE - MAIN JS
// ===================================

/**
 * Main JavaScript file for Maharashtra IT Government Website
 * Handles all interactive functionality using Vanilla JavaScript ES6+
 */

class MaharashtraITWebsite {
  constructor() {
    this.init();
  }

  init() {
    // Wait for DOM to be fully loaded
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', () => {
        this.setupEventListeners();
        this.initializeComponents();
      });
    } else {
      this.setupEventListeners();
      this.initializeComponents();
    }
  }

  setupEventListeners() {
    // Mobile menu toggle
    this.setupMobileMenu();
    
    // Hero slider
    this.setupHeroSlider();
    
    // Accessibility tools
    this.setupAccessibilityTools();
    
    // Smooth scrolling for anchor links
    this.setupSmoothScrolling();
    
    // Tab functionality
    this.setupTabs();
  }

  initializeComponents() {
    // Initialize any components that need setup
    this.initializeSliders();
    this.initializeDropdowns();
  }

  // ===================================
  // MOBILE MENU FUNCTIONALITY
  // ===================================
  
  setupMobileMenu() {
    const mobileToggle = document.querySelector('.mobile-menu-toggle');
    const mainNav = document.querySelector('.main-navigation');
    
    if (mobileToggle && mainNav) {
      mobileToggle.addEventListener('click', () => {
        mainNav.classList.toggle('mobile-open');
        mobileToggle.classList.toggle('active');
      });
    }

    // Handle dropdown menus on mobile
    const dropdownToggles = document.querySelectorAll('.nav-menu > li > a[data-dropdown]');
    dropdownToggles.forEach(toggle => {
      toggle.addEventListener('click', (e) => {
        if (window.innerWidth <= 992) {
          e.preventDefault();
          const dropdown = toggle.nextElementSibling;
          if (dropdown) {
            dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
          }
        }
      });
    });
  }

  // ===================================
  // HERO SLIDER FUNCTIONALITY
  // ===================================
  
  setupHeroSlider() {
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.slider-dot');
    
    if (slides.length === 0) return;

    let currentSlide = 0;
    const slideInterval = 5000; // 5 seconds

    const showSlide = (index) => {
      // Hide all slides
      slides.forEach(slide => slide.classList.remove('active'));
      dots.forEach(dot => dot.classList.remove('active'));
      
      // Show current slide
      if (slides[index]) {
        slides[index].classList.add('active');
      }
      if (dots[index]) {
        dots[index].classList.add('active');
      }
    };

    const nextSlide = () => {
      currentSlide = (currentSlide + 1) % slides.length;
      showSlide(currentSlide);
    };

    // Auto-advance slider
    const sliderTimer = setInterval(nextSlide, slideInterval);

    // Dot click handlers
    dots.forEach((dot, index) => {
      dot.addEventListener('click', () => {
        currentSlide = index;
        showSlide(currentSlide);
        
        // Reset timer
        clearInterval(sliderTimer);
        setTimeout(() => {
          setInterval(nextSlide, slideInterval);
        }, slideInterval);
      });
    });

    // Pause on hover
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
      heroSection.addEventListener('mouseenter', () => {
        clearInterval(sliderTimer);
      });
      
      heroSection.addEventListener('mouseleave', () => {
        setInterval(nextSlide, slideInterval);
      });
    }
  }

  // ===================================
  // ACCESSIBILITY TOOLS
  // ===================================
  
  setupAccessibilityTools() {
    const accessibilityToggle = document.querySelector('.accessibility-toggle');
    const accessibilityPanel = document.querySelector('.accessibility-panel');
    
    if (accessibilityToggle && accessibilityPanel) {
      accessibilityToggle.addEventListener('click', () => {
        accessibilityPanel.classList.toggle('active');
      });
    }

    // Font size controls
    const fontSizeControls = document.querySelectorAll('[data-font-size]');
    fontSizeControls.forEach(control => {
      control.addEventListener('click', () => {
        const size = control.dataset.fontSize;
        document.documentElement.style.fontSize = size;
        
        // Update active state
        fontSizeControls.forEach(c => c.classList.remove('active'));
        control.classList.add('active');
      });
    });

    // High contrast toggle
    const contrastToggle = document.querySelector('[data-high-contrast]');
    if (contrastToggle) {
      contrastToggle.addEventListener('click', () => {
        document.body.classList.toggle('high-contrast');
        contrastToggle.classList.toggle('active');
      });
    }
  }

  // ===================================
  // SMOOTH SCROLLING
  // ===================================
  
  setupSmoothScrolling() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    
    anchorLinks.forEach(link => {
      link.addEventListener('click', (e) => {
        const targetId = link.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
          e.preventDefault();
          targetElement.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      });
    });
  }

  // ===================================
  // TAB FUNCTIONALITY
  // ===================================
  
  setupTabs() {
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabPanes = document.querySelectorAll('.tab-pane');
    
    tabButtons.forEach(button => {
      button.addEventListener('click', () => {
        const targetTab = button.dataset.tab;
        
        // Remove active class from all buttons and panes
        tabButtons.forEach(btn => btn.classList.remove('active'));
        tabPanes.forEach(pane => pane.classList.remove('active'));
        
        // Add active class to clicked button and corresponding pane
        button.classList.add('active');
        const targetPane = document.querySelector(`[data-tab-content="${targetTab}"]`);
        if (targetPane) {
          targetPane.classList.add('active');
        }
      });
    });
  }

  // ===================================
  // SLIDER INITIALIZATION
  // ===================================
  
  initializeSliders() {
    // Initialize any additional sliders (news ticker, etc.)
    const newsTicker = document.querySelector('.news-ticker-content');
    if (newsTicker) {
      // Add scrolling animation
      newsTicker.style.animationDuration = '30s';
    }
  }

  // ===================================
  // DROPDOWN INITIALIZATION
  // ===================================
  
  initializeDropdowns() {
    // Handle dropdown menus
    const dropdownTriggers = document.querySelectorAll('[data-dropdown-trigger]');
    
    dropdownTriggers.forEach(trigger => {
      const dropdown = document.querySelector(trigger.dataset.dropdownTrigger);
      
      if (dropdown) {
        trigger.addEventListener('click', (e) => {
          e.preventDefault();
          dropdown.classList.toggle('active');
        });
        
        // Close dropdown when clicking outside
        document.addEventListener('click', (e) => {
          if (!trigger.contains(e.target) && !dropdown.contains(e.target)) {
            dropdown.classList.remove('active');
          }
        });
      }
    });
  }

  // ===================================
  // UTILITY METHODS
  // ===================================
  
  // Debounce function for performance optimization
  debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  }

  // Check if element is in viewport
  isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
  }
}

// ===================================
// INITIALIZE APPLICATION
// ===================================

// Initialize the website when script loads
const maharashtraITWebsite = new MaharashtraITWebsite();

// Export for potential module usage
if (typeof module !== 'undefined' && module.exports) {
  module.exports = MaharashtraITWebsite;
}
