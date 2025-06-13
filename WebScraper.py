import requests
from bs4 import BeautifulSoup
import csv
import time


NUM_PAGES = 2
BASE_URL = "https://www.python.org"
machine_learning_jobs = []

def get_response_from_url(page_number):
    url = f"{BASE_URL}/jobs/?page={page_number}"
    http_response = requests.get(url)

    if http_response.status_code != 200:
        raise Exception(f"Failed to retrieve page {http_response}. Status code: {http_response.status_code}")

    return http_response

def get_all_machine_learning_job_html_elements(http_response):
    soup = BeautifulSoup(http_response.content, "html.parser")

    job_ol_element = soup.find("ol", class_="list-recent-jobs list-row-container menu")
    all_jobs_span_elements = job_ol_element.find_all("span", class_="listing-job-type")
    all_machine_learning_jobs_span_elements = [element for element in all_jobs_span_elements
                                                        if "machine learning" in element.get_text().lower()]

    return [element.parent for element in all_machine_learning_jobs_span_elements]

def extract_jobs_info_from_html_elements(all_machine_learning_info_li_elements):
    for job_li_element in all_machine_learning_info_li_elements:
        machine_learning_job = {"job_title": job_li_element.find("span",
                                                                 class_="listing-company-name").a.string.strip(),
                                "link_url": BASE_URL + job_li_element.find(
                                    "span",
                                    class_="listing-company-name").a["href"],
                                "company_name": job_li_element.find("span",
                                                                    class_="listing-company-name").contents[-1].strip(),
                                "location": job_li_element.find("span",
                                                                class_="listing-location").a.text.strip(),
                                "looking_for": job_li_element.find("span",
                                                                   class_="listing-job-type").get_text().strip(),
                                "date_posted": job_li_element.find("span",
                                                                   class_="listing-posted").time.text.strip(),
                                "category": job_li_element.find("span",
                                                                class_="listing-company-category").a.text.strip()}

        machine_learning_jobs.append(machine_learning_job)

def get_machine_learning_jobs():
    for page_number in range(1, NUM_PAGES + 1):
        response = get_response_from_url(page_number)
        
        all_machine_learning_info_li_elements = get_all_machine_learning_job_html_elements(response)
        extract_jobs_info_from_html_elements(all_machine_learning_info_li_elements)

        time.sleep(2)  # Sleep to not hit the website too hard

def save_to_csv(jobs, filename="machine_learning_jobs.csv"):
    with open(filename, mode="w", encoding="utf-8") as csv_file:
        fieldnames = ["job_title", "link_url", "company_name", "location", "looking_for", "date_posted", "category"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for machine_learning_job in jobs:
             writer.writerow(machine_learning_job)

    print(f"Saved {len(jobs)} URLs to '{filename}'")

if __name__ == "__main__":
    get_machine_learning_jobs()
    save_to_csv(machine_learning_jobs)