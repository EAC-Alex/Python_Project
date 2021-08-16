import matplotlib.pyplot as plt


"""
Show a graph representing the evolution of possible combinations based on the char base
"""
def show_combinations_graph(graph_title, base, max_range):
    range_to_show = range(1, max_range+1, 1)
    combinations = [calculate_combinations(base, i) for i in range_to_show]

    plt.plot(range_to_show, combinations)
    plt.title(graph_title)
    plt.xlabel("Number of characters")
    plt.ylabel("Number of combinations")
    plt.grid()
    plt.show()


"""
Return the number of possible combinations we can make based on the base and the number of given chars
"""
def calculate_combinations(base, nb_chars):
    return base ** nb_chars
    

if __name__ == "__main__":
    show_combinations_graph("Combinations in binary", 2, 10)
    show_combinations_graph("Combinations in decimal", 10, 10)
    show_combinations_graph("Combinations in alphabet", 26, 10)
