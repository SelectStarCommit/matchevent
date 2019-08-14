from time import strftime, localtime

def write_line(file_name, line):
	with open(file_name, "a+") as f:
		f.write(line)
		
def match_update(score, min, event):
	s = ' '
	h, hs, v, vs = (score)
	current_score = str(h + s + hs + s + v + s + vs)
	time = strftime("%I:%M %p", localtime())
	date = strftime("%Y%m%d", localtime())
	match_line = time + ' | ' + current_score + ' | ' + min + '\': ' + event + '\n'
	file_name = str(date + h + v + '.txt')
	write_line(file_name, match_line)


score = ['MUN', '0', 'CHE', '0']
min = '01'
event = "We're underway, no score, no red cards yet'"

match_update(score, min, event)
