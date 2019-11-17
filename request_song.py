import requests
import random
import time
from models import FakePerson

AMOUNT = 150


def make_request(pause_min=20, pause_max=120):
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
        "nummer": "ARCADE+FIRE+-+THE+SUBURBS",
        "email": fake_person.email,
        "naam": fake_person.full_name,
        "motivatie": fake_person.story,
    }
    pause = random.randint(pause_min, pause_max)
    print("Pausing for {} seconds".format(pause))
    time.sleep(pause)
    print(
        "Making request as {} {} ({})\n\n{}".format(
            fake_person.first_name,
            fake_person.last_name,
            fake_person.email,
            fake_person.story,
        )
    )
    response = session.post(url=url, data=data, headers=headers)
    return response


requests_made = 0
for x in range(AMOUNT):
    requests_made += 1
    make_request()
    print("Requests made: {}".format(requests_made))
