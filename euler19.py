
from calendar import monthrange as mr

ans = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        fday, days = mr(year, month)
        if fday==6:
            ans += 1

print(ans)
