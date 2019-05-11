*Praktische Dialogmodellierung, Universität Potsdam, SoSe 19, David Schlangen*

# Aufgabe nach Sitzung 4: NLU mit Rasa NLU

Führen Sie das Notebook `Intro_Rasa_NLU.ipynb` in `RasaIntro` aus und machen Sie sich mit dem Umgang mit RasaNLU vertraut. (Mehr Informationen in der [Rasa NLU Dokumentation](https://rasa.com/docs/nlu/).)

Ihre Aufgabe ist es nun, eine NLU für unsere DSTC-Domäne zu trainieren. Dazu können Sie als Ausgangspunkt die automatisch aus den DSTC-Daten aufbereiteten Intents verwenden, in `Aufgabe/dev.md`.

**ACHTUNG:** Diese Daten müssen Sie noch durchsehen; bei der automatischen Überführung sind Fehler aufgetreten. (Welche? Welche Eigenart der DSTC-Daten ist problematisch für den Ansatz von Rasa NLU?)

Ziel dieser Übung ist es, ein Gefühl dafür zu bekommen, wie gut (oder schlecht) Rasa NLU verallgemeinert:

* Konstruieren Sie eine minimale Trainingsdatei (von der Art von `dev.md`, aber mit viel weniger Einträgen) und eine umfangreichere Testdatei (von der von `test.md`, aber durchgesehen).
* Werden im Test Eingaben erkannt, auch wenn sie nicht genau so in der Trainingsdatei waren?
* Wie sieht es mit den Slots aus? Wenn in der Trainingsdatei nur "moderate" und "expensive" sind, wird dann auch "cheap" erkannt? Oder "exclusive"?

Reichen Sie ein IPython-Notebook ein, das Ihre Experimente dokumentiert. (Bis Ende *Dienstag*, 14.5.)


