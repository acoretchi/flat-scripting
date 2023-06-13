from agency import Agency
from requests_html import HTMLSession
from bs4 import BeautifulSoup


class DJAlexander(Agency):
    BASE_URL = "https://www.djalexander.co.uk"
    LISTINGS_URL = "https://www.djalexander.co.uk/property/to-rent/in-edinburgh/2-and-more-bedrooms/below-1500/undefined/sortby-newest"

    def name(self) -> str:
        return "DJ Alexander"

    def get_listings_html(self, page=1):
        session = HTMLSession()
        response = session.get(DJAlexander.LISTINGS_URL + f"/page-{page}")
        session.close()
        response.html.render()
        return response.html.html

    def get_listings_soup(self, page=1) -> BeautifulSoup:
        return BeautifulSoup(self.get_listings_html(page), "html.parser")

    def fetch_all_links(self):
        page = 1
        links = []
        print("Trying to fetch properties from DJ Alexander...")
        while True:
            print(f"Trying to fetch page {page}")
            soup = self.get_listings_soup(page)
            sales_imgs = soup.find_all("div", {"class": "sales-img"})
            if len(sales_imgs) > 0:
                print(f"Fetched page {page}")
                links.extend([DJAlexander.BASE_URL + img.find("a")["href"] for img in sales_imgs])
                page += 1
            else:
                break
        return links
