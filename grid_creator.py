from PIL import Image, ImageDraw, ImageFont

LINE_WIDTH = 4
LINE_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
CELL_SIZE = 128
FONT_SIZE = 48
FONT = "Roboto-Medium.ttf"
TEXT_COLOR = (0, 0, 0)


def create_grid(
    rows,
    cols,
    cell_size=CELL_SIZE,
    font_size=FONT_SIZE,
    font=FONT,
    line_width=LINE_WIDTH,
    line_color=LINE_COLOR,
    background_color=BACKGROUND_COLOR,
    text_color=TEXT_COLOR,
):
    image = Image.new("RGBA", (cols * cell_size, rows * cell_size))
    drawer = ImageDraw.Draw(image)
    font = ImageFont.truetype(font, font_size)

    image.paste(background_color, (0, 0, image.width, image.height))

    for x in range(cols):
        for y in range(rows):
            drawer.text(
                (x * cell_size + cell_size / 2, y * cell_size + cell_size / 2),
                f"{x},{y}",
                fill=text_color,
                font=font,
                anchor="mm",
            )

    for x in range(cols + 1):
        drawer.line(
            (x * cell_size, 0, x * cell_size, rows * cell_size),
            fill=line_color,
            width=line_width,
        )

    for y in range(rows + 1):
        drawer.line(
            (0, y * cell_size, cols * cell_size, y * cell_size),
            fill=line_color,
            width=line_width,
        )
    return image


def save_grid_default_name(image, rows, cols):
    image.save(f"{rows}x{cols}grid.png", "PNG")


def save_grid(image, name):
    image.save(name, "PNG")
