from Tkinter import *
from time import sleep
from controller.deck import Deck
from static.static import Static

class App:
    def __init__(self):
        self.deck = Deck()
        self.player = 0

        self.root = Tk()
        self.root.title('King\'s Cup')

        # Pack the initial card image.
        logo = PhotoImage(file="./static/gifs/K_S.gif")
        self.card_image = Label(self.root, image=logo)
        self.card_image.image = logo
        self.card_image.pack(side='left')

        explanation = "King's Cup is a drinking game!\nJust follow the instructions."
        self.rule = Label(self.root,
                    width = 25,
                    justify=LEFT,
                    padx = 20,
                    text=explanation)
        self.rule.pack(side="left")

        self.button = Button(self.root,
                             text="Draw!",
                             command=lambda: self.change())
        self.root.bind('<Return>', self.change)
        self.button.pack(side='left')

        self.root.mainloop()

    def change(self, event=None):
        card = self.deck.getCard()

        # Set the card image.
        card_image = PhotoImage(file='./static/gifs/%s_%s.gif' % (card['val'], card['suit']))
        self.card_image.config(image=card_image)
        self.card_image.image = card_image
        self.rule.config(text = Static.cardRules[card['val']])
        self.rule.text = Static.cardRules[card['val']]

if __name__ == '__main__':
    App()

