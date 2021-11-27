n = int(input("Enter amount: ")) # 1234

fh = n//500
rm = n - fh*500
print("500 Taka: ", fh, " note(s)", ", ", rm)
oh = rm//100
rm = rm - oh*100
print("100 Taka: ", oh, " note(s)", ", ", rm)
tw = rm //20
rm = rm - tw*20
print("20 Taka: ", tw, " note(s)", ", ", rm)
t = rm //10
rm = rm - t*10
print("10 Taka: ", t, " note(s)", ", ", rm)
o = rm //1
rm = rm - o
print("1 Taka: ", 0, " note(s)", ", ", rm)

# 1234 - 2*500 = 1234 - 1000 = 234
# 234 - 2*100 = 234 - 200 = 34
# 34 - 1*20 = 34 - 20 = 14
# 14 - 1*10 = 14 - 10 = 4
# 4 - 1*4 = 4 - 4 = 0




