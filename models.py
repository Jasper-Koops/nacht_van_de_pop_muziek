import random


class FakePerson:
    def __init__(self):
        self.first_name = self.generate_first_name()
        self.last_name = self.generate_last_name()
        self.email = self.generate_email()
        self.story = self.generate_story("Arcade Fire")

    def generate_story(self, artist):
        praises = [
            "fantastisch",
            "geweldig",
            "heerlijk",
            "heel erg fijn",
            "awesome",
            "dijk van",
            "ongelooflijk lekker",
            "ongelooflijk",
        ]
        opening = "Wat een {} nummer! ".format(random.choice(praises))

        what = [
            "soundtrack",
            "achtergrondmuziek",
            "muziek",
            "herinnering",
            "een terugreis",
            "een greep uit",
            "ultieme herinnering aan",
            "reden dat ik nog altijd van deze band houd",
            "oorzaak",
        ]
        of_what = [
            "studententijd.",
            "huwelijk.",
            "vakantie.",
            "huwelijksreis.",
            "Eerste dans als getrouwd stel.",
            "van mijn zomergevoel.",
            "blijde stemming, elke keer opnieuw."
        ]

        middle = "De {} van mijn {}".format(
            random.choice(what), random.choice(of_what)
        )
        finishers = [
            "weten mij hier nog steeds naar terug te brengen",
            "hebben zichzelf hierna nooit meer overtroffen",
            "hebben hun niveau nooit meer gehaald",
            "laten hiermee horen wat ze kunnen",
            "krijgen bij mij thuis nog steeds de voeten van de vloer bij mij thuis",
            ", man! Ik kan geen genoeg van ze krijgen!",
            "Wat een helden!",
            "Heb hierop m'n toenmalige vriendin en nu vrouw ten huwelijk gevraagd.",
            "Nummer draaide na geboorte kind",
            "Kan niet wachten om volume omhoog te gooien en lekker los te gaan op deze geweldige plaat!",
        ]
        closing_statement = "De {} {}".format(artist, random.choice(finishers))

        end_choices = [
            "Dit nummer mag zeker niet ontbreken!",
            "Rock on!",
            "Geweldig!",
            "Een geweldig nummer van een gouden plaat!",
            "Kom er maar in!",
            "Ik blijf hem nog eeuwen draaien!",
            "Een klassieker!",
            "Dit lied brengt me hier altijd naar terug.",
        ]
        return (
            opening
            + " "
            + middle
            + " "
            + closing_statement
            + " "
            + random.choice(end_choices)
        )

    def generate_first_name(self):
        with open("first_names") as f:
            content = f.readlines()
        list_of_names = [x.strip() for x in content]
        return random.choice(list_of_names)

    def generate_last_name(self):
        with open("last_names") as f:
            content = f.readlines()
        list_of_names = [x.strip() for x in content]
        return random.choice(list_of_names)

    def generate_email(self):
        method = ["fullnames", "full_letter", "letter_full"]
        email_providers = ["@gmail.com", "@hotmail.com", "@icloud.com"]
        used_last_name = self.last_name
        if random.random() > 0.5:
            used_last_name = self.last_name + str(random.randint(50, 90))

        chosen_method = random.choice(method)
        if chosen_method == "fullnames":
            return "{}{}{}".format(
                self.first_name, used_last_name, random.choice(email_providers)
            )
        elif chosen_method == "full_letter":
            return "{}{}{}".format(
                self.first_name,
                used_last_name[0],
                random.choice(email_providers),
            )
        elif chosen_method == "letter_full":
            return "{}{}{}".format(
                self.first_name[0],
                used_last_name,
                random.choice(email_providers),
            )

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
