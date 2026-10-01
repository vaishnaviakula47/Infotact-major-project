import os
import pandas as pd
from config import DATA_PATH


def load_city_data(city):
    """
    Load temperature and humidity CSV files for one city.
    """

    temp_file = os.path.join(DATA_PATH, city + "_temp.csv")
    rh_file = os.path.join(DATA_PATH, city + "_rh.csv")

    if not os.path.exists(temp_file):
        raise FileNotFoundError(f"Temperature file not found: {temp_file}")

    if not os.path.exists(rh_file):
        raise FileNotFoundError(f"Humidity file not found: {rh_file}")

    temperature = pd.read_csv(temp_file)
    humidity = pd.read_csv(rh_file)

    return temperature, humidity


def get_numeric_sensor_columns(data):
    """
    Return numeric sensor columns while ignoring hour.
    """

    numeric_columns = data.select_dtypes(include="number").columns.tolist()

    if "hour" in numeric_columns:
        numeric_columns.remove("hour")

    return numeric_columns


def calculate_average(data):
    """
    Calculate the average of available numeric sensor readings.
    """

    columns = get_numeric_sensor_columns(data)

    if not columns:
        return None

    return data[columns].stack().mean()
