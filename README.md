# Rideau Canal Sensor Simulation
## Overview
This repository contains a **Python-based IoT sensor simulator** for the CST8916 final project.  
It simulates environmental readings from three Rideau Canal Skateway locations:

- **Dow's Lake**
- **Fifth Avenue**
- **NAC (National Arts Centre)**

The simulator sends telemetry every **10 seconds** to **Azure IoT Hub**, representing:

- Ice Thickness (cm)
- Surface Temperature (°C)
- Snow Accumulation (cm)
- External Temperature (°C)

This data forms the **first stage of the real-time processing pipeline**.

---

## Technologies Used
- **Python 3.x**
- **Azure IoT Device SDK for Python**
- **dotenv** for environment variables
- **JSON** for message formatting

---

## Prerequisites
Before running the simulator, ensure you have:

### ✔ Python Installed
Check using:
```bash
python --version
```

### ✔ Azure IoT Hub Created
With **three registered devices**:
- `dows-lake-device`
- `fifth-ave-device`
- `nac-device`

### ✔ Connection Strings
You must copy your **IoT Hub device connection string** from the Azure Portal.

---

## Installation
Clone the repo and install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

### 1. Create `.env` File
This project includes `.env.example`.  
Create your environment file:

```bash
cp .env.example .env
```

### 2. Add IoT Hub Connection Strings
Inside `.env`, set the device connection strings, for example:

```
IOTHUB_DEVICE_CONN_DOWS_LAKE="HostName=RideauHub.azure-devices.net;DeviceId=dows-lake;SharedAccessKey=XXXXX"
IOTHUB_DEVICE_CONN_FIFTH_AVENUE="HostName=RideauHub.azure-devices.net;DeviceId=fifth-avenue;SharedAccessKey=XXXXX"
IOTHUB_DEVICE_CONN_NAC="HostName=RideauHub.azure-devices.net;DeviceId=nac;SharedAccessKey=XXXXX"
```

---

## Usage

Run the simulator:

```bash
python sensor_simulator.py
```

The script will begin sending telemetry every 10 seconds such as:

```
Sending data to IoT Hub...
Location: Dows Lake, Ice: 32 cm, Surface Temp: -6°C, Snow: 2 cm, External Temp: -9°C
```

Leave the script running to generate enough data for:

- Stream Analytics
- Cosmos DB
- Blob Storage
- Dashboard Trend Charts

---

## Data Format (JSON Example)

Each message sent to IoT Hub follows this structure:

```json
{
  "location": "Dows Lake",
  "iceThickness": 32.5,
  "surfaceTemperature": -4.2,
  "snowAccumulation": 1.8,
  "externalTemperature": -10.0,
  "timestamp": "2025-12-02T11:42:20Z"
}
```

---

## AI Tools Disclosure

AI tools were used **only for assistance**, including:
- Writing documentation structure
- Suggesting code cleanup
- Debugging IoT connection issues

---

## Author
**Ken Biju Jacob**  
CST8916 – Remote Data & Real-Time Applications  

---
