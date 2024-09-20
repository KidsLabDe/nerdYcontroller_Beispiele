# nerdYcontroller_Beispiele

Hier ist die Dokumentation aller Funktionen der `GameController`-Bibliothek mit Beispielaufrufen in Markdown:


Die Komplette Anleitung mit Beispielen etc. findest du hier:

[Anleitung](Gamecontroller_Bausatz_Quickstart.pdf)

# GameController Bibliothek

## Funktionen

### `initialisiere()`
Initialisiert den GameController und bereitet ihn für die Verwendung vor.

**Beispiel:**
```python
GameController.initialisiere()
```

### `setzeLEDFarbe(index, farbe)`
Setzt die Farbe der LED an der angegebenen Position.

**Parameter:**
- `index` (int): Der Index der LED.
- `farbe` (tuple): Ein Tupel, das die RGB-Farbe angibt.

**Beispiel:**
```python
GameController.setzeLEDFarbe(0, (255, 0, 0))  # Setzt die erste LED auf Rot
```

### `setzeLEDaus(index)`
Schaltet die LED an der angegebenen Position aus.

**Parameter:**
- `index` (int): Der Index der LED.

**Beispiel:**
```python
GameController.setzeLEDaus(0)  # Schaltet die erste LED aus
```

### `leseTouchPin(index)`
Liest den Wert des Touch-Pins an der angegebenen Position.

**Parameter:**
- `index` (int): Der Index des Touch-Pins.

**Rückgabewert:**
- `bool`: `True`, wenn der Touch-Pin berührt wird, sonst `False`.

**Beispiel:**
```python
if GameController.leseTouchPin(0):
    print("Touch-Pin 0 wird berührt")
```

### `leseGyro()`
Liest die aktuellen Werte des Gyroskops.

**Rückgabewert:**
- `tuple`: Ein Tupel mit den Werten für `gyro_x`, `gyro_y` und `gyro_z`.

**Beispiel:**
```python
gyro_x, gyro_y, gyro_z = GameController.leseGyro()
print(f"Gyro-Werte: x={gyro_x}, y={gyro_y}, z={gyro_z}")
```

### `leseBeschleunigung()`
Liest die aktuellen Werte des Beschleunigungssensors.

**Rückgabewert:**
- `tuple`: Ein Tupel mit den Werten für `accel_x`, `accel_y` und `accel_z`.

**Beispiel:**
```python
accel_x, accel_y, accel_z = GameController.leseBeschleunigung()
print(f"Beschleunigungswerte: x={accel_x}, y={accel_y}, z={accel_z}")
```

### `spieleTon(frequenz, dauer)`
Spielt einen Ton mit der angegebenen Frequenz und Dauer.

**Parameter:**
- `frequenz` (int): Die Frequenz des Tons in Hertz.
- `dauer` (float): Die Dauer des Tons in Sekunden.

**Beispiel:**
```python
GameController.spieleTon(440, 1.0)  # Spielt einen Ton mit 440 Hz für 1 Sekunde
```

### `stoppeTon()`
Stoppt den aktuell spielenden Ton.

**Beispiel:**
```python
GameController.stoppeTon()
```

## Beispielskript

Hier ist ein Beispielskript, das die verschiedenen Funktionen der `GameController`-Bibliothek verwendet:

```python
import GameController
import time

# Initialisiere den GameController
GameController.initialisiere()

# Setze die erste LED auf Grün
GameController.setzeLEDFarbe(0, (0, 255, 0))

# Warte 1 Sekunde
time.sleep(1)

# Schalte die erste LED aus
GameController.setzeLEDaus(0)

# Überprüfe, ob der erste Touch-Pin berührt wird
if GameController.leseTouchPin(0):
    print("Touch-Pin 0 wird berührt")

# Lese die Gyro-Werte
gyro_x, gyro_y, gyro_z = GameController.leseGyro()
print(f"Gyro-Werte: x={gyro_x}, y={gyro_y}, z={gyro_z}")

# Lese die Beschleunigungswerte
accel_x, accel_y, accel_z = GameController.leseBeschleunigung()
print(f"Beschleunigungswerte: x={accel_x}, y={accel_y}, z={accel_z}")

# Spiele einen Ton mit 440 Hz für 1 Sekunde
GameController.spieleTon(440, 1.0)

# Warte 1 Sekunde
time.sleep(1)

# Stoppe den Ton
GameController.stoppeTon()
```
