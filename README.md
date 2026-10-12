# DemonicScans plugin for ZC-ComicUpdater

A [scraper plugin](https://github.com/ZornTaov/ZC-ComicUpdater/wiki/Scraper-Plugins) that keeps a series from
demonicscans.org up to date with [DemonicScans-dl](https://github.com/ZornTaov/DemonicScans-dl), which sits in
`tool/` as a submodule.

## Installing

Clone it, with its submodule, into the updater's config folder under the name `demonicscans-dl`:

```sh
git clone --recurse-submodules https://github.com/ZornTaov/<this repo>.git config/plugins/demonicscans-dl
```

Nothing has to be installed in the updater's container: the scraper needs only selenium, requests and
Chromium, all of which the image already has.

## Adding a series

On the updater's web page, pick **DemonicScans** as the scraper under Add comics. Give the series' address,
`https://demonicscans.org/manga/Series-Name`, and optionally the chapter to start at. From a shell, run from
the library's root:

```sh
python run_plugin.py --add demonicscans-dl Uncompressed/Series url=https://demonicscans.org/manga/Series-Name "start_chapter=Chapter 1"
```

Each run fetches the oldest chapters first, starting from the last one it took. The updater skips that
chapter, so it is never taken twice, and gives every chapter an archive of its own. The scraper's error
logs are kept in `logs/` here.

## Updating the scraper

```sh
git submodule update --remote tool
git commit -am "Scraper: the latest DemonicScans-dl"
```
