if root.left == root.right:
        my_list.append(root.value)
    elif root.value > root.left.value:
        if root.left is None:
            return
        else:
            return looping_listing_all_data(root.left)
    elif root.value < root.right.value:
        if root.left is None:
            return
        else:
            return looping_listing_all_data(root.right)






r_value = root.right.value
    l_value = root.left.value
    print(r_value)
    print(l_value)
    if root.left == root.right:
        my_list.append(root.value)
    elif root.value > l_value:
        if root.left is None:
            return
        else:
            return looping_listing_all_data(root.left)
    elif root.value < r_value:
        if root.left is None:
            return
        else:
            return looping_listing_all_data(root.right)