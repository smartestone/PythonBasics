"""
WRP a program to Flatten the list.

Sample Input : [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
Output Should : [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
"""

userInput = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120], 'python']


def return_list_items(list1):
    """
    This function returns a list which contain only entities of passed list.
    :param list1:
    :return: a list
    """

    sample_list = []
    for item in list1:
        if type(item) == int or type(item) == str or type(item) == float:
            sample_list.append(item)

        elif type(item) == list:
            tmp_list = return_list_items(item)
            sample_list.extend(tmp_list)

    return sample_list


outputList = return_list_items(userInput)
print(f"Sample List  : {userInput}")
print(f"Flatten List : {outputList}")
