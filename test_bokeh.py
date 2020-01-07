import numpy as np
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure
# from bokeh.plotting import figure, output_file, show

mean = 100
sigma = 10
size = 1000

data = np.random.normal(loc=mean, scale=sigma, size=size)
hist, edges = np.histogram(data, density=True, bins=int(size/25))
x = np.linspace(int(min(data)), np.ceil(max(data)), int(size/10))
pdf = 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mean)**2 / (2*sigma**2))


source_hist = ColumnDataSource(data=dict(x=edges[:-1], top=hist))
source_lin  = ColumnDataSource(data=dict(x=x, y=pdf))

# output_file("test_bokeh.html")
p = figure(plot_height=400, plot_width=800, x_range=[-150,150], y_range=[0,0.1])
p.vbar(x='x', top='top', bottom=0, source=source_hist, width=1)
p.line(x='x', y='y', color="red", line_width=2, source=source_lin)
# show(p)

mu = Slider(title="Median", value=100, start=-100, end=100, step=5)
sig = Slider(title="Std. Dev", value=10, start=0, end=50, step=5)

def update_data(attrName, old, new):
    mean = mu.value
    sigma = sig.value
    if sigma==0:
        sigma = 1
    data = np.random.normal(loc=mean, scale=sigma, size=size)
    hist, edges = np.histogram(data, density=True, bins=int(size/25))
    x = np.linspace(int(min(data)), np.ceil(max(data)), int(size/10))
    pdf = 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mean)**2 / (2*sigma**2))
    source_hist.data = dict(x=edges[:-1], top=hist)
    source_lin.data  = dict(x=x, y=pdf)
    
for w in [mu, sig]:
    w.on_change('value', update_data)

sliders = column(mu, sig)

curdoc().add_root(column(sliders, p))
curdoc().title = "Gaussian"
# import matplotlib.pyplot as plt
# plt.hist(data, bins=40)
# plt.show()
# output_file("test_bokeh.html")
# p = figure()
# p.vbar(x=edges[:-1], bottom=0, top=hist, width=0.5)
# p.line(x, pdf, color="red")
# p.vbar(hist, edges, bottom=0, width=0.5, top=500)

# show(p)