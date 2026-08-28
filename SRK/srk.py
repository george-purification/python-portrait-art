import turtle
from PIL import Image


def draw_image(image_path, scale_width=200, pixel_size=5):

    # Open image
    img = Image.open(image_path)

    # Calculate new height while keeping aspect ratio
    w_percent = scale_width / float(img.size[0])
    h_size = int(float(img.size[1]) * w_percent)

    # Resize image
    img = img.resize(
        (scale_width, h_size),
        Image.Resampling.LANCZOS
    )

    # Convert image to RGB
    img = img.convert("RGB")

    width, height = img.size

    # Create Turtle screen
    screen = turtle.Screen()
    screen.setup(
        width=width * pixel_size + 50,
        height=height * pixel_size + 50
    )
    screen.bgcolor("white")
    screen.tracer(0)

    # Create Turtle pen
    pen = turtle.Turtle()
    pen.penup()
    pen.speed(0)
    pen.hideturtle()

    # Starting position
    start_x = -(width * pixel_size) / 2
    start_y = (height * pixel_size) / 2

    print(f"Drawing {width}x{height} pixels with size {pixel_size}...")

    # Draw each pixel
    for y in range(height):
        for x in range(width):

            r, g, b = img.getpixel((x, y))

            # Set RGB color
            pen.color(r / 255, g / 255, b / 255)

            # Move to pixel position
            pen.goto(
                start_x + x * pixel_size,
                start_y - y * pixel_size
            )

            # Draw pixel
            pen.dot(pixel_size)

        # Update screen every 5 rows
        if y % 5 == 0:
            screen.update()

    # Final update
    screen.update()

    print("Drawing Complete!")

    turtle.done()


# Run the function
draw_image("srk.png", scale_width=200, pixel_size=4.5)

