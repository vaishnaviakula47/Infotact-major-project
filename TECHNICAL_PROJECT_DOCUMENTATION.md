# TECHNICAL PROJECT DOCUMENTATION

# AtmoSync: Micro-Climate Arbitrage Analytics

**Infotact Solutions Internship**

# 1. Project Overview
AtmoSync processes multi-city temperature and relative-humidity sensor data and presents comparative climate analytics through an interactive dashboard.
The project follows an end-to-end workflow from dataset organization and data-quality checks to statistical analysis, climate comparison, opportunity scoring, visualization and dashboard presentation.

# 2. Repository Structure
| Path | Purpose |
|---|---|
| `data/` | Raw datasets and data documentation |
| `notebooks/` | Exploration, statistics and analytical methodology |
| `visualizations/` | Charts, dashboard design and visualization guidelines |
| `src/` | Application modules and integration structure |
| `templates/` | Flask dashboard templates |
| `index.html` | Dashboard frontend prototype |
| `app.py` | Flask application and dashboard routing |
| `requirements.txt` | Python dependency declaration |
| `.github/workflows/` | Automation workflow area |

# 3. Data Files
The project contains city-wise temperature and relative-humidity datasets for eight urban locations.
- Baltimore: `baltimore_temp.csv`, `baltimore_rh.csv`
- Denver: `denver_temp.csv`, `denver_rh.csv`
- Las Vegas: `las_vegas_temp.csv`, `las_vegas_rh.csv`
- Los Angeles: `los_angeles_temp.csv`, `los_angeles_rh.csv`
- Miami: `miami_temp.csv`, `miami_rh.csv`
- Phoenix: `phoenix_temp.csv`, `phoenix_rh.csv`
- Portland: `portland_temp.csv`, `portland_rh.csv`
- Tucson: `tucson_temp.csv`, `tucson_rh.csv`
- `Metadata.xlsx`
In total, the project contains **16 city-level CSV datasets**, consisting of 8 temperature files and 8 relative-humidity files.

# 4. Data Structure
Temperature and RH files contain `Date - Time`, `hour` and multiple sensor-related numeric columns.
Temperature and relative humidity are maintained as separate city-wise datasets to support independent processing and comparative analysis.

# 5. Data Quality Workflow
The project follows these data-quality checks:
1. Check file availability and city/measurement pairing.
2. Check timestamp and sensor columns.
3. Check missing values.
4. Check duplicate records.
5. Check timestamp consistency.
6. Check invalid temperature values.
7. Check relative-humidity range.
8. Preserve raw files.
9. Store derived data separately.
10. Validate numeric sensor values before calculations.
The raw datasets are preserved separately from derived analytical outputs to improve traceability and reproducibility.

# 6. Analytics Modules
| Module | Purpose |
|---|---|
| Temperature analysis | Descriptive statistics, sensor variation and location comparison |
| Humidity analysis | RH metrics and location variation |
| Climate comparison | Temperature and humidity differences |
| Opportunity analysis | Criteria, thresholds, scoring and ranked signals |
| Anomaly/variability analysis | Unusual and variable climate behaviour |
| Time-period analysis | Climate behaviour across time periods |
The analytical workflow supports comparison across **8 locations**, resulting in **28 possible unique city-to-city pairs**.

# 7. Dashboard Components
The dashboard includes the following components:
- Project branding/header
- Location selector or location views
- Temperature/RH KPI cards
- Climate-difference indicator
- Opportunity count
- Climate comparison chart
- Temperature-vs-humidity chart
- Temperature trend
- Opportunity table
- Sensor summary
- Automated insights
- Execution status
- Interactive map/city directory
- Data Explorer
- Analytics Engine
- Data Quality dashboard
The dashboard is organized into separate views so that climate analysis, locations, opportunities, data exploration, analytics and data quality can be inspected independently.

