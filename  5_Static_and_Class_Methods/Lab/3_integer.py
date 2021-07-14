def romanToInt(s):
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        number += translations[char]
    return number


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(int(float_value))
        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        return cls(romanToInt(value))

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            try:
                string_to_int = int(value)
                if isinstance(string_to_int, int):
                    return cls(string_to_int)
            except Exception:
                return "wrong type"
        return "wrong type"


if __name__ == "__main__":
    first_num = Integer(10)
    second_num = Integer.from_roman("IV")

    print(Integer.from_float("2.6"))
    print(Integer.from_string(2.6))

