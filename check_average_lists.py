class CheckAverageLists:
    # функция поиска среднего значения
    def find_average(self,numbers):
        if not isinstance(numbers, list):
            raise TypeError("Не является списком")
        if not numbers: # Проверка на пустой список
            return 0
        return sum(numbers) / len(numbers)
      
    # функция сравнения средних значений списков
    def check_lists(self, list1, list2):
        average_list1 = self.find_average(list1)
        average_list2 = self.find_average(list2)
        if average_list1 > average_list2:
            return "Первый список имеет большее среднее значение"
        if average_list1 < average_list2:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
      