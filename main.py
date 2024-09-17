"""
This module is where the program is executed from
"""

from shapes import *
import math

OUTPUT_DIR = 'output_images/'
WIDTH, HEIGHT = 500, 500
BACKGROUND_COLOR = (0.9, 0.9, 0.9)


def main(shape_type):
    surface, context = create_surface(WIDTH, HEIGHT, BACKGROUND_COLOR)
    match shape_type:
        case "rectangle":
            # Rectangle with blue fill
            shape_color = (0, 0, 1)
            coordinates = (150, 100)
            draw_rectangle(
                context,
                coordinates,
                200,
                50,
                fill=True,
                fill_color=shape_color
            )

            # Rectangle with red stroke
            shape_color = (1, 0, 0)
            coordinates = (150, 250)
            draw_rectangle(
                context,
                coordinates,
                200,
                50,
                stroke=True,
                stroke_color=shape_color,
                line_width=10
            )

            # Rectangle with blue fill, green stroke
            fill_color = (0, 0, 1)
            stroke_color = (0, 1, 0)
            coordinates = (150, 400)
            draw_rectangle(
                context,
                coordinates,
                200,
                50,
                fill=True,
                stroke=True,
                fill_color=fill_color,
                stroke_color=stroke_color,
                line_width=10,
            )

            surface.write_to_png(f"{OUTPUT_DIR}rectangles.png")

        case "line":
            # Blue vertical line
            start_coordinates = (150, 50)
            end_coordinates = (150, 200)
            line_color = (0, 0, 1)
            line_width = 10
            draw_line(context, start_coordinates, end_coordinates, line_color, line_width)

            # Green horizontal line
            start_coordinates = (150, 300)
            end_coordinates = (350, 300)
            line_color = (0, 1, 0)
            line_width = 10
            draw_line(context, start_coordinates, end_coordinates, line_color, line_width)

            # Red diagonal line
            start_coordinates = (250, 50)
            end_coordinates = (350, 200)
            line_color = (1, 0, 0)
            line_width = 10
            draw_line(context, start_coordinates, end_coordinates, line_color, line_width)

            surface.write_to_png(f"{OUTPUT_DIR}lines.png")

        case "triangle":
            # Triangle with green fill
            coordinates = {
                "v1": (100, 50),
                "v2": (150, 200),
                "v3": (300, 150),
            }

            fill_color = (0, 1, 0)

            draw_polygon(
                context,
                coordinates,
                fill=True,
                fill_color=fill_color,
                line_width=10
            )

            # Triangle with red fill, blue stroke
            coordinates = {
                "v1": (300, 250),
                "v2": (300, 450),
                "v3": (200, 450),
            }

            stroke_color = (0, 0, 1)
            fill_color = (255, 0, 0)

            draw_polygon(
                context,
                coordinates,
                fill=True,
                stroke=True,
                fill_color=fill_color,
                stroke_color=stroke_color,
                line_width=10
            )

            surface.write_to_png(f"{OUTPUT_DIR}triangles.png")

        case "arc":
            coordinates = (250, 250)
            angles = (0, math.pi/2)
            color = (0, 0, 1)

            draw_arc(
                context,
                coordinates,
                radius=200,
                angles=angles,
                color=color,
                line_width=5
            )

            surface.write_to_png(f"{OUTPUT_DIR}arc.png")

        case "circle":
            coordinates = (250, 250)
            angles = (0, math.pi*2)
            color = (0, 1, 0)

            draw_arc(
                context,
                coordinates,
                radius=200,
                angles=angles,
                color=color,
                line_width=5
            )

            surface.write_to_png(f"{OUTPUT_DIR}circle.png")

if __name__ == "__main__":
    input_message = """Shape Types: 
    1. rectangle
    2. line
    3. triangle
    4. arc
    5. circle
    """
    print(input_message)
    shape = input("Enter shape type to draw: ")
    main(shape)
