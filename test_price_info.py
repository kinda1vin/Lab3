import price_info

price_list = {'apple': 1.20, 'orange': 1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear': 0.90, 'papaya': 2.95, 'pomegranate': 4.95}
item_list = {'apple': 5, 'orange': 5, 'watermelon': 1, 'pineapple': 2, 'pear': 10, 'papaya': 1, 'pomegranate': 2}  

def test_total_cost_shopping():
    total_cost = 0
    for key in price_list.keys():
        if key in item_list:
            total_cost += price_list[key]*item_list[key]
    assert total_cost == 46.75

def test_cost_of_fruits():
    for key in price_list.keys():
        if key == 'apple':
            cost = 10*price_list[key]
            break
    assert cost == 12.0
    
