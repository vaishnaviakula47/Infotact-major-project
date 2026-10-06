# AtmoSync: Micro-Climate Arbitrage Analytics

**Infotact Solutions Internship**

# Project Team
| Member | Responsibility |
|---|---|
| Vaishnavi | Data / Project Coordination |
| Raghu | Analytics / Statistical Analysis |
| Ashwitha | Visualization / Dashboard Design |
| Philomina | Application / Integration |

# 1. Abstract
AtmoSync is a data analytics project developed during the Infotact Solutions internship to study temperature and relative-humidity differences across urban locations. The project progresses from dataset organization and data-quality checks through statistical analysis, climate comparison, opportunity-signal analysis, visualization and dashboard integration.
The final output is an interactive analytical dashboard prototype that converts climate CSV data into comparative metrics, visualizations and analytical insights.

# 2. Problem Statement
Raw urban sensor datasets contain multiple cities, timestamps and sensor columns. It is difficult to compare locations consistently without a structured analytical workflow.
AtmoSync addresses this problem by organizing the data, defining quality checks, calculating climate metrics, comparing locations and presenting the results through an interactive dashboard.

# 3. Objectives
- Understand and organize multi-city temperature and relative-humidity datasets.
- Document missing-value, duplicate, timestamp and invalid-measurement checks.
- Prepare data for statistical and comparative analysis while preserving raw files.
- Calculate temperature and humidity statistics and compare locations.
- Derive climate-difference measures for opportunity analysis.
- Define a transparent prototype opportunity score.
- Develop visualizations and an interactive dashboard.
- Integrate data loading, analysis and presentation into an end-to-end workflow.

# 4. Dataset
The project uses the Dryad urban microclimate dataset (DOI: **10.5061/dryad.m63xsj47v**).
The project work identified city-wise temperature and relative-humidity files for:
- Baltimore
- Denver
- Las Vegas
- Los Angeles
- Miami
- Phoenix
- Portland
- Tucson
The dataset also includes `Metadata.xlsx`.
Temperature and relative-humidity measurements are stored as separate CSV datasets.
In total, the project contains **16 city-level CSV datasets**, consisting of:
- 8 temperature CSV files
- 8 relative-humidity CSV files
- 1 metadata workbook
During exploratory analysis, a Baltimore temperature file was inspected with **1,968 records and 20 displayed columns**, including `Date - Time`, `hour` and sensor columns.

# 5. Methodology
The project follows the following analytical workflow:
1. Dataset inventory and city/file mapping.
2. Data-quality assessment and preprocessing requirements.
3. Exploratory analysis of dimensions, columns and sensor structure.
4. Temperature statistical analysis.
5. Humidity analysis and metrics.
6. Location and micro-climate comparison.
7. Climate-difference calculation.
8. Opportunity criteria, thresholds and scoring methodology.
9. Visualization and dashboard development.
10. Application integration and execution testing.
The overall workflow is:
**Raw Data → Data Quality → Preprocessing → Statistical Analysis → Climate Comparison → Opportunity Analysis → Visualization → Dashboard**

# 6. Data Preparation and Quality Checks
The following data-quality checks were considered during the project:
- Check missing values before analysis.
- Check duplicate rows and records.
- Check `Date - Time` consistency.
- Check unrealistic temperature readings.
- Check relative-humidity values against valid limits.
- Standardize column names where required.
- Preserve original raw datasets and separate derived data.
- Validate city-wise temperature and humidity file availability.
- Verify that the required data is available before analytics processing.
- Validate numeric sensor values before calculations.
- Ensure that temperature and humidity datasets are correctly mapped to their respective cities.
The project maintains the original raw datasets separately from derived analytical outputs to improve traceability and reproducibility.

# 7. Analytical Work Completed
The analytical work includes:
- Initial data exploration and dataset structure inspection.
- Temperature statistical analysis and temperature insights.
- Humidity analysis and humidity metrics.
- Location comparison and micro-climate comparison.
- Climate-difference metrics.
- Opportunity criteria and scoring methodology.
- Opportunity thresholds and result fields.
- Baseline climate comparison and anomaly detection.
- Climate variability analysis.
- Temperature and humidity distribution analysis.
- Sensor-variation analysis.
- Time-period analysis.
- Opportunity validation.
The analysis is designed to calculate values dynamically from the available datasets instead of depending entirely on manually entered values.

