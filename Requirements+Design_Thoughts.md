# Idee
Chris möchte gerne mehrere Playlists, in denen jeweils mindestens ein Stück jedes seiner Lieblingsalben drinnen ist. Er hat aber keine Lust, das händisch zu checken.

# Zusätzliche Idee: Vlt. doch lieber nur für eine Playlist checken, deren namen man eingibt, statt gleich für alle?

# Input und Output Formate
*Input* durch einlesen mehrerer Files, die wir dem Programm geben (CSV vlt.? Oder iwo direkt über eine Schnittstelle?)
Zwei Arten von Input-Files, die gleich Importiert werden, aber unterschiedlich verarbeitet:
- Alben jeweils bestimmter Interpreten
- Playlists
Output soll sein: Array mit Namen der Playlists, die nicht von jedem Album mindestens ein Lied beinhalten + 

# Grobes Vorgehen
Keine komplizierten Algorithmen oder Funktionen notwendig, lediglich String-Abgleiche. Diese können möglicherweise einer Library überlassen werden.

# Aufbau
Das Programm wird sich aus mehreren Teilen zusammensetzen

## Globale Variablen
Eine vorerst leeres Array für den Output am Ende

## Input-Aufbereitung
Input: Alle Files über Schnittstelle
Output: Aufbereitete Files (Playlists separat, Alben-Array gemeinsam)
- Nimmt von außen die einzelnen Files und checkt, ob es sich um csv's handelt. Ansonsten Umwandlung in csv.
- "Playlists" bleiben separat, "Album" werden gemeinsam in ein mehrdimensionales Array integriert

## Playlist-Check "anwerfen"
Input: Aufbereitete Files von Input, also; Je eine Playlist und das Array der Alben
Output: Das globale Array mit allen Playlists für die Alben fehlen + Albumtiteln
- "wirft" die Funktion darunter, also "Playlist-Check (für jede Playlist einmal)" an

## Playlist-Check (für jede Playlist einmal)
Input: Aufbereitete Files von Input, also; Je eine Playlist und das Array der Alben
Output: Kein "echter" Output. Wenn mind. ein Album fehlt: Name wird ins Array gegeben; Angehängt werden alle Namen der Alben, die fehlen

## Visualisierung pro Playlist
Input: Eine Playlist und das Array der Alben
Output: Piechart mit unterschiedlichen Farben pro Album
Für fehlendes Album vlt. noch einen kleinen Blobb unter dem Piechart?

# Reihenfolge der Teile
Es muss lediglich beachtet werden, dass die Input-Aufbereitung zuerst stattfindet. Die beiden anderen Teile sind unabhängig voneinander

# Externe Hardware?
Nope.

# Welche Fehler könnten entstehen?
- Inputart falsch (haben wir bei der Input-Aufbereitung ausgeschlossen)
- Leerer Input
- Leere Arrays

# Required User-Friendliness


# Which unconditional termination criterias should be set?

