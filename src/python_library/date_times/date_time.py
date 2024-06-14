def convert_to_24_hour_format(twelve_hour_format: str) -> str | False:
    """
    Convert a 12-hour format time string to a 24-hour format time string.

    Parameters:
    time_str (str): A time string in 12-hour format (hh:mm:ssAM or hh:mm:ssPM).

    Returns:
    str: The time string in 24-hour format (HH:mm:ss), or False if the input is invalid.
    """
    if len(twelve_hour_format) != 10:
        return False

    period = twelve_hour_format[-2:]
    time_parts = twelve_hour_format[:-2].split(":")

    if len(time_parts) != 3 or not all(part.isdigit() for part in time_parts):
        return False

    hours, minutes, seconds = map(int, time_parts)

    if not (1 <= hours <= 12) or not (0 <= minutes < 60) or not (0 <= seconds < 60):
        return False

    if period == "AM":
        if hours == 12:
            hours = 0
    elif period == "PM":
        if hours != 12:
            hours += 12
    else:
        return False

    return f"{hours:02}:{minutes:02}:{seconds:02}"
