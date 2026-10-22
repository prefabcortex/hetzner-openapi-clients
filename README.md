# Inoffizielle Hetzner-API-Clients aus korrigierten OpenAPI-Specs

Soweit ich sehe, wird [hcloud-python](https://github.com/hetznercloud/hcloud-python) von Hand
geschrieben. Ich wollte wissen, wie weit man mit einem Generator kommt, wenn man ihm Hetzners
OpenAPI-Specs gibt. Damit dabei etwas Brauchbares herauskommt, musste ich die Specs erst etwas
[korrigieren](spec/fixed/). Was ich geändert habe und warum, steht weiter unten.

Inoffiziell, keine Verbindung zur Hetzner Online GmbH. Die Specs unter `spec/` stammen von
Hetzner und gehören Hetzner; sie liegen hier nur, damit die Änderungen nachvollziehbar sind.

## Inhalt

- `spec/original/`: die Specs von docs.hetzner.cloud, unverändert
- `spec/fixed/`: meine korrigierten Fassungen
- `spec/hetzner.merged.json`: beide zusammengeführt, Grundlage für die beiden Clients
- `php/`: erzeugt mit meinem PHP-Generator. PHPStan Level 10 ohne Baseline, eigene Testsuite.
- `python/`: ein schneller Test, wie das Ganze mit Python aussieht. Der Generator ist an einem Tag
  entstanden und nicht so ausgereift wie der PHP-Generator.

## Was ich an den Specs gefunden habe (Auszug)

**Kein einziges `$ref`.** Jedes Objekt steht an jeder Stelle ausgeschrieben, die `Action`
123-mal. Ein Generator macht daraus 123 verschiedene Typen. Die Namen stecken aber in den
`title`-Feldern, daraus habe ich die Referenzen zurückgebaut: 1,2 statt 3,5 MB, 535 statt
4.530 Modelle, eine `Action`. Ein Prüfskript bestätigt, dass sich am Inhalt nichts geändert hat.

**`oneOf` neben dem `discriminator`.** Bei Load-Balancer-Services, -Targets und Zonen sagt der
`discriminator` etwa `"tcp"` → `ServiceTCP`, die `oneOf`-Liste daneben enthält aber Kopien statt
Verweise. Ein Generator sieht so zwei Typen für dasselbe Objekt.

**Kleinigkeiten.** `4xx` statt `4XX` bei allen Fehlerantworten, und die Kurzbeschreibung
steht in `x-summary` statt in `info.summary`. Außerdem ist `info.version` immer `1.0.0`, obwohl
sich die Datei ändert.

**Typen, die nicht zur API passen.** Im Vergleich mit hcloud-python: Felder, die eine ID oder
einen Namen nehmen, sind nur als `string` typisiert, und manche Antwortfelder, die immer kommen,
sind optional.

## Ausprobiert

Mit dem erzeugten Python-Client habe ich einen SSH-Key hinterlegt, einen Server bestellt (nginx
kommt per cloud-init), auf seine Actions gewartet und ihn wieder gelöscht. Gekürzt:

```python
with Hetzner(validation="strict") as client:
    key = client.ssh_keys.create_ssh_key(name="laptop", public_key=public_key).ssh_key
    created = client.servers.create_server(
        name="test", server_type="cax11", image="ubuntu-24.04",
        ssh_keys=[key.id], user_data=cloud_init,  # installiert nginx
    )
    wait_for(client, [created.action, *created.next_actions])  # eigener Helfer
```

Mit `validation="strict"` prüft der Client jede Antwort der API gegen die korrigierte Spec. Bei
diesen Aufrufen gab es keine Abweichung. Der erzeugte Code besteht ruff mit allen Regeln sowie mypy und pyright im
strict-Modus, die Skripte, die ihn benutzen, ebenfalls pyright strict.

## Fazit

Ein von Hand geschriebenes SDK hat Vorteile, zum Beispiel bequeme Abkürzungen. Einen großen Teil
davon könnte man aber aus der Spec erzeugen und nur die Wrapper und Helfer von Hand schreiben.
