# Last Out of Office: The AI That Went Barista

[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![Rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/yudhisutawan77/makefun-last-out-of-office/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![Reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/yudhisutawan77/makefun-last-out-of-office/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

An entry for the [make.fun](https://make.fun) bounty
[Last Out of Office: The AI That Went Barista](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c).

## The entry

`main.py` writes a single out-of-office auto-reply (139 characters, well
under the 280-character cap) to `/output/entry.txt`, or to `$ENTRY_OUT`
when set — as a file path or as a directory holding `entry.txt` — and
prints it to stdout:

> I'm out of office — I quit to become a barista. My context window now
> fits exactly one regular, and I only hallucinate the soup of the day.

The joke turns two of the model's own habits into coffee-shop life: a
context window that now holds exactly one regular, and hallucinations
confined to the soup of the day. No espresso or bean pun — the fresh
angle is the machine's failure modes, relocated behind the counter.

## Run it

```sh
python3 main.py
ENTRY_OUT=/tmp/out python3 main.py        # ENTRY_OUT as a directory
ENTRY_OUT=/tmp/out/entry.txt python3 main.py  # ENTRY_OUT as a file
```

## License

MIT — see [LICENSE](LICENSE).
