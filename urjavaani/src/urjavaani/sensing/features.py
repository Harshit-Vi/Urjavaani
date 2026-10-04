"""Extract features on-site from machine audio; raw audio never leaves the plant.

TODO features: log-mel spectrogram, spectral centroid, band energies, and line-frequency harmonics.
"""

from typing import Any


def extract_features(samples: Any, sample_rate: int) -> dict:
    """Extract model features from samples."""
    raise NotImplementedError("Implement in Phase 2")
