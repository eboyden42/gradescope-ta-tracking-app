import webscrape
import matplotlib.pyplot as plt
import argparse


def main():
    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument("username", type=str, help="Your gradescope username/email.")
    parser.add_argument("password", type=str, help="Your gradescope password.")
    parser.add_argument("course_id", type=int, help="Your gradescope course ID.")

    args = parser.parse_args()

    main_process(args.course_id, args.username, args.password)


# Takes in a gradescope course ID and returns an array containing ["TA NAME", QUESTIONS_GRADED] for each TA
def main_process(courseID, username, password):
    driver = webscrape.login(username, password)
    ta_list = webscrape.get_tas(courseID, driver)
    print(ta_list)
    ws_links = webscrape.getWorksheetLinks(driver, courseID)
    for i in range(len(ws_links)):
        print("Getting data from " + ws_links[i][0] + "...")
        questions = webscrape.get_questions(ws_links[i], driver)
        for question in questions:
            webscrape.count_questions_graded(ta_list, question, driver)
    display_pie_chart(ta_list)

def display_pie_chart(ta_list):
    if len(ta_list) == 0:
        return

    # Extract labels (TA names) and sizes (occurrences)
    labels = [ta[0] for ta in ta_list]
    sizes = [ta[1] for ta in ta_list]

    # Generate distinct colors dynamically
    cmap = plt.cm.get_cmap('tab20', len(labels))
    colors = [cmap(i) for i in range(len(labels))]

    # Create pie chart
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)

    # Title
    plt.title("TA Name Occurrences")

    # Show chart
    plt.show()


if __name__ == "__main__":
    main()
