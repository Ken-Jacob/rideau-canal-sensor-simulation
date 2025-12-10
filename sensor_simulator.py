import os
import json
import time
import random
from datetime import datetime, timezone

from dotenv import load_dotenv
from azure.iot.device import IoTHubDeviceClient, Message

# Load environment variables from .env
load_dotenv()

# Device configurations
DEVICE_CONFIGS = [
    {
        "name": "dows-lake",
        "location": "Dow's Lake",
        "conn_str": os.getenv("IOTHUB_DEVICE_CONN_DOWS_LAKE")
    },
    {
        "name": "fifth-avenue",
        "location": "Fifth Avenue",
        "conn_str": os.getenv("IOTHUB_DEVICE_CONN_FIFTH_AVENUE")
    },
    {
        "name": "nac",
        "location": "NAC",
        "conn_str": os.getenv("IOTHUB_DEVICE_CONN_NAC")
    }
]

# Read send interval (default: 10 seconds)
SEND_INTERVAL = int(os.getenv("SEND_INTERVAL_SECONDS", "10"))


def generate_sensor_reading(location: str) -> dict:
    """Generate a random reading for a given location."""
    return {
        "location": location,
        "iceThicknessCm": round(random.uniform(20, 40), 1),
        "surfaceTempC": round(random.uniform(-10, 1), 1),
        "snowAccumulationCm": round(random.uniform(0, 10), 1),
        "externalTempC": round(random.uniform(-20, 5), 1),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


def main():
    print("Starting Rideau Canal Sensor Simulator...")
    print("Connecting devices...")

    clients = []
    for cfg in DEVICE_CONFIGS:
        if not cfg["conn_str"]:
            print(f"❌ ERROR: Missing connection string for {cfg['name']}. Check your .env file.")
            continue

        try:
            client = IoTHubDeviceClient.create_from_connection_string(cfg["conn_str"])
            clients.append((cfg, client))
            print(f"✅ Connected: {cfg['location']}")
        except Exception as e:
            print(f"❌ Failed to connect {cfg['location']}: {e}")

    if not clients:
        print("No devices connected. Exiting.")
        return

    print("\nSimulation running...\n(Press CTRL+C to stop)\n")

    try:
        while True:
            for cfg, client in clients:
                data = generate_sensor_reading(cfg["location"])
                message = Message(json.dumps(data))
                message.content_type = "application/json"
                message.content_encoding = "utf-8"

                try:
                    client.send_message(message)
                    print(f"📡 Sent from {cfg['location']}: {data}")
                except Exception as e:
                    print(f"❌ Failed to send from {cfg['location']}: {e}")

            time.sleep(SEND_INTERVAL)

    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")

    finally:
        print("Closing connections...")
        for _, client in clients:
            client.shutdown()
        print("Done.")


if __name__ == "__main__":
    main()
