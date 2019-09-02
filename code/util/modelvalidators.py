from util.validators import in_length, is_date, is_time, is_int, verify_time_diff_positive, min_length, max_length


def validate_schedule(data):
    error = ""

    if not in_length(data["schedule_name"], 3, 80):
        error = "Invalid schedule name.  Name must be from 3 to 80 characters."
    if not is_date(data["schedule_date"]):
        error = "Invalid schedule date.  MaidSchedule date must be valid datetime."
    if not is_time(data["start_time"]):
        error = "Invalid schedule start time.  MaidSchedule start time must be valid time."
    if not is_time(data["end_time"]):
        error = "Invalid schedule end time.  MaidSchedule end time must be valid time."
    if not is_int(data["post_clean_buffer"]):
        error = "Invalid schedule post clean time.  MaidSchedule post clean time must be valid number of minutes."
    if not verify_time_diff_positive(data["start_time"], data["end_time"]):
        error = "Invalid start and end time entry.  Start time must be before end time."
    return error


def validate_bnblisting(data):
    error = ""

    if not in_length(data["title"], 3, 80):
        error = "Invalid title.  Title must be from 3 to 80 characters."
    if not in_length(data["summary"], 3, 240):
        error = "Invalid summary.  Summary must be from 3 to 240 characters."
    if not min_length(data["content"].strip(), 10):
        error = "Invalid content.  Content must be at least 10 characters."
    if "active" in data and not is_int(data['active']):
        error = "Invalid active entry.  'Active' entry must be an integer."
    if "archived" in data and not is_int(data['archived']):
        error = "Invalid archived entry.  'Archived' entry must be an integer."
    if not is_int(data['bedrooms']):
        error = "Invalid bedrooms entry.  'Bedrooms' entry must be an integer."
    if not is_int(data['bathrooms']):
        error = "Invalid bathrooms entry.  'Bathrooms' entry must be an integer."
    if not in_length(data["street_address_1"], 3, 80):
        error = "Invalid street address 1.  'Street address 1' must be from 3 to 80 characters."
    if data['street_address_2'] and not max_length(data["street_address_2"], 80):
        error = "Invalid street address 2.  'Street address 2' must be 80 characters or less."
    if not in_length(data["city"], 3, 80):
        error = "Invalid city entry.  'City' must be from 3 to 80 characters."
    if not in_length(data["state"], 2, 80):
        error = "Invalid state entry.  'State' must be from 2 to 80 characters."
    if not in_length(data["zip_code"], 5, 20):
        error = "Invalid zip code entry.  'Zip code' must be from 5 to 20 characters."
    if not in_length(data["square_footage"], 2, 20):
        error = "Invalid square footage entry.  'Square footage' must be from 2 to 20 characters."
    return error


def validate_maidplan(data):
    error = ""

    if not in_length(data["title"], 3, 80):
        error = "Invalid title.  Title must be from 3 to 80 characters."
    if not in_length(data["summary"], 3, 240):
        error = "Invalid summary.  Summary must be from 3 to 240 characters."
    if not min_length(data["description"].strip(), 10):
        error = "Invalid content.  Content must be at least 10 characters."
    return error
