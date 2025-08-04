# elevateLabsInternship

# Data Cleaning and Preprocessing - Walmart Sales Data

This repository contains the results of Task 1: Data Cleaning and Preprocessing for the Walmart Sales dataset.

## Objective

The objective of this task was to clean and prepare a raw dataset (Walmart Sales Data) by handling common data quality issues such as nulls, duplicates, inconsistent formats, and incorrect data types, making it ready for analysis.

## Dataset

The original dataset used is `Walmart_Sales.csv`.

## Tools Used

* Python (Pandas library)

## Data Cleaning Steps and Changes Made

The following data cleaning and preprocessing steps were performed on the `Walmart_Sales.csv` dataset:

1.  **Initial Data Inspection:**
    * The dataset was loaded and inspected to understand its structure, column names, and initial data types.
    * It was observed that the dataset contained 6435 entries and 8 columns.

2.  **Handling Missing Values:**
    * A check for missing values across all columns was performed.
    * **Change:** No missing values were found in any column, so no action (imputation or removal) was required for this step.

3.  **Removing Duplicate Rows:**
    * The dataset was checked for any exact duplicate rows.
    * **Change:** No duplicate rows were found in the dataset, so no rows were removed.

4.  **Date Format Conversion:**
    * The `Date` column was initially of `object` (string) data type.
    * **Change:** The `Date` column was successfully converted to `datetime64[ns]` format, which is essential for proper time-series analysis and any date-based operations.

5.  **Standardizing Column Headers:**
    * The column names were reviewed for consistency and readability.
    * **Change:** All column headers were standardized to a uniform format:
        * Spaces within column names were replaced with underscores (`_`).
        * All characters in the column names were converted to lowercase.
        * For example, `Weekly_Sales` was changed to `weekly_sales`, `Holiday_Flag` to `holiday_flag`, etc.

6.  **Checking and Fixing Data Types:**
    * The data types of all columns were verified.
    * **Change:** Apart from the `Date` column (as mentioned above), all other numerical columns (`Store`, `Weekly_Sales`, `Holiday_Flag`, `Temperature`, `Fuel_Price`, `CPI`, `Unemployment`) were already in appropriate numerical data types (`int64` or `float64`) and did not require further modification.

## Deliverables

* `Walmart_Sales.csv`: The original raw dataset.
* `cleaned_walmart_sales_data.csv`: The cleaned and preprocessed dataset.
* `data_cleaning_script.py` (or `data_cleaning_notebook.ipynb`): The Python code/notebook demonstrating all cleaning steps.
* `README.md`: This summary document.

## Conclusion

The data cleaning and preprocessing steps have resulted in a clean, structured `cleaned_walmart_sales_data.csv` dataset that is ready for further analysis, visualization, or modeling.
