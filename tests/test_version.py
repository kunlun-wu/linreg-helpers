"""Unit tests for __version__.py."""

import linreg_helpers


def test_package_version():
    """Ensure the package version is defined and not set to the initial
    placeholder."""
    assert hasattr(linreg_helpers, "__version__")
    assert linreg_helpers.__version__ != "0.0.0"
