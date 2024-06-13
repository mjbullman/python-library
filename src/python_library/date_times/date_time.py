def convert_to_24_hour_format(twelve_hour_format: str) -> str:
    """
    Converts a 12-hour AM/PM time format string to a 24-hour time format string.

    Parameters:
    twelve_hour_format (str): A string representing time in 12-hour format (hh:mm:ssAM or hh:mm:ssPM).

    Returns:
    str: A string representing time in 24-hour format (HH:mm:ss) or false.

    Example:
    convert_to_24_hour_format("07:05:45PM")  # Returns "19:05:45"
    convert_to_24_hour_format("12:40:22AM")  # Returns "00:40:22"
    convert_to_24_hour_format("12:40:22PM")  # Returns "12:40:22"
    convert_to_24_hour_format("01:05:45AM")  # Returns "01:05:45"
    """

    result = ""
    max_minutes = 60
    max_seconds = 60
    twelve_hours = 12
    time_parts_length = 3
    twelve_hour_format_length = 10

    if len(twelve_hour_format) == twelve_hour_format_length:
        # split the time into components without the last two characters (AM/PM).
        time_parts = twelve_hour_format[:-2].split(":")

        if len(time_parts) == time_parts_length:
            # extract the AM/PM part from the last two characters.
            am_pm = twelve_hour_format[-2:].upper()

            if am_pm in ['AM', 'PM']:
                try:
                    hours = int(time_parts[0])
                    minutes = int(time_parts[1])
                    seconds = int(time_parts[2])

                    if 1 <= hours <= twelve_hours and 0 <= minutes < max_minutes and 0 <= seconds < max_seconds:
                        if am_pm == 'AM':
                            if hours == twelve_hours:
                                hours = 0
                        else:
                            if hours != twelve_hours:
                                hours += twelve_hours

                        hours_str = f'{hours:02}'
                        minutes_str = f'{minutes:02}'
                        seconds_str = f'{seconds:02}'

                        # Set the result to the converted time in 24-hour format.
                        result = f'{hours_str}:{minutes_str}:{seconds_str}'
                except ValueError:
                    pass

    return result
