# shuffle analyzer
def shuffle(deck, piles=5, times=1, disp=False):
	'''
	Hard shuffle your deck
	deck - list of cards
	piles=5 - piles to hard shuffle into
	times=1 - repeat how many times
	disp=False - if True, print result, otherwise return it
	'''
	for time in range(times):
		pile = []
		for x in range(piles):
			pile.append([])
		for num, card in enumerate(deck):
			pile[num%piles].append(card)
		deck = joinLists(pile)
	if disp:
		from pprint import pprint
		pprint(deck)
	else:
		return deck

def joinLists(l):
	'''
	Join a list of lists into a single list.
	'''
	out = []
	for pile in l:
		for card in pile:
			out.append(card)
	return out

def createDeck(**kwargs):
	'''
	Accepts numbers for the following types of cards:
	\t-land
	\t-instant
	\t-sorcery
	\t-creature
	In that order.
	'''
	if 'land' in kwargs:
		land = kwargs['land']
	else:
		land = 0
	if 'instant' in kwargs:
		instant = kwargs['instant']
	else:
		instant = 0
	if 'sorcery' in kwargs:
		sorcery = kwargs['sorcery']
	else:
		sorcery = 0
	if 'creature' in kwargs:
		creature = kwargs['creature']
	else:
		creature = 0
	total = land + instant + sorcery + creature
	deck = []
	for card in range(total):
		out = str(card) + ' - '
		if card < land:
			out += 'land'
		elif card < land + instant:
			out += 'instant'
		elif card < land + instant + sorcery:
			out += 'sorcery'
		elif card < land + instant + sorcery + creature:
			out += 'creature'
		deck.append(str(out))
	return deck