import time 
import datetime

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
ja = ["J", "j", "Ja"]
nee = ["N", "n", "nee"]

required = ("\nGebruik graag alleen A, B, of C\n") 

print("Hello You!, ik ben Davy")

username = input("Wie ben jij?:")

print("Hello " + username)
x = datetime.datetime.now()

print("De datum en tijd is")
print(x)

time.sleep(1)
print("Ken je mij goed genoeg?")

time.sleep(1)
def intro():
  print ("Je bent net opgestaan, en gaat naar school. Welk vervoers middel neem je? :")
  time.sleep(1)
  print ("""  A. je neemt de trein
  B. Je gaat fietsen
  C. Je gaat lopen""")
  choice = input(">>> ") 
  if choice in answer_A:
    option_wakker()
  elif choice in answer_B:
    print ("\nJe bent uitgegleden.."
    "\n\nJe bent af!")
  elif choice in answer_C:
    option_uit()
  else:
    print (required)
    intro()

def option_wakker(): 
  print ("\nNu ben je op school"
  " Hoe kom je bij je lokaal?:")
  time.sleep(1)
  print ("""  A. Je gaat zelf op onderzoek uit
  B. Je kijkt op magister en loopt naar dat lokaal toe
  C. Je volgt je klasgenoten""")
  choice = input(">>> ")
  if choice in answer_A:
    print("\nJa, goed gedaan... Nu ben je verdwaald.")
    "\n\nJe bent af!"
  elif choice in answer_B:
    print ("\n Je komt aan bij je lokaal, maar hier is het helemaal niet. Moest je toch maar je klasgenoten volgen. \n\nJe bent af!")
  elif choice in answer_C:
    option_lopen()
  else:
    print (required)
    option_wakker()

def option_lopen():
  print ("\n Je klasgenoten raken in een discussie. Een groepje zegt dat we naar links moeten, en de ander zegt naar rechts. De meerderheid gaat naar links. Ga jij mee naar rechts? J/N?")
  choice = input(">>> ")
  if choice in ja:
    print("\nJe bent bij het verkeerde lokaal sukkel. Dit is niet eens een lokaal.... het is de wc...") 
    print ("\n\nJe bent af!")
  else:
   print("Je bent eindelijk bij het lokaal, en je gaat zitten. Maar wacht... Dit is de verkeerde docent? Ga je hier iets van zeggen? \nA. Ja, voor hetzelfde ben je toch verkeerd\nB. Nee, hij weet het wel beter dan mij.")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nKomop man, hij weet toch wel waar hij moet zijn.\n\nJe bent af!")
  elif choice in answer_B:
    print ("\nHij is een blijkbaar een inval docent, toch maar goed dat je niks hebt gezecht. \n\nJe hebt het gehaalt!")
  else:
    print (required)
    option_lopen()

def option_uit():
  print ("\nJe hebt je wekker uitgezet en word veel te laat wakker.. "
  "Geef je op of ga je toch nog naar school :")
  time.sleep(1)
  print ("""  A. Boeie ik ben toch al te laat ik heb geen zin meer..
  B. Ja ik wil zo snel mogelijk op school aankomen, ik kom om te leren!""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("Je bent niet op komen dagen.. dit was niet de eerste keer je word geschorst. "
    "\n\nJe bent af!")
  elif choice in answer_B:
    print ("\nJe bent alsnog te laat.. De docenten zijn helemaal klaar met jou en laten je de les niet meer in. "
    "\n\nJe bent af!")

  else:
    print (required)
    option_uit()

intro()