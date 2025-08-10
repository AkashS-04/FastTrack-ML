import fastf1
import pandas as pd
from pathlib import Path

# Enable FastF1 cache (ensure absolute path and directory exists)
CACHE_DIR = Path(__file__).resolve().parent.parent / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)
fastf1.Cache.enable_cache(str(CACHE_DIR))  # stores downloaded data locally

# Load a session: 2023 Bahrain GP Qualifying
session = fastf1.get_session(2023, 'Bahrain', 'Q')
session.load()

# --- EVENT INFO ---
print(session.event)

# --- BASIC SESSION INFO ---
print(f"Event: {session.event['EventName']}")
print(f"Session type: {session.name}")
print(f"Date: {session.date}")
print(f"Track: {session.event['EventName']} in {session.event['Country']}")

# --- DRIVER LIST ---
print("\nDrivers in session:")
print(session.drivers)  # list of driver numbers

# --- DRIVER INFO ---
driver_info = session.get_driver('1')  # driver number 1 (Verstappen in 2023)
print("\nDriver 1 info:")
print(driver_info)

# --- LAPS DATA ---
laps = session.laps
print("\nLaps DataFrame:")
print(laps.head())

# --- TELEMETRY DATA FOR A SINGLE LAP ---
verstappen_laps = laps.pick_driver('VER')  # filter for Max Verstappen
fastest_ver_lap = verstappen_laps.pick_fastest()
telemetry = fastest_ver_lap.get_car_data().add_distance()

print("\nTelemetry columns:")
print(telemetry.head())

# --- WEATHER DATA ---
print("\nWeather data:")
print(session.weather_data.head())