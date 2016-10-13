from colorama import Fore, Back, Style
from pyfiglet import Figlet

class Journal(object):
    """Journal class"""

    journal = {}
    last = {}

    f = Figlet(font='slant')
    a = f.renderText('Welcome')
    print(Fore.GREEN + a)

    def __init__(self):
        super(Journal, self).__init__()

    def create_journal(self, title):
        self.journal[title] = {}

    def get_journal(self):
        return self.journal

    def create_entry(self, title, subtitle, entry):
        if title in self.journal:
            # prompt user to create an entry
            entries = self.journal[title]
            entries[subtitle] = entry
            last = {subtitle: entry}
            print(entries)
        else:
            print("Journal does not exist. Enter cmd to create a new journal")

    def view_last(self):
        last = 
        if type(Journal.last) is dict:
            for k,v in Journal.last.items():
                print("\tTitle : " + k)
                print("\t\t" + str(v))
        else:
            print(Journal.last)

    def list_all(self):
        journal = self.get_journal()
        for k, v in journal.items():
            print("Journal : " + k)
            if type(v) is dict and len(v) > 0:
                for k1, v1 in v.items():
                    print("\tTitle : " + k1 + "\n")
                    if type(v1) is list:
                        for index in range(len(v1)):
                            print("\t\t" + v1[index])                
                    else:
                        print("\t\t" + str(v1))


       
jn = Journal()
jn2 = Journal()
jn2.create_journal("Mandela")
jn.create_journal("Andela")
print(jn2.create_entry("Mandela", "TeamOlive", ["Me", "You"]))
print(jn.create_entry("Andela", "TeamRain", ["Ben", "Ali"]))
#print(jn.list_all())
print(jn2.view_last())