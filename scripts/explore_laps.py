import fastf1
from pathlib import Path

#Enable FastF1 cache
CACHE_DIR = Path(__file__).resolve().parent.parent / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)
fastf1.Cache.enable_cache(str(CACHE_DIR))

def explore_laps(year: int, gp_name: str, session_type: str):
    """
    Explore laps data for a specific F1 session.
    """
    print(f"\nFetching F1 laps data for {gp_name} {year} {session_type}...\n")
    
    session = fastf1.get_session(year, gp_name, session_type)
    session.load()
    
    # Get all laps from the session
    laps = session.laps
    print(f"\nTotal laps: {len(laps)}")
    
    # Print first few laps
    print("\nFirst few laps:")
    print(laps.head())
    
    # Save laps to CSV
    data_dir = Path(__file__).resolve().parent.parent / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    output_path = data_dir / f"f1_laps_{year}_{gp_name}_{session_type}.csv"
    laps.to_csv(output_path, index=False)
    print(f"\nLaps data saved to {output_path}")

if __name__ == "__main__":
    try:
        year = int(input("Enter the F1 season year (e.g., 2023): "))
        gp_name = input("Enter the Grand Prix name (e.g., 'Bahrain'): ")
        session_type = input("Enter the session type (e.g., FP1, FP2, FP3, Q, R): ").upper()
    except ValueError:
        print("Year, Grand Prix name, and session type must be valid strings.")
        exit(1)
        
    explore_laps(year, gp_name, session_type)