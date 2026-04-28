# Random Walks

A **random walk** is one of the simplest objects in probability, and one of the most surprisingly powerful. The idea:

> At each step, take a small move in a randomly chosen direction. Repeat.

That's it. No memory, no strategy, no goal. Just one random step after another.

Despite how simple this sounds, random walks describe an enormous amount of the world:

- the path of a pollen grain jiggling in water (Brownian motion)
- the price of a stock from one minute to the next
- the diffusion of heat through a metal bar
- the trajectory of a foraging animal looking for food
- the way a search algorithm explores a graph
- how a neural network's weights drift during training
- the spread of a rumor, a gene, or a virus

The reason random walks are so universal is that **anything driven by many small, roughly independent nudges starts to look like a random walk** — regardless of what those nudges actually are. This is one of the deepest ideas in probability (related to the Central Limit Theorem).

## What we'll build

This folder works through random walks from absolute scratch. Each numbered subfolder is a small standalone Jupyter notebook that interleaves explanation, code, and visualizations (including animations). Read them in order if you're new to this.

| Folder | What you'll learn |
|---|---|
| [`01_what_is_a_walk/`](01_what_is_a_walk/) | The simplest possible random walk — flip a coin, step left or right. Watch one path unfold. |
| [`02_many_paths/`](02_many_paths/) | Run the same walk a thousand times. See the *fan* of possible outcomes. |
| [`03_sqrt_t_law/`](03_sqrt_t_law/) | The headline result: the spread of outcomes grows as the **square root of time**. We'll derive it and see it. |
| [`04_two_dimensions/`](04_two_dimensions/) | Walks on a 2D grid — the classic "drunkard's walk." Will the walker ever come home? |
| [`05_multiplicative/`](05_multiplicative/) | When steps *multiply* instead of *add*. This is how compounding processes (wealth, populations, viruses) actually behave — and why their distributions get weird. |
| [`06_horizon_and_variance/`](06_horizon_and_variance/) | The strategic punchline. When you have a long horizon, how does the *variance* of your steps change what outcomes are possible? |

## The one big idea, up front

If you remember nothing else, remember this:

After $t$ steps, a random walk has typically moved a distance of about $\sqrt{t}$ from where it started — **not** $t$.

This is wildly counterintuitive at first. If each step is size 1, you might expect $t$ steps to take you a distance $t$ away. But because the steps go in random directions, they cancel each other out *most* of the time. The cancellation isn't perfect, though, and the leftover drift grows as $\sqrt{t}$.

This single fact — the **$\sqrt{t}$ law** — has consequences that ripple through physics, finance, biology, and decision-making under uncertainty. We'll spend a lot of time with it.

## How to use this folder

Each subfolder has a `.ipynb` notebook. Open it, run the cells top to bottom, stare at the pictures, tweak the parameters, and re-run. You don't need any prior probability or statistics background — just a willingness to play with code and notice patterns.

## Setup

```bash
pip install numpy matplotlib jupyter
```

Then `jupyter lab` (or `jupyter notebook`, or open the `.ipynb` in VS Code / your editor of choice).
