from typing import List
from store import read_links
import abc


class Agency(abc.ABC):

    @abc.abstractmethod
    def fetch_all_links(self) -> List[str]:
        """ Get full links to all relevant properties from the agency. """
        pass

    @abc.abstractmethod
    def name(self) -> str:
        """ Get the name of the agency. """
        pass

    def get_new_links(self) -> List[str]:
        saved_links = set(read_links(self.name()))
        print(f"Trying to fetch new properties from {self.name()}")
        fetched_links = set(self.fetch_all_links())
        print(fetched_links)
        print(f"Successfully fetched {len(fetched_links)} new properties from {self.name()}")
        return list(fetched_links - saved_links)
