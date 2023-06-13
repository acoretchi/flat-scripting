from send_email import send_property_alert
from store import save_properties
from dj_alexander import DJAlexander
from umega import Umega
from elc import ELC


if __name__ == "__main__":
    agencies = [
        DJAlexander(),
        Umega(),
        ELC(),
    ]

    new_properties = {
        agency.name(): agency.get_new_links() for agency in agencies
    }
    print("Sending an email alert")
    send_property_alert(new_properties)
    print("Saving new properties")
    save_properties(new_properties)
