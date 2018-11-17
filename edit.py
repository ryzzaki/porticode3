import moviepy.editor as mp
import start
import random
import json

st = start.Start()

class Editor:

    def __init__(self):
        self.topic = st.return_topic()
        self.default_path = "Pictures/" + self.topic
        self.used_files = []
        self.name_array = []
        self.selected_files = []
        self.edited_files = []
        self.audio_paths = ["Cetus", "Why we lose", "On and On", "Time Leap", "Blank", "Feel Good", "Hellcat", "Heroes Tonight", "Invincible", "Summer Tune"]

    def open_json(self):
        with open('nameray.json') as f:
            self.name_array = json.load(f)

    def generate_rand_song(self):
        num = random.randrange(0, len(self.audio_paths))
        return num

    def generate_rand_rotate(self):
        num = random.randrange(0, 180)
        return num

    def generate_rand_file(self):
        num = random.randrange(0, 34)
        return num

    def path_array(self):
        for name in self.name_array:
            generated_num = self.generate_rand_file()
            if generated_num not in self.used_files:
                self.used_files.append(generated_num)
                file_path = self.default_path + "/" + name
                self.selected_files.append(file_path)

    def edit_clip_img(self):
        for file in self.selected_files:
            # clip = mp.ImageClip(file, duration=10).add_mask().rotate(self.generate_rand_rotate())
            clip = mp.ImageClip(file, duration=5)
            self.edited_files.append(clip)

    def concatenate(self):
        song = "audio/" + self.audio_paths[self.generate_rand_song()] + ".mp3"
        print("Chosen song: " + song)
        merged = mp.concatenate_videoclips(self.edited_files)
        # merged = merged.set_audio(song.set_duration(merged, False))   idk why this doesnt work, help me
        merged.write_videofile("upload.mp4",fps=24,audio=song)
