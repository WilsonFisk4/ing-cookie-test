# ING Cookie Acceptance Test

Projekt automatyzuje proces zgody na ciasteczka analityczne na stronie https://www.ing.pl z wykorzystaniem Playwright.

## Jak uruchomić test

1. Sklonuj repozytorium.
2. Zainstaluj zależności (`pip install -r requirements.txt`).
3. Uruchom test (`pytest`).

## Co robi test

- Wejdzie na stronę ING.
- W menu ciasteczek kliknie „Dostosuj”.
- Zaznaczy ciasteczka analityczne.
- Kliknie „Zaakceptuj wybrane”.
- Sprawdzi, czy zapisano odpowiednie ciasteczka.
