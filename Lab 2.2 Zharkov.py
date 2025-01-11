# TODO Напишите функцию find_common_paricipants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем, отличным от запятой
def find_common_participants(str1_, str2_, n=','):
    str1_, str2_ = [i for i in str1_.split(n)], [i for i in str2_.split(n)]
    return sorted([i for i in str1_ if i in str2_])

print(find_common_participants(participants_first_group, participants_second_group, n='|'))
