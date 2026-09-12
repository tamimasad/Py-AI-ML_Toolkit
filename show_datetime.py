from datetime import datetime


def date_time():
    # Get the current date and time
    now = datetime.now()

    # Format the date and time as a string
    formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_date_time
