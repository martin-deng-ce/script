from jiekou.add import add_school
import requests
import random
s = requests.session()


def test_add_school_success():
    name = random.randint(100, 10000)
    result = add_school(name, 2, 1, "test")
    return result

def test_add_school_remark_null():
    name = random.randint(100, 10000)
    result = add_school(name, 2, 1, "")
    return result


def test_add_school_name_null():
    result = add_school("", 2, 1, "test")
    return result

if __name__ == '__main__':
    name = random.randint(100, 10000)
    result = test_add_school_success()
    print(result.text)
