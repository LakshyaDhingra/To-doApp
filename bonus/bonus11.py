def get_average():
    with open("/Users/lakshyadhingra/PycharmProjects/app1/bonusfiles/data.txt", "r") as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values]
    avg = sum(values) / len(values)
    return avg


average = get_average()
print(average)
