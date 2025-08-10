import fastf1
import pandas as pd
from pathlib import Path

# Enable local cache to speed up repeated requests
CACHE_DIR = Path(__file__).resolve().parent.parent / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)
fastf1.Cache.enable_cache(str(CACHE_DIR))

def explore_schedule(year: int):
    """
    Fetch and display the F1 event schedule for a given year.
    """
    
    print(f"\nFetching F1 event schedule for {year}...\n")
    schedule = fastf1.get_event_schedule(year)
    
    print(schedule)

    # Save to CSV for later reference
    data_dir = Path(__file__).resolve().parent.parent / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    output_path = data_dir / f"f1_schedule_{year}.csv"
    schedule.to_csv(output_path, index=False)
    print(f"\nSchedule saved to {output_path}")

if __name__ == "__main__":
    try:
        year = int(input("Enter the F1 season year (e.g., 2023): "))
    except ValueError:
        print("Year must be an integer.")
        exit(1)
    
    explore_schedule(year)