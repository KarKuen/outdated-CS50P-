def main():
    prompt = 'Date: '
    outdated(prompt)


def outdated(prompt):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        date = input(prompt)
        try:
            month, day, year = date.strip().split('/')
            if (1 <= int(day) <= 31) and (1 <= int(month) <= 12) and (len(year) == 4):
                day = int(day)
                month = int(month)
                year = int(year)
                print(f"{year}", f"{month:02}", f"{day:02}", sep='-')
                break

        except ValueError:
            try:
                month, day, year = date.split(' ')
                day = day[:-1]
                if (1 <= int(day) <= 31) and (month in months) and (len(year) == 4):
                    month = months.index(month) + 1
                    day = int(day)
                    month = int(month)
                    year = int(year)
                    print(f"{year}", f"{month:02}", f"{day:02}", sep='-')
                    break
            except ValueError:
                pass

        else:
            pass



main()