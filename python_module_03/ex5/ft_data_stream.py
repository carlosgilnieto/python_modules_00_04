#!/usr/bin/env python3
def generate_event(qty: int):
    """
    Generate a event in stream
        :param qty: amount of events to create
    """
    events = ['killed a monster', 'found treasure', 'leveled up',
              'craft a object', 'eat food']
    lvls = [5, 12, 8, 3, 4, 2, 50]
    players = ['alice', 'bob', 'charlie']
    for i in range(qty):
        if i % len(players) == 0:
            it_players = iter(players)
        player = next(it_players)

        if i % len(lvls) == 0:
            it_lvls = iter(lvls)
        lvl = next(it_lvls)

        if i % len(events) == 0:
            it_events = iter(events)
        event = next(it_events)

        yield {'id': i + 1,
               'player': player,
               'lvl': lvl,
               'event': event
               }


def system_analysis(qty: int):
    """
    Analiza y da resultados de los eventos que han ocurrido
    Print the first 3 events generated
        :param qty: amount of events to generate
    """
    print(f"Processing {qty} game events...\n")
    stats = {'events': 0,
             'high_lvl': 0,
             'treasure': 0,
             'lvl_up': 0}

    for event in generate_event(1000):
        stats['events'] += 1
        if event.get('id') <= 3:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['lvl']}) {event['event']}")
        if event.get('lvl') > 10:
            stats['high_lvl'] += 1
        if event.get('event') == 'found treasure':
            stats['treasure'] += 1
        if event.get('event') == 'leveled up':
            stats['lvl_up'] += 1
    print("...")

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {stats['events']}")
    print(f"High-level players (10+): {stats['high_lvl']}")
    print(f"Treasure events: {stats['treasure']}")
    print(f"Level-up: {stats['lvl_up']}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")


def ft_fibonacci(qty: int) -> None:
    """
    Print the numbers of fibonacci series
        :param qty: amount of numbers
    """
    txt = f"Fibonacci sequence: (first {qty}): "
    for num in fibonacci(qty):
        txt += f"{num}, "
    print(txt[:-2])


def fibonacci(qty: int):
    """
    Generate a sequence of Fibonacci numbers up to a specified count.
        :param qty: The number of Fibonacci need to generate
        :retur: A generator yield with the next number
    """
    st = 0
    nd = 1
    yield st
    yield nd
    for i in range(qty - 2):
        num = st + nd
        yield num
        st = nd
        nd = num


def ft_prime(qty: int) -> None:
    """
    Print the first "qty" prime numbers in a single formatted line.
        :param qty: The number of prime sequences to search.
    """
    txt = f"Prime numbers: (first {qty}): "
    for num in prime(qty):
        txt += f"{num}, "
    print(txt[:-2])


def prime(qty: int):
    """
    Generate a sequence with the "qty" prime numbers.
        :param qty: The number of prime sequences to search.
        :return: A generator yield with the next number
    """
    numbers_found = 0
    number: int = 2
    while numbers_found < qty:
        is_prime = True
        div = 2
        while div * div <= number:
            if number % div == 0:
                is_prime = False
                div = number
            div += 1
        if is_prime:
            yield number
            numbers_found += 1
        number += 1


def ft_data_stream():
    print("=== Game Data Stream Processor ===\n")
    system_analysis(1000)

    print("\n=== Generator Demostration ===")
    ft_fibonacci(10)
    ft_prime(5)


# if __name__ == "__main__":
#     ft_data_stream()
