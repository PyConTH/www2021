# Building the PyCon Thailand 2020 website

<!-- Markdown snippet -->
[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/pyconth/www2020)

Deploying to https://th.pycon.org/

## Local development

### Install pelican

```bash
pip install pelican
pip install Markdown
```

### Clone the repo and start a site

```bash
git clone www2020
cd www2020
# pelican-quickstart # Only necessary the first time, already done
```

### Specify the theme to use

```bash
pelican-themes --symlink theme
```

Specify `THEME = 'theme'` in `pelicanconf.py`

## Content editing

Create posts (listed chronologically) in Markdown format in `./content/`.
Create pages (about, programme, etc.) in `./content/pages/`.
Translations are specified using the `lang` metadata, see
[Translations](https://docs.getpelican.com/en/stable/content.html#translations)
for details.

----

# Syncing content from Notion

This is work in progress, the building blocks are there but I haven't completed
the config (API token, pages in Notion).

Content that is maintained in Notion doesn't need to be committed to git. 
In fact, committing it to git would probably just confuse things. 
So commit special pages, such as e.g. the frontpage if it has special layout,
as e.g. `./content/pages/frontpage.html` and enlist developer support in
updating it.

In order to retrieve pages from Notion on your machine, install the API
and configure the API key:

```bash
pip install --user notion
export NOTION_BLOG_POSTS_PAGE=https://www.notion.so/pyconth/News-08d5aa2f573348e1b96671488947f997
export NOTION_TOKEN=...
```

Grab the API key from your browser session (see https://github.com/jamalex/notion-py#quickstart).


----

TODO

- Setup automatic sync.
