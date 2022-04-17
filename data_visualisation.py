import matplotlib.pyplot as plt
import method_type as m


def _data_viz(title, data1, data2, data3):
    plt.plot(*data1, 'r-', label="mergesort")
    plt.plot(*data2, 'b-', label="heapsort")
    plt.plot(*data3, 'g-', label="quicksort")
    plt.xlabel("len")
    plt.ylabel("time")
    plt.rcParams["figure.figsize"] = (8, 3)
    plt.title(title)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    _data_viz("sort", *(m.run_method([[j for j in range(i)] for i in range(11)])))

