import pathlib

import pytest

PAGES = pathlib.Path(__file__).parent / "pages"


@pytest.fixture
def page_url():
    """Returns a file:// URL for a demo page bundled in the repo."""
    return lambda name: (PAGES / name).resolve().as_uri()
