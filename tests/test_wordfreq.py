from features.word_frequency import word_frequency

def test_word_frequency():
    text = "Hello world hello"
    result = word_frequency(text)
    assert result["hello"] == 2
    assert result["world"] == 1