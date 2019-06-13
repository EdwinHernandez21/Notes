
def AddString(one, two):
    if one is not None and two is not None:
        return one+two
    elif one is None and isinstance(two, str):
        return ""
    elif two is None and isinstance(one, str):
        return ""
    elif
        return None

def test_addString():
    assert AddString(None, None) == None
    assert AddString("", "") == ""
    assert len(addString("","")) == len("")+len("")
    assert AddString(None,"") == ""
    assert AddString("",None) == ""
    assert AddString(1, 'one')
    try:
        AddString(1, 'one')
        assert False
    excpet TypeError:
        assert True

def AddString(one, two):
    if one is not None and two is not None:
        return one+two
    else:
        return None

def Test_addString():
    assert AddString(None, None) == None
    assert AddString("", "") == ""

test_addString()
