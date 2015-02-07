class CoinDispenser:
    coins = [25, 10, 5, 1]

    def make_change(self, total):
        new_total = total
        change = []
        for coin in self.coins:
            coin_value = new_total // coin
            new_total = (new_total - coin) % coin
            change.append(coin_value)
        return change
