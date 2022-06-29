def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """
    playlist = []
    if songs[0][2] < max_size:
        playlist.append(songs[0][0])
    else:
        return []
    playlist_size = songs[0][2]
    sorted_songs = sorted(songs, key=lambda song: song[2])
    sorted_songs.remove(songs[0])
    for song in sorted_songs:
        new_size = playlist_size+song[2]
        if new_size <= max_size:
            playlist.append(song[0])
            playlist_size = new_size
        else:
            break
    return playlist


songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
max_size = 1
print(song_playlist(songs, max_size))