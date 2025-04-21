import matplotlib.pyplot as plt
from io import BytesIO
from datetime import datetime

def add_current_datetime_to_chart():
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    plt.figtext(0.99, 0.01, current_datetime, ha='right', fontsize=10, color='white', backgroundcolor='black')

def create_line_chart_image(measurements: list[float], caption: str, x_label: str, y_label: str, line_color: str = 'blue', marker: str = 'o'):
    plt.figure(figsize=(10, 6), facecolor='black')
    ax = plt.gca()
    ax.set_facecolor('black')
    plt.plot(measurements, color='green', marker=marker, linewidth=2, markersize=8)
    plt.title(caption, fontsize=16, fontweight='bold', color='white')
    plt.xlabel(x_label, fontsize=12, color='white')
    plt.ylabel(y_label, fontsize=12, color='white')
    plt.grid(True, linestyle='--', color='gray', alpha=0.7)
    plt.tight_layout()

    add_current_datetime_to_chart()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    return buffer.getvalue()

def create_scatter_plot_image(measurements: list[float], caption: str, x_label: str, y_label: str, point_color: str = 'red'):
    
    plt.figure(figsize=(10, 6), facecolor='black')
    
    ax = plt.gca()
    ax.set_facecolor('black')
    
    plt.scatter(range(len(measurements)), measurements, color=point_color, s=50)
    
    plt.title(caption, fontsize=16, fontweight='bold', color='white')
    plt.xlabel(x_label, fontsize=12, color='white')
    plt.ylabel(y_label, fontsize=12, color='white')
    
    plt.grid(True, linestyle='--', color='gray', alpha=0.7)
    plt.tight_layout()

    add_current_datetime_to_chart()
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    
    buffer.seek(0)
    return buffer.getvalue()