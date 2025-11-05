"""Workout AI - A multi-agent fitness planning system."""

__version__ = "0.1.0"

# Make key classes easily importableimport os
from pathlib import Path
import os

# Determine project root (two levels up from this file)
WORKOUT_HOME = Path(__file__).resolve().parent.parent

# Set environment variable if not already set
os.environ.setdefault("WORKOUT_HOME", str(WORKOUT_HOME))