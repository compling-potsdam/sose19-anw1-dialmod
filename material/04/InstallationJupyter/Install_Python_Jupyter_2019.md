**Sommersemester 2019, David Schlangen, Universität Potsdam**

# Hinweise zur Installation von Python / IPython / Jupyter

Wie in der Veranstaltung angekündigt, werden wir mit Python (genauer:
IPython) innerhalb der Jupyter-Umgebung arbeiten. Falls Sie nicht
schon eine Installation aus früheren Veranstaltungen haben, ist es am
einfachsten, wenn Sie diese über die *Anaconda Distribution*
vornehmen. Diese Distribution liefert direkt schon einige der
Zusatzpakete mit, die wir in diesem Semester oder auf jeden Fall in
späteren benötigen werden.


## Installieren der *Anaconda Distribution*

Auf der Seite
[Download Anaconda Distribution](https://www.anaconda.com/download)
finden Sie Installer für Windows, macOS und Linux. Wählen Sie den für
Ihren Computer geeigneten aus. **Wichtig:** Wir werden erstmal mit der
älteren Version von Python (2.7) arbeiten. Wählen Sie also diesen
Download-Link aus. (Wenn Sie mit der Kommandozeile umgehen können,
wählen Sie den "command-line installer", ansonsten den "graphical
installer".)

## Weitere Pakete

Für einige Veranstaltungen benötigen wir weitere Pakete:

```
pandas
nltk
numpy
matplotlib
scikit_learn
ipython
```

(Und ggfs noch weitere.)  Wenn dem so ist, wird das in der Veranstaltung angekündigt. Sie können
diese Pakete über den
[Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator)
installieren (bzw. updaten, falls sie schon installiert sind; einige
davon sind Teil der Distribution). Sie können dies auch über die
Kommandozeile machen, indem Sie dem Paketnamen ein `conda install`
bzw. `conda update` voranstellen.




## Ein erster Test

Damit sollte jetzt alles bereit sein. Sie sollten jetzt in der Lage sein, das IPython notebook zu starten wie folgt (wieder in `Terminal` / Eingabeaufforderung):

* `jupyter notebook`

Es sollte jetzt ein Webbrowser-Fenster erscheinen, mit dem Jupyter
*dashboard*. Wenn dies in der Tat passiert, hat die Installation von
*Jupyter / IPython* selbst jedenfalls schon einmal funktioniert.

In demselben Ordner wie die Datei, die Sie gerade lesen, liegt auch ein erstes Test-Notebook, `testnb.ipynb`. Dieses *notebook* können Sie öffnen, indem Sie die Datei in Windows oder OS X einfach in dem Browserfenster auf den Bereich ziehen, in dem jetzt noch "Notebook list is empty." steht; besser ist allerdings (denn so werden wir es in Zukunft machen), wenn Sie den *notebook server* (den Sie mit dem `jupyter notebook` Kommando  aufgerufen haben) in dem Verzeichnis starten, in dem das *notebook* schon liegt. (D.h., Sie sollen vorher in der Kommandozeile mit `cd` in das entsprechende Verzeichnis "gegangen" sein. Überzeugen Sie sich davon, indem Sie `ls` (macOS und Linux) bzw. `dir` (Windows) aufrufen. Wenn der Name des Notebooks angezeigt wird, sind Sie im richtigen Verzeichnis.)




[^1]: Wenn Sie wissen, was Sie tun, können Sie `IPython` natürlich aber auch auf anderem Wege installieren.
