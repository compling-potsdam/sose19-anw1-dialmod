*Praktische Dialogmodellierung, Universität Potsdam, SoSe 19, David Schlangen*

# Aufgabe nach Sitzung 3: NLU mit regulären Ausdrücken [ Beispiellösung ]

Zuerst `compile_nlu_regexp_data.py` im `DSTC`-Verzeichnis ausführen. (Davor sollten Sie den Anweisungen in `README.md` gefolgt sein.) Danach sollten Sie nach dem Muster `usr_sem-dstc2_SPLIT.json` benannte Dateien vorfinden, jeweils für `dev` und `train` als `SPLIT`, und jeweils noch einmal mit `-test.json`.

Schieben Sie diese Dateien in ein Unterverzeichnis `Input`.

Erzeugen Sie ein Unterverzeichnis `Output`.

Sie können nun mit `python regexp_nlu.py Input/usr_sem-dstc2_dev-test.json Output/out-dev.json` die Verarbeitung des Entwicklungssets starten.

Mit `python eval_nlu.py Output/out-dev.json Input/usr_sem-dstc2_dev.json Output/errlog.json` können Sie die Ausgabe evaluieren.

Zum Abschluss können Sie diese Schritte auch auf der größeren Teilmenge der Daten ausführen:

* `python regexp_nlu.py Input/usr_sem-dstc2_train-test.json Output/out-train.json`
* `python eval_nlu.py Output/out-train.json Input/usr_sem-dstc2_train.json Output/errlog-train.json`
