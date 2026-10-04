from flask import Flask, jsonify, render_template
import os
import csv
import math
import re

app = Flask(__name__)

# ============================================================
# ATMOSYNC
# MICRO-CLIMATE ARBITRAGE ANALYTICS
# ============================================================

DATA_DIR = r"C:\Users\q\Desktop\infotact project\Infotact-major-project\data"


# ============================================================
# CITY COORDINATES
# ============================================================

CITY_COORDINATES = {

    "baltimore": {
        "lat": 39.2904,
        "lon": -76.6122
    },

    "denver": {
        "lat": 39.7392,
        "lon": -104.9903
    },

    "las_vegas": {
        "lat": 36.1699,
        "lon": -115.1398
    },

    "los_angeles": {
        "lat": 34.0522,
        "lon": -118.2437
    },

    "miami": {
        "lat": 25.7617,
        "lon": -80.1918
    },

    "phoenix": {
        "lat": 33.4484,
        "lon": -112.0740
    },

    "portland": {
        "lat": 45.5152,
        "lon": -122.6784
    },

    "tucson": {
        "lat": 32.2226,
        "lon": -110.9747
    }
}


# ============================================================
# FORMAT CITY NAME
# ============================================================

def format_city_name(filename):

    name = os.path.basename(filename)

    name = re.sub(
        r"_(temp|rh)\.csv$",
        "",
        name,
        flags=re.IGNORECASE
    )

    name = name.replace("_", " ")

    return name.title()


# ============================================================
# READ NUMERIC VALUES
# ============================================================

