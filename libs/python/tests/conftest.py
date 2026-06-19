"""Test fixtures — temporary .acontext directory."""
import tempfile
from pathlib import Path
import pytest
from acontext import AContext


@pytest.fixture
def acontext():
    with tempfile.TemporaryDirectory() as tmp:
        ctx = AContext(tmp)
        yield ctx
