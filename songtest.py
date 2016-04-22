import urllib2

print ("\nCHECK SONGS by Alex McHugh\n")

artist = raw_input("Artist to check: ")

print("")

songs = []

while(1):
	song = raw_input("Enter song to check: ")
	if (not song):
		break
	songs.append(song)

words = ["damn", "bitch", "shit", "fuck", " ass "]

print("")
for song in songs:
	try:
		a = artist.replace(" ", "-")
		s = song.replace(" ", "-")
		s1 = s.replace("'", "")
		url="http://genius.com/" + a + "-" + s1 + "-lyrics"

		req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
		page = urllib2.urlopen(req)
		data = page.read()
		newData = data.split("<h2 class=\"text_label text_label--gray u-top_margin\">")
		finalData = newData[1].split("</lyrics>")
		bad = False
		for word in words:
			if (word in finalData[0]):
				print(song + " is not clean")
				bad = True
				break
		if (not bad):
			print(song + " is clean!")
	except:
		print ("\nThere was an error when checking " + song + "\n")
		continue
print("")
