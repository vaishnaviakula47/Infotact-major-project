# Application Data Flow

The Autosync application will process data through several stages.

## Stage 1 - Dataset

Temperature and relative humidity datasets are stored in the data directory.

## Stage 2 - Data Loading

The data loader module loads the required datasets.

## Stage 3 - Data Processing

The loaded data is passed to analysis modules.

## Stage 4 - Analysis

Temperature, humidity and location-level information can be analyzed.

## Stage 5 - Results

The processed results can be provided to the visualization or application layer.

## Overall Flow

Dataset
↓
Data Loader
↓
Data Processing
↓
Analysis
↓
Results
↓
Visualization / Application
Commit message:
Document application data flo
