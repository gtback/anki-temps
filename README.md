<!--
SPDX-FileCopyrightText: Greg Back <git@gregback.net>
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# anki-temps

Create [Anki](https://apps.ankiweb.net/) decks for Celsius↔Fahrenheit conversions.

## The Decks

- The "Basic Fahrenheit → Celsius" deck contains a card for every 9°F from -40°F (-40°C) to +104°F (+40°C), displaying the exact Celsius equivalent (which is a whole number).
- The "Basic Celsius → Fahrenheit" deck contains a card for every 5°C from -40°C (-40°F) to +40°C (+104°F), displaying the exact Fahrenheit equivalent (which is a whole number).
- The "Advanced Fahrenheit → Celsius" deck contains a card for every 1°F from -40°F to +104°F, displaying the Celsius equivalent rounded to a whole number and to one decimal digit.
- The "Advanced Celsius → Fahrenheit" deck contains a card for every 1°C from -40°C to +40°C, displaying the Fahrenheit equivalent rounded to a whole number, as well as the exact value (which contains one decimal digit).

## Setup

```bash
poetry install
```

## Usage

```console
$ poetry run python main.py
Writing 'Basic Fahrenheit → Celsius.apkg'
Writing 'Basic Celsius → Fahrenheit.apkg'
Writing 'Advanced Fahrenheit → Celsius.apkg'
Writing 'Advanced Celsius → Fahrenheit.apkg'
```

Or, you can just download them from the [Releases page](https://github.com/gtback/anki-temps/releases).

Then, [import them](https://docs.ankiweb.net/importing/packaged-decks.html) to Anki.
