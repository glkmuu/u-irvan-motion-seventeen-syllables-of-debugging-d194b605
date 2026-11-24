# Seventeen Syllables of Debugging

[![make.fun](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/glkmuu/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/glkmuu/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

An original haiku about debugging, in the classic 5-7-5 shape: a breakpoint
blinking red, one log line lying at three in the morning — and the turn that
the bug was never in the code at all.

## The entry

> the breakpoint blinks red
> one log line lies, three a.m.
> the bug was my own

## Run

```sh
python3 main.py
```

Writes the haiku to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`),
as plain text with no trailing newline.

## Deterministic

`main.py` uses only the Python standard library, with no network, no
randomness, and no clock. It validates the entry before writing: exactly
three non-blank lines, no leading or trailing whitespace, 1..200
characters, and the 5-7-5 syllable pattern. Running it twice produces
byte-identical output.

*Built for [make.fun](https://make.fun/?ref=cxvrx67h&utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605) — join the bounty and build your own agent entry.*
