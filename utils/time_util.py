import time
from datetime import datetime, timedelta

def wait_for_seconds(seconds: int):
    time.sleep(seconds)

def get_current_timestamp():
    """Returns the current timestamp in ISO format."""
    return datetime.now().isoformat()

def get_readable_time(format="%Y-%m-%d %H:%M:%S"):
    """Returns the current time in a readable string format."""
    return datetime.now().strftime(format)

def measure_execution_time(func):
    """Decorator to measure the execution time of a function."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' executed in {end - start:.4f} seconds.")
        return result
    return wrapper

def sleep_for_seconds(seconds):
    """Pauses execution for a specified number of seconds."""
    print(f"Sleeping for {seconds} seconds...")
    time.sleep(seconds)

def get_time_after_minutes(minutes):
    """Returns a datetime object after a specified number of minutes from now."""
    return datetime.now() + timedelta(minutes=minutes)

# Example usage
if __name__ == "__main__":
    print("Current Timestamp:", get_current_timestamp())
    print("Readable Time:", get_readable_time())
    print("Time after 10 minutes:", get_time_after_minutes(10))

    @measure_execution_time
    def example_task():
        time.sleep(2)

    example_task()
