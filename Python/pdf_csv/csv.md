# CSV
CSV stands for comma separated variables. It i a common output for spreadsheet programs.
Example:
- Name, Hours, Rates
- David, 20, 15
- Claire, 40, 20
Things like formulas, images, and macros cannot be in a .csv file. It's possible to export excel files and Google Spreadsheets to .csv, but it will *only* import the information. A .csv file only contains the raw data from the spreadsheet.
## CSV in Python
Python has a built-in csv module, which allows you to grab columns, rows, and values from a .csv file as well as write to a .csv file.
### Other Libraries
Pandas
- Full data analysis library, can work with many tabular data types
- Runs visualizations and analysis
Openpyxl
- Designed specifically for excel files
- Retains many of Excel-specific functionality
- Supports formulas
Google Sheets Python API
- Direct Python interface for working with Google Spreadsheets
- Allows direct changes to the spreadsheets hosted online
- More complex syntax