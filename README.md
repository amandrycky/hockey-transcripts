# hockey-transcripts
Digestion of hockey transcripts - Python script to read in transcript of hockey game and analyze for player "mentions" throughout an announcer's call.
### Required Inputs
- **Roster File** (csv): Roster of players in game. Must include a unique identifier (first column = "Identifier". This file could be pulled from a game summary on war-on-ice.com
- **Transcript File** (txt): Actual transcript of game. Any references to a player should match the "Identifier" in the roster file in order to be matched. Any stoppages in play -- or how you may otherwise want the play split up -- should be designated by two new lines.

### Current Outputs
- **Mention Sequence** (csv): Output of mention sequence in format of (MentionID, Portion, Player, Team)
- **Mention Summary** (csv): Summarized results in format of (Player, Team, Portion, MentionCount)

I tried to make the python readable enough so that a newbie to programming might be able to follow along. Contact @alexgoogs if you have any questions. 