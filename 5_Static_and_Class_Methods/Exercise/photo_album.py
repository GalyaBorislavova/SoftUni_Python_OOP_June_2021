class PhotoAlbum:
    PHOTO_MARK = "[]"

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for r in range(self.pages)]
        self.empty_album = [[""] * 4 for _ in range(pages)]
        self.capacity = pages * 4

    @classmethod
    def from_photos_count(cls, photos_count):
        number_of_pages = photos_count // 4
        if photos_count % 4 != 0:
            number_of_pages += 1
        return cls(number_of_pages)

    def add_photo(self, label: str):
        check_for_empty_space = \
            [(r, c) for r in range(self.pages) for c in range(len(self.empty_album[r])) if
             self.empty_album[r][c] == ""]
        if check_for_empty_space:
            empty_space = check_for_empty_space[0]
            self.photos[empty_space[0]].append(f"{label}")
            self.empty_album[empty_space[0]][empty_space[1]] = PhotoAlbum.PHOTO_MARK
            return f"{label} photo added successfully on page {empty_space[0] + 1} slot {empty_space[1] + 1}"
        return "No more free slots"

    def display(self):
        dashes = "-" * 11
        separator_pages = f"\n{dashes}\n"
        pages = f'{separator_pages}'.join([' '.join([el.strip() for el in row if el != ""]) for row in self.empty_album])
        return dashes + "\n" + pages + "\n" + dashes


if __name__ == "__main__":
    import unittest


    class TestsPhotoAlbum(unittest.TestCase):
        def test_init_creates_all_attributes(self):
            album = PhotoAlbum(2)
            self.assertEqual(album.pages, 2)
            self.assertEqual(album.photos, [[], []])

        def test_from_photos_should_create_instace(self):
            album = PhotoAlbum.from_photos_count(12)
            self.assertEqual(album.pages, 3)
            self.assertEqual(album.photos, [[], [], []])

        def test_add_photo_with_no_free_spots(self):
            album = PhotoAlbum(1)
            album.add_photo("baby")
            album.add_photo("first grade")
            album.add_photo("eight grade")
            album.add_photo("party with friends")
            result = album.add_photo("prom")
            self.assertEqual(result, "No more free slots")

        def test_add_photo_with_free_spots(self):
            album = PhotoAlbum(1)
            album.add_photo("baby")
            album.add_photo("first grade")
            album.add_photo("eight grade")
            album.add_photo("party with friends")
            self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])

        def test_display_with_one_page(self):
            album = PhotoAlbum(1)
            album.add_photo("baby")
            album.add_photo("first grade")
            album.add_photo("eight grade")
            album.add_photo("party with friends")
            result = album.display().strip()
            self.assertEqual(result, "-----------\n[] [] [] []\n-----------")

        def test_display_with_three_pages(self):
            album = PhotoAlbum(3)
            for _ in range(8):
                album.add_photo("asdf")
            result = album.display().strip()
            self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------")


    if __name__ == "__main__":
        unittest.main()

    album = PhotoAlbum(2)

    print(album.add_photo("baby"))
    print(album.add_photo("first grade"))
    print(album.add_photo("eight grade"))
    print(album.add_photo("party with friends"))
    print(album.photos)
    print(album.add_photo("prom"))
    print(album.add_photo("wedding"))

    print(album.display())