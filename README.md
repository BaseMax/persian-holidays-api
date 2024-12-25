# Persian Holidays API

An API for fetching Persian (Shamsi), Gregorian, and Hijri holidays. The project scrapes holiday data from the `time.ir` website, processes the data, and outputs it as JSON files. This API allows developers to retrieve holiday data for any given year and month, with the dates converted into both Persian and English digits.

### Demo: https://basemax.github.io/persian-holidays-api/holidays.json

## Features

- Fetches holidays for a given year and month.
- Converts dates into Shamsi, Gregorian, or Hijri formats.
- Handles both Persian and Arabic digits, converting them into English digits.
- Outputs holiday data as structured JSON files.

## Requirements

To run this project, you'll need the following Python packages:

- `requests`
- `beautifulsoup4`
- `re` (for regex operations)

You can install the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### How It Works

The script scrapes the holiday data from the website time.ir. It retrieves the list of holidays for a given year and month, then processes the data by:

- Identifying whether each event is a holiday.
- Extracting the event name.
- Converting the event date into Persian (Shamsi), Gregorian, or Hijri format.
- Converting Persian and Arabic digits to English digits.
- Saving the holiday data in JSON format.

### Example of JSON Output

Here is an example of what the JSON output looks like:

```json
[
    {
        "is_holiday": true,
        "event_name": "جشن نوروز/جشن سال نو",
        "date": {
            "type": "shamsi",
            "date": [
                "1",
                "فروردین"
            ]
        }
    },
    {
        "is_holiday": false,
        "event_name": "روز جهانی شادی",
        "date": {
            "type": "gregorian",
            "date": [
                "20",
                "March"
            ]
        }
    },
    {
        "is_holiday": true,
        "event_name": "عیدنوروز",
        "date": {
            "type": "shamsi",
            "date": [
                "2",
                "فروردین"
            ]
        }
    }
]
```

### JSON Schema

The structure of the JSON file is as follows:

- `is_holiday`: A boolean indicating whether the event is a holiday.
- `event_name: The name of the event in Persian.
- `date:
  - `type`: The type of the date (either "shamsi", "gregorian", or "hijri").
  - `date`: A list containing the day and month of the event. For Shamsi dates, the month is in Persian, while for Gregorian and Hijri dates, the month is in English.

### Example Usage

To fetch holidays for a specific year and month:

```python
from persianholiday import get_for_a_month

# Specify the year and month
year = 1403  # Persian year
month = 1    # January

holidays = get_for_a_month(year, month)
print(holidays)
```

This will fetch the holidays for the specified month and year and output the holidays in the structure defined above.

### File Structure

```bash
C:\Files\Projects\persian-holidays-api
├── .git
├── .gitignore
├── LICENSE
├── README.md
├── holidays-1.json
├── holidays-2.json
├── holidays-3.json
├── holidays-4.json
├── holidays-5.json
├── holidays-6.json
├── holidays-7.json
├── holidays-8.json
├── holidays-9.json
├── holidays-10.json
├── holidays-11.json
├── holidays-12.json
├── holidays.json
├── requirements.txt
├── test.py
├── update.py
└── persianholiday.py
```

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Contributing

Feel free to fork the repository and submit pull requests for improvements. If you encounter any issues, please report them via the Issues section.

Copyright 2024, Max Base
