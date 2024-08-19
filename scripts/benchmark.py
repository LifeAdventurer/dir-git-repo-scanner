import subprocess
import time


def run_command(command: list[str]) -> tuple[str | None, str | None]:
    try:
        result = subprocess.run(
            command, check=True, capture_output=True, text=True
        )
        return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return e.stdout, e.stderr


def run_and_time(command: list[str]) -> tuple[float, str | None, str | None]:
    start_time = time.perf_counter()
    output, error = run_command(command)
    end_time = time.perf_counter()
    return end_time - start_time, output, error


def main():
    command = ["python", "main.py"]
    execution_time, output, error = run_and_time(command)
    print(f"Execution time: {execution_time: .6f} seconds")
    if error:
        print("Error output:")
        print(error)


if __name__ == "__main__":
    main()
