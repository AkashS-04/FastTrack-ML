import fastf1
import matplotlib.pyplot as plt
from pathlib import Path

#Enable FastF1 cache
CACHE_DIR = Path(__file__).resolve().parent.parent / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)
fastf1.Cache.enable_cache(str(CACHE_DIR))

def explore_telemetry(year: int, gp_name: str, session_type: str, driver: str):
    """
    Explore telemetry data for a specific driver's fastest lap in a session.
    """
    print(f"\nFetching F1 telemetry data for {driver} in {gp_name} {year} {session_type}...\n")
    
    session = fastf1.get_session(year, gp_name, session_type)
    session.load()
    
    # Get laps for the driver
    driver_laps = session.laps.pick_driver(driver)
    print(f"Retrieved {len(driver_laps)} laps for {driver}")

    # Find fastest lap
    fastest_lap = driver_laps.pick_fastest()
    print(f"Fastest Lap Time: {fastest_lap['LapTime']}")

    # Get telemetry for fastest lap
    telemetry = fastest_lap.get_car_data().add_distance()
    print("\n=== Telemetry Columns ===")
    print(telemetry.columns)
    
    # Save telemetry to CSV
    data_dir = Path(__file__).resolve().parent.parent / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    output_path = data_dir / f"f1_telemetry_{driver}_{year}_{gp_name}_{session_type}.csv"
    telemetry.to_csv(output_path, index=False)
    print(f"\nTelemetry data saved to {output_path}")
    
    # Plot speed trace
    plt.figure(figsize=(12, 6))
    plt.plot(telemetry['Distance'], telemetry['Speed'], label=f"{driver} Speed")
    plt.xlabel('Distance (m)')
    plt.ylabel('Speed (km/h)')
    plt.title(f"{driver} Speed Trace - {gp_name} {year} ({session_type})")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    try:
        year = int(input("Enter season year (e.g., 2023): "))
        gp_name = input("Enter Grand Prix name (e.g., Bahrain): ")
        session_type = input("Enter session type (FP1, FP2, FP3, Q, R): ").upper()
        driver = input("Enter driver abbreviation (e.g., VER, HAM, LEC): ").upper()
    except ValueError:
        print("Invalid input. Try again.")
        exit(1)

    explore_telemetry(year, gp_name, session_type, driver)