# hockey-transcripts
Digestion of hockey transcripts - Python script to read in transcript of hockey game and identify player "mentions" in an announcer's call.

## Background
I performed this activity to test if a play-by-play announcer dictates the "flow" of play in a hockey game in a meaningful way. That is, would we be able to approximate the movement of the puck between players using an announcer's calls. No conclusions yet!
### Obtaining the transcript
After some internet searching and twitter questioning, I couldn't find a resource for "archived" transcripts of hockey games. So, for initial testing - NHL Gamecenter, closed captioning, my ears, and really fast typing was utilized. After "completing" the transcript, I read through it to make sure all player references matched a unique identifier for that player (see below). It was by no means an exact science. 

## Script
I tried to make the python readable enough so that a newbie to programming might be able to follow along. 
### Required Inputs
- **Roster File** (csv): Roster of players in game. Must include a unique identifier (first column = "Identifier". This file could be pulled from a game summary on war-on-ice.com
- **Transcript File** (txt): Actual transcript of game. Any references to a player should match the "Identifier" in the roster file in order to be matched. Any stoppages in play -- or how you may otherwise want the play split up -- should be designated by two new lines.
### Current Outputs
- **Mention Sequence** (csv): Output of mention sequence in format of (MentionID, Portion, Player, Team)
- **Mention Summary** (csv): Summarized results in format of (Player, Team, Portion, MentionCount)

