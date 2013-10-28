from storage import Storage
from json_decoder import JSONDecoder
import json

class StaticStorage(Storage):
    """Simple implementation using the static courses.json file created by Scrapy.
    """

    def __init__(self, file_to_use = 'scraper/courses.json'):
        self.departments = {}
        json_file = open(file_to_use)
        json_data = json.load(json_file)
        json_file.close()
        self._load_departments(json_data)

    def _load_departments(self, json_data):
        decoder = JSONDecoder()
        courses = decoder.decode_courses(json_data)

        for course in courses:
            if course.department not in self.departments:
                self.departments[course.department.code] = course.department
            department = self.departments[course.department.code]
            department.add_course(course)

    def list_departments(self):
        return self.departments.values()

    def find_department_by_code(self, code):
        return self.departments.get(code)

    def list_all_courses(self, department_code = None):
        all_courses = []
        for department in self.departments.values():
            all_courses.extend(department.courses)
        return all_courses

    def last_update_date(self):
        # TODO: check the creation date of courses.json file
        raise Exception('Not implemented yet.')

    def store_course_base(self, course_json):
        raise Exception('Not implemented.')