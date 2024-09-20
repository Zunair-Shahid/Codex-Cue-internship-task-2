
print("Zunair Shahid Second Project of Codex Cue Python Development internship program")

import pyshorteners # type: ignore

longurl = input('Enter the Long url: ')


def shorturl(longurl):
    s = pyshorteners.Shortener()
    print("Short URL:" + s.tinyurl.short(longurl))

shorturl(longurl)