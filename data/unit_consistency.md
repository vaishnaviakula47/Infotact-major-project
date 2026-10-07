# Unit Consistency in Climate Data

## Purpose

Unit consistency ensures that temperature and humidity values are interpreted correctly during analysis.

## Temperature Units

The climate datasets contain temperature measurements.

Before analysis, temperature values should be checked to ensure that all datasets use the same unit.

The expected temperature unit should be verified from the dataset metadata.

If different datasets use different units, they should be converted to a common unit before comparison.

## Humidity Units

The relative humidity datasets contain humidity measurements.

Relative humidity should be interpreted as a percentage value.

Humidity values should normally be within the range of 0% to 100%.

Values outside this range should be flagged for data-quality review.

## Consistency Checks

The following checks should be performed:

- Verify temperature units from metadata.
- Verify humidity representation.
- Ensure temperature datasets use a common unit.
- Ensure humidity values use a common percentage scale.
- Avoid changing raw dataset values.
- Record any required conversions separately.

## Importance for Analysis

Consistent units are necessary when:

- Comparing different cities.
- Comparing different sensors.
- Calculating climate differences.
- Detecting unusual climate conditions.
- Preparing values for arbitrage analysis.

## Data Preservation

Original dataset values should remain unchanged.

Any unit conversion should be documented as a preprocessing step so that the original data remains traceable.
