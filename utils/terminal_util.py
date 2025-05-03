import subprocess

def run_cmd(command: str, shell=True) -> str:
    result = subprocess.run(command, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {command}\nError: {result.stderr}")
    return result.stdout.strip()
