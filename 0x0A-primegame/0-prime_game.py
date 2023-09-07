#!/usr/bin/python3


def isWinner(x, nums):
    """
    checks the winner of a round
    """

    def is_prime(num):
        """
        checks for a prime number
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
            return True

    def rounds_played(n):
        """
        number of rounds played
        """
        if n == 1:
            return "Ben"
        if n % 2 == 0:
            return "Maria"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = rounds_played(n)
        queue = [(n, "Maria")]

        while queue:
            current_n, current_player = queue.pop(0)

            if current_n == 1:
                if current_player == "Maria":
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            for i in range(2, current_n + 1):
                if is_prime(i):
                    new_n = current_n - i * (current_n // i)
                    new_player = "Maria" if current_player == "Ben" else "Ben"
                    queue.append((new_n, new_player))

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
