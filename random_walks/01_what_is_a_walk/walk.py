"""
A single 1D random walk.

At each of N steps, we flip a fair coin: heads sends us +1, tails -1.
The walker's position over time is the running total of those flips.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- parameters you can tweak ---
N_STEPS = 1000
SEED = 42  # change this (or set to None) to see a different walk

# --- generate the walk ---
rng = np.random.default_rng(SEED)
steps = rng.choice([-1, 1], size=N_STEPS)

# Position at time t = the running total of all steps taken so far.
# We prepend a 0 so the path starts at the origin at step 0.
positions = np.concatenate([[0], np.cumsum(steps)])

print(f"final position after {N_STEPS} steps: {positions[-1]}")
print(f"highest position reached:           {positions.max()}")
print(f"lowest  position reached:           {positions.min()}")

# --- plot it ---
fig, ax = plt.subplots(figsize=(10, 4.5))
ax.plot(positions, linewidth=1)
ax.axhline(0, color="gray", linewidth=0.6, linestyle="--", alpha=0.7)
ax.set_xlabel("step number (t)")
ax.set_ylabel("position")
ax.set_title(f"A single random walk — {N_STEPS} coin-flip steps")
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig("walk.png", dpi=120)
print("saved figure to walk.png")
plt.show()
