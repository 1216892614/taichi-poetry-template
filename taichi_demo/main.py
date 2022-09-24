import taichi as ti
import numpy as np

UP_TO = 15000

gui = ti.GUI("circles", res=(400, 400))

i = 1
while gui.running:
    pos = np.random.random((i%UP_TO, 2))
    indices = np.random.randint(0, 2, size=(i%UP_TO,))
    # Create an array of 50 integer elements whose values are randomly 0, 1, 2
    # 0 corresponds to 0x068587
    # 1 corresponds to 0xED553B
    # 2 corresponds to 0xEEEEF0
    gui.circles(pos, radius=5, palette=[0x068587, 0xED553B, 0xEEEEF0], palette_indices=indices)
    gui.show()
    i += 2