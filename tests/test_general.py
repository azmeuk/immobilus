from immobilus.logic import immobilus

import time
from datetime import datetime


def test_transmutations():
    now = datetime.now()
    timetuple = now.timetuple()
    mktime = time.mktime(timetuple)
    fromtimestamp = datetime.fromtimestamp(mktime)

    assert now.replace(microsecond=0) == fromtimestamp

    with immobilus('1970-01-01 00:00:00', tz_offset=2):
        now = datetime.now()
        timetuple = now.timetuple()
        mktime = time.mktime(timetuple)
        fromtimestamp = datetime.fromtimestamp(mktime)

        assert now.replace(microsecond=0) == fromtimestamp
