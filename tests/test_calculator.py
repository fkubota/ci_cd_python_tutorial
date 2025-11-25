import sys
import os

# tests の一個上（project_root）をパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from calculator import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
