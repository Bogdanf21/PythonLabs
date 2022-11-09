import utils as ut


def run():
    while True:
        try:
            x = input("Insert number : ")
            if x == 'q':
                break
            else:
                print(ut.process_item(int(x)))
        except ValueError:
            print("Not a number")
