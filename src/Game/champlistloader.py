from __future__ import annotations
from ast import List
from typing import Dict
from .core import Champion

def _parse_champ(champ_text: str) -> Champion:
    name, rock, paper, scissors = champ_text.split(sep=',')
    return Champion(name, float(rock), float(paper), float(scissors))


def from_csv(filename: str) -> dict[str, Champion]:
    champions = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            champ = _parse_champ(line)
            champions[champ.name] = champ
    return champions


def load_some_champs():
    return from_csv('src/Game/some_champs.txt')


def _clientParseChamp(champs: List[Dict[str, str]]) -> Dict[Champion]:
    champions: Dict[str, Champion] = dict()
    for champ in champs:
        champions[champ['name']] = (Champion(champ['name'], champ['rock'], champ['paper'], champ['scissors']))
    return champions

