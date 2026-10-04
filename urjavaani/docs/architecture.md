# Architecture

UrjaVaani is organized into four layers:
- **Edge node**: ESP32 + MEMS microphone or phone captures sound and vibration windows.
- **Plant gateway**: Offline-first service buffers readings, applies local rules, and syncs to cloud.
- **Cloud services**: Acoustic energy model, tariff-aware scheduler, and carbon engine.
- **Outputs**: WhatsApp/SMS/voice alerts, web dashboard, Carbon Passport PDF + QR, and Tally/ERP export.

## Core entities
- `machine`
- `sensor_reading`
- `energy_estimate`
- `job`
- `tariff_slab`
- `emission_factor`
- `batch`
- `passport`

## Data flow
1. Machines are observed by the edge node.
2. Sensor readings move to the plant gateway.
3. Gateway syncs validated readings to cloud services.
4. Cloud services produce energy estimates, schedules, and batch footprints.
5. Outputs are delivered to operators and reporting systems.
