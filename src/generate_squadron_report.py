"""
Squadron Activity Report Generator

This script demonstrates how to use the report_functions module
to generate a comprehensive squadron activity report.

Students will build this step-by-step in the assignment.
"""

import report_functions as rf


def generate_squadron_report(squadron_code, output_file):
    """
    Generates a comprehensive activity report for a specific squadron.

    Args:
        squadron_code (str): Squadron identifier (e.g., 'VFA-41')
        output_file (str): Path to save the report
    """
    # TODO: PART 1 - Load the data files
    pilots = rf.read_csv_file('data/pilots.csv')
    aircraft = rf.read_csv_file('data/aircraft.csv')
    flight_logs = rf.read_csv_file('data/flight_logs.csv')

    # TODO: PART 2 - Filter data for the specified squadron
    squadron_pilots = rf.filter_by_field(
        pilots,
        'squadron',
        squadron_code
    )


    squadron_aircraft = rf.filter_by_field(
        aircraft,
        'squadron',
        squadron_code
    )
    # TODO: PART 3 - Get flights for squadron pilots
    squadron_flights = []

    for flight in flight_logs:
        for pilot in squadron_pilots:
            if flight['pilot_id'] == pilot['pilot_id']:
                squadron_flights.append(flight)

    flights_with_pilots = rf.join_data(
            squadron_flights,
            squadron_pilots,
            'pilot_id',
            'pilot_id'
        )


    flights_with_aircraft = rf.join_data(
            flights_with_pilots,
            squadron_aircraft,
            'aircraft_id',
            'aircraft_id'
        )
    # TODO: PART 4 - Calculate statistics
    total_flight_hours = rf.calculate_total(
        squadron_flights,
        'duration_hours'
    )

    total_missions = rf.count_records(
        squadron_flights
    )

    average_mission_duration = rf.calculate_average(
        squadron_flights,
        'duration_hours'
    )

    mission_types = rf.get_unique_values(
            squadron_flights,
            'mission_type'
        )

    mission_breakdown = {}

    for mission_type in mission_types:

        missions = rf.filter_by_field(
            squadron_flights,
            'mission_type',
            mission_type
        )

        mission_breakdown[mission_type] = rf.count_records(
            missions
        )

    active_aircraft = rf.filter_by_field(
            squadron_aircraft,
            'status',
            'Active'
        )

    maintenance_aircraft = rf.filter_by_field(
        squadron_aircraft,
        'status',
        'Maintenance'
    )

    active_count = rf.count_records(
        active_aircraft
    )

    maintenance_count = rf.count_records(
        maintenance_aircraft
    )

    # TODO: PART 5 - Build the report content
    report = ""

    # Header
    report += rf.format_header(
        f"{squadron_code} SQUADRON ACTIVITY REPORT"
    )

    report += "\n\nPERSONNEL ROSTER\n"
    report += "-" * 60 + "\n"

    report += f"Total Pilots: {len(squadron_pilots)}\n\n"

    for pilot in squadron_pilots:

        report += (
            f"{pilot['rank']} "
            f"{pilot['first_name']} "
            f"{pilot['last_name']} "
            f"\"{pilot['callsign']}\" "
            f"- {pilot['years_experience']} years experience\n"
        )

    report += "\n\nAIRCRAFT INVENTORY\n"
    report += "-" * 60 + "\n"

    report += f"Total Aircraft: {len(squadron_aircraft)}\n"
    report += f"Active: {active_count}\n"
    report += f"Maintenance: {maintenance_count}\n\n"

    for plane in squadron_aircraft:

        report += (
            f"{plane['tail_number']} | "
            f"{plane['model']} | "
            f"Status: {plane['status']}\n"
        )

    report += "\n\nFLIGHT OPERATIONS\n"
    report += "-" * 60 + "\n"

    report += (
        f"Total Flight Hours: "
        f"{total_flight_hours:.2f}\n"
    )

    report += (
        f"Total Missions Flown: "
        f"{total_missions}\n"
    )

    report += (
        f"Average Mission Duration: "
        f"{average_mission_duration:.2f} hours\n"
    )

    report += "\n\nMISSION BREAKDOWN\n"
    report += "-" * 60 + "\n"

    for mission_type, count in mission_breakdown.items():

        report += (
            f"{mission_type}: "
            f"{count} missions\n"
        )

    report += "\n\nCURRENT OPERATIONAL STATUS\n"
    report += "-" * 60 + "\n"

    if maintenance_count == 0:

        report += "STATUS: FULLY OPERATIONAL\n"

    elif active_count > 0:

        report += "STATUS: PARTIALLY OPERATIONAL\n"

    else:

        report += "STATUS: NOT OPERATIONAL\n"

    report += f"Aircraft Active: {active_count}\n"
    report += f"Aircraft in Maintenance: {maintenance_count}\n"

    # TODO: PART 6 - Write the report to file
    rf.write_report_to_file(
        output_file,
        report
    )


# Main execution
if __name__ == '__main__':
    # TODO: Students will customize this to generate reports for different squadrons
    print("Generating squadron activity reports...")

    # Example: Generate report for VFA-41 (Black Aces)
    # generate_squadron_report('VFA-41', '../reports/vfa-41-report.txt')

    generate_squadron_report(
        'VFA-41',
        'reports/vfa-41-report.txt'
    )

    print(
        "Report generated successfully: "
        "reports/vfa-41-report.txt"
    )


