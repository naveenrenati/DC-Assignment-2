"""
Generates the System Architecture Diagram as a PNG image.
Saves to: docs/images/architecture_diagram.png
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

fig, axes = plt.subplots(1, 2, figsize=(18, 9))
fig.patch.set_facecolor("#1e1e2e")

# ─────────────────────────────────────────────
# LEFT PANEL — P2P Mesh
# ─────────────────────────────────────────────
ax = axes[0]
ax.set_facecolor("#1e1e2e")
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

ax.text(5, 9.4, "Peer-to-Peer Network", fontsize=15, fontweight="bold",
        color="#cdd6f4", ha="center", va="center",
        fontfamily="monospace")
ax.text(5, 8.8, "(No Central Coordinator)", fontsize=10,
        color="#a6adc8", ha="center", va="center", fontstyle="italic")

# Peer node positions (diamond shape)
peer_positions = {
    "P1\n(Server 1)": (2.5, 6.5),
    "P2\n(Server 2)": (7.5, 6.5),
    "P3\n(Server 3)": (7.5, 2.5),
    "P4\n(Server 4)": (2.5, 2.5),
}

peer_color   = "#89b4fa"
peer_text    = "#1e1e2e"
arrow_color  = "#a6e3a1"

# Draw all peer-to-peer connections (full mesh)
positions = list(peer_positions.values())
for i in range(len(positions)):
    for j in range(i + 1, len(positions)):
        x1, y1 = positions[i]
        x2, y2 = positions[j]
        ax.plot([x1, x2], [y1, y2],
                color=arrow_color, linewidth=1.5,
                linestyle="--", alpha=0.6, zorder=1)

# Draw peer nodes
for label, (x, y) in peer_positions.items():
    circle = plt.Circle((x, y), 1.1, color=peer_color,
                         ec="#74c7ec", linewidth=2, zorder=2)
    ax.add_patch(circle)
    ax.text(x, y, label, fontsize=10, fontweight="bold",
            color=peer_text, ha="center", va="center",
            fontfamily="monospace", zorder=3)

# Legend
ax.text(5, 1.2, "← Direct TCP connections (no middleman)",
        fontsize=9, color="#a6adc8", ha="center", fontstyle="italic")
ax.text(5, 0.6, "Gossip broadcast every 8 seconds",
        fontsize=9, color="#a6adc8", ha="center", fontstyle="italic")

# ─────────────────────────────────────────────
# RIGHT PANEL — Cluster Star
# ─────────────────────────────────────────────
ax2 = axes[1]
ax2.set_facecolor("#1e1e2e")
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis("off")

ax2.text(5, 9.4, "Cluster Computing", fontsize=15, fontweight="bold",
         color="#cdd6f4", ha="center", va="center",
         fontfamily="monospace")
ax2.text(5, 8.8, "(Star Topology — Master coordinates workers)",
         fontsize=10, color="#a6adc8", ha="center", va="center",
         fontstyle="italic")

master_color = "#f38ba8"
worker_color = "#fab387"
worker_text  = "#1e1e2e"
line_color   = "#f5c2e7"

# Master node
mx, my = 5, 6
master_circle = plt.Circle((mx, my), 1.2,
                            color=master_color, ec="#eba0ac",
                            linewidth=2.5, zorder=2)
ax2.add_patch(master_circle)
ax2.text(mx, my + 0.15, "Master", fontsize=11, fontweight="bold",
         color=worker_text, ha="center", va="center",
         fontfamily="monospace", zorder=3)
ax2.text(mx, my - 0.4, "Server 1\n:6000", fontsize=8,
         color=worker_text, ha="center", va="center",
         fontfamily="monospace", zorder=3)

# Worker positions
workers = {
    "W1\nServer 2\n:6001": (1.8, 2.2),
    "W2\nServer 3\n:6002": (5.0, 2.2),
    "W3\nServer 4\n:6003": (8.2, 2.2),
}

for label, (wx, wy) in workers.items():
    # Draw line from master to worker
    ax2.annotate("", xy=(wx, wy + 1.0), xytext=(mx, my - 1.2),
                 arrowprops=dict(
                     arrowstyle="-|>",
                     color=line_color,
                     lw=2.0,
                     mutation_scale=18
                 ), zorder=1)
    wc = plt.Circle((wx, wy), 1.0,
                    color=worker_color, ec="#fe8019",
                    linewidth=2, zorder=2)
    ax2.add_patch(wc)
    ax2.text(wx, wy, label, fontsize=8.5, fontweight="bold",
             color=worker_text, ha="center", va="center",
             fontfamily="monospace", zorder=3)

# W4 dynamic label
ax2.text(5, 0.9, "+ W4 (dynamic) can join/leave at any time",
         fontsize=9, color="#a6adc8", ha="center", fontstyle="italic")
ax2.text(5, 0.3, "Tasks split → parallel execution → merge",
         fontsize=9, color="#a6adc8", ha="center", fontstyle="italic")

# Peer-to-cluster arrow between panels (drawn on figure level)
# Add a label at the bottom center
fig.text(0.5, 0.03,
         "Any Peer can submit a heavy task to the Master  →  Cluster processes it in parallel  →  Result returned to Peer",
         ha="center", fontsize=10, color="#cba6f7",
         fontfamily="monospace", fontweight="bold")

# Divider line
fig.add_artist(plt.Line2D([0.5, 0.5], [0.06, 0.96],
               transform=fig.transFigure,
               color="#45475a", linewidth=1.5, linestyle="--"))

fig.suptitle(
    "Distributed Resource Sharing & Processing System  —  Group 8  —  BITS Pilani DC Lab Assignment II",
    fontsize=12, color="#cdd6f4", fontfamily="monospace",
    fontweight="bold", y=0.985
)

plt.tight_layout(rect=[0, 0.07, 1, 0.97])

output = "/Users/naveenrenati/Downloads/DC/docs/images/architecture_diagram.png"
plt.savefig(output, dpi=150, bbox_inches="tight",
            facecolor=fig.get_facecolor())
print(f"Saved: {output}")
