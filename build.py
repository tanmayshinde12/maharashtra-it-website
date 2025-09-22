#!/usr/bin/env python3
"""
Simple build script for Maharashtra IT Website
Compiles SCSS to CSS and copies files to dist folder
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

def main():
    print("🏛️  Building Maharashtra IT Website...")
    
    # Get project root
    project_root = Path(__file__).parent
    src_dir = project_root / "src"
    dist_dir = project_root / "dist"
    
    # Create dist directory if it doesn't exist (don't clean if server is running)
    dist_dir.mkdir(exist_ok=True)
    
    print("📁 Copying HTML files...")
    # Copy HTML files
    for html_file in src_dir.glob("*.html"):
        shutil.copy2(html_file, dist_dir)
    
    print("📁 Copying assets...")
    # Copy assets
    if (src_dir / "assets").exists():
        shutil.copytree(src_dir / "assets", dist_dir / "assets")
    
    print("📁 Copying JavaScript...")
    # Copy JS files
    if (src_dir / "js").exists():
        shutil.copytree(src_dir / "js", dist_dir / "js")
    
    print("🎨 Preserving existing modern CSS...")
    # Create CSS directory if it doesn't exist
    css_dir = dist_dir / "css"
    css_dir.mkdir(exist_ok=True)
    
    # Don't overwrite the existing modern CSS file
    # create_basic_css(css_dir / "main.css")  # Disabled to preserve modern styles
    
    print("✅ Build complete!")
    print(f"📂 Files are ready in: {dist_dir}")
    print("🌐 You can now serve the dist folder with any web server")

def create_basic_css(output_file):
    """Create a basic CSS file with essential styles"""
    css_content = """
/* Maharashtra IT Website - MODERN COMPILED CSS */

/* Government Brand Colors */
:root {
  --primary-orange: #FF6600;
  --primary-blue: #1E3A8A;
  --secondary-blue: #3B82F6;
  --white: #FFFFFF;
  --light-gray: #F8F9FA;
  --medium-gray: #6B7280;
  --dark-gray: #374151;
  --black: #000000;
}

/* Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 16px;
  scroll-behavior: smooth;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
  font-size: 1rem;
  line-height: 1.6;
  color: var(--dark-gray);
  background-color: var(--white);
}

.devanagari {
  font-family: 'Noto Sans Devanagari', 'Mangal', 'Kokila', sans-serif;
}

/* Container */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

/* Government Header */
.gov-header {
  background: var(--white);
  border-bottom: 3px solid var(--primary-orange);
}

.top-bar {
  background: var(--light-gray);
  padding: 0.5rem 0;
  border-bottom: 1px solid #ddd;
}

.gov-branding {
  color: var(--primary-blue);
  font-size: 0.875rem;
}

.main-header {
  padding: 1.5rem 0;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.emblem {
  width: 80px;
  height: auto;
}

.devanagari-title {
  font-size: 1.125rem;
  color: var(--dark-gray);
  margin-bottom: 0.25rem;
  display: block;
}

.english-title {
  font-size: 1.5rem;
  color: var(--primary-blue);
  font-weight: 700;
  margin: 0;
  line-height: 1.2;
}

.header-logos {
  display: flex;
  gap: 1.5rem;
  align-items: center;
}

.header-logos img {
  height: 60px;
}

/* Navigation */
.main-navigation {
  background: var(--primary-orange);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.nav-menu {
  list-style: none;
  display: flex;
  margin: 0;
  padding: 0;
}

.nav-menu > li > a {
  display: block;
  padding: 1rem 1.5rem;
  color: var(--white);
  text-decoration: none;
  font-weight: 500;
  font-size: 0.875rem;
  transition: background-color 0.3s ease;
}

.nav-menu > li > a:hover,
.nav-menu > li > a.active {
  background: rgba(0, 0, 0, 0.1);
}

/* Hero Section */
.hero-section {
  position: relative;
  height: 400px;
  overflow: hidden;
}

.hero-slider {
  position: relative;
  width: 100%;
  height: 100%;
}

.hero-slide {
  position: absolute;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  opacity: 0;
  transition: opacity 0.5s ease-in-out;
}

.hero-slide.active {
  opacity: 1;
}

.hero-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.7));
  color: var(--white);
  padding: 3rem;
}

.hero-text {
  font-size: 2rem;
  font-weight: 700;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.slider-controls {
  position: absolute;
  bottom: 1.5rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 0.5rem;
}

.slider-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.5);
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.slider-dot.active {
  background: var(--white);
}

/* Leadership Section */
.leadership-section {
  background: var(--light-gray);
  padding: 4rem 0;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 3rem;
}

.latest-news-title {
  background: var(--primary-blue);
  color: var(--white);
  padding: 1rem 2rem;
  margin: 0;
  font-size: 1.125rem;
  font-weight: 700;
  text-transform: uppercase;
}

.leadership-gallery {
  display: flex;
  justify-content: center;
  gap: 2rem;
  flex-wrap: wrap;
}

.leader-card {
  text-align: center;
  background: var(--white);
  border-radius: 1rem;
  padding: 2rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  max-width: 200px;
}

.leader-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

.leader-photo {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 1.5rem;
  border: 4px solid var(--primary-orange);
}

