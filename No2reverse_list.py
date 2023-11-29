list_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def terbalik(list_buah):
    list_baru = []
    for i in range(len(list_buah) - 1, -1, -1):
        list_baru.append(list_buah[i])
    return list_baru


hasil_terbalik = terbalik(list_buah)
print(hasil_terbalik)