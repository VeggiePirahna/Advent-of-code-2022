with open("calories.txt", "r") as fd:
    dataset = fd.read()
    calories_for_elves = []
    total = 0
    num = ""
    dataset = dataset.split("\n\n")
    for i, item in enumerate(dataset):
        dataset[i] = item.split("\n")
    
    for i, item in enumerate(dataset):
        new_int = 0
        for obj in item:
            new_int += int(obj)
        dataset[i] = new_int

    # biggest = 0
    # for item in dataset:
    #     if item > biggest:
    #         biggest = item
    dataset.sort()
    top_3 = dataset[-1] + dataset[-2] + dataset[-3]



print (top_3)
    