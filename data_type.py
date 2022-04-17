import random as r
import os.path as path

data_type = {
    "BEST": "Best case",
    "AVERAGE": "Average case",
    "BAD": "Bad case"
}


def generic_data(case_type, file_name, generator):
    return {"case_type": case_type, "file_name": file_name, "generator": generator}


def best_case():
    return generic_data(data_type.get("BEST"), "files/best_case.txt", generate_best_case)


def generate_best_case(number):
    return [j for j in range(number)]


def bad_case():
    return generic_data(data_type.get("BAD"), "files/bad_case.txt", generate_bad_case)


def generate_bad_case(number):
    return [j for j in range(number, 0, -1)]


def average_case():
    return generic_data(data_type.get("AVERAGE"), "files/average_case.txt", generate_average_case)


def generate_average_case(number):
    return [r.randint(0, j) for j in range(number)]


def _build_case(case, max_number=100_000, interval=10):
    with open(case.get("file_name"), "w") as f:
        for i in range(interval, max_number, 200):
            f.write((" ".join(map(str, case.get("generator")(i))) + "\n"))


def data_generator(max_number=100_000):
    _build_case(best_case(), max_number)
    _build_case(bad_case(), max_number)
    _build_case(average_case(), max_number)


def file_exist(file_name):
    return path.isfile(file_name)


def get_data(type):

    types = {
        "BEST": lambda: best_case(),
        "AVERAGE": lambda: average_case(),
        "BAD": lambda: bad_case()
    }

    if type not in types.keys():
        raise Exception("This Data type not exist")

    case = types.get(type)()

    if not file_exist(case.get("file_name")):
        _build_case(case)

    data = []
    with open(case.get("file_name")) as f:
        for line in f:
            data.append([int(v) for v in line.split()])

    return data


if __name__ == "__main__":
    for t in ["BEST", "AVERAGE", "BAD"]:
        print(get_data(t))
