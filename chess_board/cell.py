import random


class Cell:
    """Store the information of every cell"""
    def __init__(self):

        self.status = ''
        self.x = ''
        self.y = ''
        self.next_status = False
        self.random_init()

    def random_init(self):
        if random.random() > 0.6:
            self.status = True
        else:
            self.status = False

    def show_status(self):
        """print status"""
        print(self.status)

    def update(self):
        """update status"""
        self.status = self.next_status
