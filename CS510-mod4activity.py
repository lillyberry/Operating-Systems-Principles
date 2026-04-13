"""
A program that prints basic CPU and memory details
using the psutil library.

The display part is provided. The first three
functions retrieve real system information.

Modify as you like. Experimentation is encouraged.
"""

import psutil


def get_cpu_usage():
    """
    Return the current CPU usage percentage.
    psutil.cpu_percent() measures CPU utilization.
    """
    return psutil.cpu_percent(interval=1)


def get_cpu_count():
    """
    Return the number of logical CPU cores
    detected on the system.
    """
    return psutil.cpu_count(logical=True)


def get_memory_stats():
    """
    Return total memory, used memory, and available memory
    in gigabytes for readability.

    Uses psutil.virtual_memory().
    """
    BYTES_PER_GB = 1024 ** 3

    memory = psutil.virtual_memory()

    total = memory.total / BYTES_PER_GB
    used = memory.used / BYTES_PER_GB
    available = memory.available / BYTES_PER_GB

    return total, used, available


def display_resource_report():
    """
    Display a formatted report of CPU and memory information.
    """
    mem_total, mem_used, mem_available = get_memory_stats()

    print("\n===== System Resource Report =====")
    print(f"CPU Usage: {get_cpu_usage():5.1f}%")
    print(f"CPU Cores: {get_cpu_count()}")
    print(f"Total Memory: {mem_total:5.2f} GB")
    print(f"Memory Usage: {mem_used:5.2f} GB")
    print(f"Memory Available: {mem_available:5.2f} GB")
    print("===================================\n")


def main():
    """
    Program entry point.
    """
    display_resource_report()


if __name__ == "__main__":
    main()