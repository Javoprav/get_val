import pytest
from utils import dicts
'''data = {"vcs": "mercurial"}
data1 = {}'''

@pytest.fixture
def data():
    return {"vcs": "mercurial"}
@pytest.fixture
def data1():
    return {}

def test_get_val():
    assert dicts.get_val(data, "vcs") == 'mercurial'
    assert dicts.get_val(data, "vcs", "git") == 'mercurial'
    assert dicts.get_val(data1, "vcs", "git") == 'git'