# from nltk.metrics import edit_distance
# import random
# import string

# scores = []

# def four_letter_string():
#     temp = ""
#     for i in range(4):
#         temp += random.choice(string.ascii_letters).lower()
#     return temp

# str1 = four_letter_string()
# print(str1)

# for i in range(1000000):
#     str2 = four_letter_string()
#     temp = edit_distance(str1,str2)
#     scores.append(temp)
#     # print(f"dist between {str1} and {str2} is {temp}")

# # print(scores)
# # print(sum(scores)/len(scores))

# for i in range(0,5):
#     print(f"{i}s: {scores.count(i)}")

test_list = [2,4,5,6,1]
print(filter(lambda x: x < 5, test_list))