# Berechnungsmethoden in der Aerodynamik - Rechnerübung

Willkommen zum Computer-basierten Teil der Übung zur Vorlesung "Berechnungsmethoden in der Aerodynamik". Hier findet ihr alle benötigten Ressourcen und Anleitungen, um erfolgreich an den Übungen teilzunehmen. Die Übungen werden als Jupyter Notebooks, also einer Kombination aus Python Quellcode und Markdown Text, nach und nach bereitgestellt.

## Inhaltsverzeichnis

1. [Einführung](#einführung)
2. [Voraussetzungen](#voraussetzungen)
3. [Installation von VS Code](#installation-von-vs-code)
4. [Installation von Python](#installation-von-python)
5. [Einrichten eines virtuellen Environments](#einrichten-eines-virtuellen-environments)
6. [Verwendung von Jupyter Notebooks in VS Code](#verwendung-von-jupyter-notebooks-in-vs-code)

## Einführung

Diese Anleitung hilft euch bei der Einrichtung eurer Entwicklungsumgebung, um die Übungen zur Vorlesung "Berechnungsmethoden in der Aerodynamik" durchzuführen. Wir verwenden Visual Studio Code (VS Code) als Haupt-Editor und Python als Programmiersprache. VS Code ist kostenlos, open-source und unterstützte Jupyter Notebooks. Ein virtuelles Environment wird eingerichtet, um die Dependencies (Pakete) zu verwalten und die Kompatibilität zu gewährleisten. Warum braucht man ein solches virtuelles Environment? Es bietet eine isolierte Programmierumgebung und es werden Konflikte zwischen verschiedenen Projekten mit verschiedenen Paket-Versionen vermieden. Isoliert bedeutet in dem Fall auch, dass die globale Python-Installation eures Computers unberührt bleibt, wodurch auch die globalen Systemwerkzeuge unberührt bleiben. Darüber hinaus gibt es weitere Gründe, aber der Kerngedanke sollte klar sein: Isolation. 

In Software-Projekten ist es üblicherweise "Good Practice" die benötigten Pakete mit ihrer Version in eine `requirements.txt` zu schreiben, sodass man sie von dort gebündelt installieren kann. Hat man eine solche Datei in dem Ordner, in den man auch das virtuelle Environment installiert, wird sie automatisch von VS Code erkannt und beim aufsetzen werden die benötigten Pakete direkt mit installiert. 

## Voraussetzungen

Bevor ihr beginnt, stellt sicher, dass ihr die folgenden Voraussetzungen erfüllt:

- Ein Computer mit Windows, macOS oder Linux
- Internetzugang, um die benötigte Software herunterzuladen

## Installation von VS Code

1. **Herunterladen und Installieren:**
   - Besucht die [VS Code Webseite](https://code.visualstudio.com/).
   - Ladet die passende Version für euer Betriebssystem herunter.
   - Folgt den Installationsanweisungen auf der Webseite.

2. **Erste Schritte mit VS Code:**
   - Startet VS Code nach der Installation.
   - Erkundet die Benutzeroberfläche und macht euch mit den grundlegenden Funktionen vertraut.

## Installation von Python

1. **Herunterladen und Installieren:**
   - Besucht die [Python Webseite](https://www.python.org/downloads/).
   - Ladet eine aktuelle Version von Python herunter, die Notebooks basieren auf Python 3.12.4
   - Stellt sicher, dass ihr die Option *"Add Python to PATH"* während der Installation aktiviert.
   - Folgt den Installationsanweisungen.

2. **Überprüfen der Installation:**
   - Öffnet eine Kommandozeile (Command Prompt, Terminal).
   - Gebt `python --version` ein, um zu überprüfen, ob Python korrekt installiert ist.

## Einrichten eines virtuellen Environments

- Erstellt euch einen Projektordner, in dem ihr zukünftig arbeiten wollt, bspw. nennt ihr ihn *"aero-lecture"*
- dort fügt ihr die bereitgestellten Datein `requirements.txt` und `README.md` (hier befindet ihr euch gerade) ein und später auch die Juypter Notebooks

### Methode 1: Über VS Code

Es gibt mehrere Möglichkeiten ein virtuelles Enviroment zu erzeugen. VS Code selbst bieten eine solche Funktionalität an und sie ist sehr einfach zu bedienen.

1. **Öffnen des Projekts:**
   - Öffnet VS Code
   - Geht auf `File -> Open Folder`
   - Ihr solltet im Explorer nun euren gewählten Ordnernamen sehen und darin die   `requirements.txt` und `README.md`

2. **Erstellen des Environments:**
   - Öffnet die Command Palette (F1 oder Strg+Shift+P).
   - Gebt `Python: Create Environment` ein und wählt die Option `Venv` aus.
   - Folgt den Anweisungen, um das virtuelle Environment zu erstellen.
   - VS Code erkennt automatisch die `requirements.txt`, klickt auf das Kästchen und alle benötigten Pakete werden automatisch installiert

3. **Auswählen des Environments:**
   - Navigiert rechts zu `Select Kernel` und wählt das Python-Environment aus, das ihr zuvor erstellt habt
   - Alternativ startet ihr das Notebook, wobei eine Meldung kommt und ihr daraufhin ein Environment auswählen müsst

### Methode 2: Über die Kommandozeile

1. **Erstellen des Environments:**
   - Öffnet eine Kommandozeile.
   - Navigiert zu dem Ordner, in dem euer Projekt gespeichert ist (siehe *linux_help.pdf*).
   - Gebt den folgenden Befehl ein, um ein virtuelles Environment zu erstellen:
     ```bash
     python -m venv venv
     ```

2. **Aktivieren des Environments:**
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Installieren der Abhängigkeiten:**
   - Nachdem das Environment aktiviert ist, installiert die benötigten Pakete:
     ```bash
     pip install -r requirements.txt
     ```

## Verwendung von Jupyter Notebooks in VS Code

1. **Installieren der Jupyter Erweiterung:**
   - Öffnet VS Code.
   - Geht zum Extensions-Tab (seitliches Symbol mit den Quadraten) und sucht nach "Jupyter".
   - Installiert die Jupyter Erweiterung.

2. **Starten eines Jupyter Notebooks:**
   - Öffnet die Command Palette (F1 oder Strg+Shift+P).
   - Gebt `Jupyter: Create New Blank Notebook` ein und wählt das Python-Environment aus, das ihr zuvor erstellt habt
   - Oder ihr öffnet eines der Notebooks zur Übung, navigiert rechts zu `Select Kernel` und wählt das Python-Environment aus, das ihr zuvor erstellt habt

3. **Arbeiten mit Jupyter Notebooks:**
   - Ihr könnt nun Zellen hinzufügen und euren Python-Code ausführen.
   - Speichert euer Notebook regelmäßig, um eure Fortschritte zu sichern.

## Weitere Ressourcen

- [VS Code Dokumentation](https://code.visualstudio.com/docs)
- [Python Dokumentation](https://docs.python.org/3/)
- [Jupyter Dokumentation](https://jupyter.org/documentation)

Viel Spaß und Erfolg bei den Übungen zu Berechnungsmethoden der Aerodynamik!
