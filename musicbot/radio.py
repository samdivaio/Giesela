import urllib.request
from random import shuffle

from bs4 import BeautifulSoup


class Radio:

    def __init__(self):
        self.song_list = []
        self.old_songs = []

    def update_list_capitalfm(self, replay_songs=False):
        with urllib.request.urlopen('http://www.capitalfm.com/digital/radio/last-played-songs/') as response:
            html = response.read()

            soup = BeautifulSoup(html, "lxml")
            tags = soup.find_all('div', class_="song_wrapper", limit=10)
            for t in tags:
                name = t.find("a", class_="track") or t.find(
                    "span", class_="track")
                author = t.find("a", class_="first") or t.find(
                    "span", class_="artist")
                if name is not None:
                    information = (name.text.strip(), author.text.strip()
                                   if author is not None else "Unknown")
                    if (information not in self.song_list and information not in self.old_songs) or (replay_songs and information not in self.song_list):
                        self.song_list.append(information)

    def update_list(self, replay_songs=False):
        self.song_list = []

        self.update_list_capitalfm(replay_songs)

    def refresh(self):
        print("Refreshing!")
        self.song_list = []
        self.old_songs = []

    def get_next_song(self, update=True, replay_songs=True):
        if len(self.song_list) < 1 or update:
            self.update_list()

            if len(self.song_list) < 1 and replay_songs:
                print("capitalfm couldn't keep up\nReplaying songs (cleaning the lists)")
                self.refresh()
                self.update_list()
                shuffle(self.song_list)

                if len(self.song_list) < 1:
                    if len(self.old_songs) > 0:
                        print("Still nothing. Going to replay the oldest song now")
                        return self.old_songs.pop()
                    else:
                        print(
                            "Still nothing. Something must either be wrong with capitalfm or there is no music being played")
                        return None
            elif not replay_songs:
                return None

        song = self.song_list.pop(0)
        self.old_songs.append(song)
        return song