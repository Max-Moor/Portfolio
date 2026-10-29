# Portfolio — Max Moor

Multilingual (FR / NL / EN / DE) portfolio presented as a timeline.

- `index.html` — the site (single self-contained file)
- `mealvend-app.html`, `mealvend-site.html` — the two MealVend prototypes (also embedded in the page)
- `source/` — template (`tpl.html`), images (`img.json`) and `build.py` to regenerate `index.html`

## Added
- `og.jpg` — preview image used when the link is shared (WhatsApp, LinkedIn, mail)
- `cv/` — one-page CV in FR / NL / EN / DE (also downloadable from the page)
- `qr-portfolio.png` — QR code to print on a CV or business card
- Page URL assumed in the meta tags: https://max-moor.github.io/portfolio/ — if the repo has another name, change it in `source/tpl.html` (search `max-moor.github.io`) and run `python3 source/build.py`.
