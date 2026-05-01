# Flow Cytometry Panel Conflict Checker

## What it does
A command line tool that checks a flow cytometry panel for known 
fluorochrome conflict pairs and warns you if any are detected.

## Why I built it
I work with flow cytometers and design multi-color panels regularly. 
As someone early in their computational journey, I wanted to build 
tools that solve real problems I encounter at the bench. This is a 
first step toward a full panel building workflow.

## How to run it
Open your terminal from the folder where your panel CSV file is located:

```bash
python3 panel_checker.py --panel your_panel.csv
```

## Input format
Your CSV file should have two columns: Channel and Fluorochrome - with the channels you're planning to use (FITC, PE, APC, etc) stored under the Channel row and the fluorochromes you're planning to use in the respective channels (CD56, CD16, KIR2DL1, etc.) store under the Fluorochromes row.

## Example output
Warning: FITC and PE are known to have spectral overlapvand may cause issues in your panel design.

## Conflict pairs currently checked
- PE / PE-CF594
- PerCP / PerCP-Cy5.5
- PE-Cy5 / PE-Cy5.5
- FITC / PE

## Coming soon
- Clean up the CSV input irrespective of the format it's used in
- Replace hardcoded conflict pairs with a CSV database
- Check conflicts based on emission wavelength proximity
- Brightness matching recommendations