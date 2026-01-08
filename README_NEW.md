# Jonathan Shulgach - Personal Website

A professional academic portfolio website built with Jekyll and the [minimal-mistakes](https://mmistakes.github.io/minimal-mistakes/) theme.

🌐 **Live Site**: [jshulgach.github.io](https://jshulgach.github.io)

## Features

- 🌙 **Dark Theme**: Easy on the eyes, professional look
- 📱 **Responsive**: Looks great on all devices
- 🔍 **SEO Optimized**: Built-in meta tags and sitemap
- 📊 **Project Portfolio**: Showcase of 9 featured projects
- 📚 **Publications**: Academic papers and presentations
- 🤝 **Outreach**: STEM education and community involvement

## Structure

```
├── _config.yml          # Site configuration
├── _data/
│   └── navigation.yml   # Navigation menu
├── _pages/
│   ├── about.md         # About me page
│   ├── contact.md       # Contact information
│   ├── outreach.md      # Community activities
│   ├── projects.md      # Project gallery
│   └── publications.md  # Academic publications
├── _projects/           # Individual project pages
├── _sass/
│   └── _custom.scss     # Custom styling
├── assets/
│   ├── css/
│   └── img/
├── index.md             # Homepage
└── Gemfile              # Ruby dependencies
```

## Local Development

### Prerequisites
- Ruby 2.7+
- Bundler (`gem install bundler`)

### Setup
```bash
# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve

# Visit http://localhost:4000
```

## Customization

### Colors
Edit `_sass/_custom.scss` to change the color scheme:
```scss
$primary-color: #1abc9c;      // Main accent color
$background-color: #1a1a2e;   // Page background
```

### Navigation
Edit `_data/navigation.yml` to add/remove menu items.

### Adding a Project
1. Create a new file in `_projects/` (e.g., `my-project.md`)
2. Add front matter with title, excerpt, teaser image
3. Write your project description in Markdown

## Deployment

This site is automatically deployed via GitHub Pages when you push to the `main` branch.

## To-Do

- [ ] Add real photo to replace AI avatar
- [ ] Update Google Scholar ID in _config.yml
- [ ] Add actual publication entries
- [ ] Review and personalize all project descriptions

## Credits

- Theme: [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) by Michael Rose
- Icons: [Font Awesome](https://fontawesome.com/)
- Fonts: [Google Fonts](https://fonts.google.com/) (Montserrat, Lato)

## License

Content © Jonathan Shulgach. Theme licensed under MIT.
