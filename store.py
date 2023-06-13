from typing import List, Dict


SAVE_FOLDER = "properties/"


def filepath(agency_name: str):
    return SAVE_FOLDER + "".join(agency_name.lower().split()) + ".txt"


def save_links(agency_name: str, links: List[str]):
    saved_links = read_links(agency_name)
    with open(filepath(agency_name), "a+") as f:
        for link in links:
            if link not in saved_links:
                f.write(link + "\n")


def read_links(agency_name: str):
    try:
        return [
            line.strip()
            for line
            in open(filepath(agency_name), "r").readlines()
        ]
    except Exception:
        return []


def save_properties(properties: Dict[str, List[str]]):
    for agency, links in properties.items():
        save_links(agency, links)
