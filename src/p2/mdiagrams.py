import matplotlib.pyplot as plt
from io import BytesIO

def create_line_chart_image(measurements: list[float], caption: str, x_label: str, y_label: str, line_color: str = 'blue', marker: str = 'o'):
    """
    Create a line chart image from the given measurements and caption.
    :param measurements: List of measurements to plot.
    :param caption: Caption for the chart.
    :param x_label: Label for the x-axis.
    :param y_label: Label for the y-axis.
    :param line_color: Color of the line in the chart.
    :param marker: Marker style for the data points.
    :return: Binary data of the generated image.
    """

    # Create a line chart with enhancements
    plt.plot(measurements, color=line_color, marker=marker)
    plt.title(caption)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)  # Add grid lines

    # Save the chart as binary data
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    return buffer.getvalue()
