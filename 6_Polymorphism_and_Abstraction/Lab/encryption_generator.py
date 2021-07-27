class EncryptionGenerator:
    def __init__(self, text: str):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")

        encrypted = ""

        for char in self.text:
            encrypted_char = ord(char) + other
            while encrypted_char < 32:
                encrypted_char += 95  # 95 -> difference between start and end allowed ascii
            while encrypted_char > 126:
                encrypted_char -= 95
            encrypted += chr(encrypted_char)

        return encrypted



