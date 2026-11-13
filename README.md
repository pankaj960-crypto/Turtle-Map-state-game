# Turtle Map State Game

A fun interactive Python game where the player tries to guess Indian states and place them on a blank India map. The game uses a map image as the background and shows the guessed state names at their correct locations on the map.

This project is a simple geography quiz built to help users learn Indian state names and locations in an engaging way.

## Project Overview

The game displays a blank India map and asks the player to enter a state name. If the entered state is valid and has not already been guessed, it is marked on the map. The player keeps guessing until all states are found.

There are two main Python scripts in this project:

- `project.py` - the actual game that lets the player guess states
- `app.py` - a helper script used to collect coordinates for each state and save them in a CSV file

## Features

- Interactive state guessing game
- India map background using a GIF image
- Real-time tracking of correct guesses
- State names written onto the map at their coordinates
- CSV-based state coordinate data
- Option to exit the game and save missing states for later learning

## Technologies Used

- Python
- Turtle Graphics (`turtle` module)
- Pandas (`pandas`) for reading and writing CSV data
- CSV data file for state coordinates
- GIF image for the India map background
- Basic Python loops, conditionals, and user input handling

## Project Files

- `project.py` - main gameplay logic
- `app.py` - coordinate collector for generating map locations
- `new_india_state.csv` - contains state names with x/y coordinates
- `new_india_state.gif` - background map image

## How to Run

1. Install the required package:

```bash
pip install pandas
```

2. Run the game:

```bash
python project.py
```

3. Enter state names in the popup window until all states are guessed.

## Notes

This project is a beginner-friendly Python game that combines graphics, data handling, and interactivity. It is a great example of using Python libraries to build a learning-based game.

## Future Improvements

- Add score tracking
- Add timer mode
- Add sound effects
- Add a leaderboard or difficulty levels
- Include all union territories with the states
