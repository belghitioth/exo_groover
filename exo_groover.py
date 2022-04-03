
def retrieve_all_combinaisons_of_n_tracks(tracks,nb_tracks_for_premiere):
    tracklist_combinaisons=[]
    nb_tracks = len(tracks)
    indices = list(tracks.keys())[0:nb_tracks_for_premiere]
    tracklist = dict(filter(lambda key: key[0] in indices, tracks.items()))
    tracklist_combinaisons.append(tracklist)

    index = nb_tracks_for_premiere-1
    while (index !=-1):
       indices[index] +=1

       for j in range(index+1,nb_tracks_for_premiere):
         indices[j] = indices[j-1] +1

       if indices[index]== (nb_tracks-(nb_tracks_for_premiere-2) + index):
        index -=1
       else :
        index = nb_tracks_for_premiere-1

        tracklist = dict(filter(lambda key: key[0] in indices, tracks.items()))
        tracklist_combinaisons.append(tracklist)

    return tracklist_combinaisons


def is_combinaison_of_n_tracks_ok_for_concert_premiere(tracklist_combinaisons,concert_premiere_length):
    for tracklist in tracklist_combinaisons:
        tracklist_length= sum(tracklist.values())
        if tracklist_length == concert_premiere_length:
            return True
    return False

#Initialize values
tracks = {
    1 : 10,
    2 : 12,
    3 : 5,
    4 :7,
    5 : 9
}
print("---- Number of tracks : ",len(tracks)," ----")

nb_tracks_for_premiere = 4
concert_premiere_length = 26



def is_tracklist_ok_for_premier_concert(tracks, nb_tracks_for_premiere, concert_premiere_length):

    """
    Returns True if there is a tracklist of n elements that have a length equals to premiere_concert_length
    """
    tracklist_combinaisons = retrieve_all_combinaisons_of_n_tracks(tracks,nb_tracks_for_premiere)
    print("---- Combinaisons possibles  : ",tracklist_combinaisons," ----")
    resultat = is_combinaison_of_n_tracks_ok_for_concert_premiere(tracklist_combinaisons, concert_premiere_length)
    return resultat

print(is_tracklist_ok_for_premier_concert(tracks,nb_tracks_for_premiere,concert_premiere_length))