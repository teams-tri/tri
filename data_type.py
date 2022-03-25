import random as r

data_type = {
    "BEST": "Best case",
    "AVERAGE": "Average case",
    "BAD": "Bad case"
}


def generic_data(case_type, file_name):
    return {"case_type": case_type, "file_name": file_name}


def best_case():
    return generic_data(data_type.get("BEST"), "files/best_case.txt")


def generate_best_case(number):
    return [j for j in range(number)]


def bad_case():
    return generic_data(data_type.get("BAD"), "files/bad_case.txt")


def generate_bad_case(number):
    return [j for j in range(number, 0, -1)]


def average_case():
    return generic_data(data_type.get("AVERAGE"), "files/average_case.txt")


def generate_average_case(number):
    return [r.randint(0, j) for j in range(number)]


def data_generator(max_number):
    def _build_case(case, generator, interval=10):
        with open(case.get("file_name"), "w") as f:
            for i in range(interval, max_number, 200):
                f.write((" ".join(map(str, generator(i))) + "\n"))

    _build_case(best_case(), generate_best_case)
    _build_case(bad_case(), generate_bad_case)
    _build_case(average_case(), generate_average_case)
