from time import strftime, localtime

def write_line(file_name, line):
	with open(file_name, "a+") as f:
		f.write(line)

def match_update(score, minute, event):
	h, hs, v, vs = (score)
	current_score = f"{h} {hs} {v} {vs}"
	time = strftime("%I:%M %p", localtime())
	date = strftime("%Y%m%d", localtime())
	match_line = f"{time} | {current_score} | {min}\': {event}\n"
	file_name = f"{date}.{h}{v}.txt"
	write_line(file_name, match_line)

def score():
	home_team = "MUN"
	home_score = 1
	away_team = "CHE"
	away_score = 0
	current_score = [home_team, home_score, away_team, away_score]
	return current_score

minute = '24'
event = "Rashford finishes the penalty"

match_update(score(), minute, event)
