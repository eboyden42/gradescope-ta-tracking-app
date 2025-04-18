import matplotlib.pyplot as plt

def display_pie_chart(ta_list):
    if len(ta_list) == 0:
        return

    # Extract labels (TA names) and sizes (occurrences)
    labels = [ta[0] for ta in ta_list]
    sizes = [ta[1] for ta in ta_list]

    # Create pie chart
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#ff9999', '#66b3ff', '#99ff99'])

    # Title
    plt.title("TA Name Occurrences")

    # Show chart
    plt.show()

# display_pie_chart([["Alice", 3], ["Bob", 5], ["Charlie", 2]])