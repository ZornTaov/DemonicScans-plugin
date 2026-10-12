#the DemonicScans plugin's own command. tool/ is DemonicScans-dl (a submodule), run on a series address:
#oldest chapter first, writing its archives into the folder the updater hands it, and starting from the
#last chapter taken - which it fetches again, and the updater does not take twice.
import os
import sys

PLUGIN = os.path.dirname(os.path.abspath(__file__))


def build_command(settings, state, staging):
    #the chapter to start from: where the last run got to, or, before anything has been taken, the one the
    #comic was added with. none at all starts from the series' first chapter
    start = state.get("last_chapter") or (settings.get("plugin") or {}).get("start_chapter")
    command = [sys.executable, os.path.join(PLUGIN, "tool", "scraper.py"), settings["url"],
               #the series page lists newest first
               "--reverse",
               "--output", staging,
               #kept in the plugin's own folder, since the staging folder is cleared after every run
               "--log-dir", os.path.join(PLUGIN, "logs")]
    if start:
        command += ["--start-chapter", start]
    return command
