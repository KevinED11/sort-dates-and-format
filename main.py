import datetime

def get_dates(dates: list[str | datetime.date]) -> list[datetime.date]:
    if not dates:
        raise ValueError("List is empty")
    return [datetime.datetime.strptime(date, "%Y-%m-%d").date() for date in dates]


def sort_dates(dates: list[datetime.date]) -> list[datetime.date]:
    return sorted(dates)


def format_sort_dates(sort_dates: list[datetime.date]) ->  list[str]:
    return [date.strftime("%d-%m-%Y") for date in sort_dates]


def old_and_new_date(sort_dates: list[str]) -> tuple[str, str]:
    return (sort_dates[0], sort_dates[-1])

if __name__ == "__main__":
    dates = get_dates(["1995-12-17", "2022-04-21", "2005-02-28"])

    sort = sort_dates(dates)
    format_dates = format_sort_dates(sort)
    print(format_dates)
    print(dates)
    print(sort)

    fechas = old_and_new_date(format_dates)
    print(fechas)

