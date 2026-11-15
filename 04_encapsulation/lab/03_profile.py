class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 > len(value) or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_eight_chars_long = len(value) >= 8
        have_one_upper_letter = any([char.isupper() for char in value])
        have_at_least_one_digit = any([char.isdigit() for char in value])

        if not (is_eight_chars_long and have_one_upper_letter and have_at_least_one_digit):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
