def song_decoder(song):
    out_str = song.replace("WUB", " ")
    out_str = ' '.join(out_str.split())
    return out_str