from data_type import get_data, data_type
from method_type import run_method
from data_visualisation import _data_viz

if __name__ == "__main__":
    for t in ["BEST", "AVERAGE", "BAD"]:
        tab = get_data(t)
        viz_data = run_method(tab)
        _data_viz(data_type.get(t), *viz_data)

