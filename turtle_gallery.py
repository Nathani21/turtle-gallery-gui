import tkinter as tk
import turtle

from creations import CREATIONS


class GalleryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Turtle Gallery")
        self.geometry("1000x700")
        self.minsize(700, 500)
        self.tiles = {}
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
        canvas = turtle.ScrolledCanvas(
            self, width=800, height=700, canvwidth=1000, canvheight=1000
        )
        canvas.pack(side="right", fill="both", expand=True)
        self.screen = turtle.TurtleScreen(canvas)
        self.screen.tracer(0)

    def show(self, name):
        for tile_name, tile in self.tiles.items():
            tile.config(relief="sunken" if tile_name == name else "raised")
        self.screen.clear()
        self.screen.tracer(0)
        pen = turtle.RawTurtle(self.screen)
        pen.hideturtle()
        CREATIONS[name](pen)
        self.screen.update()


def main():
    GalleryApp().mainloop()


if __name__ == "__main__":
    main()