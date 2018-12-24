# Experimenting with utf-8 encoding for Greek symbols (warning).
# Added set encoding=utf-8 in .vimrc file to make this work.
from numpy import sqrt, arctan2, linspace, meshgrid


def stress_from_line(x1, y1, x2, y2, P, a, λ, x, y):
    c = (x2 - x1) / sqrt((x2 - x1)**2 + (y2 - y1)**2)
    s = (y2 - y1) / sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Compute "temporaries" that appear in the expressions
    # below multiple times to avoid redundant computation.
    term0 = (x*c + y*s)
    term1 = (x1*c + y1*s) - term0
    term2 = (-x*s + y*c)
    term3 = (-x2*s + y2*c) - term2
    term4 = (x2*c + y2*s) - term0
    term5 = term1**2 + term3**2
    term6 = term4**2 + term3**2

    const = -P * a**2 * λ
    xx_ = const * (term1 / term5 - term4 / term6)
    xy_ = const * (term3 / term5 - term3 / term6)

    xx = (c**2 - s**2) * xx_ - 2*c*s*xy_
    xy = 2*c*s*xx_ + (c**2 - s**2) * xy_
    return xx, xy


def ret(σ_xx, σ_xy, C, L):
    return C * L * sqrt((2 * σ_xx)**2 + 4*σ_xy**2)


def slow_angle(σ_xx, σ_xy):
    return 0.5 * arctan2(2 * σ_xy, 2 * σ_xx)


def plot(ret, θ):
    figure, (ret_ax, θ_ax) = pyplot.subplots(nrows=1, ncols=2)
    ret_image = ret_ax.imshow(ret)
    θ_image = θ_ax.imshow(θ,cmap="twilight")
    figure.colorbar(ret_image, ax=ret_ax)
    figure.colorbar(θ_image, ax=θ_ax)
    ret_ax.set_title('retardation')
    θ_ax.set_title('slow-axis angle')
    figure.tight_layout()  # Improve spacing.
    return figure
