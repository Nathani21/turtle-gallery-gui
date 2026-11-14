import tkinter
import turtle

import pytest

from creations import CREATIONS, rainbow_circle


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


def test_registry_is_not_empty():
    assert len(CREATIONS) > 0


def test_registry_entries_are_named_and_callable():
    for name, draw in CREATIONS.items():
        assert isinstance(name, str) and name.strip()
        assert callable(draw)


def test_rainbow_colors_are_valid():
    assert len(rainbow_circle.COLORS) == 36
    for color in rainbow_circle.COLORS:
        assert len(color) == 3
        assert all(0 <= channel <= 1 for channel in color)


@pytest.mark.parametrize("name", list(CREATIONS))
def test_creation_runs_to_completion(pen, name):
    CREATIONS[name](pen)