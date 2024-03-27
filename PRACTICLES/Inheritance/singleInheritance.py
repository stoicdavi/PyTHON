class Box:
    def __init__(self, contents):
        self.contents = contents
    def open_box(self):
        print(f"Opening the box.....")
        print("The box contains: {}".format(self.contents))
my_box = Box("A pair of shoes")
my_box.open_box()