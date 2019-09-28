Building the PyCon Thailand 2020 website

## Install pelican

```
pip install pelican
pip install Markdown
```

## Clone the repo and start a site

```
git clone www2020
cd www2020
pelican-quickstart
```

## Fork the `elegant` theme, clone it, and symlink the fork

```
cd ..
git clone https://github.com/PyConTH/elegant.git
pelican-themes --symlink elegant
```

Specify `THEME = 'elegant'` in `pelicanconf.py`

TODO

- Rename the 'elegant' theme.
- Setup deploy to Netlify.
- Setup content sync from Notion.
- Setup automatic sync.
