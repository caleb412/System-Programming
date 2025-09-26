import inotify
import inotify.adapters
import os
from datetime import datetime


def monitor_downloads():
    watch_path = r"C:\Users\Caleb\Downloads\tmp"

    if not os.path.exists(watch_path):
        os.makedirs(watch_path)
        print(f"Created directory: {watch_path}")

    i = inotify.adapters.Inotify()
    i.add_watch(watch_path)

    print(f"Monitoring for file changes in: {watch_path}")
    print("Press Ctrl+C to stop monitoring\n")

    try:
        for event in i.event_gen(yield_nones=False):
            (_, type_names, path, filename) = event
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print(f"[{timestamp}] PATH: {path} FILE: {filename} EVENTS: {type_names}")

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")


if __name__ == '__main__':
    monitor_downloads()