#!usr/bin/python3
class MyList(list):
    """
    Sort is different from sorted

    """
    def print_sorted(self):
        """
            We can use sort, a copy of the list is neccesary
            def print_sorted(self):
            my_list = self.copy()
            my_list.sort()
            print(my_list)

            Alsoz
        """
        my_list = self.copy()
        my_list.sort()
        print(my_list)
