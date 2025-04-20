import threading
import psutil


def monitor_until_cancel(stop_event) -> list[float]:
    """
    Monitor CPU usage until the user cancels it (e.g., via a keyboard interrupt).
    :param stop_event: threading.Event instance to signal when to stop monitoring.
    :return: list of CPU usage measurements over the monitoring period.
    """
    cpu_usage: list[float] = []

    def monitor():
        while not stop_event.is_set():
            cpu_usage.append(psutil.cpu_percent(interval=0.2))

    monitor_thread = threading.Thread(target=monitor)
    monitor_thread.start()

    stop_event.wait()  # Wait until the stop_event is set
    monitor_thread.join()  # Wait for the thread to finish

    return cpu_usage  # Return the list of measurements
