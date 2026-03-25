# Dictionary to store candidates and their vote counts
candidates = {
    "raj": 0,
    "raja": 0,
    "raju": 0
}

# Function to add a vote to a candidate
def add_vote(candidate_name):
    if candidate_name in candidates:
        candidates[candidate_name] += 1
        print(f"Vote added to {candidate_name}. Current votes: {candidates[candidate_name]}")
    else:
        print(f"Candidate {candidate_name} does not exist.")

# Function to display current vote counts
def display_votes():
    print("Current vote counts:")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {votes} votes")

# Function to display the winner(s)
def display_winner():
    max_votes = max(candidates.values())
    winners = [candidate for candidate, votes in candidates.items() if votes == max_votes]
    if len(winners) == 1:
        print(f"Winner is {winners[0]} with {max_votes} votes!")
    else:
        print(f"It's a tie between: {', '.join(winners)} with {max_votes} votes each!")

# Example usage
if __name__ == "__main__":
    add_vote("raj")
    add_vote("raja")
    add_vote("raj")
    add_vote("raju")
    add_vote("raju")
    display_votes()
    display_winner()
