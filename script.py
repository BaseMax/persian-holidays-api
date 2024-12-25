from bs4 import BeautifulSoup
import re
import requests
from typing import List
import json


def contains_persian_or_arabic_digits(text: str) -> bool:
	# \u06F0-\u06F9 covers Persian digits.
	# \u0660-\u0669 covers Arabic digits.
	pattern = r'[\u06F0-\u06F9\u0660-\u0669]'
	
	if re.search(pattern, text):
		return True
	return False


def convert_to_english_digits(text: str) -> str:
	digit_map = str.maketrans(
		'٠١٢٣٤٥٦٧٨٩' + '۰۱۲۳۴۵۶۷۸۹',
		'01234567890123456789'
	)
	
	return text.translate(digit_map)


def get_for_a_month(year: int, month: int) -> List[str]:
	month_str = f"{month:02d}"

	cookies = {
		'ASP.NET_SessionId': 'mz1qqyodkh1xwowdo3lbib4b',
		'__AntiXsrfToken': '282305cb073f4068bbd0c8b7b60ff481',
		'City': '95',
		'Province': '8',
	}

	headers = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'en-US,en;q=0.9,fa;q=0.8,it;q=0.7',
		'cache-control': 'max-age=0',
		'priority': 'u=0, i',
		'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'none',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
	}

	response = requests.get(f'https://www.time.ir/fa/event/list/0/{year}/{month_str}', cookies=cookies, headers=headers)

	text = response.text

	f = open(f"data-{year}-{month_str}.html", "w", encoding="utf-8")
	f.write(text)
	f.close()

	soup = BeautifulSoup(text, 'html.parser')

	holiday_elements = soup.select('ul.list-unstyled li')

	holidays = []

	for element in holiday_elements:
		is_holiday = "eventHoliday" in element.get("class", [])
		event_name = ''.join([str(child) for child in element.children if isinstance(child, str)]).strip()

		event_date_span = element.select_one('span')
		event_date = event_date_span.get_text(strip=True).strip() if event_date_span else "No Date"

		event_bracket_text_span = element.select_one('span[style="white-space: nowrap"]')
		bracket_text = event_bracket_text_span.get_text(strip=True).strip().lstrip('[').rstrip(']').strip() if event_bracket_text_span else ""

		if bracket_text == "":
			date = {
				"type": "shamsi",
				"date": convert_to_english_digits(event_date).split(" ")
			}
		else:
			date = {
				"type": "hijri" if contains_persian_or_arabic_digits(bracket_text) else "gregorian",
				"date": convert_to_english_digits(bracket_text).split(" ")
			}

		holidays.append({
			"is_holiday": is_holiday,
			"event_name": convert_to_english_digits(event_name),
			"date": date
		})

	with open(f'holidays-{month_str}.json', 'w', encoding='utf-8') as json_file:
		json.dump(holidays, json_file, ensure_ascii=False, indent=4)

	return holidays


year = 1403
max_month = 1
max_month = 12
for month in range(1, max_month + 1):
	print(month)

	days = get_for_a_month(year, month)
	print(days)
