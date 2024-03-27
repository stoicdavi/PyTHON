class Box:
    def __init__(self, contents):
        self.contents = contents
    def open_box(self):
        print(f"Opening the box.....")
        print("The box contains: {}".format(self.contents))
my_box = Box("A pair of shoes")
my_box.open_box()

#single inheritance
class GiftBox(Box):
    def __init__(self, contents, recipient):
        super().__init__(contents)
        self.recipient = recipient
    def open_box(self):#override the open_box method in super class
        print(f"\nOpening the box.....")
        print("The box contains: {}".format(self.contents))
        print("The recipient is: {}".format(self.recipient))
my_gift_box = GiftBox("A pair of shoes", "John")
my_gift_box.open_box()