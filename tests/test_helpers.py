from mb_solana import helpers


def test_check_private_key():
    public_key = "2b8bUknUbyLmUdKPH6o4jUbgNeztKSVwCN5w2QtEm61r"
    private_key = "[100,43,148,189,179,174,228,31,193,2,233,109,26,249,247,176,51,187,172,105,83,69,170,251,45,160,23,57,212,255,9,236,23,154,5,130,7,89,91,131,59,109,150,73,105,110,198,19,222,132,173,40,62,99,162,166,44,212,129,180,49,177,253,181]"  # noqa
    assert helpers.check_private_key(public_key, private_key)

    public_key = "2b8bUknUbyLmUdKPH6o4jUbgNeztKSVwCN5w2QtEm61r"
    private_key = [
        100,
        43,
        148,
        189,
        179,
        174,
        228,
        31,
        193,
        2,
        233,
        109,
        26,
        249,
        247,
        176,
        51,
        187,
        172,
        105,
        83,
        69,
        170,
        251,
        45,
        160,
        23,
        57,
        212,
        255,
        9,
        236,
        23,
        154,
        5,
        130,
        7,
        89,
        91,
        131,
        59,
        109,
        150,
        73,
        105,
        110,
        198,
        19,
        222,
        132,
        173,
        40,
        62,
        99,
        162,
        166,
        44,
        212,
        129,
        180,
        49,
        177,
        253,
        181,
    ]
    assert helpers.check_private_key(public_key, private_key)

    public_key = "5pPavVyApDBxVQfssMGDY25dGdUfC27pTn4PygRPzFmn"
    private_key = "2nNCy96F9b11mnbrhmKn1ETdFEc6uEfaVaM5e9crn1qJmVMZnt6bMqBYhVDZt5BrhaYToJyZznK1twgF77sm63Re"
    assert helpers.check_private_key(public_key, private_key)
