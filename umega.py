from agency import Agency
from typing import List
from requests_html import HTMLSession
from bs4 import BeautifulSoup


class Umega(Agency):
    LISTINGS_URL = "https://www.umega.co.uk/properties/?wpp_search%5Bsort_order%5D=ASC&wpp_search%5Bsort_by%5D=price&wpp_search%5Bpagination%5D=off&wpp_search%5Bper_page%5D=12&wpp_search%5Bstrict_search%5D=false&wpp_search%5Bproperty_type%5D=long_term_let&wpp_search%5Bsearch_furnished%5D=F&wpp_search%5Bsearch_students%5D=true&wpp_search%5Bproperty_address%5D=&wpp_search%5Brental_price%5D%5Bmin%5D=&wpp_search%5Brental_price%5D%5Bmax%5D=1400&wpp_search%5Bbedrooms%5D%5Bmin%5D=2&wpp_search%5Bbedrooms%5D%5Bmax%5D=2&wpp_search%5Bproperty_county%5D=-1"

    def name(self):
        return "Umega"

    def get_listings_html(self):
        session = HTMLSession()
        response = session.get(Umega.LISTINGS_URL)
        session.close()
        response.html.render()
        return response.html.html

    def get_listings_soup(self) -> BeautifulSoup:
        return BeautifulSoup(self.get_listings_html(), "html.parser")

    def fetch_all_links(self) -> List[str]:
        soup = self.get_listings_soup()
        property_imgs = soup.find_all("a", {"class": "property-image-link"})
        return [img["href"] for img in property_imgs]
