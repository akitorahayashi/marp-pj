import os

import pytest

from src.marp_service import MarpService


@pytest.fixture
def marp_service(tmp_path):
    """
    Pytest fixture to create a MarpService instance with a temporary output directory.
    """
    # tmp_path is a Path object provided by pytest
    output_dir = tmp_path / "output"
    output_dir.mkdir()

    # The slides_path is constant
    slides_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src", "slides.md")
    )

    service = MarpService(slides_path=slides_path, output_dir=str(output_dir))
    return service
