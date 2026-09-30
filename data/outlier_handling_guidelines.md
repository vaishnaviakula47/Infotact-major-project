# Outlier Handling Guidelines

## Purpose

Outlier handling helps identify unusual climate observations without removing valid environmental events.

## What Is an Outlier?

An outlier is an observation that is significantly different from the general pattern of the dataset.

Climate data may contain unusual values because of:

- Sensor errors.
- Measurement problems.
- Environmental events.
- Temporary sensor conditions.
- Data recording issues.

## Temperature Outliers

Temperature observations should be reviewed when they are substantially different from the normal range observed for the dataset.

An unusual temperature value should first be flagged for investigation rather than immediately deleted.

## Humidity Outliers

Humidity values should be checked against the valid relative humidity range.

Values below 0% or above 100% should be flagged as potentially invalid.

Other unusual humidity observations should be reviewed using the surrounding observations and sensor information.

## Handling Process

The recommended process is:

1. Detect unusual observations.
2. Check the original record.
3. Check the date and time.
4. Check the sensor identifier.
5. Compare with nearby observations.
6. Decide whether the value is valid or potentially erroneous.
7. Document any correction or exclusion.

## Important Rule

Valid extreme weather observations should not automatically be treated as errors.

Outlier handling should preserve meaningful climate variation whenever possible.

## Raw Data Preservation

The original data should never be overwritten.

Any removed, corrected, or flagged observations should be documented separately.
