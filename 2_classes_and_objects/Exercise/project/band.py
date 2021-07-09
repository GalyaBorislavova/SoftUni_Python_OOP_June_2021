from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, new_album: Album):
        for a in self.albums:
            if a.name == new_album.name:
                return f"Band {self.name} already has {new_album.name} in their library."
        self.albums.append(new_album)
        return f"Band {self.name} has added their newest album {new_album.name}."

    def remove_album(self, album_name: str):
        for a in self.albums:
            if a.name == album_name:
                if a.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(a)
                return f"Album {a.name} has been removed."

        return f"Album {album_name} is not found."

    def details(self):
        band_data = [Album.details(a) for a in self.albums]
        return f"Band {self.name}" + "\n" + '\n'.join(band_data)


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
