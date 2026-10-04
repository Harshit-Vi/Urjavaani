"""Carbon accounting helpers for Scope 1 and Scope 2."""

from dataclasses import dataclass, field


@dataclass
class Batch:
    """Production batch inputs for footprinting."""

    batch_id: str
    product: str
    good_units: int
    kwh_by_hour: dict[int, float] = field(default_factory=dict)
    scope1_kg_co2e: float = 0.0


def scope2_kg(kwh_by_hour: dict[int, float], ef_by_hour: dict[int, float]) -> float:
    """Calculate Scope 2 emissions in kg CO2e."""
    return sum(kwh * ef_by_hour[hour] for hour, kwh in kwh_by_hour.items())


def batch_footprint(batch: Batch, ef_by_hour: dict[int, float]) -> dict[str, float | str | None]:
    """Return per-batch footprint summary."""
    scope2 = scope2_kg(batch.kwh_by_hour, ef_by_hour)
    total = batch.scope1_kg_co2e + scope2
    kg_per_unit = None if batch.good_units == 0 else total / batch.good_units
    return {
        "batch_id": batch.batch_id,
        "scope1_kg": batch.scope1_kg_co2e,
        "scope2_kg": scope2,
        "total_kg": total,
        "kg_per_unit": kg_per_unit,
    }
