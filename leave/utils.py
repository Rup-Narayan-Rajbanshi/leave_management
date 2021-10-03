
def no_of_days(to_date, from_date):
    """
    Calculate number of days between two dates
    """
    diff = to_date - from_date
    return diff.days + 1