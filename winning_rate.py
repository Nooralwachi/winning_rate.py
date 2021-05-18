def winning_rate(filename):
	with open(filename, 'r') as f:
		total_games =wins=maxmum=streak=0
		f.readline()
		for line in f:
			total_games+=1
			home,guest,result= line.strip().split()
			h,g = result.split('-')
			if (home == 'ABC' and int(h)>int(g)) or (guest == 'ABC' and int(g)>int(h)):
					streak+=1
					wins +=1
			else:
				maxmum = max(maxmum,streak)
				streak=0

		print(f'The win rate is: {wins*100/total_games}%')
		print(f'The longest winning streak {maxmum}')

winning_rate('results.txt')
