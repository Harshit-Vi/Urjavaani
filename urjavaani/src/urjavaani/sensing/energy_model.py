"""Energy model with one-point clamp-meter calibration and a small regressor.

Report MAPE on held-out data, targeting roughly +/-10-15% after calibration.
"""

from typing import Any


class EnergyModel:
    """Placeholder energy model."""

    def fit(self, features: Any, measured_kw: Any) -> None:
        """Fit model to labeled power data."""
        raise NotImplementedError("Implement in Phase 2")

    def predict_kw(self, features: Any) -> Any:
        """Predict kW from extracted features."""
        raise NotImplementedError("Implement in Phase 2")
