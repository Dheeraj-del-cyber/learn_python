class MusicPlayer:
    def play(self):
        print("Playing music...")
class Spotify(MusicPlayer):
    def play(self):
        print("Playing music from Spotify")
class YouTubeMusic(MusicPlayer):
    def play(self):
        print("Playing music from YouTube Music")
class AppleMusic(MusicPlayer):
    def play(self):
        print("Playing music from Apple Music")
s=Spotify()
y=YouTubeMusic()
a=AppleMusic()
players=[s,y,a]
for player in players:
    player.play()
