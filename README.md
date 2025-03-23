# Projekt

Biblioteka Pythona z podstawowymi narzędziami do operacji matematycznych, przetwarzania danych i obsługi tekstu.

## Instalacja
Aby zainstalować bibliotekę, sklonuj to repozytorium i uruchom:

pip install -e .


## Użycie

```python
from lib.math_tools import add
print(add(2, 3))  # Wynik powinien wyjśc: 5

from lib.data_utils import normalize_data
print(normalize_data([1, 2, 3, 4, 5]))  # Wyniki powinny wyglądać następująco: [0.0, 0.25, 0.5, 0.75, 1.0]

from lib.text_processing import to_uppercase
print(to_uppercase('cześć'))  # Powinno pokazać się: 'CZEŚĆ'
