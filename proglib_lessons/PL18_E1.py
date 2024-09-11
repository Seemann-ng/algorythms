import random
from typing import List


class MusicAlbum:
    def __init__(self, title: str, artist: str, release_year: int, genre: str, tracklist: List[str]):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist

    def playRandomTrack(self):
        """

        Returns:

        """
        track_number = random.randrange(1, len(self.tracklist))
        print(f"Track #{track_number + 1}: \"{self.tracklist[track_number]}\" is playing.")

    def platTrack(self, track_number: int):
        print(f"Track #{track_number}: \"{self.tracklist[track_number - 1]}\" is playing.")


album4 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue deutsche Härte",
                    ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex",
                     "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo", "Hallomann"])

print(f"""Album title: {album4.title}
      \nArtist: {album4.artist}
      \nRelease year: {album4.release_year}
      \nGenre: {album4.genre}
      \nTracks: {album4.tracklist}""")
album4.playRandomTrack()
while True:
    try:
        track_num = int(input("Choose the track number: "))
        if not track_num :
            raise IndexError
        album4.platTrack(track_num)
        break
    except IndexError:
        print("There is no such track.")
