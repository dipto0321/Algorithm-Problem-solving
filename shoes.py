# codechef problem: SHOES


def shoe_need_to_buy(N: int, M: int) -> int:
    """Calculate the total number of shoes needed to ensure each friend has a pair.

    This function determines how many additional shoes need to be purchased based on the number of friends (N)
    and the number of existing left shoes (M). If there are more friends than left shoes, each friend without a left shoe
    will need a complete pair. If there are enough left shoes for every friend, only right shoes for each left are needed.

    Args:
        N (int): Number of friends who need shoes.
        M (int): Number of available left shoes.

    Returns:
        int: The total number of shoes that need to be bought to ensure each friend has one pair.
    """

    if N <= M:
        return N
    else:
        return 2 * N - M


t = int(input())
res = []
for i in range(t):
    N, M = map(int, input().split())
    res.append(shoe_need_to_buy(N, M))

for r in res:
    print(r)
