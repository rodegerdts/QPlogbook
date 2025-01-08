import QPlogbook.importandclean as importandclean


keymap = {"point": "point",
          "text": "text",
          "position_source": "fix_type",
          "log": "log",
          "engine_hours": "enginehours",
          "course": "cog",
          "heading": "heading",
          "speed_sog": "sog",
          "speed_stw": "stw",
          "barometer": "air_pressure",
          "wind_speed": "tws",
          "wind_direction": "twd"}

d1 =  {"a": 1, "b": 2, "c": 3, "g": {"e": 5, "f": 6}, "k": ["Karin", "Enno", "Steffi"]}
d2 =  {"a": 1.1, "b": 2.2, "d": 4.4, "i": {"e": 5.5, "h": 7.7, "n": ""}, "j": {}, "k": ["Karin", "Enno", "Klaus"], "l": {"m": ""}}
d2c = {"a": 1.1, "b": 2.2, "d": 4.4, "i": {"e": 5.5, "h": 7.7}, "k": ["Karin", "Enno", "Klaus"]}
d_merged = {'a': 1.1, 'b': 2.2, 'c': 3, 'g': {'e': 5, 'f': 6}, 'k': ['Enno', 'Karin', 'Klaus', 'Steffi'], 'd': 4.4, 'i': {'e': 5.5, 'h': 7.7, 'n': ''}, 'j': {}, 'l': {'m': ''}}
yimp = importandclean.getSKlog("/Users/enno/Documents/dev/VScode/VSCpython/QPlogbook/data/testlog.yml") 
jimp = importandclean.getQPlog("/Users/enno/Documents/dev/VScode/VSCpython/QPlogbook/data/qptesttlog.json")

def test_remove_empty():
    assert importandclean.remove_empty(d2) == d2c

def test_logmap():
    assert str(importandclean.logmap(dic, keymap)) == "[{'point': 2024-08-20T11:03:12+00:00 66.7972793 13.4532821, 'text': 'Sailing x', 'fix_type': 'GPS', 'log': 7974.2, 'cog': 49, 'heading': 51, 'sog': 6.8, 'stw': 7.1, 'air_pressure': 1004.14, 'tws': 2.8, 'twd': 59}, {'point': 2024-08-21T11:03:12+00:00 66.7972793 13.4532821, 'text': 'Sailing y', 'fix_type': 'GPS', 'log': 7974.2, 'cog': 49, 'heading': 51, 'sog': 6.8, 'stw': 7.1, 'air_pressure': 1004.14, 'tws': 2.8, 'twd': 59}, {'point': 2024-08-20T11:51:12+00:00 66.8451454 13.5365294, 'text': 'Stopped', 'fix_type': 'GPS+SBAS/WAAS', 'log': 7979.4, 'cog': 292, 'heading': 298, 'sog': 0.4, 'stw': 0, 'air_pressure': 1003.31, 'tws': 3.3, 'twd': 187}]"

def test_merge():
    assert importandclean.merge_entrys(d1, d2) == d_merged

Def test_