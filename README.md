
# Solution for problem at AGH PYTHON 2017 Course at WIEiT

### Usage:  
python3 ./make_midi_main.py -o mim.mid -r 15 -f "sin,cos,x,x*x*x,2-x,cos,3*x,sin,x + 2" -c 7 -s 480

# Programowanie w jezyku Python 2016/2017 zadanie 1

Uporczywe narkotyczne melodie potrafią czasem na długo przylgnąć do umysłu.
Napisz program, który generuje narkotyczne melodie. Program powinien generować różne melodie w zależności od tego, jakie użytkownik poda opcje. Użytkownik będzie tak długo modyfikował opcje programu aż wygenerowana melodia utkwi mu na stałe w głowie.

Melodie te powinny być generowane w postaci plików midi i zapisywane na dysku twardym, przy czym użytkownik powinien mieć możliwość podania lokalizacji. Obsługa karty dźwiękowej w celu odtworzenia wygenerowanej melodii nie jest konieczna. Można użyć dowolnej biblioteki do obslugi formatu midi, przykladowo https://pypi.python.org/pypi/miditime


Program ten powinien wykorzystywać następujące elementy:
 - klasy
 - funkcje
 - parsowanie argumentów linii poleceń za pomocą modułu argparse ze standardowej biblioteki
 - zewnętrzna biblioteka do obsługi formatu midi



