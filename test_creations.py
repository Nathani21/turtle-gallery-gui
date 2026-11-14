import tkinter
import turtle

import pytest

from creations import CREATIONS, spectrum_rosette


@pytest.fixture(scope="module")
def screen():
    """One hidden window shared by all the drawing tests."""
    try:
        root = tkinter.Tk()
    except tkinter.TclError as error:
        pytest.skip(f"no display available for Tk: {error}")
    root.withdraw()
    yield turtle.TurtleScreen(tkinter.Canvas(root, width=600, height=600))
    root.destroy()


@pytest.fixture
def pen(screen):
    """A fresh turtle with animation off, and a clean screen afterwards."""
    screen.tracer(0)
    yield turtle.RawTurtle(screen)
    screen.clear()


def run(creation, pen):
    """Draw a whole creation and return how many steps it took."""
    return sum(1 for _ in creation.draw(pen))


def test_registry_is_not_empty():
    assert len(CREATIONS) > 0


def test_registry_entries_are_valid():
    for name, creation in CREATIONS.items():
        assert isinstance(name, str) and name.strip()
        assert callable(creation.draw)
        assert creation.EXTENT > 0
        assert creation.STEP_MS > 0


def test_rosette_colors_are_valid():
    assert len(spectrum_rosette.COLORS) == 36
    for color in spectrum_rosette.COLORS:
        assert len(color) == 3
        assert all(0 <= channel <= 1 for channel in color)


@pytest.mark.parametrize("name", list(CREATIONS))
def test_creation_runs_to_completion(pen, name):
    assert run(CREATIONS[name], pen) > 0


@pytest.mark.parametrize("name", list(CREATIONS))
def test_creation_stays_within_its_extent(pen, name):
    creation = CREATIONS[name]
    run(creation, pen)
    pen.getscreen().update()
    bounds = pen.getscreen().getcanvas().bbox("all")
    assert max(abs(value) for value in bounds) <= creation.EXTENT