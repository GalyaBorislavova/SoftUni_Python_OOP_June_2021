from song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        if songs:
            self.songs = list(songs)
        else:
            self.songs = []
        self.published = False

    def add_song(self, new_song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        if new_song.single:
            return f"Cannot add {new_song.name}. It's a single"
        for s in self.songs:
            if s.name == new_song.name:
                return "Song is already in the album."

        self.songs.append(new_song)
        return f"Song {new_song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        for s in self.songs:
            if s.name == song_name:
                self.songs.remove(s)
                return f"Removed song {s.name} from album {self.name}."

        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        songs_details = [f"== {Song.get_info(s)}" for s in self.songs]
        return f"Album {self.name}" + "\n" + "\n".join(songs_details)
