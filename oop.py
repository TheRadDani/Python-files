class AudioPlaying(object):
    def __init__(self, file_name):
        if not file_name.endswith(self.ext):
            raise Exception("Invalid format")
        self.file_name = file_name


class MP3FILE(AudioPlaying):
    ext = "mp3"

    def playing(self):
        print(f"Playing {self.file_name} music to all volumn!")


object = MP3FILE("Lacabrita.mp3")
object.playing()
