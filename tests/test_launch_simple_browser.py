import pybrowser


def test_launch_simple_browser():
    code = pybrowser.launch_simple_browser()
    assert code == 0
