import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='urllib3')
warnings.filterwarnings("ignore", category=ImportWarning, module='urllib3')
warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL 1.1.1+")

import requests
from bs4 import BeautifulSoup

url = "Colocapaginaaca"

if "__main__" == __name__:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    def has_data_search(tag):
        return tag.has_attr("data-search-sol-meta")

    results = soup.find_all(has_data_search)

    for job in results:
        try:
            title = job.find("a", attrs={"data-automation": "jobTitle"}).get_text()
            company = job.find("a", attrs={"data-automation": "JobCompany"}).get_text()
            joblink = "Colocapaginaaca" + job.find("a", attrs={"data-automation": "jobTitle"})["href"]

            job = "Titulo: {}\nEmpresa: {}\nLink: {}a\n"

            job = job.format(title, company, joblink)

            print(job)
        except Exception as e:
            print("Exception: {}".format(e))
            pass