.leader-name {
  font-weight: 600;
  color: var(--dark-gray);
  margin-bottom: 0.5rem;
  font-size: 0.875rem;
  line-height: 1.3;
}

.leader-title {
  color: var(--medium-gray);
  font-size: 0.75rem;
  line-height: 1.4;
  margin: 0;
}

/* Content Section */
.content-section {
  background: var(--primary-blue);
  color: var(--white);
  padding: 4rem 0;
}

.about-section h2 {
  color: var(--white);
  margin-bottom: 2rem;
  font-size: 2rem;
  font-weight: 700;
}

.about-text {
  line-height: 1.7;
  margin-bottom: 2rem;
  font-size: 1rem;
}

.read-more-btn {
  background: var(--primary-orange);
  color: var(--white);
  padding: 1rem 2rem;
  text-decoration: none;
  border-radius: 0.25rem;
  font-weight: 500;
  transition: background-color 0.3s ease;
  display: inline-block;
}

.read-more-btn:hover {
  background: #e55a00;
  color: var(--white);
}

.tabs-section {
  background: var(--white);
  border-radius: 1rem;
  overflow: hidden;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

.tab-headers {
  display: flex;
  background: var(--light-gray);
}

.tab-button {
  flex: 1;
  padding: 1.5rem;
  text-align: center;
  background: var(--medium-gray);
  color: var(--white);
  border: none;
  cursor: pointer;
  font-weight: 500;
  transition: background-color 0.3s ease;
}

.tab-button:hover {
  background: #4b5563;
}

.tab-button.active {
  background: var(--white);
  color: var(--primary-blue);
}

.tab-content {
  padding: 2rem;
  min-height: 250px;
}

.tab-pane {
  display: none;
}

.tab-pane.active {
  display: block;
}

.content-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.content-list li {
  padding: 0.5rem 0;
  border-bottom: 1px solid var(--light-gray);
  color: var(--dark-gray);
  position: relative;
  padding-left: 1.5rem;
}

.content-list li:before {
  content: "▶";
  color: var(--primary-orange);
  position: absolute;
  left: 0;
  top: 0.5rem;
}

.content-list li:last-child {
  border-bottom: none;
}

/* Resources Section */
.resources-section {
  background: var(--white);
  padding: 4rem 0;
}

.resource-column h3 {
  color: var(--primary-blue);
  font-size: 1.25rem;
  margin-bottom: 2rem;
  font-weight: 600;
  border-bottom: 2px solid var(--primary-orange);
  padding-bottom: 0.5rem;
}

.resource-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.resource-list li {
  margin-bottom: 1rem;
}

.resource-list a {
  color: var(--dark-gray);
  text-decoration: none;
  line-height: 1.5;
  transition: color 0.3s ease;
}

.resource-list a:hover {
  color: var(--primary-blue);
  text-decoration: underline;
}

/* Partner Logos */
.partner-logos-section {
  background: var(--light-gray);
  padding: 3rem 0;
}

.partner-logos {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 3rem;
  flex-wrap: wrap;
}

.partner-logos img {
  height: 60px;
  max-width: 150px;
  object-fit: contain;
  filter: grayscale(100%);
  transition: filter 0.3s ease;
}

.partner-logos img:hover {
  filter: grayscale(0%);
}

/* Footer */
.site-footer {
  background: var(--dark-gray);
  color: var(--white);
  padding: 3rem 0;
}

.footer-content {
  text-align: center;
}

.footer-menu {
  margin-bottom: 2rem;
}

.footer-menu ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.footer-menu a {
  color: var(--white);
  text-decoration: none;
  font-size: 0.875rem;
}

.footer-menu a:hover {
  color: var(--primary-orange);
  text-decoration: underline;
}

.footer-info {
  margin-bottom: 2rem;
}

.footer-info p {
  margin-bottom: 0.5rem;
  font-size: 0.875rem;
}

.footer-info .ownership {
  font-weight: 600;
}

.footer-logos {
  display: flex;
  justify-content: center;
  gap: 2rem;
  align-items: center;
}

.footer-logos img {
  height: 40px;
  filter: brightness(0) invert(1);
}

/* Accessibility */
.sr-only {
  position: absolute !important;
  width: 1px !important;
  height: 1px !important;
  padding: 0 !important;
  margin: -1px !important;
  overflow: hidden !important;
  clip: rect(0, 0, 0, 0) !important;
  white-space: nowrap !important;
  border: 0 !important;
}

.accessibility-tools {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    text-align: center;
  }
  
  .logo-section {
    flex-direction: column;
    text-align: center;
  }
  
  .nav-menu {
    flex-direction: column;
  }
  
  .hero-text {
    font-size: 1.5rem;
  }
  
  .leadership-gallery {
    gap: 1rem;
  }
  
  .leader-card {
    max-width: 160px;
    padding: 1.5rem;
  }
  
  .leader-photo {
    width: 100px;
    height: 100px;
  }
  
  .partner-logos {
    gap: 1.5rem;
  }
  
  .partner-logos img {
    height: 50px;
    max-width: 120px;
  }
  
  .footer-menu ul {
    gap: 1rem;
  }
}
"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(css_content)

if __name__ == "__main__":
    main()
