import csv
import time
import msvcrt
import argparse
import random

def moving_animation():
  # define the characters to use in the "moving" animation
  characters = ["◐","◓","◑","◒"]
  character = random.choice(characters)
  # print the chosen character
  print(character, end='\r')
  # pause for a short amount of time
  time.sleep(0.1)


def track_activity(activity_name, category, notes=''):
  # get the current time
  start_time = time.time()
  start_time_formatted = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
  print(f'\033[32mPress any key to start tracking {activity_name} (started at {start_time_formatted})\033[0m')
  msvcrt.getch()
  print(f'Tracking {activity_name}...')

  # initialize the elapsed time to 0
  elapsed_time = 0
  # do the activity here
  while True:
    moving_animation()
    # check for a key press
    if msvcrt.kbhit():
      # get the key press
      key_press = msvcrt.getch()
      # check if the key press was the 'p' key
      if key_press == b'p':
        # pause the timer
        print(f'\033[31m{activity_name} paused. Press any key to continue.\033[0m')
        msvcrt.getch()
        print(f'Continuing {activity_name}...')
      # check if the key press was the 'q' key
      elif key_press == b'q':
        # stop tracking the activity
        break
      # check if the key press was the 's' key
      elif key_press == b's':
        # add seconds to the elapsed time
        extra_time = input('Enter the number of seconds to add: ')
        elapsed_time += int(extra_time)
        print(f'{extra_time} seconds added to {activity_name}')

  # calculate the final elapsed time
  end_time = time.time()
  elapsed_time += end_time - start_time
  end_time_formatted = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))

  # write the activity details to a CSV file
  with open('activity_tracker.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([activity_name, category, start_time_formatted, end_time_formatted, elapsed_time, notes])
    # print the summary of the tracking
  print(f'\033[32m{activity_name} tracked for {int(elapsed_time)} seconds\033[0m')


def main():
  # read the activity_tracker.csv file and store the data in a list
  activities = []
  with open('activity_tracker.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
      activities.append(row)

  # get the last 10 activities
  last_10_activities = activities[-10:]

  # create an argument parser
  parser = argparse.ArgumentParser()
  # add the activity name, category, and notes arguments
  parser.add_argument('activity_name', nargs='?', help='the name of the activity to track')
  parser.add_argument('category', nargs='?', help='the category of the activity')
  parser.add_argument('--notes', help='optional notes about the activity')
  # parse the command-line arguments
  args = parser.parse_args()

  # if the activity name and category arguments are not provided, display a list of the last 10 activities and allow the user to select one to start tracking
  if args.activity_name is None and args.category is None:
    print('\033[32mLast 10 activities:\033[0m')
    for i, activity in enumerate(last_10_activities):
      print(f'{i+1}. {activity}')

        # prompt the user to select an activity or create a new one
    selected_activity = input('\033[31mEnter the number of the activity to start tracking or "n" to create a new activity: \033[0m')
    # if the user selected an existing activity
    if selected_activity.isdigit():
      # get the selected activity from the list
      selected_activity = last_10_activities[int(selected_activity)-1]
      # track the selected activity
      track_activity(selected_activity[0], selected_activity[1])
    # if the user chose to create a new activity
    elif selected_activity == 'n':
      # prompt the user for the activity name, category, and notes
      activity_name = input('\033[31mEnter the name of the activity: \033[0m')
      category = input('\033[31mEnter the category of the activity: \033[0m')
      notes = input('\033[31mEnter any notes about the activity (optional): \033[0m')
      # track the new activity
      track_activity(activity_name, category, notes)
  # if the activity name and category arguments are provided, track the activity using the provided arguments
  else:
    track_activity(args.activity_name, args.category, args.notes)


if __name__ == '__main__':
  main()