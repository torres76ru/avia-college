def makeHash(querySet):
	return {c.name: c.content for c in querySet}