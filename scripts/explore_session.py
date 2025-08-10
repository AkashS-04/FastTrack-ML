import fastf1
from pathlib import Path

#Enable FastF1 cache
CACHE_DIR = Path(__file__).resolve().parent.parent / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)
fastf1.Cache.enable_cache(str(CACHE_DIR))

def explore_session(year: int, gp_name: str, session_type: str):
    """
    Explore a specific F1 session.
    :param year: e.g., 2023
    :param gp_name: Grand Prix name, e.g., "Bahrain"
    :param session_type: 'FP1', 'FP2', 'FP3', 'Q', 'R'
    """
    print(f"\nFetching F1 session data for {gp_name} {year} {session_type}...\n")
    
    session = fastf1.get_session(year, gp_name, session_type)
    session.load()
    
    print("=== Session Info ===")
    print(session)  # Quick summary
    print(session.event)
    print("\nDate:", session.date)
    print("\nTrack:", session.event.EventName)
    print("\nLocation:", session.event.Location)
    print("Country:", session.event.Country)
    print("Session Type:", session.name)
    print("Weather Data Available:", session.weather_data)

if __name__ == "__main__":
    try:
        year = int(input("Enter the F1 season year (e.g., 2023): "))
        gp_name = input("Enter the Grand Prix name (e.g., 'Bahrain'): ")
        session_type = input("Enter the session type (e.g., FP1, FP2, FP3, Q, R): ").upper()
    except ValueError:
        print("Year, Grand Prix name, and session type must be valid strings.")
        exit(1)
        
    explore_session(year, gp_name, session_type)