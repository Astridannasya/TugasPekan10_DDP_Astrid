def huruf_konsonan(kalimat):
    vokal = 'aiueoAIUEO'
    hasil = ""
    for huruf in kalimat:
        if huruf not in vokal and huruf != ' ':
            hasil += huruf
    return hasil

hasilnya = huruf_konsonan('Nurul Fikri')
print('Huruf konsonan dari kata Nurul Fikri adalah', hasilnya)