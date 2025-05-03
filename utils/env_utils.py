import os

def load_env_file(env_path=".env"):
    """
    Loads key-value pairs from a .env file into environment variables.
    """
    if not os.path.exists(env_path):
        print(f"Environment file '{env_path}' not found.")
        return

    with open(env_path, "r") as file:
        for line in file:
            if line.strip() == "" or line.strip().startswith("#"):
                continue
            if "=" in line:
                key, value = line.strip().split("=", 1)
                os.environ.setdefault(key.strip(), value.strip())

def get_env_variable(key, default=None):
    """
    Retrieves an environment variable with a default fallback.
    """
    return os.getenv(key, default)

def require_env_variable(key):
    """
    Retrieves a required environment variable or raises an exception.
    """
    value = os.getenv(key)
    if value is None:
        raise EnvironmentError(f"Required environment variable '{key}' is not set.")
    return value

# Example usage
if __name__ == "__main__":
    load_env_file()
    print("API_URL:", get_env_variable("API_URL", "https://default.local"))
    print("DB_HOST (required):", require_env_variable("DB_HOST"))  # Will raise error if not set
