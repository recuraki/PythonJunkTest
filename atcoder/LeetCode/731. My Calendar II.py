class MyCalendarTwo:
    def __init__(self):
        self.dat = list()
        self.DoubleBooking = list()

    def book(self, start: int, end: int) -> bool:
        cnt = 0
        for a, b in self.DoubleBooking:
            if start < a < end or start < b < end:
                return False
            if a < start < b or a < end < b:
                return False
            if a == start and b == end:
                return False

        for a, b in self.dat:
            if start == a and end == b:
                self.DoubleBooking.append((max(a, start), min(b, end)))
                continue
            if start < a < end or start < b < end:
                self.DoubleBooking.append((max(a, start), min(b, end)))
                continue
            if a < start < b or a < end < b:
                self.DoubleBooking.append((max(a, start), min(b, end)))
                continue
        self.dat.append((start, end))
        return True
