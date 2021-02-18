# starcraft-ii-replays-sort
Script for sorting Starcraft 2 replays into subfolders by matchup.

Parses input directory with unsorted replays, creates subfolders structure in the output directory, sort replays into subfolders by matchup and renames them adding information about the result.

For example:

    output_dir
    |-- TvZ
    |    |-- 2019-08-17_17-16-50_TvZ_AcropolisLE_win.SC2Replay
    |    |-- 2019-07-16_21-32-38_TvZ_KairosJunctionLE_win.SC2Replay
    |    +-- 2018-05-26_11-09-06_TvZ_DreamcatcherLE_win.SC2Replay
    |-- TvP
    |    +-- 2020-03-13_00-33-03_TvP_ZenLE_lost.SC2Replay
    +-- TvT
         |-- 2020-03-23_20-19-39_TvT_ZenLE_lost.SC2Replay
         +-- 2020-03-22_22-31-06_TvT_SimulacrumLE_win.SC2Replay
         
Uses **sc2reader** parser:

    pip install sc2reader

For more info see its gihub:

https://github.com/ggtracker/sc2reader
