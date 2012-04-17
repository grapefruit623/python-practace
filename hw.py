# -*- coding: utf-8 -*-
import re
import sys

def main():
	f = open(sys.argv[1], 'r')
	w = f.read()
	dic = {} 
	count = 0
	for s in re.findall('<DOC>[\s\S]*?</DOC>', w):	 #單一文章
		title = re.search('<DOCNO>(.*?)</DOCNO>', s)#文章段落
		docTitle = title.group(1)
		sp = re.split('[ |\n]', s)		#用空白或換行抓字
		for n in sp:
			l = re.search('.*\(.*\)', n)	#關鍵字(詞性)	
			if l:
				s = l.group(0) 
				if s in dic.keys():	#檢查所有關鍵字
					if docTitle in dic[s].keys():	#確認關鍵字是否出現在本段落
						dic[s][docTitle] = dic[s][docTitle] + 1 #在本文出現次數加1
					else:
						dic[s][docTitle] = 1 #表格中已有該關鍵字並蒂一次於本段落出現 
				else:
						dic[s] = {} #用新關鍵字作辭典索引並預設為空
						dic[s][docTitle] = 1 #關鍵字出現一次
	for i in dic.keys():
		print "%s " %i 
		for t in dic[i].keys():
			print "\t出現在  %s  %d 次\n" %(t, dic[i][t]),
		print  
if __name__ == "__main__":
	main()
