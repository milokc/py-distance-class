class Distance:
    def __init__(self, km):
        self.km = km

    # def instance_check(other):
    #     return other.km if isinstance(other, Distance) else other

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        other_km = other.km if isinstance(other, Distance) else other
        return Distance(
            km=self.km + other_km
        )

    def __iadd__(self, other):
        other_km = other.km if isinstance(other, Distance) else other
        self.km = self.km + other_km
        return self

    def __mul__(self, other):
        other_km = other if not isinstance(other, Distance) else None
        return Distance(km=self.km * other_km)

    def __truediv__(self, other):
        other_km = other if not isinstance(other, Distance) else None
        return Distance(km=round(self.km / other_km, 2))

    def __lt__(self, other):
        other_km = other.km if isinstance(other, Distance) else other
        return self.km < other_km

    def __gt__(self, other):
        other_km = other.km if isinstance(other, Distance) else other
        return self.km > other_km

    def __eq__(self, other):
        other_km = other.km if isinstance(other, Distance) else other
        return self.km == other_km

    def __le__(self, other):
        other_km = other.km if isinstance(other, Distance) else other
        return self.km <= other_km

    def __ge__(self, other):
        other_km = other.km if isinstance(other, Distance) else other
        return self.km >= other_km
