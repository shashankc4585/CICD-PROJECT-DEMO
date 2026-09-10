from src.ran_simulator import RANSimulator


def test_ru_start():
    ran = RANSimulator()

    result = ran.start_ru()

    assert result == "RU started"
    assert ran.ru_status == "UP"


def test_du_start():
    ran = RANSimulator()

    result = ran.start_du()

    assert result == "DU started"
    assert ran.du_status == "UP"


def test_cu_start():
    ran = RANSimulator()

    result = ran.start_cu()

    assert result == "CU started"
    assert ran.cu_status == "UP"


def test_ran_status():
    ran = RANSimulator()

    ran.start_ru()
    ran.start_du()
    ran.start_cu()

    status = ran.get_status()

    assert status["RU"] == "UP"
    assert status["DU"] == "UP"
    assert status["CU"] == "UP"