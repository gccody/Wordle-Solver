import requests
from datetime import datetime

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


def save_date(y: int, m: int, d: int, sol: str):
    with open('solutions.txt', 'a') as f:
        f.write(f"{months[m]} {d}{'st' if d == 1 else 'nd' if d == 2 else 'rd' if d == 3 else 'th'}, {y}: {sol}\n")


today = datetime.today()

y = today.year
m = today.month
d = today.day

res = requests.get(f"https://www.nytimes.com/svc/wordle/v2/{y}-{m}-{d}.json")

save_date(y, m, d, res.json()['solution'])

print(res.json()['solution'])
