import fastf1
import matplotlib.pyplot as plt
from pathlib import Path

#Enable FastF1 cache
CACHE_DIR = Path(__file__).resolve().parent.parent / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)
fastf1.Cache.enable_cache(str(CACHE_DIR))

def compare_drivers_speed(year: int, gp_name: str, session_type: str, driver1: str, driver2: str, lap_number: int):
    """
    Compare the speed of two drivers on a specific lap in a session.
    """
    print(f"\nComparing {driver1} and {driver2} on lap {lap_number} of {gp_name} {year} {session_type}...\n")
    
    session = fastf1.get_session(year, gp_name, session_type)
    session.load()
    
    # Pick the lap for each driver
    lap1 = session.laps.pick_driver(driver1).pick_lap(lap_number)
    lap2 = session.laps.pick_driver(driver2).pick_lap(lap_number)
    
    # Get telemetry for each lap
    tel1 = lap1.get_car_data().add_distance()
    tel2 = lap2.get_car_data().add_distance()
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(tel1['Distance'], tel1['Speed'], label=driver1, color='blue')
    plt.plot(tel2['Distance'], tel2['Speed'], label=driver2, color='red')
    
    plt.xlabel('Distance (m)')
    plt.ylabel('Speed (km/h)')
    plt.title(f"{driver1} vs {driver2} - Lap {lap_number} Speed Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    try:
        year = int(input("Enter season year (e.g., 2023): "))
        gp_name = input("Enter Grand Prix name (e.g., Bahrain): ")
        session_type = input("Enter session type (FP1, FP2, FP3, Q, R): ").upper()
        driver1 = input("Enter first driver abbreviation (e.g., VER, HAM): ").upper()
        driver2 = input("Enter second driver abbreviation (e.g., LEC, PER): ").upper()
        lap_number = int(input("Enter lap number to compare: "))
    except ValueError:
        print("Invalid input. Try again.")
        exit(1)
    
    compare_drivers_speed(year, gp_name, session_type, driver1, driver2, lap_number)