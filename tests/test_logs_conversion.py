from converters.debug_logs_to_csv import convert_logs

def test_log_conversion():
    assert convert_logs("../dataset/sample_debug.log", "../dataset/output.csv")
