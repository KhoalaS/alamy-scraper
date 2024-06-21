# Alamy Scraper

Scrapes image URLs from Alamy. The images are the zoomed in previews. 

## Usage

### Set up a Venv (Optional)

__Linux__
```bash
python3 -m venv .venv
source .venv/bin/activate.fish
```

__Windows__
```shell
python -m venv .venv
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Script

__Usage__

```bash
usage: Alamy downloader [-h] FILE OUTPUT_DIR

positional arguments:
  FILE        file with links to download
  OUTPUT_DIR  output directory

options:
  -h, --help  show this help message and exit
```

__Example__

```
python main.py images.txt out
```
