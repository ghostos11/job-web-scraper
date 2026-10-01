# Jobs Scraper

A small Python web scraper that collects job listings from the
[Real Python Fake Jobs](https://realpython.github.io/fake-jobs/) practice site
and saves them to a clean CSV file.

The target site is a sandbox built for learning web scraping, so it is safe to
scrape and all of the data is fictional.

## What it collects

For each of the 100 job postings, the scraper extracts:

| Column | Description | Example |
|---|---|---|
| Job Title | Name of the position | Senior Python Developer |
| Company Name | Hiring company | Payne, Roberts and Davis |
| Location | City and state code | Stewartbury, AA |
| Job Detail Page URL | Link to the job's "Apply" page | https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html |

## Requirements

- Python 3.9 or newer
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

Install the dependencies:

```bash
pip install requests beautifulsoup4
```

## Usage

```bash
python scrape_jobs.py
```

The script downloads the page, parses every job card, and writes the results to
`fake_jobs.csv` in the same folder.

## How it works

The code is split into small functions, each with one responsibility:

| Function | Purpose |
|---|---|
| `fetch_page(url)` | Downloads the page and returns parsed HTML |
| `parse_job(card)` | Extracts the four fields from one job card |
| `save_to_csv(jobs, filename)` | Writes the records to a CSV file |
| `main()` | Runs the steps in order |

## Output

`fake_jobs.csv` contains 100 rows and 4 columns:

```csv
Job Title,Company Name,Location,Job Detail Page URL
Senior Python Developer,"Payne, Roberts and Davis","Stewartbury, AA",https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html
Energy engineer,Vasquez-Davidson,"Christopherville, AA",https://realpython.github.io/fake-jobs/jobs/energy-engineer-1.html
```

## Data quality notes

- No missing values, empty strings, or duplicate rows.
- All columns are text (strings).
- Some job titles repeat (for example "Python Programmer (Entry-Level)"), but each
  posting has a different company and location.
- Location state codes are only `AA`, `AE`, and `AP`, which comes from the
  site's data generator and does not represent real places.

## Possible improvements

- Split `Location` into separate `City` and `State` columns.
- Add a flag for Python-related jobs.
- Export to Excel in addition to CSV.
- Scrape the full description from each job detail page.

## project url
https://roadmap.sh/projects/job-listings-scraper
