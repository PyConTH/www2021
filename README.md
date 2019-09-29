Building the PyCon Thailand 2020 website

<!-- Markdown snippet -->
[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/pyconth/www2020)

## Local development

### Install pelican

```
pip install pelican
pip install Markdown
```

### Clone the repo and start a site

```
git clone www2020
cd www2020
pelican-quickstart
```

### Fork the `elegant` theme, clone it, rename the repo, and symlink the fork

```
cd ..
git clone https://github.com/PyConTH/www2020-elegant.git
pelican-themes --symlink www2020-elegant
```

Specify `THEME = 'www2020-elegant'` in `pelicanconf.py`

TODO

- Setup content sync from Notion.
- Setup automatic sync.
