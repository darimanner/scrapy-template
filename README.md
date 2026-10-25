# scrapy-template

[Copier](https://copier.readthedocs.io/) template for [Scrapy](https://scrapy.org/) projects on Python 3.14, managed with [uv](https://docs.astral.sh/uv/).

## What you get

- Scrapy project with `src/` as the project package and polite default settings
- an example spider using the async `start()` API, with a dataclass item
- a parse test that runs against a static HTML response, no network needed
- `pyproject.toml` with project metadata, dev dependencies, pytest and ruff config
- `uv.lock`, `.python-version` pinned to 3.14 and `.pre-commit-config.yaml`

## Usage

```bash
uvx copier copy gh:darimanner/scrapy-template my-scraper
cd my-scraper
uv sync
uv run scrapy crawl quotes -O quotes.jsonl
```

Copier asks for the project name, description and author. To pull later template changes into a generated project, run `uvx copier update` inside it.

## Generated layout

```
my-scraper/
  src/
    spiders/quotes.py
    items.py
    settings.py
  tests/test_quotes.py
  .pre-commit-config.yaml
  .python-version
  pyproject.toml
  scrapy.cfg
  uv.lock
```
