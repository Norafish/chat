# 聊天紀錄轉換
# 轉換的function中，使用continue換到下一行
# None用來當預設值
#讀取程式function

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f: # \ufeff存在於記事本編碼，我們看不到，遇到時在utf-8後面-sig
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #如果person有值才做下一步加入的動作
			new.append(person + ':' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	lines = convert(lines) # 投入lines	，得到new
	write_file('output.txt', lines)

main() # 進入點，function都是不執行的，除非使用他