#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    count = 0
    for i in range(list_length):
        try:
            count = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            count = 0
            print("{:s}".format('division by 0'))
        except TypeError:
            count = 0
            print("{:s}".format('wrong type'))
        except IndexError:
            count = 0
            print("{:s}".format('out of range'))
        finally:
            result.append(count)
    return result