def read_csv_numbers(filepath):

    values = []

    if not os.path.exists(filepath):
        return values

    try:

        with open(
            filepath,
            "r",
            encoding="utf-8-sig",
            errors="ignore",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            if not reader.fieldnames:
                return values

            for row in reader:

                for column, value in row.items():

                    if column is None:
                        continue

                    column_name = str(
                        column
                    ).strip().lower()

                    if (
                        "date" in column_name
                        or "time" in column_name
                        or column_name == "hour"
                    ):
                        continue

                    if value is None:
                        continue

                    value = str(value).strip()

                    if value == "":
                        continue

                    try:

                        number = float(value)

                        if math.isfinite(number):
                            values.append(number)

                    except ValueError:
                        continue

    except Exception as error:

        print(
            f"Error reading {filepath}: {error}"
        )

    return values


# ============================================================
# AVERAGE
# ============================================================

def calculate_average(values):

    if not values:
        return 0

    return sum(values) / len(values)


# ============================================================
# DETECT ALL CITY DATASETS
# ============================================================

def detect_cities():

    cities = {}

    if not os.path.exists(DATA_DIR):

        print(
            "\nDATA DIRECTORY NOT FOUND:"
        )

        print(DATA_DIR)

        return cities

    for filename in os.listdir(DATA_DIR):

        if not filename.lower().endswith(".csv"):
            continue

        lower_name = filename.lower()

        if lower_name.endswith("_temp.csv"):

            city_key = lower_name[
                :-len("_temp.csv")
            ]

            if city_key not in cities:
                cities[city_key] = {}

            cities[city_key]["temp"] = filename

        elif lower_name.endswith("_rh.csv"):

            city_key = lower_name[
                :-len("_rh.csv")
            ]

            if city_key not in cities:
                cities[city_key] = {}

            cities[city_key]["rh"] = filename

    return cities


# ============================================================
# CITY ANALYTICS
# ============================================================

def get_city_data():

    detected_cities = detect_cities()

    results = []

    for city_key, files in sorted(
        detected_cities.items()
    ):

        temperature_values = []
        humidity_values = []

        # Temperature
        if "temp" in files:

            temp_path = os.path.join(
                DATA_DIR,
                files["temp"]
            )

            temperature_values = (
                read_csv_numbers(temp_path)
            )

        # Humidity
        if "rh" in files:

            humidity_path = os.path.join(
                DATA_DIR,
                files["rh"]
            )

            humidity_values = (
                read_csv_numbers(humidity_path)
            )

        temperature = calculate_average(
            temperature_values
        )

        humidity = calculate_average(
            humidity_values
        )

        coordinates = CITY_COORDINATES.get(
            city_key,
            {
                "lat": 0,
                "lon": 0
            }
        )

        results.append({

            "city":
                format_city_name(
                    files.get(
                        "temp",
                        files.get(
                            "rh",
                            city_key + ".csv"
                        )
                    )
                ),

            "cityKey":
                city_key,

            "temperature":
                round(
                    temperature,
                    2
                ),

            "humidity":
                round(
                    humidity,
                    2
                ),

            "temperatureRecords":
                len(
                    temperature_values
                ),

            "humidityRecords":
                len(
                    humidity_values
                ),

            "latitude":
                coordinates["lat"],

            "longitude":
                coordinates["lon"],

            "temperatureFile":
                files.get(
                    "temp",
                    ""
                ),

            "humidityFile":
                files.get(
                    "rh",
                    ""
                )

        })

    return results


# ============================================================
# OPPORTUNITY ANALYSIS
# ============================================================

def calculate_opportunities(city_data):

    opportunities = []

    for i in range(
        len(city_data)
    ):

        for j in range(
            i + 1,
            len(city_data)
        ):

            city_a = city_data[i]
            city_b = city_data[j]

            temperature_difference = abs(
                city_a["temperature"]
                -
                city_b["temperature"]
            )

            humidity_difference = abs(
                city_a["humidity"]
                -
                city_b["humidity"]
            )

            # Prototype analytical score
            score = (
                temperature_difference
                +
                humidity_difference / 10
            )

            if score >= 8:
                status = "HIGH"

            elif score >= 4:
                status = "MEDIUM"

            else:
                status = "LOW"

            opportunities.append({

                "cityA":
                    city_a["city"],

                "cityB":
                    city_b["city"],

                "temperatureDifference":
                    round(
                        temperature_difference,
                        2
                    ),

                "humidityDifference":
                    round(
                        humidity_difference,
                        2
                    ),

                "score":
                    round(
                        score,
                        2
                    ),

                "status":
                    status

            })

    opportunities.sort(
        key=lambda item:
            item["score"],
        reverse=True
    )

    return opportunities


# ============================================================
# DASHBOARD API
# ============================================================

@app.route("/api/dashboard")
def dashboard_api():

    city_data = get_city_data()

    valid_temperature = [

        city["temperature"]

        for city in city_data

        if city["temperature"] != 0

    ]

    valid_humidity = [

        city["humidity"]

        for city in city_data

        if city["humidity"] != 0

    ]

    average_temperature = (
        calculate_average(
            valid_temperature
        )
    )

    average_humidity = (
        calculate_average(
            valid_humidity
        )
    )

    if valid_temperature:

        minimum_temperature = min(
            valid_temperature
        )

        maximum_temperature = max(
            valid_temperature
        )

        climate_difference = (
            maximum_temperature
            -
            minimum_temperature
        )

    else:

        climate_difference = 0

    opportunities = (
        calculate_opportunities(
            city_data
        )
    )

    temperature_records = sum(

        city["temperatureRecords"]

        for city in city_data

    )

    humidity_records = sum(

        city["humidityRecords"]

        for city in city_data

    )

    total_records = (
        temperature_records
        +
        humidity_records
    )

    hottest_city = None

    if city_data:

        hottest_city = max(
            city_data,
            key=lambda city:
                city["temperature"]
        )

    most_humid_city = None

    if city_data:

        most_humid_city = max(
            city_data,
            key=lambda city:
                city["humidity"]
        )

    highest_opportunity = None

    if opportunities:

        highest_opportunity = (
            opportunities[0]
        )

    return jsonify({

        "project": {

            "name":
                "AtmoSync",

            "title":
                "Micro-Climate Arbitrage Analytics"

        },

        "cities":
            city_data,

        "opportunities":
            opportunities,

        "summary": {

            "averageTemperature":
                round(
                    average_temperature,
                    2
                ),

            "averageHumidity":
                round(
                    average_humidity,
                    2
                ),

            "climateDifference":
                round(
                    climate_difference,
                    2
                ),

            "opportunityCount":
                len(
                    opportunities
                ),

            "cityCount":
                len(
                    city_data
                ),

            "temperatureRecords":
                temperature_records,

            "humidityRecords":
                humidity_records,

            "totalRecords":
                total_records,

            "hottestCity":
                hottest_city,

            "mostHumidCity":
                most_humid_city,

            "highestOpportunity":
                highest_opportunity

        }

    })


# ============================================================
# MAIN DASHBOARD PAGE
# ============================================================

@app.route("/")
def index():

    return render_template(
        "index.html"
    )


# ============================================================
# SEPARATE PAGES
# ============================================================

@app.route("/climate")
def climate():

    return render_template(
        "climate.html"
    )


@app.route("/locations")
def locations():

    return render_template(
        "locations.html"
    )


@app.route("/opportunities")
def opportunities():

    return render_template(
        "opportunities.html"
    )


@app.route("/explorer")
def explorer():

    return render_template(
        "explorer.html"
    )


@app.route("/analytics")
def analytics():

    return render_template(
        "analytics.html"
    )


@app.route("/quality")
def quality():

    return render_template(
        "quality.html"
    )


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 70)

    print(
        "AtmoSync"
    )

    print(
        "Micro-Climate Arbitrage Analytics"
    )

    print("=" * 70)

    print()

    print(
        "Dataset directory:"
    )

    print(
        DATA_DIR
    )

    print()

    detected = detect_cities()

    print(
        f"Cities detected: {len(detected)}"
    )

    print()

    for city_key, files in sorted(
        detected.items()
    ):

        print(
            "✓",
            city_key.replace(
                "_",
                " "
            ).title()
        )

        if "temp" in files:

            print(
                "   Temperature:",
                files["temp"]
            )

        if "rh" in files:

            print(
                "   Humidity:",
                files["rh"]
            )

    print()

    print(
        "Dashboard URL:"
    )

    print(
        "http://127.0.0.1:5000"
    )

    print("=" * 70)

    app.run(
        debug=True
    )
