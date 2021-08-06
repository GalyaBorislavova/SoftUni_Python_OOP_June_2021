from project.student import Student

from unittest import TestCase, main


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Ivan")

    def test_student_init_method_only_with_name(self):
        student = Student("Ivan")
        self.assertEqual("Ivan", student.name)
        self.assertEqual({}, student.courses)

    def test_student_init_method_with_course(self):
        student = Student("Ivan", {"Python": ["note1"]})
        self.assertEqual("Ivan", student.name)
        self.assertEqual({"Python": ["note1"]}, student.courses)

    def test_student_init_method_none_course(self):
        student = Student("Ivan", None)
        self.assertEqual("Ivan", student.name)
        self.assertEqual({}, student.courses)

    def test_enroll_exist_course_extend_notes(self):
        self.student.courses = {"Python": ["note1"]}
        result = self.student.enroll("Python", ["note2"])
        self.assertEqual({"Python": ["note1", "note2"]}, self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_exist_course_extend_with_new_notes(self):
        self.student.courses = {"Python": []}
        result = self.student.enroll("Python", ["note1"], add_course_notes="N")
        self.assertEqual({"Python": ["note1"]}, self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_new_course_with_notes_Y(self):
        result = self.student.enroll("Python", ["note1", "note2", "note3"], add_course_notes="Y")
        self.assertEqual({"Python": ["note1", "note2", "note3"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_new_course_with_notes(self):
        result = self.student.enroll("Python", ["note1", "note2", "note3"], add_course_notes="")
        self.assertEqual({"Python": ["note1", "note2", "note3"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_new_course_without_notes(self):
        result = self.student.enroll("Python", [], add_course_notes="N")
        self.assertEqual({"Python": []}, self.student.courses)
        self.assertEqual("Course has been added.", result)

    def test_enroll_new_course_without_notes_with_note(self):
        result = self.student.enroll("Python", ["note1"], add_course_notes="N")
        self.assertEqual({"Python": []}, self.student.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_update_notes_on_exist_course(self):
        self.student.courses = {"Python": ["note1"]}
        result = self.student.add_notes("Python", "note2")
        self.assertEqual({"Python": ["note1", "note2"]}, self.student.courses)
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_with_not_exist_course_raises(self):
        self.assertEqual({}, self.student.courses)
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Python", ["note1"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_with_exist_course(self):
        self.student.courses = {"Python": ["note1"]}
        self.assertEqual({"Python": ["note1"]}, self.student.courses)
        result = self.student.leave_course("Python")
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_with_not_exist_course_raises(self):
        self.assertEqual({}, self.student.courses)
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Python")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()