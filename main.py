
import TweetCollector
import CSVTreatment
import datetime #Come back to this

theList = []
timestamp = 0
endtime = datetime.time #TODO: Showing the class not actual time


def menu():
    print("\nHere is the list of people you're following:\n")
    for person in theList[1:]:
        print(person)
    selection = input("""\nMain menu, please enter a number for corresponding option:
    \n 1: Add People to the list.
    \n 2: Remove People from the list.
    \n 3: Collect Tweets.
    \n 4: Exit.
    \n >> """)
    
    if   selection == '1':
        addPeopleToList()
    elif selection == '2':
        removePeopleFromList()
    elif selection == '3':
        collectTweets() 
    elif selection == '4':
        print("Exiting.")
        timestamp = endtime # Update time
        CSVTreatment.saveListToCSV(theList)
        quit
    else:
        menu()
        
    
def addPeopleToList():
    addMe = input("\nWho would you like to add?\n >> ")
    if (TweetCollector.checkName(addMe)):
        theList.append(addMe)
        print("Added " + str(addMe) + " to the list\n")
    else:
        print("Person was not found, sorry.")
    menu()


def removePeopleFromList():
    print(theList)
    removeMe = input("\nWho would you like to remove?\n >> ")
    if removeMe in theList[1:]:
        theList.remove(removeMe)
        print("Removed " + str(removeMe) + " from the list\n")
    else: 
        print("Person is not on the list.")
        return removePeopleFromList()
    menu()

    
def collectTweets():
    print("Collecting tweets.")
    tweetsList = []
    for username in theList[1:]:
        TweetCollector.getTweets(username, timestamp, tweetsList)
        CSVTreatment.appendTweets(tweetsList)
    menu()

def startup():
    print("\n-- Tweet Link Collector --")
    CSVTreatment.csvToDictionary(theList)
    menu()

    # Intializes when tweets were last collected
    timestamp = theList[0]

# print(endtime) FixMe
startup()
