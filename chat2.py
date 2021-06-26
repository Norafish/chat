# 聊天紀錄轉換
# 轉換的function中，使用continue換到下一行
# None用來當預設值
# 讀取程式function
# 清單分割: n[開始值, 結束值](開始有包含，結束不包含)
# 範例: n[:3]可以拿到前三個，開始值是0可以不用寫。n[2, 4]可以拿到n[2]、n[3]。n[-2:]可以拿到最後兩個，-表示從後面數到前面，結尾值不寫表示到底。

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f: # \ufeff存在於記事本編碼，我們看不到，遇到時在utf-8後面-sig
			lines.append(line.strip())
	return lines

# 將字串分割統計每個人說話長度
def convert(lines):
	person = None
	allen_word_count = 0 # s[2]以後才是對話紀錄，allen講的字數就把他家在這
	viki_work_count = 0
	allen_image_count = 0
	allen_sticker_count = 0
	viki_image_count = 0
	viki_sticker_count = 0
	for line in lines:
		s = line.split(' ') #切割，切完變清單
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '圖片':
				allen_image_count += 1
			elif s[2] == '貼圖':
				allen_sticker_count +=1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '圖片':
				viki_image_count += 1
			elif s[2] == '貼圖':
				viki_sticker_count +=1
			else:
				for m in s[2:]:
					viki_work_count += len(m)
	
	print('allen說了', allen_word_count,'個字', '傳了', allen_image_count,'圖片和', allen_sticker_count, '個貼圖')
	print('viki說了', viki_work_count,'個字', '傳了', viki_image_count,'圖片和', viki_sticker_count, '個貼圖')


def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines) # 投入lines	，得到new
	# write_file('output.txt', lines) #改成註解就不會寫入檔案，因為function不會持行

main() # 進入點，function都是不執行的，除非使用他