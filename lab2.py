def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()
    str_values = user_input.split(",")
    float_values = [float(value.strip()) for value in str_values] #Convert the list of strings to a list of floats
    return float_values
    
def calc_average(temps):
    if len(temps) == 0:
        return 0.0
    return sum(temps) / len(temps)

def find_min_max(temps):
    if len(temps) == 0:
        return [0, 0]
    min_temp = min(temps)
    max_temp = max(temps)
    return [int(min_temp), int(max_temp)]

def sort_temperature(temps):
    if len(temps) > 0:
        temps.sort()
        return temps
    else:   
        return []

def calc_median_temperature(temps):
    print("calc_median_temperature")
    temp_array = sort_temperature(temps)
    num_array = len(temp_array)
    if num_array % 2 == 0:
        median1 = temp_array[num_array//2]
        median2 = temp_array[num_array//2 - 1]
        median = (median1 + median2) / 2
    else:
        median = temp_array[num_array//2]
    return median

#main function
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    avg_temp = calc_average(num_list)
    min_max_temp = find_min_max(num_list)
    
    print(f"Average temperature: {avg_temp}")
    print(f"Min and Max temperatures: {min_max_temp}")

if __name__ == "__main__":
    main()