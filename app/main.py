from app.tasks import get_temperature, get_humidity
import time
import statistics

def get_coordinates_from_user():
    print("Enter the location you want to query.")
    lat = float(input("Latitude: "))
    lon = float(input("Longitude: "))
    return lat, lon

def ask_user_stat_operation():
    print("\nWhat statistic would you like to compute?")
    print("1. Average")
    print("2. Median")
    print("3. Standard Deviation")
    choice = input("Enter 1, 2, or 3: ")
    return choice

def extract_stat(data, variable_name, stat_type):
    values = data.get("hourly", {}).get(variable_name, [])
    if not values:
        return None
    if stat_type == "1":
        return sum(values) / len(values)
    elif stat_type == "2":
        return statistics.median(values)
    elif stat_type == "3":
        return statistics.stdev(values)
    else:
        return None

def main():
    # lat, lon = get_coordinates_from_user()
    # stat_choice = ask_user_stat_operation()
    lat = -23.542269766074636
    lon = -46.64827445884045
    stat_choice = "2"

    print("\nFetching weather data (async)...")
    temp_task = get_temperature.delay(lat, lon)
    humidity_task = get_humidity.delay(lat, lon)

    temp_done = False
    humidity_done = False

    while not (temp_done and humidity_done):
        if not temp_done and temp_task.ready():
            temp_data = temp_task.get()
            temp_result = extract_stat(temp_data, "temperature_2m", stat_choice)
            print(f"\n✅ Temperature result is ready: {temp_result:.2f}°C")
            temp_done = True

        if not humidity_done and humidity_task.ready():
            humidity_data = humidity_task.get()
            humidity_result = extract_stat(humidity_data, "relative_humidity_2m", stat_choice)
            print(f"\n✅ Humidity result is ready: {humidity_result:.2f}%")
            humidity_done = True

        if not (temp_done and humidity_done):
            print("Waiting for remaining result...")
            time.sleep(2)

if __name__ == "__main__":
    main()
