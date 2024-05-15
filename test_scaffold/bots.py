class Bots:
    def __init__(self):
        self.copies = 1
        self.active = True
        pass
    
    def get_name(self):
        bot_name = input("give the bot a name ")        
        return bot_name



if __name__ == "__main__":    
    x = Bots()
    name = x.get_name()
    print(f"The bot {name}'s number of copies is {x.copies}. Is it active? {x.active}.")    
    pass
    