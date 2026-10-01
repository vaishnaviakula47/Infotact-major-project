import os
from config import CITIES, RESULTS_PATH
from analysis import analyze_all_cities, calculate_opportunities


def main():
    print("======================================")
    print("AUTOSYNC MICRO-CLIMATE ANALYTICS")
    print("======================================")

    print("\nLoading climate data...")

    city_summary = analyze_all_cities(CITIES)

    print("\nCity Climate Summary:")
    print(city_summary.to_string(index=False))

    print("\nCalculating micro-climate opportunities...")

    opportunities = calculate_opportunities(city_summary)

    print("\nOpportunity Results:")
    print(opportunities.to_string(index=False))

    os.makedirs(RESULTS_PATH, exist_ok=True)

    city_summary.to_csv(
        os.path.join(RESULTS_PATH, "city_summary.csv"),
        index=False
    )

    opportunities.to_csv(
        os.path.join(RESULTS_PATH, "opportunity_results.csv"),
        index=False
    )

    print("\n======================================")
    print("ANALYSIS COMPLETED SUCCESSFULLY")
    print("======================================")
    print(f"\nResults saved in: {RESULTS_PATH}")


if __name__ == "__main__":
    main()
