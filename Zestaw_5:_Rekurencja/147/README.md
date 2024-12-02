<picture>
  <source srcset="../../srt/zbior_zadan/147.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_147.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_147.png" alt="zadanie 147">
</picture>

```python
def move(from_start, to_end):
    print("Move", from_start, "to", to_end)


def tower_of_hanoi(n, A, B, C):
    if n == 0:
        print("0")
        return
    if n == 1:
        move(A, C)
        return
    else:
        tower_of_hanoi(n - 1, A, C, B)  # transfer z A do B z pomocą C
        move(A, C)
        tower_of_hanoi(n - 1, B, A, C)



```