
import TweetCollector
import CSVTreatment

# CHANGE LIST TO CSV, create and maintain the list
# Change functions to edit this csv file
# via twitter api use this list
# Time doesn't make sense to keep, since all will be the same

theList = []

def menu():
    print("\nHere is the list of people you're following:")
    print(theList) # TODO: Fix so it doesn't look like a list.
    # Remember to change nrs if you add more options.
    selection = input("""Main menu, please select option:
    \n 1: Add People to the list.
    \n 2: Remove People from the list.
    \n 3: Collect Tweets.\n 4: Exit.\n >>""")
    
    if   selection == '1':
        addPeopleToList()
    elif selection == '2':
        removePeopleFromList()
    elif selection == '3':
        collectTweets() 
    elif selection == '4':
        print("Exiting.")
        CSVTreatment.saveListToCSV(theList)
        quit
    else:
        menu()
        
    
def addPeopleToList():
    addMe = input("\nWho would you like to add?\n")
    # TODO: Find/make sure person is on twitter.
    theList.append(addMe)
    print("Added " + str(addMe) + " to the list\n")
    menu()


def removePeopleFromList():
    print(theList)
    removeMe = input("\nWho would you like to remove?\n")
    if removeMe in theList:
        theList.remove(removeMe)
        print("Removed " + str(removeMe) + " from the list\n")
    else: 
        print("Person is not on the list.")
        return removePeopleFromList()
    menu()

    
def collectTweets():
    nrTweets = input("How many tweets would you like to collect?\n")
    tweetsList = []
    for username in theList:
        TweetCollector.getTweets(username, nrTweets, tweetsList)
        CSVTreatment.appendTweets(tweetsList)
    menu()


CSVTreatment.csvToDictionary(theList)
menu()
# Next is doing something about time (So as to not add the same tweet),
# specifically related to the getTweets function.
