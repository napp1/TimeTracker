
# TimeTracker ⏲️📒

A small Python script to track activities and time spent on a CSV file.

Written for fun in only 30 minutes using ChatGPT support. 😉

## Usage
Launch the script using:

```
  python time_tracker.py TaskName ProjectName --notes "Bla bla bla"
```
Notes are optional.

Launching the script without arguments:

```
  python time_tracker.py
```

it will show the last 10 recorded tasks. So you can:
- start track one of them 
- or use 'n' key to record a new one.



## Control keys

After the launch of a tracking the control keys are:

- 'p' - to pause time tracking
- 's' - to add an amount of seconds to the current activity
- 'q' - to quit and record the time spent

## CSV structure
At the end of a tracking - after pressing of 'q' key - a new line will be write in the CSV file ```activity_tracker.csv```.
The structure of the file (to open it in Libre Office or Microsoft Excel) is:

| Activity Name  |  Project Name | Start Time  | End Time  | Total Seconds ('s' adding included)  | Notes |
|---|---|---|---|---|---|
|   |   |   |   |   |   |
|   |   |   |   |   |   |