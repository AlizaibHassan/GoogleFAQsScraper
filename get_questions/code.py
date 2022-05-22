import people_also_ask
import csv
import re

cnt=0

all_questions = []

with open('input.csv', mode='r') as inp:
    reader = csv.reader(inp)
    all_questions = {rows[0] for rows in reader}



for lst in all_questions:

	question = people_also_ask.get_related_questions(lst)

	s = "\n".join(question)

	cnt+=1

	s = re.sub("\\?[a-zA-Z0-9].+?\\?", "", s)

	f= open("op.txt","a+")
	f.write(str(s))
	f.write(str("\n"))
	print(cnt)


print("\n")
print("Complete")