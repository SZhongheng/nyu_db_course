import csv
import operator


def main():
    print("Welcome to the Met database")
    search_string = input(
        "What type of object are you searching for (eg. Painting, Coin or all if you're feeling dangerous): ")
    if search_string != "all":
        with open("metdata.csv", "r") as fp_in, open("newfile.csv", "w") as fp_out:
            rowcount = 0
            reader = csv.reader(fp_in, delimiter=",")
            sortedlist = sorted(
                reader, key=operator.itemgetter(23), reverse=True)  # sorts item according to time period. unknown to latest to earliest
            writer = csv.writer(fp_out, delimiter=",")
            header_row_needed = True
            for row in sortedlist:
                del row[0:4]
                del row[5:9]  # remove columns that i deem as unnecessary.
                del row[21:40]
                # string matching to object type
                if row[1] == search_string or (row[0] == "Department" and header_row_needed):
                    if header_row_needed and row[0] == "Department":
                        header_row_needed = False
                    writer.writerow(row[0:15])
                    rowcount = rowcount + 1
            # print a new row with number of objects
            writer.writerow(["Number of object:", rowcount])
        print("Number of Objects: " + str(rowcount))
    else:  # if user request all, print all objects
        with open("metdata.csv", "r") as fp_in, open("newfile.csv", "w") as fp_out:
            rowc = 0
            reader = csv.reader(fp_in, delimiter=",")
            writer = csv.writer(fp_out, delimiter=",")
            sortedlist = sorted(
                reader, key=operator.itemgetter(23), reverse=True)  # sort
            for row in sortedlist:
                del row[0:4]
                del row[5:9]  # remove columns that i deem as unnecessary.
                del row[21:40]
                writer.writerow(row[0:15])
                rowc += 1
            # print a new row with number of objects
            writer.writerow(["Number of objects:", rowc])
            print("Number of Objects: " + str(rowc))


main()
