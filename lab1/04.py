tim = int(input())
H = tim//3600
tim = tim%3600
M = tim//60
tim = tim%60
S = tim
print(f"{H:02d}:{M:02d}:{S:02d}")