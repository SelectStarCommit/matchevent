from time import strftime, localtime

def match_update(score, minute, event):
	ht, hts, at, ats = (score)
	current_score = f"{ht} {hts} {at} {ats}"
	time = strftime("%I:%M %p", localtime())
	date = strftime("%Y%m%d", localtime())
	match_line = f"{time} | {current_score} | {minute}\': {event}\n"
	file_name = f"{date}.{ht}{at}.txt"
	write_line(file_name, match_line)

def write_line(file_name, line):
	with open(file_name, "a+") as f:
		f.write(line)

def score():
	home_team = "MUN" #Home team in TV caps, used in file name
	home_score = 1
	away_team = "CHE" #Away team in TV caps, used in file name
	away_score = 0
	current_score = [home_team, home_score, away_team, away_score]
	return current_score

minute = '24'
event = "Rashford finishes the penalty"

match_update(score(), minute, event)
