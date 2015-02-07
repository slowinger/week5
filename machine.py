class CoinDispenser:
    coins = [25, 10, 5, 1]

    def make_change(self, total):
        change = []
        for coin in self.coins:
            coin_value = total // coin
            total = total % coin
            change.append(coin_value)
        return change
