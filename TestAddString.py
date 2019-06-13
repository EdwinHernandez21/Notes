import AddString

def AddString(one, two):
    if one is not None and two is not None:
        return one+two
    else:
        return None

def Test_addString():
    assert AddString(None, None) == None
    assert AddString("", "") == ""

test_addString()