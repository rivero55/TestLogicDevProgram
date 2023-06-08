def pattern_count(text, pattern):
    # Menghitung panjang teks dan pola
    text_length = len(text)
    pattern_length = len(pattern)


    if pattern_length == 0:
        return 0

    # Inisialisasi variabel untuk menyimpan jumlah kemunculan pola
    count = 0

    # Mengiterasi melalui teks
    for i in range(text_length - pattern_length + 1):
        # Memeriksa apakah pola cocok dengan bagian teks saat ini
        if text[i:i + pattern_length] == pattern:
            count += 1

    return count

# Contoh penggunaan
text='aaaaaa'
pattern=''
jumlah_pola= pattern_count(text,pattern)
print("Output:", jumlah_pola)
