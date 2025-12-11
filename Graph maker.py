import matplotlib.pyplot as plt

graph_type = input("Enter graph type (line/bar/scatter): ").lower()
values = list(map(int, input("Enter values separated by space: ").split()))

x = list(range(1, len(values)+1))

if graph_type == "line":
    plt.plot(x, values)
elif graph_type == "bar":
    plt.bar(x, values)
elif graph_type == "scatter":
    plt.scatter(x, values)
else:
    print("Invalid graph type!")

plt.show()
