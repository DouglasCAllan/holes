# Example
# Draw one vertical line of holes.

import matplotlib
# Matplotlib supports many "backends" corresponding to
# different GUI frameworks. We don't need a GUI; we just
# need to export an image file.
matplotlib.use('Agg')
from numpy import linspace, meshgrid
from holes.ret import stress_from_line, ret, slow_angle, plot

x, y = meshgrid(linspace(-2000, 2000, num=40),
                linspace(-4000, 4000, num=80))

σ_xx, σ_xy = stress_from_line(
    x1=0, y1=-1000, x2=0, y2=1000, P=5, a=1, λ=1/10, x=x, y=y)
figure = plot(ret(σ_xx, σ_xy, C=3, L=1), slow_angle(σ_xx, σ_xy))
figure.savefig('vertical_line.png')
