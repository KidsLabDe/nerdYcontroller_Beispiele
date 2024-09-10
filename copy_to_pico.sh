#!/bin/bash

# Pfad zum Pico (angepasst an Ihr System)
PICO_PATH="/Volumes/CIRCUITPY"

# Zielverzeichnis (aktuelles Verzeichnis)
TARGET_DIR="."

# Kopieren Sie alle Dateien vom Pico in das aktuelle Verzeichnis
rsync -av --progress "$TARGET_DIR/" "$PICO_PATH/" 

echo "Alle Dateien wurden erfolgreich vom Pico in das aktuelle Verzeichnis kopiert."

