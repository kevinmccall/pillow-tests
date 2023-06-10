import argparse
from grid_creator import create_grid, save_grid, save_grid_default_name

LINE_WIDTH = 4
LINE_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
CELL_SIZE = 128
FONT_SIZE = 48
FONT = "Roboto-Medium.ttf"
TEXT_COLOR = (0, 0, 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="GridGenerator", description="Creates a nxm grid and saves it to a png"
    )
    parser.add_argument("rows", type=int, help="number of rows in the generated graph")
    parser.add_argument("cols", type=int, help="number of cols in the generated graph")
    parser.add_argument(
        "-o", "--output", metavar="FILE", help="Output file (must be png)"
    )

    group = parser.add_argument_group("display settings")
    group.add_argument("--line-width", type=int, default=LINE_WIDTH)
    group.add_argument(
        "--line-color", type=int, nargs=3, metavar=("R", "G", "B"), default=LINE_COLOR
    )
    group.add_argument(
        "--background-color",
        type=int,
        nargs=3,
        metavar=("R", "G", "B"),
        default=BACKGROUND_COLOR,
    )
    group.add_argument("--cell-size", type=int, default=CELL_SIZE)
    group.add_argument("--font-size", type=int, metavar="pt", default=FONT_SIZE)
    group.add_argument("--font", type=str, default=FONT)
    group.add_argument(
        "--text-color", type=int, nargs=3, metavar=("R", "G", "B"), default=TEXT_COLOR
    )

    args = parser.parse_args()

    image = create_grid(
        rows=args.rows,
        cols=args.cols,
        line_width=args.line_width,
        line_color=args.line_color,
        background_color=args.background_color,
        cell_size=args.cell_size,
        font_size=args.font_size,
        font=args.font,
        text_color=args.text_color,
    )

    if args.output:
        save_grid(image, args.output)
    else:
        save_grid_default_name(image, args.rows, args.cols)
