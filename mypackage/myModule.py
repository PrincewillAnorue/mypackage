def top_n(items, n):
    """Function that returns the top n items from a list, in descending order.
    Args:
        items (array): list or array-like object to be sorted.
        n (int): number of top items to return
    Returns:
        array: top n items from the list, in desc order.
    E.g.:
        >>> top_n([8,9,5,7,3,4,1,0], 3)
        [9,8,7]
    """
    for i in range(n):  # Keep sorting until we have the top n items. This loop runs n times.
                        # If n = 3, it runs: i = 0
                        #                    i = 1
                        #                    i = 2
                        # Why? Because we only care about putting the top n biggest numbers at the 
                        # end of the list. This is a partial bubble sort.
        for j in range(len(items)-1-i):   # Let’s understand this: 
                                          # len(items) → total number of elements
                                          # -1 → because we compare j with j+1. If we didn’t subtract 1, 
                                          # we would go out of bounds.
                                          # -i → because after each pass, the biggest values move 
                                          # to the end. So we don’t need to check that part again.
                                          # That’s why we reduce the range by i.
                                          # This loop moves through the list comparing neighbors.
            if items[j] > items[j+1]:  # if this item is bigger than the next item on the list
                items[j] , items[j+1] = items[j+1] , items[j]   # Swap the two items

    # Get the last n items
    top_n = items[-n:]  # This uses list slicing. -n means: Start from n elements from the end.
                        # Example: items = [1,2,3,4,5] ; n = 2 ; items[-2:]
                        # Result: [4,5]

    # Return in descending order
    return top_n[::-1]  # This is called list slicing. The general slicing format is: 
                        # list[start:stop:step]. In: top_n[::-1] ; We are saying:
                        # start = (not specified) ; stop = (not specified) ; step = -1
                        # So it becomes: “Go through the entire list, stepping backward by 1.”
