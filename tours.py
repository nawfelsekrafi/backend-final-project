import math


# def from_big_list_to_small_tours(students):




def convert_to_nearest_neighbor(bus_location, students):
    tab = {}
    for s in students:
        # distance between tow points : d=√((x_2-x_1)²+(y_2-y_1)²)
        distance = math.sqrt(
            (s["home_location"][0] - bus_location[0]) ** 2 + (s["home_location"][1] - bus_location[1]) ** 2)
        d = {s["name"]: distance}
        tab.update(d)
    # sorting tab
    return sorted(tab.items(), key=lambda x: x[1])