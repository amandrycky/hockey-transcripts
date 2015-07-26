import csv
from re import findall

fileDir = "20150320-BUFNJ"
# INPUT FILE NAMES
transcriptFileName = fileDir + r"\HOME-P1.txt"
rosterFileName = fileDir + r"\roster.csv"
# OUTPUT FILE NAMES
mentionSeqFileName = fileDir + r"\OUT-mentionSeq.csv"
mentionSummaryFileName = fileDir + r"\OUT-mentionSummary.csv"

# Read roster file
rosterFile = open(rosterFileName)
rosterCSVreader = csv.reader(rosterFile, delimiter = ",")

# Set up dictionary to store game roster info
rosterDict = {}
rowCount = 0
for row in rosterCSVreader:
    # Initial count is 0. will be updated while reading file
    if rowCount > 0:
        rosterDict[row[0]] = {"TEAM": row[1], 
                                "TOI": float(row[6]), 
                                "POS": row[5], 
                                "TOT-MENTIONS": 0, 
                                "PORTION-MENTIONS": {}, 
                                "POSS_POS": 0, 
                                "POSS_NEG": 0}
    rowCount += 1
rosterFile.close() # done with roster file

# Make a regular expression string with all the identifiers, for later use.
# Want all players separated by a | character
idRegEx = ""
for playerId in rosterDict.keys():
    idRegEx += playerId + "|"
idRegEx = idRegEx[:-1] # remove last pipe
fullRegEx = "(" + idRegEx + ")"

# Read in transcript file
transcriptFile = open(transcriptFileName)
transcriptStr = transcriptFile.read()
transcriptFile.close()

# Break up the file based on new line characters. 
# These designate stoppages in play.
transcriptList = transcriptStr.split("\n\n")

# Iterate over the transcript text by portion
portionNum = 1
masterPortionList = []
for portion in transcriptList:
    portionProgressionList = findall(fullRegEx, portion)
    for player in portionProgressionList:
        # add to total
        rosterDict[player]["TOT-MENTIONS"] += 1
        # add for specific portion
        if portionNum in rosterDict[player]["PORTION-MENTIONS"].keys():
            rosterDict[player]["PORTION-MENTIONS"][portionNum] += 1
        else: 
            rosterDict[player]["PORTION-MENTIONS"][portionNum] = 1
    portionNum += 1
    masterPortionList.append(portionProgressionList)

    for playerIndex in range(len(portionProgressionList)):
        playerId = portionProgressionList[playerIndex]
        if playerIndex < len(portionProgressionList) - 1:
            nextPlayerId = portionProgressionList[playerIndex + 1]
            playerTeam = rosterDict[playerId]["TEAM"]
            nextPlayerTeam = rosterDict[nextPlayerId]["TEAM"]
            # Define "positive possession" as one where your team has the puck after your call
            if playerTeam == nextPlayerTeam and playerId != nextPlayerId:
                rosterDict[playerId]["POSS_POS"] += 1
            else:
                rosterDict[playerId]["POSS_NEG"] += 1
        # If this is the last touch, record as a positive possession
        else:
            rosterDict[playerId]["POSS_POS"] += 1
            
# Create output csv with summary for player/portion.
mentionSummaryOutList = [["Player", "Team", "Portion", "MentionCount"]]
for player in rosterDict:
    for playerPortion in rosterDict[player]["PORTION-MENTIONS"]:
        mentionSummaryOutList.append([player, 
                           rosterDict[player]["TEAM"], 
                           playerPortion, 
                           rosterDict[player]["PORTION-MENTIONS"][playerPortion]])

with open(mentionSummaryFileName, "wb") as mentionSummaryFile:
    csvSummary = csv.writer(mentionSummaryFile)
    csvSummary.writerows(mentionSummaryOutList)
                           
# Create output csv for mention sequence.
mentionID = 1
portionID = 1
mentionSeqOutList = [["MentionID", "Portion", "Player", "MentionTeam"]]
for portion in masterPortionList:
    for playerMention in portion:
        mentionSeqOutList.append([mentionID, portionID, playerMention, rosterDict[playerMention]["TEAM"]])
        mentionID += 1
    portionID += 1

with open(mentionSeqFileName, "wb") as mentionSeqFile:
    csvSummary = csv.writer(mentionSeqFile)
    csvSummary.writerows(mentionSeqOutList)
                           