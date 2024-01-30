from tqdm.rich import trange
# 变成彩色了
for i in trange(100000):
    for j in range(100):
        k = i * j

from tqdm.notebook import trange
# 专为ipynb打造
# for i in trange(100000):
    # for j in range(100):
        # k = i * j