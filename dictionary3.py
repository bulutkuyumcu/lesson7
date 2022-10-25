prices = {"spagetti":35,"cola":5,"tost":7.5,"su":1}
increased_prices = {"spagetti":32,"tost":10,"ayran":10}

# Eski fiyatlar
print(prices)

# Farklı sözlükten güncelleme
prices.update(increased_prices)

# Yeni fiyatlar
print(prices)
