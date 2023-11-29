def duplikasi(list_buah):
    baru = []
    for buah in list_buah:
        baru.append(buah)
        baru.append(buah)
    return baru


list_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
hasil_duplikasi = duplikasi(list_buah)
print(hasil_duplikasi)



