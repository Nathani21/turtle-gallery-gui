import tkinter as tk
import turtle

from creations import CREATIONS

FIT_MARGIN = 1.05  # leave a little empty space around each drawing


class GalleryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Turtle Gallery v1.0")
        self.geometry("1000x700")
        self.minsize(700, 500)
        self.tiles = {}
        self._steps = None
        self._step_ms = 0
        self._job = None
        self._build_tiles()
        self._build_canvas()

    def _build_tiles(self):
        panel = tk.Frame(self, padx=8, pady=8)
        panel.pack(side="left", fill="y")
        tk.Label(panel, text="Creations", font=("Segoe UI", 12, "bold")).pack(
            anchor="w", pady=(0, 8)
        )
        for name in CREATIONS:
            tile = tk.Button(
                panel,
                text=name,
                width=18,
                height=3,
                command=lambda n=name: self.show(n),
            )
            tile.pack(pady=4)
            self.tiles[name] = tile

    def _build_canvas(self):
        self.canvas = turtle.ScrolledCanvas(
            self, width=800, height=700, canvwidth=1000, canvheight=1000
        )
        self.canvas.pack(side="right", fill="both", expand=True)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.tracer(0)

    def _fit_view(self, extent):
        """Zoom so a square of half-width `extent` fits the visible canvas."""
        self.update_idletasks()
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        self.screen.screensize(width, height)
        half = extent * FIT_MARGIN
        short = min(width, height)
        self.screen.setworldcoordinates(
            -half * width / short,
            -half * height / short,
            half * width / short,
            half * height / short,
        )

    def show(self, name):
        self._stop()
        creation = CREATIONS[name]
        for tile_name, tile in self.tiles.items():
            tile.config(relief="sunken" if tile_name == name else "raised")
        self.screen.clear()
        self.screen.tracer(0)
        self._fit_view(creation.EXTENT)
        pen = turtle.RawTurtle(self.screen)
        pen.hideturtle()
        self._steps = creation.draw(pen)
        self._step_ms = creation.STEP_MS
        self._advance()

    def _advance(self):
        """Draw one step, then schedule the next one."""
        try:
            next(self._steps)
        except StopIteration:
            self._job = None
            return
        self.screen.update()
        self._job = self.after(self._step_ms, self._advance)

    def _stop(self):
        """Cancel the drawing in progress, if any."""
        if self._job is not None:
            self.after_cancel(self._job)
            self._job = None
        if self._steps is not None:
            self._steps.close()
            self._steps = None


def main():
    GalleryApp().mainloop()


if __name__ == "__main__":
    main()