class Shiritori(object):
    """docstring for ."""
    words = []
    game_over = False
    bool_text,bool_found = True,True

    def __init__(self,words = [],game_over = False):
        self.words = words
        self.game_over = game_over
        pass

    def getWords(self):
        print(self.words)

    def restart(self):
        self.game_over = False
        self.bool_text,self.bool_found = True,True
        self.words = []
        print("game restarted")

    def check_found(self,text):
        if text not in self.words:
            return False
        else:
            self.bool_found = False
            return True


    def check_text(self,text):
        if(self.words == []):
            return ""
        if text[0] == self.words[-1][-1]:
            return False
        else:
            self.bool_text = False
            return True


    def play(self,text):
        if not self.game_over:
            if not self.check_found(text.lower()) and not self.check_text(text.lower()):
                self.words.append(text.lower())
                print(self.words)
                return self.words
            elif self.check_found(text.lower()):
                print("Invalid! - " + text + " has already been said")
                if(not self.bool_found and not self.bool_text):
                    print("game_over")
                    self.game_over = True
                    return "game_over"
            else:
                print("Invalid! - " + text + " should start with " + self.words[-1][-1])
                if(not self.bool_found and not self.bool_text):
                    self.game_over = True
                    print("game_over")
                    return "game_over"



my_shiratori = Shiritori()
my_shiratori.play("apple")

my_shiratori.play("ear")
my_shiratori.play("rhino")
my_shiratori.play("corn")
my_shiratori.getWords()

my_shiratori.restart()
my_shiratori.getWords()

my_shiratori.play("hostess")

my_shiratori.play("stash")
my_shiratori.play("hostess")
