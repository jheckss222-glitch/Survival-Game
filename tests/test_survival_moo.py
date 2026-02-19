import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import survival_moo


def _stable_game(monkeypatch):
    game = survival_moo.SurvivalGame()
    monkeypatch.setattr(game, "advance_time", lambda hrs=1: None)
    return game


def test_gather_depletes_node(monkeypatch):
    game = _stable_game(monkeypatch)
    env = game.current_env()
    node = next(iter(env.resource_nodes.values()))
    node.count = 1
    monkeypatch.setattr(survival_moo.random, "choice", lambda seq: node)
    monkeypatch.setattr(survival_moo.random, "randint", lambda a, b: 3)

    before = game.player.inventory[node.item]
    game.gather()

    assert game.player.inventory[node.item] == before + 1
    assert node.count == 0


def test_hunt_success_increases_raw_meat(monkeypatch):
    game = _stable_game(monkeypatch)
    monkeypatch.setattr(survival_moo.random, "choice", lambda seq: seq[0])
    monkeypatch.setattr(survival_moo.random, "random", lambda: 0.0)
    monkeypatch.setattr(survival_moo.random, "randint", lambda a, b: 2)

    before = game.player.inventory["raw_meat"]
    game.hunt()

    assert game.player.inventory["raw_meat"] == before + 2


def test_drink_reduces_thirst(monkeypatch):
    game = _stable_game(monkeypatch)
    game.player.thirst = 70
    monkeypatch.setattr(survival_moo.random, "choice", lambda seq: seq[0])

    game.drink()

    assert game.player.thirst == 35


def test_eat_cooked_meat_reduces_hunger(monkeypatch):
    game = _stable_game(monkeypatch)
    game.player.hunger = 80
    game.player.inventory["cooked_meat"] = 1

    game.eat()

    assert game.player.hunger == 45
    assert game.player.inventory["cooked_meat"] == 0


def test_rest_recovers_health(monkeypatch):
    game = _stable_game(monkeypatch)
    game.player.health = 50
    game.player.shelter.level = 1
    game.player.fire_lit = True

    game.rest()

    assert game.player.health == 66
