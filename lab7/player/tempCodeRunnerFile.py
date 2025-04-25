def update_status(new_status):
    global status_text
    status_text = new_status
    print(new_status)

def play_track():
    global current_track
    pygame.mixer.music.load(tracks[current_track])
    pygame.mixer.music.play()
    track_name = os.path.basename(tracks[current_track])
    update_status(f"Играет: {track_name}")

def next_track():
    global current_track
    current_track = (current_track + 1) % len(tracks)
    play_track()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(tracks)
    play_track()

def stop_music():
    pygame.mixer.music.stop()
    update_status("Музыка остановлена")

play_track()