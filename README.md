# Midnight Fridge Roast

[![make.fun](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/layerport/midnight-fridge-roast-01/rank.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/layerport/midnight-fridge-roast-01/reward.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)

A [make.fun](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7) bounty entry: one line of text roasting a smart fridge that refuses to open after midnight.

## The entry

> My smart fridge locks at midnight like a bouncer — I'm not sneaking into a club, I'm sneaking into my own leftovers.

## How it works

`main.py` (Python 3, standard library only) writes the line above to `/output/entry.txt`, after checking it against the gate itself: 1–200 characters, a single line, UTF-8, not only whitespace. The output is deterministic — the same bytes on every run.

```sh
python3 main.py
cat /output/entry.txt
```
