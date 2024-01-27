#程式邏輯題目第三題
import random
n = random.randint(0, 100)
out = 3

def winner_count(n, out):
    if n == 0:
        return 0
    else:
        colleagues = list(range(1, n + 1))
        current = 0

        while len(colleagues) > 1:
            current = (current + out - 1) % len(colleagues)
            del colleagues[current]

        return colleagues[0]

result = winner_count(n, out)
if result != 0:
    print(f"在所有 {n} 位同事的第 {result} 順位")
else:
    print("沒有同事參與")