# 8. Visualization and Dashboard
The dashboard combines KPI cards, climate comparison charts, temperature and humidity analysis, opportunity results, sensor summaries, automated insights and execution status.
The dashboard prototype was developed using HTML, CSS and JavaScript and integrated with the project data-processing workflow.
Major dashboard components include:
- Average Temperature KPI
- Average Humidity KPI
- Climate Difference KPI
- Opportunity Count
- Location Climate Comparison
- Temperature vs Humidity Analysis
- Temperature Trend
- Opportunity Result Table
- Sensor and Record Summary
- Automated Insights
- Execution Status
- Interactive Location Map
- City Directory
- Data Explorer
- Analytics Engine
- Data Quality Dashboard
The HTML/JavaScript prototype calculates values from CSV and API data rather than relying only on manually entered numbers.
The dashboard provides separate analytical views so that data exploration, climate analysis, opportunity analysis, location information, analytics processing and data-quality information can be inspected independently.

# 9. Opportunity Analysis
The project compares locations using temperature and humidity differences.
The dashboard prototype uses the following transparent demonstration rule:
**Prototype Opportunity Score = Temperature Difference + (Humidity Difference / 10)**
The current demonstration threshold is:
**Opportunity Score ≥ 5**
Location pairs meeting the threshold are displayed in the opportunity table and classified according to the configured score ranges.
This score is intended only as an analytical demonstration metric and is **not a financial trading recommendation**.
The project's separately documented scoring methodology should be treated as authoritative for the final integrated implementation.

# 10. System Architecture
The overall system follows this workflow:
**Raw CSV Data → Quality Checks → Preprocessing → Temperature/RH Analysis → Climate Differences → Opportunity Analysis → Visualization → Dashboard**
### Data Layer
City-wise temperature and relative-humidity CSV files together with metadata.
### Analytics Layer
Descriptive statistics, temperature and humidity metrics, climate differences, location comparisons and opportunity calculations.
### Visualization Layer
Charts, tables, KPI cards, automated insights and location views.
### Application Layer
Python/Flask integration, data-processing services and application routing.
### Frontend Layer
HTML, CSS and JavaScript dashboard interface.
### Version-Control Layer
Git and GitHub repository with team-specific branches and contributions.

# 11. Team Contributions
## Vaishnavi — Data / Project Coordination
- Dataset inventory and project overview.
- Data cleaning and quality documentation.
- Sensor mapping and statistics.
- Preprocessing.
- Analysis readiness.
- Data relationships.
- Application integration.
- Traceability and provenance.
- City mapping.
- Preparation checklists.
- Dashboard integration.
- Overall project coordination.

## Raghu — Analytics / Statistical Analysis
- Exploratory temperature analysis.
- Statistical insights.
- Humidity analysis.
- Location comparison.
- Climate differences.
- Opportunity criteria and scoring.
- Opportunity thresholds and result fields.
- Baseline comparison.
- Anomaly detection.
- Climate variability analysis.
- Distribution analysis.
- Sensor variation analysis.
- Time-period analysis.
- Opportunity validation.

## Ashwitha — Visualization / Dashboard Design
- Temperature and humidity visualizations.
- Chart mapping.
- Dashboard layout.
- Climate comparison.
- Opportunity display.
- Dashboard components.
- Tables.
- KPI cards.
- Filters.
- Legends.
- Annotations.
- Responsive design.
- Tooltips.
- Navigation.
- Empty-state handling.

## Philomina — Application / Integration
- Data-loader and analysis module structure.
- Module responsibilities.
- Data-flow design.
- Inputs and outputs.
- Processing pipeline.
- Validation.
- Error handling.
- Logging.
- Runtime configuration.
- Dependencies.
- State management.
- Result export.
- Input processing.
- Analysis service.
- Integration and API flow.

# 12. Tools and Technologies
- **Python**
- **Pandas**
- **HTML**
- **CSS**
- **JavaScript**
- **Papa Parse**
- **Chart-based visualizations**
- **Flask**
- **Git**
- **GitHub**
- **GitHub Actions**
- **Dryad Data Repository**

