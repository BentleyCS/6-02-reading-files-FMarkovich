import CSP_6_02_reading_files as HW
def test_longestLine():
    assert HW.longestLine("6.02 Longest Line.txt") == "Felix Markovich"
def test_toBinary():
    assert HW.toBinary("6.02 Binary.txt") == ['10101000', '01010101', '00100001', '00101111', '01100010', '1011101']