import random


class FakePerson:
    def __init__(self):
        self.first_name = self.generate_first_name()
        self.last_name = self.generate_last_name()
        self.email = self.generate_email()

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
