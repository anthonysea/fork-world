import sys, pickle, webbrowser, urllib

print "Which craigslist page would you like to crawl? "
webpage = raw_input("> ")

if 'http://' not in webpage:
	webpage = 'http://' + webpage
	
page = urllib.urlopen(webpage)
pages = page.readlines()

searchWord = raw_input("What would you like to search for? ")
matches = []
for line in pages:
	if searchWord in line.lower():
		matches.append(line)
		
if len(matches) == 0:
	print "You're search query did not match anything on the page"

count = 0
for item in matches:
	firstQuote = item.find('="')
	endQuote = item.find('">')
	print item[firstQuote+2:endQuote]
	if count < 10:
		webbrowser.get('windows-default').open(item[firstQuote+2:endQuote])
		count = count + 1
	
	