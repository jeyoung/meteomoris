import meteomoris


# integration tests todo
# this one just a dirty scheme for me
def test_weekforecast():


    assert isinstance(meteomoris.get_weekforecast(), list)



def test_moonphase():
    assert isinstance(meteomoris.get_moonphase(), dict)


def test_cityforecast():
    assert isinstance(meteomoris.get_cityforecast(), list)


def test_main_message():
    assert isinstance(meteomoris.get_main_message(), str)



def test_sunrisemu():
    assert isinstance(meteomoris.get_sunrisemu(), dict)



def test_sunriserodr():
    assert isinstance(meteomoris.get_sunriserodr(), dict)