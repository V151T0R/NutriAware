# 🍏 NutriAware

NutriAware is a modern, responsive web application built with Django using server-side rendering. It's a dedicated platform for publishing, reading, and managing articles centered on nutritional science, holistic health, and dietary wellness.

## Demonstration

![NutriAware Demo](demo/demo.gif)

---

## Key Features

* **Dynamic Theme Toggling:** Switch effortlessly between a sleek charcoal Dark Mode and a clean Light Mode. Your preference is saved locally so it carries over across sessions.
* **Responsive CSS Grid:** Articles appear in a modern, card-based grid that adjusts automatically for desktop, tablet, and mobile screens.
* **Full CRUD Functionality:**
    * View detailed articles rendered dynamically from the database.
    * Add new posts via a secure, styled form.
    * Remove posts securely through POST requests, with JavaScript confirmation prompts guarding against accidental deletion.
* **Modern UI/UX:** Crafted with raw CSS variables, flexbox, and the Poppins font family — delivering a lightweight, fast, and polished interface without heavy external CSS frameworks.

---

## Tech Stack

* **Backend:** Python 3, Django 6.x
* **Frontend:** HTML5, Native CSS3 (CSS Variables, Flexbox, Grid), Vanilla JavaScript
* **Database:** SQLite (Default Django setup)
