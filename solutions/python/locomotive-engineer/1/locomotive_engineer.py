"""Functions which helps the locomotive engineer to keep track of the train."""

def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers."""
    return list(args)

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons."""
    
    first, second, locomotive, *rest = each_wagons_id

    return [locomotive, *missing_wagons, *rest, first, second]

def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict."""
    
    route["stops"] = list(kwargs.values())

    return route

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information."""
    
    return {**route, **more_route_information}

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons."""

    return [list(row) for row in zip(*wagons_rows)]
