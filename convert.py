import argparse

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

def parse_sexagesimal(input_str):
    input_str = input_str.replace('°', ' ').replace('\'', ' ').replace('\"', ' ').replace('º', ' ')
    parts = input_str.split()
    
    if len(parts) < 4:
        raise ValueError("Input string format is incorrect")
    
    degrees = int(parts[0])
    minutes = int(parts[1])
    seconds = float(parts[2])
    direction = parts[3]
    
    return degrees, minutes, seconds, direction

def main():
    parser = argparse.ArgumentParser(description="Convert coordinates between decimal and sexagesimal.")
    parser.add_argument('-1', '--decimal-to-sexagesimal', action='store_true', help="Convert from decimal to sexagesimal")
    parser.add_argument('-2', '--sexagesimal-to-decimal', action='store_true', help="Convert from sexagesimal to decimal")
    args = parser.parse_args()

    if args.decimal_to_sexagesimal:
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

    elif args.sexagesimal_to_decimal:
        latitude_sexagesimal = input("Enter latitude sexagesimal (format: XX° XX' XX.XX\" N/S): ")
        longitude_sexagesimal = input("Enter longitude sexagesimal (format: XX° XX' XX.XX\" E/W): ")

        latitude_deg, latitude_min, latitude_sec, latitude_direction = parse_sexagesimal(latitude_sexagesimal)
        longitude_deg, longitude_min, longitude_sec, longitude_direction = parse_sexagesimal(longitude_sexagesimal)

        latitude_decimal = sexagesimal_to_decimal(latitude_deg, latitude_min, latitude_sec, latitude_direction)
        longitude_decimal = sexagesimal_to_decimal(longitude_deg, longitude_min, longitude_sec, longitude_direction)

        print(f"Latitude: {latitude_decimal}")
        print(f"Longitude: {longitude_decimal}")

    else:
        print("Invalid choice. Use -1 for decimal -> sexagesimal or -2 for sexagesimal -> decimal.")

if __name__ == "__main__":
    main()
