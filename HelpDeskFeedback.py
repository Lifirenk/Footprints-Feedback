#Help Desk Feedback Tool
#Written by Andrew Slentz
#Created: 3-23-16
#Utilizes the exported email file for Footprints feedback to generate a 
#customized report for the service desk.

#4-5-16
#added writing to file
#defined keywords and locations to be removed

dir = 'F:\\Feedback\\'
file = 'feedback.csv'
item = []
report = []
cont = []
isa = []
cont.append('https://footprints02')
cont.append('Entered on')

errata= ('Student','Studemp','Staff','Faculty','Admissions','Affiliate','Alumni','Retiree','(no data)','Excellent','Good','Poor')

def popper( lusitania ):
        while len(lusitania) > 0:
                lusitania.pop()

def stripper( candy ):
        for sug in range(0, len(candy)):
                for 
               print candy[sug]
        #line to strip of from known content
        #strip from known context lines
      #if in candy[1]:
              

#open read and close the file
with open(dir+file, 'r') as openfo:
    rep = openfo.readlines()
rep = [r.strip('\n') for r in rep]

#only take from bottom of the ITEM to the DATE stamp

#Detects the end of an item then determines if the item is of the type we are 
#looking for (by length) filters out irrelevant information then adds to the
#final output, ortherwise it assembles more info for the item
for x in range(0, len(rep)):
        if rep[x] == '________________________________':
                if len(item) < 10:
                        popper(item)
                        continue
                elif "HelpDesk" not in item[5]:
                        popper(item)
                        continue
                if 'No Description Entered' in item[10]:
                        popper(item)
                        continue
                stripper(item)
                report.append(item)
                for i in item:
                        print 'main'
                item.pop(1)
                popper(item)
        else:
                item.append(rep[x])


#ext = open('F:\\Feedback\\LatestReport.txt', 'w+')
#print report
#for item in report:
        #for l in item:
                #print l#text.write(f)
#text.close()
