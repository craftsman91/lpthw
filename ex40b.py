class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
    
    def happy_bday(self):
        print("Happy birthday to you",
              "Nie chcę zostać pozwany",
              "Więc tutaj przerwę.")


bulls_on_parade = Song(["They rally around tha family"])

piosenka = Song()
piosenka.happy_bday()

bulls_on_parade.sing_me_a_song()