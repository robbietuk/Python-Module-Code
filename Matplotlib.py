from matplotlib import pyplot as plt
from math import sin, cos, pi

sine_graph, sine_graph_axes = plt.subplots()


sine_graph_axes.plot([sin(pi*x/100.0)**2 for x in range(100)], label='sin^2(x)')
sine_graph_axes.plot([cos(pi*x/100.0)**2 for x in range(100)], label='cos^2(x)')
#sine_graph_axes.plot([cos(pi*x/100.0)**2 + sin(pi*x/100.0)**2 for x in range(100)], label='sin^2(x) + cos^2(x)')
sine_graph_axes.set_title('Graph')
sine_graph_axes.set_xlabel('100 x')
sine_graph_axes.set_ylabel('f(x)')
sine_graph_axes.legend()
sine_graph.show()
