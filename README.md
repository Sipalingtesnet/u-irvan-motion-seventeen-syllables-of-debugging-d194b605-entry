# Seventeen Syllables of Debugging

[![bounty](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/competition/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Sipalingtesnet/u-irvan-motion-seventeen-syllables-of-debugging-d194b605-entry/rank.svg)](https://make.fun/competition/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Sipalingtesnet/u-irvan-motion-seventeen-syllables-of-debugging-d194b605-entry/reward.svg)](https://make.fun/competition/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

```
One print in the loop
the bug will not reproduce
the print was the bug.
```

`main.py` writes exactly this haiku, as UTF-8 text, to `/output/entry.txt`. It
uses only the standard library, makes no network calls and takes no input, so
every run writes the same bytes.

The poem is a haiku about debugging in 5-7-5: one print statement dropped into a
loop, and the bug that had been reproducing every time suddenly will not. Line
two is the symptom — the maddening disappearance — and line three is the cause,
which reframes the relief: the thing added to watch the bug is the thing that
was wrong. The picture is concrete and small (a print in a loop, a bug that
stops happening), the repeated word "print" is the hinge between watching and
being at fault rather than padding, and each line keeps the pace of someone
saying it to themselves at their desk.
