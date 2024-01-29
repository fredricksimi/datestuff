import datefinder
date_inputs = [
    # "19th September 2022 - 21th October 2022",
    # "19th September 2022-22th October 2022",
    # "19th September 2022 to 25th October 2022",
    # "I have been working from 3rd Aug 2022 to 9th Sep 2022 and I haven't been paid yet"
    "10th May 1994",
    "My name - John, - 10th September 2022 TO 21th October 2022 - am a prisoner",
    ""
]

def split_date(date_text):
    for text in date_text:
        date_parts = text.split('-')
        new_date_parts = [part.strip() for part in date_parts]
        new_date_string = " to ".join(new_date_parts)
        date_list = []
        matches = datefinder.find_dates(new_date_string)
        for match in matches:
            date_list.append(match)
        if len(date_list) > 1:
            no_of_days = (date_list[1] - date_list[0]).days
            print(f"{date_list[0].date()} to {date_list[1].date()} is {no_of_days} days")
        elif len(date_list) == 1:
            print((date_list[0]).strftime("%Y-%m-%d"))

split_date(date_inputs)

