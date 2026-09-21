# Module Responsibilities

The Autosync source code is divided into modules with separate responsibilities.

## data_loader.py

Responsible for loading project datasets from the data directory.

## analysis.py

Responsible for processing the loaded data and performing analysis.

## config.py

Contains configuration values such as dataset paths.

## Future Analysis Modules

Additional modules can later be added for:

- Temperature analysis
- Humidity analysis
- Location comparison
- Microclimate analysis
- Arbitrage calculations

## Purpose

Separating responsibilities into modules will make the application easier to maintain and extend.
