
tracks = {
    1 : 10,
    2 : 12,
    3 : 5
}

concert_premiere_length = 27
print("---- Number of tracks : ",len(tracks)," ----")

def retrieve_all_combinaisons_of_3_tracks(tracks):
    tracklist_combinaisons=[]
    nb_tracks = len(tracks)
    indices = list(tracks.keys())[0:3]
    tracklist = dict(filter(lambda key: key[0] in indices, tracks.items()))
    tracklist_combinaisons.append(tracklist)
    return tracklist_combinaisons


def is_combinaison_of_3_tracks_ok_for_concert_premiere(tracklist_combinaisons,concert_premiere_length):
    for tracklist in tracklist_combinaisons:
        tracklist_length= sum(tracklist.values())
        if tracklist_length == concert_premiere_length:
            return True
    return False


tracklist_combinaisons = retrieve_all_combinaisons_of_3_tracks(tracks)
print(tracklist_combinaisons)
print(is_combinaison_of_3_tracks_ok_for_concert_premiere(tracklist_combinaisons, concert_premiere_length))