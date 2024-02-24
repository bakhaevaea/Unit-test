import pytest
from check_average_lists  import CheckAverageLists


class TestCheck:
    def test_first_average(self):
        check = CheckAverageLists()
        result = check.check_lists([10,20,3,4,5], [1,2,3])
        assert result == "Первый список имеет большее среднее значение" , "Значение первого списка должно быть больше"
    
    def test_second_average(self):
        check = CheckAverageLists()
        result = check.check_lists([1,2,3], [10,20,3,4,5])
        assert result == "Второй список имеет большее среднее значение" , "Значение второго списка должно быть больше"

    def test_equal_average(self):
        check = CheckAverageLists()
        result = check.check_lists([1,2,3,4,5], [3,3,3])
        assert result == "Средние значения равны" , "Значения должны быть равны"

    def test_first_not_list(self):
        check = CheckAverageLists()
        with pytest.raises(TypeError):
            check.check_lists("not a list", [1,2,3]) # Передаем строку вместо списка

    def test_second_not_list(self):
        check = CheckAverageLists()
        with pytest.raises(TypeError):
            check.check_lists([1,2,3], 1) # # Передаем число вместо списка
   
    def test_emty_list_average(self):
        check = CheckAverageLists()
        result = check.check_lists([], [3,3,3])
        assert result == "Второй список имеет большее среднее значение" , "Значение второго списка должно быть больше"
    