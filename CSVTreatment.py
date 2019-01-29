
import csv


def csvToDictionary(myList):
    with open('ListOfPeople.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        temp = []
        for row in reader:
            temp.append(row)
    myList += [val for sublist in temp for val in sublist]

        
def saveListToCSV(myList):
    with open('ListOfPeople.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter='\n')
        writer.writerow(myList)

# Write the tweets to a csv file
def appendTweets(tweetWithLink):
    with open('LinksList.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(tweetWithLink)
