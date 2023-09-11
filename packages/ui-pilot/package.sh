#!/bin/bash

rm -rf ./build
rm -rf ./dist
rm -rf ./UI\ Pilot.spec

pyinstaller \
    --name "UI Pilot" \
    --icon assets/icon.icns \
    --add-data="assets/icon.png:assets" \
    --windowed \
    ui-pilot/tray.py
