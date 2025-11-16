class Film:
    def __init__(self, title, director, year, rating):
        self.title = title
        self.director = director
        self._year = year
        self.__rating = rating

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if 0 <= value <= 10:
            self.__rating = value
        else:
            raise ValueError("Invalid rating.")

    @rating.deleter
    def rating(self):
        self.__rating = 0

class FilmLog:
    def __init__(self):
        self.__films = []

    def add(self, film):
        self.__films.append(film)

    @property
    def films(self):
        return tuple(self.__films)

log = FilmLog()
f1 = Film("Mirror", "Tarkovsky", 1979, 10)
f2 = Film("Memories of Murder", "Bong Joon-ho", 2003, 9.5)
log.add(f1)
log.add(f2)
print([(f.title, f.rating) for f in log.films])

