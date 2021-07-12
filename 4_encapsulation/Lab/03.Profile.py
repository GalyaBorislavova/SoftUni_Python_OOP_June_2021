class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    def is_valid_length(self, password: str):
        return len(password) >= 8

    def contains_digit(self, password: str):
        digits = [letter for letter in password if letter.isdigit()]
        return True if digits else False

    def contains_uppercase(self, password: str):
        uppercase = [letter for letter in password if letter.isupper()]
        return True if uppercase else False

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.is_valid_length(value) and self.contains_uppercase(value) and self.contains_digit(value):
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        secret_pass = len(self.password) * "*"
        return f'You have a profile with username: "{self.username}" and password: {secret_pass}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
