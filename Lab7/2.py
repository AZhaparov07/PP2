import pygame
import os
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")
music_folder = r"C:\Users\User\Desktop\pp2 start\PP2\Lab7\songsmp3"
tracks = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
if not tracks:
    exit()
current_index =0
def play_track(index):
    global current_index
    current_index= index
    path= os.path.join(music_folder, tracks[current_index])
    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        print(f"playing: {tracks[current_index]}")
    except Exception as e:
        print(f"error playing {tracks[current_index]}: {e}")
play_track(current_index)
running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    print("Paused")
                else:
                    pygame.mixer.music.unpause()
                    print("Resumed")
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                print("Stopped")
            elif event.key == pygame.K_n:
                current_index = (current_index + 1) % len(tracks)
                play_track(current_index)
            elif event.key == pygame.K_b:
                current_index = (current_index - 1) % len(tracks)
                play_track(current_index)
    pygame.display.flip()
pygame.quit()

