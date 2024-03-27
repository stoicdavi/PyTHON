class ElectronicDevice:
    def __init__(self, brand):
        self.brand = brand
    def power_on(self):
        print("Turing on the electronic device.....")

class MusicPlayer:
    def play_music(self):
        print("Playing the music player.....")

class MP3Player(ElectronicDevice, MusicPlayer):
    def __init__(self, brand, capacity):
        super().__init__(brand)
        self.capacity = capacity
    def playerName(self):
        print(f"Brand: {self.brand}")
        print(f"Capacity: {self.capacity}")

my_device = MP3Player("Apple", "32GB")

my_device.power_on()
my_device.play_music()
my_device.playerName()
