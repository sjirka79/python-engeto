"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jiří Sedláček
email: sjirka@gmail.com
"""

# import functions and modules
from sys import exit
    # used in login verification for application termination

# ============================================================================
# ******************* class for user *****************************************
# ============================================================================
class User_logged:
    
    # entering user name
    def user_name(self):
        self.name = input("Zadej své uživatelské jméno: ")
    
    # entering password
    def user_pwd(self):
        self.pwd = input("Zadej přístupové heslo: ")

    def login_fce(self):
        # auxilliary variable for login verification
        login_success = False

        self.user_name()

        # log in process
        try:
            while login_success is False:
                # entering password
                # allows multiple attempts if password id entered incorrectly
                # until var "login_success" is changed to True or application
                # is terminating using sys.exit method
                self.user_pwd()

                # login verification
                if self.pwd == USERS.get(str(self.name)):
                    # login and password correct -> continue in app
                    login_success = True

                elif self.name in USERS.keys():
                    # wrong password for existing user
                    print(f"""{"-" * sep_no}
POZOR: Chybně zadané heslo. Pokud chceš zkusit zadat
heslo znovu, zadej \"C\", pokud chceš program ukončit,
zadej cokoliv jiného.""")
                    cont_quit = input()
                    if cont_quit.upper() == "C":
                        # enter "C" for new attempt
                        continue
                    else:
                        # user does not want to enter pwd again -> app termination
                        exit("Pro změnu hesla kontaktuj administrátora.")

                else:
                    # not existing user
                    exit(f"Uživatel \"{self.name}\" nemá přístup.")

        except Exception:
            # another exception -> termination
            exit("Chyba při ověření přístupu, kontaktuj administrátora.")

# ============================================================================
# ******************* class for analyzed_text ********************************
# ============================================================================
class Analyzed_text:
    def __init__(self, anal_text):
        self.anal_text = anal_text
    
    # method for text analyzing
    def analyza(self):
        # list of words from analyzed text, split using whitespaces
        words_list = self.anal_text.split()

        # clean the words from unwanted characters (,.:) at the end
        REM_CHAR = (",", ".", ":") # characters to remove
        for i in range(len(words_list)):
            word = words_list[i]
            if word[-1] in REM_CHAR:
                word = word[:(len(word)-1)]
                words_list[i] = word

        # definition of counters for different sets of words
        # list "number" is used for store numbers
        first_capital = 0
        all_capitals = 0
        all_small = 0
        number_list = []

        # list containing lenght of every word in analyzed text
        letters_count_list = []
        
        # analyzing the words from the list
        for word in words_list:

            if word.istitle() is True:
                # just first letter is capital
                first_capital += 1
            elif word.isupper() is True:
                # all letters are capitals
                all_capitals += 1
            elif word.islower():
                # all letters are small
                all_small += 1      
            elif word.isnumeric() is True:
                # word is number
                number_list.append(int(word))
        
            # add word lenght to list
            letters_count_list.append(len(word))

        # counting sum of all numbers
        number_sum = sum(number_list)            

        # dictionary for frequency of every word lenght in analyzed text 
        frequency = {key: letters_count_list.count(key) 
                     for key in letters_count_list}

        # value just for output formating
        # max. occurence of words lenght       
        max_oc = 6 if max(frequency.values()) <= 6 else max(frequency.values())
        # not necessary for column DÉLKA as there are not such long words

        # print summary of text (number of words totally and number of words 
        # of particular type, sum of all numbers in text)
        print(f"""{"-" * sep_no}
Ve vybraném textu je celkem {len(words_list)} slov.
Velkým písmenem začíná {first_capital} slov.
Velkými písmeny je psáno {all_capitals} slov.
Malými písmeny je psáno {all_small} slov.
Text obsahuje {len(number_list)} číselných řetězců.
Součet všech čísel je {number_sum}.
{"-" * sep_no}""")

        # print header of table
        print("DÉLKA", "|", "VÝSKYT", " " * (max_oc - 6), "|", "POČET")
        print("-" * sep_no)

        # print single raws of table (frequncy of words with given lenght)
        for key, value in sorted(frequency.items()):
            print(" " * (4 - len(str(key))), key, "|", "*" * value,
                " " * (max_oc - value), "|", value)

# ============================================================================
# ******************* function for choosing text *****************************
# ============================================================================        
def anal_choose(logged_user):
    # number of items in TEXTS list
    text_count = len(TEXTS)

    # welcome to app, number of texts to analyze
    print(f"""{"-" * sep_no}
Vítej v analyzátoru textu, {logged_user}.
Počet textů k analýze: {text_count}""")

    # entering the number of text and its verification
    try:
        # var for input verification
        inp_ok = False
        
        while inp_ok is False:

            # entering number of analyzed text
            text_no = input(f"""{"-" * sep_no}
Vlož číslo analyzovaného textu (1 - {text_count}): """)
        
            if text_no.isnumeric() is False:
                print("POZOR: Musíš zadat kladné číslo!")
                continue
            
            # index of text in list (1 less than user input, beginning from 0)
            text_no = int(text_no) - 1

            if text_no not in range(text_count):
                # No. of analyzed text is of ouf range (<0 or >=tetx_count)
                print("POZOR: Musíš zadat číslo v daném rozsahu!")
                continue
            else:
                inp_ok = True

    except Exception:
        exit("Chyba při zadávání textu, kontaktuj administrátora.")

    return text_no


# ============================================================================
# ******************* app data and setting ***********************************
# ============================================================================

# dictionary of users and passwords
USERS = {
    "bob":"123",
    "ann":"pass123",
    "mike":"password123",
    "liz":"pass123"
    }

# list of texts to be analyzed
TEXTS = [
    """Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley. """,
    """At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present."""
    ]

# number of separators
sep_no = 42

# ============================================================================
# ******************* app main code ******************************************
# ============================================================================

if __name__ == "__main__":
    act_user = User_logged()
    act_user.login_fce()
    anal_text_no = anal_choose(act_user.name)
    chosen_text = Analyzed_text(TEXTS[anal_text_no])
    chosen_text.analyza()