from threading import Thread


def odds():
    odd_nums = [x for x in range(1, 101, 2)]
    #print(odd_nums)

    for i in range(1, 101, 2):
        print(i)

def even():
    even_nums = [x for x in range(2, 101, 2)]
    #print(even_nums)

    for x in range(2, 101, 2):
        print(x)

if __name__ == "__main__":

    t_odds = Thread(target=odds)
    t_evens = Thread(target=even)
    t_odds2 = Thread(target=odds)
    t_evens2 = Thread(target=even)

    t_odds.start()
    t_evens.start()
    t_odds2.start()
    t_evens2.start()

    t_odds.join()
    t_evens.join()
    t_odds2.join()
    t_evens2.join()

    print("finished")
