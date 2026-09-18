# Micro-Climate Dataset Data Dictionary

## Dataset Description

This dataset contains micro-climate measurements collected from different locations.

## Files

The dataset contains temperature and relative humidity (RH) files for different cities.

Examples:
- baltimore_temp.csv
- baltimore_rh.csv
- denver_temp.csv
- denver_rh.csv
- las_vegas_temp.csv
- las_vegas_rh.csv
- los_angeles_temp.csv
- los_angeles_rh.csv
- miami_rh.csv

## Main Columns

### Date - Time
Contains the date and time when the measurement was recorded.

### hour
Represents the hour associated with the measurement.

### Sensor Columns
Columns such as H16, H17, H18, H19, L17, L18, M16, M18, VH16, VH17, etc. contain measurements recorded by different sensors.

### Temperature
Temperature files contain temperature measurements recorded by the sensors.

### Relative Humidity (RH)
RH files contain relative humidity measurements recorded by the sensors.

## Data Types

- Date - Time: Object/Text
- hour: Object/Text
- Sensor measurements: Float64/Numeric

## Data Quality

The initial exploration showed that the Baltimore temperature dataset contains 1,968 rows and 20 columns.

No missing values were found in the columns checked during the initial exploration.