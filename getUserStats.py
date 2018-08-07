from secret import client_id, client_secret
import praw
from collections import defaultdict
import sys

try:
	targetName = sys.argv[1]
except IndexError:
	targetName = 'thepolm3'

reddit = praw.Reddit(client_id = client_id,
					client_secret = client_secret,
					user_agent = 'Python:getUserStats:v1 (by /u/thepolm3)')

target = reddit.redditor(targetName)
subredditScores = defaultdict(lambda: [0,0,0,0])

print(f'Sucessfully reached /u/{targetName}\'s profile, now creating scores.txt (This may take up to a minute)')

for comment in target.comments.new(limit = None):
    subredditScores[comment.subreddit.display_name][0] += comment.score
    subredditScores[comment.subreddit.display_name][2] += 1

for submission in target.submissions.new(limit = None):
    subredditScores[submission.subreddit.display_name][1] += submission.score
    subredditScores[submission.subreddit.display_name][3] += 1

subredditScores = sorted(subredditScores.items(), key=lambda t: t[1][0] + t[1][1], reverse = True)

with open('scores.txt','w+') as f:
	f.write(f'{targetName}\n' + '\n'.join([f'{subreddit}:{v[0]}+{v[1]}:{v[2]}+{v[3]}' for  subreddit, v in subredditScores]))

