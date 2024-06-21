# Alamy Scraper

Scrapes image URLs from Alamy. The images are the zoomed in previews. 

## Usage

### Clone the repo

```
git clone https://github.com/KhoalaS/alamy-scraper.git
```

Or download as a [Zip file](https://github.com/KhoalaS/alamy-scraper/archive/refs/heads/main.zip) and extract it.


Then change to the repos directory

```
cd alamy-scraper
```

---

### Set up a Venv (Optional)

__Linux__
```bash
python3 -m venv .venv
source .venv/bin/activate
```

__Windows__
```shell
python -m venv .venv
.venv\Scripts\activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Run the Script

```bash
usage: Alamy downloader [-h] [-t T] FILE OUTPUT_DIR

positional arguments:
  FILE        file with links to download
  OUTPUT_DIR  output directory

options:
  -h, --help  show this help message and exit
  -t T        delay in seconds between downloads, default is 1 second
```

__Examples__

```
python main.py images.txt out
```

---

No delay between downloads
```
python -t 0 main.py images.txt out
```