import pandas as pd
from data_loader import load_city_data, calculate_average


def analyze_city(city):
    """
    Calculate average temperature and humidity for one city.
    """

    temperature_data, humidity_data = load_city_data(city)

    avg_temperature = calculate_average(temperature_data)
    avg_humidity = calculate_average(humidity_data)

    return {
        "city": city,
        "average_temperature": round(avg_temperature, 2),
        "average_humidity": round(avg_humidity, 2)
    }


def analyze_all_cities(cities):
    """
    Analyze all cities and return a summary DataFrame.
    """

    results = []

    for city in cities:
        result = analyze_city(city)
        results.append(result)

    return pd.DataFrame(results)


def calculate_opportunities(city_summary):
    """
    Compare cities and identify micro-climate differences.

    This is a prototype opportunity score for the project workflow.
    """

    opportunities = []

    for i in range(len(city_summary)):
        for j in range(i + 1, len(city_summary)):

            city_a = city_summary.iloc[i]
            city_b = city_summary.iloc[j]

            temperature_difference = abs(
                city_a["average_temperature"]
                - city_b["average_temperature"]
            )

            humidity_difference = abs(
                city_a["average_humidity"]
                - city_b["average_humidity"]
            )

            opportunity_score = (
                temperature_difference
                + (humidity_difference / 10)
            )

            opportunities.append({
                "city_a": city_a["city"],
                "city_b": city_b["city"],
                "temperature_difference": round(
                    temperature_difference, 2
                ),
                "humidity_difference": round(
                    humidity_difference, 2
                ),
                "prototype_opportunity_score": round(
                    opportunity_score, 2
                )
            })

    return pd.DataFrame(opportunities)
