def decimal_to_sexagesimal(decimal):
    degrees = int(abs(decimal))
    minutes_float = (abs(decimal) - degrees) * 60
    minutes = int(minutes_float)
    seconds = (minutes_float - minutes) * 60
    return degrees, minutes, seconds

def sexagesimal_to_decimal(degrees, minutes, seconds, direction):
    decimal = degrees + minutes / 60 + seconds / 3600
    if direction in ['S', 'W']:
        decimal *= -1
    return decimal

def format_sexagesimal(degrees, minutes, seconds, direction):
    return f"{degrees}° {minutes}' {seconds:.2f}\" {direction}"

def clean_input(input_str):
    return ''.join(filter(lambda x: x.isdigit() or x in ['.', '-', ' '], input_str))

def main():
    choice = input("Choose the conversion (1 for decimal -> sexagesimal, 2 for sexagesimal -> decimal): ")
    print("\r")

    if choice == '1':
        latitude_decimal = float(input("Enter latitude in decimal: "))
        longitude_decimal = float(input("Enter longitude in decimal: "))

        latitude_deg, latitude_min, latitude_sec = decimal_to_sexagesimal(latitude_decimal)
        longitude_deg, longitude_min, longitude_sec = decimal_to_sexagesimal(longitude_decimal)

        latitude_direction = 'N' if latitude_decimal >= 0 else 'S'
        longitude_direction = 'E' if longitude_decimal >= 0 else 'W'

        latitude_sexagesimal = format_sexagesimal(latitude_deg, latitude_min, latitude_sec, latitude_direction)
        longitude_sexagesimal = format_sexagesimal(longitude_deg, longitude_min, longitude_sec, longitude_direction)

        print(f"Latitude: {latitude_sexagesimal}")
        print(f"Longitude: {longitude_sexagesimal}")

    elif choice == '2':
        latitude_sexagesimal = input("Enter latitude sexagesimal (format: XX° XX' XX.XX\" N/S): ")
        longitude_sexagesimal = input("Enter longitude sexagesimal (format: XX° XX' XX.XX\" E/W): ")

        latitude_cleaned = clean_input(latitude_sexagesimal)
        longitude_cleaned = clean_input(longitude_sexagesimal)

        latitude_parts = latitude_cleaned.split()
        longitude_parts = longitude_cleaned.split()

        latitude_deg = float(latitude_parts[0])
        latitude_min = float(latitude_parts[1]) if len(latitude_parts) > 1 else 0
        latitude_sec = float(latitude_parts[2]) if len(latitude_parts) > 2 else 0
        latitude_direction = 'S' if 'S' in latitude_sexagesimal else 'N'

        longitude_deg = float(longitude_parts[0])
        longitude_min = float(longitude_parts[1]) if len(longitude_parts) > 1 else 0
        longitude_sec = float(longitude_parts[2]) if len(longitude_parts) > 2 else 0
        longitude_direction = 'W' if 'W' in longitude_sexagesimal else 'E'

        latitude_decimal = sexagesimal_to_decimal(latitude_deg, latitude_min, latitude_sec, latitude_direction)
        longitude_decimal = sexagesimal_to_decimal(longitude_deg, longitude_min, longitude_sec, longitude_direction)

        print(f"Latitude: {latitude_decimal}")
        print(f"Longitude: {longitude_decimal}")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