# 8. Application Integration
The application structure includes `data_loader.py`, `analysis.py` and `config.py` for data loading, analytical processing and runtime configuration.
The application workflow covers:
- Data loading
- Data validation
- Analysis processing
- Error handling
- Logging
- Runtime configuration
- Dependency management
- State management
- Result generation/export
- Service flow
- Flask integration
Flask integration was developed to scan city CSV files and serve dashboard routes. During testing, the server successfully detected **eight cities**, and template integration was subsequently corrected during the application development process.

# 9. Frontend Prototype
The HTML/JavaScript dashboard loads project CSV files using Papa Parse and calculates dashboard values dynamically.
The frontend prototype supports:
- Dynamic city detection
- Temperature and RH calculations
- Climate comparison
- Opportunity calculation
- Charts
- KPI cards
- Tables
- Automated insights
- Location information
The dashboard should be served through GitHub Pages, Flask or another local web server rather than opened directly through `file://`.

# 10. Opportunity Score
The dashboard prototype uses the following transparent analytical formula:
**Prototype Score = |Temperature Difference| + |Humidity Difference| / 10**
A prototype threshold of:
**Score ≥ 5**
was used to identify higher-scoring location comparisons.
The score is intended for **analytical demonstration only** and must not be represented as a validated financial arbitrage algorithm or financial recommendation.

# 11. GitHub Workflow
The project follows a structured GitHub workflow:
1. Select the correct branch.
2. Create or edit files through the GitHub web interface.
3. Use clear, task-specific commit messages.
4. Commit changes to the intended branch.
5. Use pull requests when integrating branches.
6. Keep team contributions distinct.
7. Keep the `main` branch stable before final integration.
8. Review changes before final submission.

# 12. Testing Checklist
The following checks are used before final demonstration:
- All expected city files exist.
- CSV files load successfully.
- Numeric sensor values are recognized.
- Averages are calculated dynamically.
- Location differences are generated.
- Opportunity table populates.
- Charts render without errors.
- Dashboard works through a web server or deployed environment.
- Flask routes and template paths match when the backend version is used.
- Data-quality checks execute correctly.
- Final score matches the documented methodology.
- Dashboard modules load without broken navigation.

# 13. Implementation Status
| Area | Status |
|---|---|
| Dataset organization | Completed/documented |
| Data-quality documentation | Completed/documented |
| Exploratory/statistical analysis | Completed across analysis artifacts |
| Visualization design | Completed |
| HTML/JavaScript dashboard prototype | Implemented |
| Python application structure | Created/documented |
| Flask integration | Developed and integrated |
| Dashboard routing | Implemented |
| GitHub Actions | Explored; dependency requirements addressed |
| Validated financial arbitrage model | Not claimed |

# 14. Final Demonstration Flow
The final project demonstration follows this sequence:
1. Open the AtmoSync dashboard.
2. Show the detected city datasets.
3. Show temperature and humidity KPIs.
4. Show location comparison.
5. Show the temperature/humidity relationship.
6. Show the opportunity table and explain the prototype score.
7. Show sensor and record summaries.
8. Show automated analytical insights.
9. Show Data Explorer and Data Quality views.
10. Explain the data-to-dashboard pipeline.
11. Explain team contributions.
12. Explain limitations and future scope.

# 15. Reporting Note
The final report must clearly distinguish between:
- Implemented features
- Documented methodology
- Analytical prototypes
- Application integration
- Future work
The prototype opportunity score should not be described as a validated financial arbitrage algorithm or financial trading recommendation.
The project focuses on comparative micro-climate analytics and dashboard-based analytical decision support.

# 16. Final Conclusion
The technical work separates data, analytics, visualization and application responsibilities and provides a reproducible foundation for AtmoSync.
The project covers **8 urban locations, 16 climate CSV datasets and 28 possible city-to-city comparisons**.
The workflow connects raw climate data with quality checks, statistical analysis, climate comparison, opportunity scoring, visualization and an interactive dashboard.
The remaining development focus is on maintaining formula alignment, validating the integrated application, improving execution reliability and extending the analytical capabilities rather than adding unnecessary documentation.
