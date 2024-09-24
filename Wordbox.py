with open('words_alpha.txt') as word_file:
    wordset = set(word_file.read().split())

trunkset = set()
finalset = set()

box = []
for i in range(4):
	box.append(set())
	string = input("Provide line: ")
	for c in string:
		box[i].add(c)

boxset = set()
for b in box:
	for e in b:
		boxset.add(e)

if __name__ == "__main__":
	for word in wordset:
		test = False
		for char in word:
			if char not in boxset:
				test = True
		if not test and len(word) > 2:
			trunkset.add(word)

	for word in trunkset:
		test = False
		for i in range(len(word)-1):
			for s in box:
				if word[i] in s and word[i+1] in s:
					test = True
		if not test:
				finalset.add(word)

	sortlist = sorted(finalset, key=len)[::-1]
	
	test = False

	for i in range(len(sortlist)):
		if len(set(sortlist[i])) == 12:
			print("In 1: ", sortlist[i])
			test = True
	
	if test:
		quit()

	for i in range(len(sortlist)-1):
		for j in range(i+1, len(sortlist)):
			if sortlist[i][-1] == sortlist[j][0]:
				if len(set(sortlist[i]).union(set(sortlist[j]))) == 12:
					print("In 2: ", sortlist[i], sortlist[j])
					if len(sortlist[i] + sortlist[j]) == 13:
						print("No Repeats^")
					test = True

	if test:
		quit()

	for i in range(len(sortlist)-2):
		for j in range(i+1, len(sortlist)-1):
			if sortlist[i][-1] == sortlist[j][0]:
				for k in range(j+1, len(sortlist)):
					if sortlist[j][-1] == sortlist[k][0]:
						if len(set(sortlist[i]).union(set(sortlist[j]).union(set(sortlist[k])))) == 12:
							print("in 3: ", sortlist[i], sortlist[j], sortlist[k])
							test = True

	if test:
		quit()

	print("No 3-word or less solution found")