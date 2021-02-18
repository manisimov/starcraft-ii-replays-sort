'''Script for sorting Starcraft 2 replays to folders by matchup.

PLAYER_NAME - your nick-name in the game.
INPUT_DIR   - directory with replays. Script does not go into subfolders.
OUTPUT_DIR  - where to store sorted files. Subfolders are created automatically
              if do not exist.
'''

import os
import sys
import shutil
import sc2reader

PLAYER_NAME = 'anisimov'
INPUT_DIR = os.path.normpath('../')
OUTPUT_DIR = os.path.normpath('../test_dir/out')

if not os.path.isdir(OUTPUT_DIR):
    raise Exception(f"OUTPUT_DIR '{OUTPUT_DIR}' does not exist")

file_names = os.listdir(INPUT_DIR)
replay_names = [x for x in file_names if 'SC2Replay' in x]
for rep in replay_names:
    replay_full_name = os.path.join(INPUT_DIR, rep)
    replay = sc2reader.load_replay(replay_full_name, load_level=2)
    if replay.is_ladder:
        for p in replay.players:
            if p.name == PLAYER_NAME:
                me = p
            else:
                foe = p
        if me in replay.winner.players:
            result = 'win'
        else:
            result = 'lost'
        # Take only first letter of the race.
        my_race = me.pick_race[0]
        foe_race = foe.pick_race[0]
        # Map name without whitespaces.
        map_name = "".join(replay.map_name.split())
        # Convert date to string in format so than it can be sorted as string.
        date_str = replay.date.strftime("%Y-%m-%d_%H-%M-%S")
        # Sub-folder name with matchup info.
        sub_dir_name = f"{my_race}v{foe_race}"
        # Compose filename.
        file_name_str = f"{date_str}_{my_race}v{foe_race}_{map_name}_{result}.SC2Replay"

        sub_dir_full = os.path.join(OUTPUT_DIR, sub_dir_name)
        try:
            os.mkdir(sub_dir_full)
        except FileExistsError:
            pass
        shutil.copy2(replay_full_name, sub_dir_full)
        copy_full_name = os.path.join(sub_dir_full, rep)
        new_full_name  = os.path.join(sub_dir_full, file_name_str)
        try:
            os.rename(copy_full_name, new_full_name)
        except FileExistsError:
            # File is already here, remove not yet renamed copy.
            os.remove(copy_full_name)
