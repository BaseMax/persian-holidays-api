from persianholiday import get_for_a_month
import json

YEAR = 1403
MAX_MONTH = 12

all_holidays = []

for month in range(1, MAX_MONTH + 1):
	print(month)

	holidays = get_for_a_month(YEAR, month)
	print(holidays)

	# with open(f'holidays-{month}.json', 'w', encoding='utf-8') as json_file:
	# 	json.dump(holidays, json_file, ensure_ascii=False, indent=4)

	all_holidays += holidays

with open(f'holidays.json', 'w', encoding='utf-8') as json_file:
	json.dump(all_holidays, json_file, ensure_ascii=False, indent=4)
