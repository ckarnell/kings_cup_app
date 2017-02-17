# import sys
# sys.path.append('./Static')
# sys.path.append('./Controller')
from static.static import Static
from controller.deck import Deck

class Main_loop:
    from time import sleep
    cardRules = Static.cardRules
    suitSentence = Static.suitSentence
    options = Static.options

    def __init__(self, players):
        self.deck = Deck()
        self.player = 0

    def viewRules(self):
        for key in self.cardRules:
            print '%s: %s' % (key, self.cardRules[key])
        print ''
        self.sleep(1)
        self.optionChange()

    def setRule(self):
        val = raw_input('Which card\'s rule would you like to change?\n')
        val = val.upper()
        while val not in self.cardRules.keys():
            print('That\'s not a valid input. Choose from one of the following:\n')
            val = raw_input(str(self.cardRules.keys()))
        rule = raw_input('Enter what you want the new rule to be.\n')
        self.cardRules[val] = rule
        print 'Rule for %s set to "%s".\n' % (val, rule)
        self.sleep(1)
        self.optionChange()

    def optionChange(self):
        option = raw_input('''Options (choose an option key and press enter):
                 f: Finish game
                 v: View rules
                 c: Change a rule
                 e: Exit options and continue game\n''')

        option = option.lower()
        if option not in ['f', 'v', 'e', 'c']:
            print "You didn't enter a valid option."
            self.optionChange()
        elif option == 'f':
            self.options['finishAfterTurn'] = True
            print '\nThanks for playing retard!'
        elif option == 'c':
            self.setRule()
        elif option == 'v':
            self.viewRules()
        elif option == 'e':
            print ''

    def turn(self):
        options = raw_input('Press Enter to draw your card player %d! (or enter "o" for options)\n' % (self.player + 1))
        if options.lower() == 'o':
            self.optionChange()

        if not self.options['finishAfterTurn']:
            self.player = (self.player + 1) % players
            card = self.deck.getCard()
            print '%s%s' % (card['val'], self.suitSentence[card['suit']])
            print self.cardRules[card['val']] + '\n'

            self.sleep(2)
            self.turn()

if __name__ == '__main__':
    players = raw_input('How many players?\n')
    while type(players) != type(0):
        try:
            players = int(players)
        except:
            players = raw_input('Enter an integer idiot! How many players?\n')
    game = Main_loop(players)
    game.turn()
