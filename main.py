"""
This module is where the program is executed from
"""

from shapes import *
import math

OUTPUT_DIR = 'output_images/'
WIDTH, HEIGHT = 700, 700
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
                fill = True,
                fill_color = shape_color
            )

            # Rectangle with red stroke
            shape_color = (1, 0, 0)
            coordinates = (150, 250)
            draw_rectangle(
                context,
                coordinates,
                200,
                50,
                stroke = True,
                stroke_color = shape_color,
                line_width = 5
            )

            # Rectangle with green fill, blue stroke
            fill_color = (0, 1, 0)
            stroke_color = (0, 0, 1)
            coordinates = (150, 400)
            draw_rectangle(
                context,
                coordinates,
                200,
                50,
                fill = True,
                stroke = True,
                fill_color = fill_color,
                stroke_color = stroke_color,
                line_width = 5,
            )

            surface.write_to_png(f"{OUTPUT_DIR}rectangles.png")

        case "line":
            # Red vertical line
            start_coordinates = (150, 50)
            end_coordinates = (150, 200)
            line_color = (1, 0, 0)
            line_width = 10
            draw_line(context, start_coordinates, end_coordinates, line_color, line_width)

            # Blue horizontal line
            start_coordinates = (150, 300)
            end_coordinates = (350, 300)
            line_color = (0, 0, 1)
            line_width = 10
            draw_line(context, start_coordinates, end_coordinates, line_color, line_width)

            # Green diagonal line
            start_coordinates = (350, 50)
            end_coordinates = (250, 200)
            line_color = (0, 1, 0)
            line_width = 10
            draw_line(context, start_coordinates, end_coordinates, line_color, line_width)

            surface.write_to_png(f"{OUTPUT_DIR}lines.png")

        case "triangle":
            # # Triangle with green fill
            # coordinates = {
            #     "v1": (100, 50),
            #     "v2": (150, 200),
            #     "v3": (300, 150),
            # }
            #
            # fill_color = (0, 1, 0)
            #
            # draw_polygon(
            #     context,
            #     coordinates,
            #     fill = True,
            #     fill_color = fill_color,
            #     line_width = 10
            # )

            # Triangle with red fill, blue stroke
            coordinates = {
                "v1": (100, 200),
                "v2": (100, 400),
                "v3": (400, 400),
            }


            stroke_color = (1, 0, 0)
            fill_color = (0, 0, 0)


            draw_polygon(
                context,
                coordinates,
                fill = True,
                stroke = True,
                fill_color = fill_color,
                stroke_color = stroke_color,
                line_width = 10
            )
            
            surface.write_to_png(f"{OUTPUT_DIR}triangles.png")


        case "arc":
            coordinates = (250, 250)
            angles = (0, math.pi/2)
            color = (0, 0, 1)

            draw_arc(
                context,
                coordinates,
                radius = 200,
                angles = angles,
                color = color,
                line_width = 5
            )

            surface.write_to_png(f"{OUTPUT_DIR}arc.png")

        case "circle":
            coordinates = (250, 250)
            angles = (0, math.pi*2)
            color = (0, 1, 0)

            draw_arc(
                context,
                coordinates,
                radius = 200,
                angles = angles,
                color = color,
                line_width = 5
            )

            surface.write_to_png(f"{OUTPUT_DIR}circle.png")

        case "bezier":
            start_coordinates = (100, 100)
            bezier_points1 = (200, 0, 400, 200, 500, 100)
            bezier_points2 = (400, 400, 200, 200, 100, 300)
            line_coordinates1 = (500, 300)
            line_coordinates2 = (100, 300)
            line_color = (0, 1, 0)
            line_width = 10
            draw_bezier(context, start_coordinates, bezier_points1, bezier_points2, line_coordinates1, line_coordinates2, line_color, line_width)
            surface.write_to_png(f"{OUTPUT_DIR}bezier.png")


if __name__ == "__main__":
    input_message = """Shape Types: 
    1. rectangle
    2. line
    3. triangle
    4. arc
    5. circle
    6. bezier
    """
    print(input_message)
    shape = input("Enter shape type to draw: ")
    main(shape)


