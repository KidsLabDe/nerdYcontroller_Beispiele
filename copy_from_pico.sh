#!/bin/bash

# Pfad zum Pico (angepasst an Ihr System)
PICO_PATH="/Volumes/CIRCUITPY"

# Zielverzeichnis (aktuelles Verzeichnis)
TARGET_DIR="."

# Kopieren Sie alle Dateien vom Pico in das aktuelle Verzeichnis
rsync -av --progress --exclude ".*" --exclude '*.mpy' --exclude '*.sh' --exclude '_*'  "$PICO_PATH/" "$TARGET_DIR/"

echo "Alle Dateien wurden erfolgreich vom Pico in das aktuelle Verzeichnis kopiert."

