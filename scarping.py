import csv

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
OUTPUT_FILE = "fake_jobs.csv"
FIELDS = ["Job Title", "Company Name", "Location", "Job Detail Page URL"]


def fetch_page(url: str) -> BeautifulSoup:
    """Download the page and return it as a parsed BeautifulSoup object."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def parse_job(card) -> dict:
    """Extract the four fields from a single job card."""
    return {
        "Job Title": card.find("h2", class_="title").get_text(strip=True),
        "Company Name": card.find("h3", class_="company").get_text(strip=True),
        "Location": card.find("p", class_="location").get_text(strip=True),
        "Job Detail Page URL": card.find("a", string="Apply")["href"],
    }


def save_to_csv(jobs: list[dict], filename: str) -> None:
    """Write the job records to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(jobs)


def main() -> None:
    soup = fetch_page(URL)
    cards = soup.find_all("div", class_="card-content")
    jobs = [parse_job(card) for card in cards]
    save_to_csv(jobs, OUTPUT_FILE)
    print(f"Saved {len(jobs)} jobs to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()