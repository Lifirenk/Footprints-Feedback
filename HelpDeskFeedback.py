#Help Desk Feedback Tool
#Written by Andrew Slentz
#Created: 3-23-16
#Utilizes the exported email file for Footprints feedback to generate a customized report for the service desk.

#import sys.stdout

dir = 'C:\\Feedback\\'
file = 'feedback.csv'
item = []
report = []


with open(dir+file, 'r') as openfo:
    rep = openfo.readlines()
rep = [r.strip('\n') for r in rep]


for x in range(0, len(rep)):
    print 'help 1'
    while rep[x] != '________________________________':
        print 'help 2'
        item.append(rep[x])
        print 'help 3'
    print item[1]
    print item[2]
    report.append(item)
    while len(item) > 0:
        item.pop()
print rep

			

