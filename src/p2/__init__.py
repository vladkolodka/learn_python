import os
import threading
import time

import monitoring
from mprint import print_colored, Color
from mdiagrams import create_line_chart_image, create_scatter_plot_image
from enum import Enum

class ChartType(Enum):
    LINE = 'line'
    SCATTER = 'scatter'

def save_graph(results, chart_type=ChartType.LINE):
    """
    Save the CPU usage graph to a file.
    :param results: List of CPU usage data points.
    :param chart_type: Type of chart to create (ChartType.LINE or ChartType.SCATTER).
    """
    print('Saving graph...')
    
    match chart_type:
        case ChartType.LINE:
            chart_generator = create_line_chart_image
        case ChartType.SCATTER:
            chart_generator = create_scatter_plot_image
        case _:
            raise ValueError(f"Unsupported chart type: {chart_type}")

    chart = chart_generator(results, "CPU Usage Over Time", 'Time (s)', 'CPU Usage (%)')
    
    path = get_next_file_path("images", "cpu_usage")
    
    os.makedirs("images", exist_ok=True)
    with open(path, "wb") as f:
        f.write(chart)

def wait_for_enter():
    event = threading.Event()

    def wait_user_input():
        input()
        event.set()

    print_colored("Press Enter to stop monitoring...", Color.BLUE)
    threading.Thread(target=wait_user_input).start()

    return event

def expiration_event(seconds: int):
    """
    Create an event that will be set after a specified number of seconds.
    :param seconds: Number of seconds to wait before setting the event.
    :return: threading.Event instance that will be set after the specified time.
    """
    event = threading.Event()

    def set_event_after_delay():
        time.sleep(seconds)
        event.set()

    threading.Thread(target=set_event_after_delay).start()
    
    return event

def combine_events(event1: threading.Event, event2: threading.Event) -> threading.Event:
    """
    Combine two events into a single event that is set when either of the two events is set.
    :param event1: First event.
    :param event2: Second event.
    :return: A new threading.Event that is set when either event1 or event2 is set.
    """
    combined_event = threading.Event()

    def monitor_events():
        while not (event1.is_set() or event2.is_set()):
            time.sleep(0.1)  # Polling interval
        combined_event.set()

    threading.Thread(target=monitor_events, daemon=True).start()
    return combined_event

def main():
    root_event = wait_for_enter()
    
    while not root_event.is_set():
        combined_event = combine_events(root_event, expiration_event(5))

        results = monitoring.monitor_until_cancel(combined_event)

        save_graph(results)
        save_graph(results, ChartType.SCATTER)
    
    print_colored("Monitoring stopped.", Color.RED)

def get_next_file_path(directory: str, file_name: str) -> str:
    """
    Get the next available file path in the specified directory.
    :param directory: Directory to check for existing files.
    :param file_name: Base file name (without extension).
    :return: Next available file path.
    """
    base_path = os.path.join(directory, file_name)
    counter = 1
    while os.path.exists(f"{base_path}_{counter}.png"):
        counter += 1
    return f"{base_path}_{counter}.png"

if __name__ == "__main__":
    main()
