"""
This module contains functions for drawing shapes using pycairo library.
"""

import cairo

# Set up surface
def create_surface(width, height, background_color):
    """
    create an image surface and context
    :param width: width of surface
    :param height: height of surface
    :param background_color: background color of surface
    :return: Image surface and context objects
    """
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(surface)
    context.set_source_rgb(*background_color)

    return surface, context

def draw_rectangle(
        context: cairo.Context,
        coordinates: tuple[int, int],
        width,
        height,
        fill = None,
        stroke = None,
        fill_color = (0, 0, 0),
        stroke_color = (0, 0, 0),
        line_width = 0
):
    """
    Draws a rectangle.
    :param context: a cairo.Context object
    :param coordinates: coordinates of the rectangle in the form (x, y)
    :param width: width of rectangle
    :param height: height of rectangle
    :param fill: specifies whether to fill the rectangle with color
    :param stroke: specifies whether to apply stroke to a rectangle
    :param fill_color: fill color of the rectangle
    :param stroke_color: stroke color of the rectangle
    :param line_width: line width of the rectangle's stroke
    :return: None
    """
    context.rectangle(*coordinates, width, height)
    fill_and_stroke(context, fill, stroke, fill_color, stroke_color, line_width)


def draw_line(
        context: cairo.Context,
        start_coordinates,
        end_coordinates,
        line_color,
        line_width
):
    """
       Draws a line.
       :param context: a cairo.Context object
       :param start_coordinates: the coordinates of the start of the line
       :param end_coordinates: the coordinates of the end of the line
       :param line_color: the color of the line
       :param line_width: the width of the stroke
       :return: None
       """
    context.move_to(*start_coordinates)
    context.line_to(*end_coordinates)
    fill_and_stroke(context, fill=False, stroke=True, stroke_color=line_color, line_width=line_width)

def draw_polygon(
        context,
        coordinates,
        closed_polygon=True,
        fill: bool=None,
        stroke: bool=None,
        fill_color=(0, 0, 0),
        stroke_color=(0, 0, 0),
        line_width=0
):
    """
    Draws a polygon (closed by default).
    :param context: a cairo.Context object
    :param coordinates: a dictionary specifying the coordinates of the vertices
    - The first coordinate should start with a key of "v1"
    :param closed_polygon: specifies whether to draw a closed polygon
    :param fill: specifies whether to fill the polygon with color
    :param stroke: specifies whether to apply a stroke to the polygon
    :param fill_color: fill color of the polygon
    :param stroke_color: stroke color of the polygon
    :param line_width: the width of the stroke
    :return: None
    """
    context.move_to(*coordinates["v1"])
    for coordinate in coordinates.values():
        if coordinate == coordinates["v1"]:
            continue
        else:
            context.line_to(*coordinate)

    if closed_polygon:
        context.close_path()

    fill_and_stroke(context, fill, stroke, fill_color, stroke_color, line_width)


def draw_arc(context: cairo.Context, coordinates, radius, angles, color, line_width):
    """
    Draws an arc.
    :param context: a cairo.Context object
    :param coordinates: the coordinates of the centre of the arc
    :param radius: radius of the arc
    :param angles: the angles of the arc - (start_angle, end_angle)
    :param color:
    :param line_width:
    :return: None
    """
    context.arc(*coordinates, radius, *angles)
    fill_and_stroke(context, stroke=True, stroke_color=color, line_width=line_width)


def fill_and_stroke(
        context,
        fill=None,
        stroke=None,
        fill_color=(0, 0, 0),
        stroke_color=(0, 0, 0),
        line_width=0
):
    """
    Determine whether to apply fill and/or stroke to a shape.
    :param context: a cairo.Context object
    :param fill: specifies whether to fill the shape
    :param stroke: specifies whether to add a stroke to the shape
    :param fill_color: fill color of the shape
    :param stroke_color: stroke color of the shape
    :param line_width: the thickness of the stroke
    :return: None
    """
    # Fill only
    if fill and not stroke:
        context.set_source_rgb(*fill_color)
        context.fill()

    # Stroke only
    elif stroke and not fill:
        context.set_source_rgb(*stroke_color)
        if line_width == 0:
            raise ValueError("For fill and stroke, line width should be greater than zero.")
        else:
            context.set_line_width(line_width)
            context.stroke()

    # Fill and stroke
    elif stroke and fill:
        context.set_source_rgb(*fill_color)
        context.fill_preserve()
        context.set_source_rgb(*stroke_color)
        if line_width == 0:
            raise ValueError("For fill and stroke, line width should be greater than zero.")
        else:
            context.set_line_width(line_width)
            context.stroke()

    else:
        raise ValueError("Either fill or stroke (or both) must be specified.")