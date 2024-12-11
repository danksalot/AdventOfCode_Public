discs = [[7,0],[13,0],[3,2],[5,2],[17,0],[19,7]]
i = 0

while True:
	if (discs[0][1] + i+1) % discs[0][0] == 0:
		if (discs[1][1] + i+2) % discs[1][0] == 0:
			if (discs[2][1] + i+3) % discs[2][0] == 0:
				if (discs[3][1] + i+4) % discs[3][0] == 0:
					if (discs[4][1] + i+5) % discs[4][0] == 0:
						if (discs[5][1] + i+6) % discs[5][0] == 0:
							print i
							break

	i += 1