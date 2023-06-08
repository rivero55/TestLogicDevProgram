def count_and_sort_letters(input_string):
    # Inisialisasi kamus untuk menyimpan jumlah kemunculan huruf
    letter_count = {}

    # Mengiterasi setiap karakter dalam string input
    for char in input_string:
        # Mengabaikan karakter selain huruf
        if not char.isalpha():
            continue

        # Menentukan apakah huruf kapital atau tidak
        is_uppercase = char.isupper()

        # Mengubah huruf menjadi huruf kecil untuk konsistensi
        char = char.lower()

        # Memeriksa apakah huruf sudah ada dalam kamus
        if char in letter_count:
            # Memisahkan huruf jika sudah ada dengan jumlah huruf kapital yang berbeda
            if is_uppercase:
                letter_count[char]['uppercase'] += 1
            else:
                letter_count[char]['lowercase'] += 1
        else:
            # Menginisialisasi jumlah kemunculan huruf
            if is_uppercase:
                letter_count[char] = {'lowercase': 0, 'uppercase': 1}
            else:
                letter_count[char] = {'lowercase': 1, 'uppercase': 0}

    # Mengurutkan kamus berdasarkan huruf dalam urutan abjad
    sorted_letters = sorted(letter_count.items())

    # Membentuk list hasil akhir dengan huruf dan jumlah kemunculannya
    result = []
    for letter, counts in sorted_letters:
        lowercase_count = counts['lowercase']
        uppercase_count = counts['uppercase']
        if lowercase_count > 0:
            result.append(f'"{letter}": {lowercase_count}')
        if uppercase_count > 0:
            uppercase_letter = letter.upper()
            result.append(f'"{uppercase_letter}": {uppercase_count}')

    return result

# Contoh penggunaan
input_string = input("Masukkan string: ")
result = count_and_sort_letters(input_string)
print("Hasil:")
print(', '.join(result))