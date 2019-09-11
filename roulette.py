import random
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


# Simulate
def simulate(bankroll, roll, bet):
	red_num = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
	black_num = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
	zeros = [0, 37]
	win_count = 0
	lose_count = 0
	while roll <= 100:
		print("-----------")
		print("Current Bet: ", bet)
		print("Bank roll: ", bankroll)
		if bet > bankroll:
			print("Bet is more than bankroll, can't play")
			return bankroll
		else:
			bankroll = bankroll - bet
			result = random.randint(0, 37)
			#betting the money away, hence minus
			if result in black_num:
				# Win
				bankroll = bankroll + (bet * 2)
				print("Win,Bank Roll: ", bankroll)
				# Roll count
				roll = roll + 1
				# Reset bet
				bet = 1
				print("Reset bet: ", bet)
				#count wins
				win_count = win_count +1
				continue
			else:
				#print(result, "Red")
				# Lose
				print("Lose,Bank Roll: ", bankroll)
				# Roll count
				roll = roll + 1
				# Double bet
				bet = bet * 2
				print("Double bet: ", bet)
				#count lose
				lose_count = lose_count + 1
				continue
	# Return final bankroll for 1 run
	print("------------")
	print("wins: ", win_count)
	print("loses: ", lose_count)
	return bankroll


# Main
def main():
	# Init variables
	roll = 1
	bankroll = 255
	bet = 1
	plays = []
	wins =[]
	loses = []
	# Simulate 1000 times
	for i in range(1000):
		result = simulate(bankroll, roll, bet)
		plays.append(result)
	# Histogram
	print("Bankroll after 1000 simulations: ", plays)

	# Create figure
	plt.figure()
	plt.hist(plays, bins='auto', histtype='bar', rwidth=0.9)

	# Title and labels
	plt.ylabel('Frequency')
	plt.xlabel('Bankroll')
	plt.title('100 Roulette')

	# save as pdf
	print("PDF is saving... ")
	plt.savefig('histogram_roulette.png', bbox_inches='tight')
	print("PDF saved.")


if __name__ == '__main__':
	main()
