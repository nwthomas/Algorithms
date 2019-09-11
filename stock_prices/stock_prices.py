#!/usr/bin/python

import argparse


def find_max_profit(prices):
    if len(prices) <= 1:
        return None
    prior_smallest = prices[0]
    max_profit_so_far = prices[1] - prior_smallest
    for i in range(1, len(prices) - 1):
        new_profit = prices[i] - prior_smallest
        if new_profit > max_profit_so_far:
            max_profit_so_far = new_profit
        if prices[i] < prior_smallest:
            prior_smallest = prices[i]
    return max_profit_so_far


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
