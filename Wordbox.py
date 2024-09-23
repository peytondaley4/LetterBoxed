from english_words import get_english_words_set
wordset = get_english_words_set(['web2'], alpha=True, lower=True)
trunkset = set()
finalset = set()

box = [{'u', 'h', 'k'}, {'a', 'l', 'g'}, {'p', 'd', 'r'}, {'s', 'o', 'n'}]
boxset = {'u', 'h', 'k', 'a', 'l', 'g', 'p', 'd', 'r', 's', 'o', 'n'}

if __name__ == "__main__":
	for word in wordset:
		test = False
		for char in word:
			if char not in boxset:
				test = True
		if not test and len(word) > 2:
			trunkset.add(word)

	print(len(trunkset))

	for word in trunkset:
		test = False
		for i in range(len(word)-1):
			for s in box:
				if word[i] in s and word[i+1] in s:
					test = True
		if not test:
				finalset.add(word)

	sortlist = sorted(finalset, key=len)[::-1]
	print(len(sortlist))
	print(sortlist)