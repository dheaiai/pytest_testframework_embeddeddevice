import datetime

def format_date(date_obj, format_str="%Y-%m-%d"):
    """Formats a datetime object to a string."""
    return date_obj.strftime(format_str)

def parse_date(date_str, format_str="%Y-%m-%d"):
    """Parses a date string into a datetime object."""
    return datetime.datetime.strptime(date_str, format_str)

def format_number(number, decimals=2):
    """Formats a number to the specified decimal places."""
    return f"{number:.{decimals}f}"

def format_percentage(number, decimals=2):
    """Formats a float as a percentage string."""
    return f"{number * 100:.{decimals}f}%"

def capitalize_words(text):
    """Capitalizes each word in a string."""
    return text.title()

def snake_to_camel(snake_str):
    """Converts snake_case to camelCase."""
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def camel_to_snake(camel_str):
    """Converts camelCase to snake_case."""
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

# Example usage
if __name__ == "__main__":
    print("Formatted Date:", format_date(datetime.datetime.now()))
    print("Parsed Date:", parse_date("2025-04-30"))
    print("Formatted Number:", format_number(123.456789))
    print("Formatted Percentage:", format_percentage(0.8765))
    print("Capitalized:", capitalize_words("hello world"))
    print("Snake to Camel:", snake_to_camel("test_logger"))
    print("Camel to Snake:", camel_to_snake("testLogger"))
