class Time:

    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0

        return Time.get_time(self)


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 9)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
time = Time(00, 00, 59)
print(time.next_second())

# for h in range(0, 24):
#     for m in range(0, 60):
#         for s in range(0, 60):
#             time = Time(h, m, s)
#             print(time.next_second())
