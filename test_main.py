import pytest
from main import fantasyf1
def test_fantasyf1():
    assert fantasyf1()["Result"].startswith("Your fantasy F1 team is")
    
    