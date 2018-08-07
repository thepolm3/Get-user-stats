import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

subredditScores = []
with open('scores.txt') as f:

	for line in f.readlines():
		subreddit, scores, n = line.split(':')
		scores = [int(i) for i in scores.split('+')]
		n = [int(i) for i in n.split('+')]
		subredditScores.append((subreddit, scores, n))

N = 20
N = min(N,len(subredditScores))
ind = np.arange(N + 1)*2
width = 1

labels = [s[0] for s in subredditScores[:N]] + ['other']
votes = [s[1][0] + s[1][1] for s in subredditScores]
votes = votes[:N] + [sum(votes[N:])]
bar1 = plt.bar(ind, votes, width, color = 'red')

votes = [s[1][0] for s in subredditScores]
votes = votes[:N] + [sum(votes[N:])]
bar2 = plt.bar(ind, votes, width, color = 'blue')

plt.legend([bar1,bar2], ['submissions','comments'])
plt.xticks(ind, labels, rotation='vertical')

plt.tight_layout()
plt.savefig('plot.png')

if __name__ == '__main__':
	plt.show()