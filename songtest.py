import urllib2

words = ["damn", "bitch", "shit", "fuck", " ass "]

def checkSong(artist, song):
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
				bad = True
				return 0
		if (not bad):
			return 1
	except:
		return 2

