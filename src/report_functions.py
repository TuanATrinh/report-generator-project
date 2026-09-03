"""
Report Generation Functions for Flight Operations

This module contains functions for reading, processing, and reporting on
military flight operations data. Students will implement these functions
to practice file I/O, data manipulation, and report generation.
"""

import csv


def read_csv_file(filepath):
    """
    Reads a CSV file and returns the data as a list of dictionaries.
    """
    # TODO: Your code here
    # Hint: Use csv.DictReader to read CSV files into dictionaries
    # Hint: Remember to use 'with open()' for proper file handling
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)


def count_records(data_list):
    """Counts the number of records in a dataset."""
    # TODO: Your code here
    # Hint: Use the len() function
    return len(data_list)


def get_unique_values(data_list, field_name):
    """Gets all unique values for a specific field in the dataset."""
    # TODO: Your code here
    # Hint: Use a set to collect unique values
    # Hint: Convert the set to a list and sort it before returning
    unique_values = set()

    for record in data_list:
        unique_values.add(record[field_name])

    return sorted(unique_values)


def filter_by_field(data_list, field_name, field_value):
    """Filters records where a specific field matches a given value."""
    # TODO: Your code here
    # Hint: Use a list comprehension to filter or a loop!
    # see here for more info: https://docs.python.org/3.13/tutorial/datastructures.html#list-comprehensions
    filtered_data = []

    for record in data_list:
        if record[field_name] == field_value:
            filtered_data.append(record)

    return filtered_data


def calculate_total(data_list, field_name):
    """Calculates the sum of a numeric field across all records."""
    # TODO: Your code here
    # Hint: Initialize a total variable to 0
    # Hint: Loop through each record and add float(record[field_name]) to total
    # Hint: Remember to convert string values to float!
    total = 0

    for record in data_list:
        total += float(record[field_name])

    return total


def calculate_average(data_list, field_name):
    """Calculates the average value of a numeric field."""
    # TODO: Your code here
    # Hint: Use calculate_total() and count_records() functions
    # Hint: Average = total / count
    if count_records(data_list) == 0:
        return 0

    total = calculate_total(data_list, field_name)
    count = count_records(data_list)

    return total / count


def find_record_by_id(data_list, id_field, id_value):
    """Finds a specific record by its ID field."""
    # TODO: Your code here
    # Hint: Loop through data_list
    # Hint: Return the record when record[id_field] == id_value
    for record in data_list:
        if record[id_field] == id_value:
            return record

    return None


def join_data(primary_list, secondary_list, primary_key, foreign_key):
    """
    Joins two datasets together based on matching key fields.
    Similar to a SQL JOIN.
    """
    # TODO: Your code here
    # Hint: Create a dictionary mapping secondary_list IDs to records
    # Hint: For each record in primary_list, look up the matching secondary record
    # Hint: Use dict.update() to merge dictionaries
    secondary_lookup = {}

    for record in secondary_list:
        secondary_lookup[record[foreign_key]] = record

    joined_data = []

    for primary_record in primary_list:
        joined_record = primary_record.copy()

        matching_record = secondary_lookup.get(primary_record[primary_key])

        if matching_record:
            joined_record.update(matching_record)

        joined_data.append(joined_record)

    return joined_data


def write_report_to_file(filepath, content):
    """Writes a text report to a file."""
    # TODO: Your code here
    # Hint: Use 'with open(filepath, 'w')' to open file for writing
    with open(filepath, 'w') as file:
        file.write(content)


def format_header(title):
    """Creates a formatted header for reports."""
    # TODO: Your code here
    # Hint: Use "=" * 60 to create a line of equals signs
    # Hint: Use .center(60) to center the title
    line = "=" * 60
    return f"{line}\n{title.center(60)}\n{line}"


# Testing functions
if __name__ == '__main__':
    print("Testing report functions...")

    #print("Implement functions above, then uncomment test code below")

#Phase 1 Tests:
    print("Phase 1 Tests:")
    print("|||----- Phase 1 test start -----|||")
    # # Test read_csv_file
    pilots = read_csv_file('data/pilots.csv')
    print(f"Loaded {len(pilots)} pilots")

    # Test count_records
    print(f"Number of pilots: {count_records(pilots)}")

    #Test get_unique_values
    squadrons = get_unique_values(pilots, 'squadron')
    print(f"Squadrons: {squadrons}")

    #Test filter_by_field
    squadron_pilots = filter_by_field(pilots, 'squadron', 'VFA-41')
    print("VFA-41 pilots: {squadron_pilots}")

    #End Phase 1 Tests
    print("|||----- Phase 1 test End -----|||")


#Phase 2 Tests
    print("\n Phase 2 Tests")
    #Phase 2 Test Start
    print("|||----- Phase 2 Tests Start -----|||")

    #Test flight_logs
    flight_logs = read_csv_file('data/flight_logs.csv')

    #Test calculate_total
    total_hours = calculate_total(flight_logs, 'duration_hours')
    print(f"Total flight hours: {total_hours}")

    #Test calculate_average
    average_duration = calculate_average(flight_logs, 'duration_hours')
    print(f"Average flight duration: {average_duration}")

    #Test find_record_id
    pilot = find_record_by_id(pilots, 'pilot_id', 'P001')
    print(f"Found pilot: {pilot}")

    missing_pilot = find_record_by_id(pilots, 'pilot_id', 'P999')
    print(f"Missing pilot: {missing_pilot}")

    #End Phase 2 Test
    print("|||----- Phase 2 Tests End ----- |||")

#Phase 3 Test
    print("\n Phase 3 Tests")
    #Phase 3 Test Start
    print("|||----- Phase 3 Test Start -----|||")

    #Test join_data
    joined_flights = join_data(
        flight_logs,
        pilots,
        'pilot_id',
        'pilot_id'
    )
    print(f"Joined flight records: {len(joined_flights)}")
    print(f"First joined record: {joined_flights[0]}")

    #Phase 3 Test End
    print("|||----- Phase 3 Test End -----|||")

#Phase 4 Test
    print("\n Phase 4 Tests")
    #Phase 4 Test Start
    print("|||----- Phase 4 Test Start -----|||")

    #Header Test
    header = format_header("VFA-41 SQUADRON REPORT")
    print(header)

    #write_report_to_file test
    write_report_to_file(
        'reports/test-report.txt',
        header
    )

    print("Test report written to reports/test-report.txt")
