# Digimon Card Game Documentation

Do you want to live the experience of playing Digimon Card Game from your pc and/or mobile, without spending money to buy the cards? This app makes that dream come true!

## Installation

```sh
poetry install

poetry shell

pre-commit install
```

## Test

```sh
pytest

mypy --strict digimon_card_game tests

pre-commit run --all-files
```

## Update

```sh
poetry self update

poetry install

pre-commit autoupdate
```
