"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    new_list = []
    first, second, third, *rest = each_wagons_id
    new_list = [third, *missing_wagons, *rest, first, second]
    return new_list

def add_missing_stops(routing_dict, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    destinations = {**routing_dict, "stops": list(stops.values())}
    return destinations
    
def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    for key, value in more_route_information.items():
        route[key] = value
    return route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    """
    a, b, c = wagons_rows
    a_1, a_2, a_3 = a
    b_1, b_2, b_3 = b
    c_1, c_2, c_3 = c
    new_list = []
    new_list.append([a_1, b_1, c_1])
    new_list.append([a_2, b_2, c_2])
    new_list.append([a_3, b_3, c_3])
    return new_list    
    """

    row1, row2, row3 = zip(*wagons_rows)
    return [list(row1), list(row2), list(row3)]

print(fix_wagon_depot([
                    [(2, "red"), (4, "red"), (8, "red")],
                    [(5, "blue"), (9, "blue"), (13,"blue")],
                    [(3, "orange"), (7, "orange"), (11, "orange")],
                    ]))