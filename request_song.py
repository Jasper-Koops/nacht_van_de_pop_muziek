import requests
import random
import time
from models import FakePerson

AMOUNT = 150


def make_request(pause_min=60, pause_max=180):
    """Uses spoofed headers on url """
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) "
        + "AppleWebkit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html, application/xhtml+xml,application/xml;"
        + " q=0.9,image/webp,*/*;q=0.8",
    }
    url = "https://www.ntr.nl/dynamic/nachtvandepopmuziek/aanvraag-iframe.php"
    fake_person = FakePerson()
    data = {
        "nummer": "GORILLAZ+-+STYLO+(2010)",
        "email": fake_person.email,
        "naam": fake_person.full_name,
        "motivatie": "",
    }
    pause = random.randint(pause_min, pause_max)
    print("Pausing for {} seconds".format(pause))
    time.sleep(pause)
    print(
        "Making request as {} {} ({})".format(
            fake_person.first_name, fake_person.last_name, fake_person.email
        )
    )
    response = session.post(url=url, data=data, headers=headers)
    return response


for x in range(AMOUNT):
    make_request()