# 13. Results
The completed AtmoSync project produced measurable outputs across the dataset, analytics pipeline and dashboard.
## Dataset Coverage
- **8 urban locations** were successfully identified: Baltimore, Denver, Las Vegas, Los Angeles, Miami, Phoenix, Portland and Tucson.
- The project contains **16 city-level CSV datasets**: 8 temperature files and 8 relative-humidity files.
- **1 Metadata.xlsx** file is included for dataset information.
- An exploratory Baltimore temperature dataset contained **1,968 records and 20 displayed columns**, including timestamp, hour and sensor measurements.
- The system was configured to automatically detect the available city datasets rather than relying on a fixed single-city input.
## Analytical Results
- Temperature and relative-humidity datasets were processed separately and prepared for comparative analysis.
- Temperature and humidity averages were calculated dynamically from the loaded sensor data.
- Climate differences were calculated between locations to identify significant environmental variation.
- With **8 locations**, the system can evaluate **28 unique city-to-city pairs** for comparative opportunity analysis.
- The dashboard ranks location pairs according to the calculated climate-difference score.
## Opportunity Analysis Metrics
The prototype opportunity calculation uses:
**Opportunity Score = Temperature Difference + (Humidity Difference / 10)**
The current demonstration threshold is:
**Opportunity Score ≥ 5**
Location pairs meeting this threshold are displayed in the opportunity table and classified according to the configured score ranges.
This score is used strictly as an analytical demonstration metric and **does not represent a validated financial arbitrage or trading recommendation**.
## Dashboard Results
The final application provides **7 connected dashboard views/modules**:
1. Main Dashboard
2. Climate Analysis
3. Locations
4. Opportunities
5. Data Explorer
6. Analytics Engine
7. Data Quality
The dashboard provides measurable KPIs including:
- Number of detected cities
- Average temperature
- Average relative humidity
- Climate difference/range
- Opportunity count
- Total processed records
- City-level temperature and humidity statistics
- Sensor and record counts
The application also provides:
- Interactive location map
- City directory
- Climate comparison charts
- Temperature and humidity analysis
- Opportunity matrix
- Opportunity result table
- Automated analytical insights
- Data explorer
- Analytics engine
- Data-quality indicators
- Execution status
## Overall Outcome
The project demonstrates an end-to-end analytics workflow:
**16 raw climate CSV files → Data-quality checks → Preprocessing → Temperature/RH analysis → 28 possible city-pair comparisons → Opportunity scoring → Visualization → Interactive dashboard**
The final result is a functional **micro-climate comparative analytics prototype** capable of converting multi-city sensor data into structured metrics, visual comparisons and opportunity signals.

# 14. Limitations
- The opportunity score is a prototype analytical metric, not a financial trading model.
- Sensor counts and structures can vary by location.
- The main dataset is historical observational data.
- The available dataset does not represent real-time weather conditions.
- The project emphasizes comparative analytics and dashboard presentation rather than production-scale forecasting.
- Opportunity signals should not be interpreted as financial recommendations.
- The prototype requires further validation before being used in a production environment.

# 15. Future Scope
Future development can include:
- Integration of the exact documented scoring methodology.
- Automated validation and result export.
- Real-time weather and API inputs.
- Machine-learning prediction or classification.
- Sensor-coordinate-based geospatial analysis.
- Alerts for high-difference locations.
- More advanced anomaly detection.
- Time-series forecasting.
- Production-ready deployment.
- Cloud-based data processing.
- Automated dashboard refresh.
- Real-time environmental monitoring.
- Historical-to-real-time climate comparison.

# 16. Conclusion
AtmoSync establishes a structured micro-climate analytics workflow from raw sensor data to comparative insights and dashboard presentation.
The project organizes multi-city temperature and relative-humidity data, performs data-quality checks, applies statistical and comparative analysis, derives climate-difference measures and presents the results through an interactive dashboard.
The project covers **8 locations, 16 climate CSV datasets and 28 possible city-to-city comparisons**, providing a measurable foundation for comparative climate analysis.
The team divided responsibilities across data management, analytics, visualization and application integration. This division enabled the development of an end-to-end prototype that connects raw observational data with analytical results and dashboard-based decision support.
AtmoSync provides a clear foundation for further development in real-time climate analytics, geospatial analysis, anomaly detection, forecasting and intelligent environmental monitoring.

# 17. References
1. Dryad Data Repository, Urban Microclimate Relative Humidity and Air Temperature Dataset, DOI: **10.5061/dryad.m63xsj47v**.
2. AtmoSync Project GitHub Repository: **vaishnaviakula47/Infotact-major-project**.
3. Project data, analysis, visualization and application artifacts maintained in the project repository.
