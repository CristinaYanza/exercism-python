"""Functions to help Azara and Rui locate pirate treasure."""

def get_coordinate(record):
    """Return coordinate value from a tuple."""
    
    return record[1]

def convert_coordinate(coordinate):
    """Split coordinate into individual components."""
    
    return (coordinate[0], coordinate[1])

def compare_records(azara_record, rui_record):
    """Compare two records and determine if coordinates match."""

    coordenada_azara = convert_coordinate(get_coordinate(azara_record))
    coordenada_rui = rui_record[1]

    return coordenada_azara == coordenada_rui

def create_record(azara_record, rui_record):
    """Combine records if coordinates match."""

    if compare_records(azara_record, rui_record):
        return (
            azara_record[0],
            azara_record[1],
            rui_record[0],
            rui_record[1],
            rui_record[2]
        )

    return "not a match"

def clean_up(combined_record_group):
    """Clean up combined records into a multi-line string."""

    report = []

    for record in combined_record_group:
        clean_record = (
            record[0],
            record[2],
            record[3],
            record[4]
        )

        report.append(str(clean_record))

    return "\n".join(report) + "\n"