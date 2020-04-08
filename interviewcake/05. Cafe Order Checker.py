# https://www.interviewcake.com/question/python3/cafe-order-checker
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    take_out_idx = 0
    dine_in_idx = 0
    take_out_max_idx = len(take_out_orders) - 1
    dine_in_max_idx = len(dine_in_orders) - 1

    for order in served_orders:
        # If we still have orders in take_out_orders
        # and the current order in take_out_orders is the same
        # as the current order in served_orders
        if take_out_idx <= take_out_max_idx and order == take_out_orders[take_out_idx]:
            take_out_idx += 1

        # If we still have orders in dine_in_orders
        # and the current order in dine_in_orders is the same
        # as the current order in served_orders
        elif dine_in_idx <= dine_in_max_idx and order == dine_in_orders[dine_in_idx]:
            dine_in_idx += 1

        # If the current order in served_orders doesn't match the current
        # order in take_out_orders or dine_in_orders, then we're not serving first-come,
        # first-served.
        else:
            return False

    # Check for any extra orders at the end of take_out_orders or dine_in_orders
    if dine_in_idx != len(dine_in_orders) or take_out_idx != len(take_out_orders):
        return False

    # All orders in served_orders have been "accounted for"
    # so we're serving first-come, first-served!
    return True
