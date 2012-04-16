# -*- coding: utf-8 -*-
import re
import sys

def main():
	f = open(sys.argv[1], 'r')
	w = f.read()
	dic = {} 
	for s in re.findall('<DOC>[\s\S]*?</DOC>', w):
		title = re.search('<DOCNO>(.*?)</DOCNO>', s)
		docTitle = title.group(1)
		sp = re.split('[ |\n]', s)
		for n in sp:
			l = re.search('.*\(.*\)', n)
			if l:
				s = l.group(0) 
				if s in dic.keys():
					if docTitle in dic[s].keys():
						dic[s][docTitle] = dic[s][docTitle] + 1
					else:
						dic[s][docTitle] = 1
				else:
					dic[s] = {}
					dic[s][docTitle] = 1 
	for i in dic.keys():
		print "%s " %i #( re.search('(.*)', i) ).group(1) )
		for t in dic[i].keys():
			print "\t出現在  %s  %d 次" %(t, dic[i][t]),
		print  
if __name__ == "__main__":
	main()
