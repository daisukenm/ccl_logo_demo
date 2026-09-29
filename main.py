import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import random

# Set Seed
random.seed(123)

# -------------------------------------------------------
# Canvas
# -------------------------------------------------------
fig, ax = plt.subplots(figsize=(16, 9), dpi=160)

fig.patch.set_facecolor("#020d2c")
ax.set_facecolor("#020d2c")

ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis("off")


# -------------------------------------------------------
# Cubic Bézier curve
# -------------------------------------------------------
def bezier_curve(p0, p1, p2, p3, color, alpha=0.25, lw=0.7):

    verts = [p0, p1, p2, p3]

    codes = [
        Path.MOVETO,
        Path.CURVE4,
        Path.CURVE4,
        Path.CURVE4
    ]

    path = Path(verts, codes)

    patch = PathPatch(
        path,
        facecolor="none",
        edgecolor=color,
        lw=lw,
        alpha=alpha
    )

    ax.add_patch(patch)


# -------------------------------------------------------
# Three source groups
# -------------------------------------------------------
sources = [
    (4.0, 6.0, "#00d9ff", "Computational"),
    (4.0, 5.0, "#ff25c9", "Communication"),
    (4.0, 4.0, "#ffd52a", "Science")
]

# -------------------------------------------------------
# Target positions
# -------------------------------------------------------
n_lines = 100
target_x = 7.6

targets = np.linspace(1.5, 8.5, n_lines)


# -------------------------------------------------------
# Draw flowing connections
# -------------------------------------------------------
for sx, sy, color, label in sources:

    for i, ty in enumerate(targets):

        # Add a little randomness
        ty2 = ty + np.random.normal(0, 0.025)

        p0 = (sx, sy)

        # Control points create the fan shape
        p1 = (
            sx + 1.0,
            sy + (ty2 - sy) * 0.05
        )

        p2 = (
            sx + 2.7,
            ty2
        )

        p3 = (
            target_x,
            ty2
        )

        bezier_curve(
            p0, p1, p2, p3,
            color,
            alpha=0.18,
            lw=0.65
        )


# -------------------------------------------------------
# Bright source points
# -------------------------------------------------------
for x, y, color, label in sources:

    # Glow
    for r, a in [(0.22, .02), (0.13, .05), (0.07, .12)]:
        circle = plt.Circle(
            (x, y),
            r,
            color=color,
            alpha=a
        )
        ax.add_patch(circle)

    # ax.scatter(
    #     x, y,
    #     s=20,
    #     color=color,
    #     zorder=10
    # )


# -------------------------------------------------------
# Vertical node columns
# -------------------------------------------------------

node_x = [7.6, 7.7, 7.8]

node_colors = [
    "#00d9ff",
    "#ff25c9",
    "#ffd52a"
]

for y in targets:

    for x in node_x:

        ax.scatter(
            x,
            y,
            s=np.random.uniform(4, 18),
            color=np.random.choice(node_colors),
            alpha=np.random.uniform(0.25, 0.7)
        )


# -------------------------------------------------------
# Binary field
# -------------------------------------------------------
chars = "01"

for row, y in enumerate(np.linspace(1.5, 8.5, 70)):

    for col, x in enumerate(np.linspace(8.0, 14.7, 75)):

        # Fade toward right
        alpha = max(
            0.03,
            0.65 * np.exp(-(x - 8) / 4)
        )

        # occasional brighter characters
        if random.random() < .08:
            color = "#00d9ff"
            alpha *= 1.5
        else:
            color = "#008cff"

        ax.text(
            x,
            y,
            random.choice(chars),
            fontsize=4.8,
            color=color,
            alpha=alpha,
            ha="center",
            va="center",
            family="monospace"
        )


# -------------------------------------------------------
# Binary strings on left
# -------------------------------------------------------
for x, y, color, label in sources:

    ax.text(
        x - 1.5,
        y,
        label,
        fontsize=8,
        color=color,
        alpha=.75,
        family="monospace",
        va="center"
    )


plt.savefig(
    "demo_ccl_logo.png",
    dpi=300,
    facecolor=fig.get_facecolor(),
    bbox_inches="tight"
)

plt.show()
