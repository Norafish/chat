# 清單切割，清單的切割也可以用在字串上
# 把時間跟人名黏在一起的字串切割，取出人名

# 讀取檔案
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())
for line in lines:
	s = line.split()
	name = s[0][5:]
	time = s[0][:5]
	print(time, name)	
