#!/usr/bin/env python

# SPDX-FileCopyrightText: Greg Back <git@gregback.net>
# SPDX-License-Identifier: MIT

import genanki

convert_basic = genanki.Model(
    model_id=2049964422,
    name="Temp Convert Basic",
    fields=[
        {"name": "Convert From"},
        {"name": "Convert To"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Convert From}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Convert To}}',
        },
    ],
)

convert_advanced = genanki.Model(
    model_id=1977139614,
    name="Temp Convert Advanced",
    fields=[
        {"name": "Convert From"},
        {"name": "Convert To (Int)"},
        {"name": "Convert To (1 Decimal)"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Convert From}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Convert To (Int)}}<br>{{Convert To (1 Decimal)}}',
        },
    ],
)


def fahren_to_cels(degrees_fahrenheit: int) -> float:
    return (degrees_fahrenheit - 32) * 5.0 / 9.0


def cels_to_fahren(degrees_celsius: int) -> float:
    return (degrees_celsius * 9.0 / 5.0) + 32.0


def basic_decks():

    f2c_deck = genanki.Deck(2109879251, "Basic Fahrenheit → Celsius")
    c2f_deck = genanki.Deck(1651740584, "Basic Celsius → Fahrenheit")

    for c in range(-40, 41, 5):
        f = int(cels_to_fahren(c))

        f2c_deck.add_note(
            genanki.Note(model=convert_basic, fields=[f"{f}°F", f"{c}°C"])
        )
        c2f_deck.add_note(
            genanki.Note(model=convert_basic, fields=[f"{c}°C", f"{f}°F"])
        )

    return [f2c_deck, c2f_deck]


def advanced_f2c():

    deck = genanki.Deck(2007330762, "Advanced Fahrenheit → Celsius")

    for f in range(-40, 104):
        c = fahren_to_cels(f)

        fields = [f"{f}°F", f"{round(c)}°C", f"{round(c, 1)}°C"]

        deck.add_note(genanki.Note(model=convert_advanced, fields=fields))

    return deck


def advanced_c2f():

    deck = genanki.Deck(1165998090, "Advanced Celsius → Fahrenheit")

    for c in range(-40, 41):
        f = cels_to_fahren(c)

        fields = [f"{c}°C", f"{round(f)}°F", f"{round(f, 1)}°F"]

        deck.add_note(genanki.Note(model=convert_advanced, fields=fields))

    return deck


def main():

    for deck in basic_decks() + [advanced_f2c(), advanced_c2f()]:
        filename = f"{deck.name}.apkg"
        print(f"Writing '{filename}'")
        genanki.Package(deck).write_to_file(filename)


if __name__ == "__main__":
    main()
