class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you", "Nie chcę zostać pozwany", "Więc tutaj przerwę."])

bulls_on_parade = Song(["They rally around tha family"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
isinstance([])
print(isinstance)