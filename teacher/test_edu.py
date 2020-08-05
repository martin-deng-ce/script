import unittest
import requests
import random
s = requests.session()
from interface.school import School


class TestAdd(unittest.TestCase):
    def setUp(self):
        self.l = School(s)
        self.l.login("admin", "660B8D2D5359FF6F94F8D3345698F88C")

    def test_add_success(self):
        name = random.randint(10000, 10000000)
        r = self.l.add(name)
        return r

    def test_add_name_null(self):
        name = random.randint(10000, 10000000)
        r = self.l.add("")
        return r

    def tes1t_add_type_error(self):
        pass

    def test_add_remark_null(self):
        pass


if __name__ == '__main__':
    unittest.main()