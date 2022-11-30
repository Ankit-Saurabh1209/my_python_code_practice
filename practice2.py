import pandas as pd
world_cup = pd.read_html('https://en.wikipedia.org/wiki/Cricket_World_Cup')
print(len(world_cup))
