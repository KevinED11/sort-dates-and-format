import datetime

def get_dates(dates: list[str | datetime.date]) -> list[datetime.date]:
    if not dates:
        raise ValueError("List is empty")
    return [datetime.datetime.strptime(date, "%Y-%m-%d").date() for date in dates]


def sort_dates(dates: list[datetime.date]) -> list[datetime.date]:
    return sorted(dates)


def format_dates(dates: list[datetime.date], format: str = "%d-%m-%Y") -> list[str]:
    return [date.strftime(format) for date in dates]


def old_and_new_date(sort_dates: list[str]) -> tuple[str, str]:
    if len(sort_dates) < 2:
        raise ValueError("List must have at least 2 dates")
    return (sort_dates[0], sort_dates[-1])



if __name__ == "__main__":
    dates = get_dates(["1995-12-17", "2022-04-21", "2005-02-28"])

    sort_dates = sort_dates(dates)
    format_dates = format_dates(sort_dates, "%d-%m-%Y")
    print(format_dates)
    print(dates)
    print(sort_dates)

    old_date, new_date = old_and_new_date(format_dates)
    print("Oldest date:", old_date)
    print("Newest date:", new_date)
    print(datetime.datetime.now())

