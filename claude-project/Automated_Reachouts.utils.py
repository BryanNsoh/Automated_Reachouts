import pytz
from datetime import datetime, timezone


def get_utc_scheduled_time(day, tz_string, year=2024, month=1, hour=8, minute=0):
    # Specify the local timezone
    local_tz = pytz.timezone(tz_string)

    # Create a datetime object in the specified timezone
    local_time = local_tz.localize(datetime(year, month, day, hour, minute))

    # Convert the time to UTC
    utc_time = local_time.astimezone(timezone.utc)

    # Format it as an RFC3339 string
    return utc_time.isoformat()
