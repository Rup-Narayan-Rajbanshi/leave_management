
def no_of_days(to_date, from_date):
    """
    Calculate number of days between two dates
    """
    diff = to_date - from_date
    return diff.days + 1

def no_of_leaves(to_date, from_date):
    pass


def filter_leave_dates(date, month):

    if date.month == month:
        return True
    else:
        return False