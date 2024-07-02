import os
list_jenis_item: list[str] = ['Keluar', 'Hijau', 'Biru', 'Ungu', 'Emas']

def fungsi_input_pilihan() -> int:
    while True:
        # mengambil input_pilihan dari user
        input_pilihan: int = input('\n Masukkan pilihan: ')
        # verifikasi apakah input merupakan input_pilihan >= 0
        if input_pilihan.isdigit():
            # jika True, maka konversi input_pilihan menjadi int 
            input_pilihan: int = int(input_pilihan)
            # verifikasi apakah input_pilihan < dari pilihan yang tersedia
            if input_pilihan < len(list_jenis_item):
                break
            else:
                # jika input_pilihan tidak < pilihan tersedia
                print(f' Tolong masukkan angka antara 0 - {len(list_jenis_item)}')
        else:
            # jika input_pilihan bukan merupakan angka >= 0 
            print(f' Tolong masukkan angka antara 0 - {len(list_jenis_item)}')
    return input_pilihan

def fungsi_input_jenis_item(pesan: str) -> int:
    while True:
        # mengambil input_pilihan dari user
        input_hijau: int = input(f'{pesan}')
        # verifikasi apakah input_hijau adalah angka >= 0
        if input_hijau.isdigit():
            # jika True, maka konversi input_hijau menjadi int
            input_hijau: int = int(input_hijau)
            break
        else:
            # jika input_hijau bukan merupakan angka >= 0
            print('Tolong masukkan angka > 0.')
    return input_hijau

def fungsi_main() -> None:
    while True:
        os.system('cls')
        print('\n',20 * '=', 'Material Calculator', 20 * '=')
        print('\n Masukkan pilihan sesuai dengan jenis item yang kamu butuhkan.\n')

        # menampilkan macam pilihan jenis item yang tersedia
        for nomor, jenis_item in enumerate(list_jenis_item):
            print(f' {nomor}. {jenis_item}')

        # meminta user memilih antara pilihan diatas
        input_pilihan: int = fungsi_input_pilihan()

        # keluar
        if input_pilihan == 0:
            # keluar dari loop
            break
        
        # hijau
        elif input_pilihan == 1:
            # mengambil informasi tentang jumlah item hijau yang dimiliki user
            hijau_dimiliki: int = fungsi_input_jenis_item('\n Berapa item hijau yang kamu miliki? ')
            # mengambil informasi tentang jumlah item hijau yang dibutuhkan user
            hijau_dibutuhkan: int = fungsi_input_jenis_item(' Berapa item hijau yang kamu butuhkan? ')
            # verifikasi apakah jumlah item hijau yang dimiliki lebih sedikit dari jumlah item hijau yang dibutuhkan
            if hijau_dimiliki < hijau_dibutuhkan:
                # update jumlah item hijau yang dibutuhkan user setelah dikurangi dengan jumlah item hijau yang sudah dimiliki user
                hijau_dibutuhkan -= hijau_dimiliki
                print(f' Dibutuhkan {hijau_dibutuhkan} item hijau.')
            # jika jumlah item hijau yang sudah dimiliki user lebih sedikit dari jumlah item hijau yang dibutuhkan user 
            else:
                # jika hasil verifikasi adalah jumlah item hijau yang sudah dimiliki user sama dengan atau lebih dari jumlah item hijau yang dibutuhkan user
                print(' Jumlah item sudah cukup.')

        # biru
        elif input_pilihan == 2:
            # mengambil informasi tentang jumlah item biru yang sudah dimiliki user
            biru_dimiliki: int = fungsi_input_jenis_item('\n Berapa jumlah item biru yang kamu miliki? ')
            # mengambil informasi tentang jumlah item hijau yang sudah dimiliki user
            hijau_dimiliki: int = fungsi_input_jenis_item(' Berapa jumlah item hijau yang kamu miliki? ')
            # mengambil informasi tentang jumlah item biru yang dibutuhkan user
            biru_dibutuhkan: int = fungsi_input_jenis_item(' Berapa jumlah item biru yang kamu butuhkan? ')
            # update jumlah item hijau yang sudah dimiliki user setelah ditambah hasil konversi dari jumlah item biru
            hijau_dimiliki: int = (biru_dimiliki * 3) + hijau_dimiliki
            # menghitung jumlah item hijau yang dibutuhkan user setelah mengonversi input jumlah item biru yang sudah dimiliki user 
            hijau_dibutuhkan: int = biru_dibutuhkan * 3
            # verifikasi apakah jumlah item hijau yang sudah dimiliki user lebih sedikit dari jumlah item hijau yang dibutuhkan user
            if hijau_dimiliki < hijau_dibutuhkan:
                # update jumlah item hijau yang dibutuhkan user setelah dikurangi dengan jumlah item hijau yang sudah dimiliki user 
                hijau_dibutuhkan -= hijau_dimiliki 
                # update jumlah item biru yang dibutuhkan user dengan mengambil int dari hasil bagi jumlah item hijau yang dibutuhkan user dengan 3
                biru_dibutuhkan: int = hijau_dibutuhkan // 3
                # update jumlah item hijau yang dibutuhkan setelah dilakukan operasi modulo dengan 3
                hijau_dibutuhkan %= 3
                print(f' Dibutuhkan {biru_dibutuhkan} item biru ({biru_dibutuhkan * 3} item hijau) dan {hijau_dibutuhkan} jumlah item hijau.')
            # jika hasil verifikasi adalah jumlah item hijau yang sudah dimiliki user sama dengan atau lebih dari jumlah item hijau yang dibutuhkan user
            else:
                print(' Jumlah item sudah cukup.')
            
        # ungu
        elif input_pilihan == 3:
            # mengambil informasi tentang jumlah item ungu yang sudah dimiliki user
            ungu_dimiliki: int = fungsi_input_jenis_item('\n Berapa jumlah item ungu yang kamu miliki? ')
            # mengambil informasi tentang jumlah item biru yang sudah dimiliki user 
            biru_dimiliki: int = fungsi_input_jenis_item(' Berapa jumlah item biru yang kamu miliki? ') 
            # mengambil informasi tentang jumlah item hijau yang sudah dimiliki user 
            hijau_dimiliki: int = fungsi_input_jenis_item(' Berapa jumlah item hijau yang kamu miliki? ') 
            # mengambil informasi tentang jumlah item ungu yang dibutuhkan user 
            ungu_dibutuhkan: int = fungsi_input_jenis_item(' Berapa jumlah item ungu yang kamu butuhkan? ') 
            # update jumlah item hijau yang sudah dimiliki user setelah mengonversi jumlah item ungu dan biru lalu ditambah dengan jumlah item hijau yang sudah dimiliki user
            hijau_dimiliki: int = (ungu_dimiliki * 9) + (biru_dimiliki * 3) + hijau_dimiliki
            # menghitung jumlah item hijau yang dibutuhkan user setelah mengonversi jumlah item ungu yang dibutuhkan user
            hijau_dibutuhkan: int = ungu_dibutuhkan * 9 
            # verifikasi apakah jumlah item hijau yang sudah dimiliki user lebih sedikit dari jumlah item hijau yang dibutuhkan user
            if hijau_dimiliki < hijau_dibutuhkan: 
                # update jumlah item hijau yang dibutuhkan user setelah dikurangi dengan jumlah item hijau yang sudah dimiliki user
                hijau_dibutuhkan -= hijau_dimiliki 
                # update jumlah item ungu yang dibutuhkan user dengan mengambil int dari hasil bagi jumlah item hijau yang dibutuhkan user dengan 9
                ungu_dibutuhkan: int = hijau_dibutuhkan // 9 
                # update jumlah item hijau yang dibutuhkan user setelah dilakukan operasi modulo dengan 9
                hijau_dibutuhkan %= 9 
                print(f' Dibutuhkan {ungu_dibutuhkan} item ungu ({ungu_dibutuhkan * 3} item biru atau {ungu_dibutuhkan * 9} item hijau) dan {hijau_dibutuhkan} item hijau.')
            # jika hasil verifikasi adalah jumlah item hijau yang sudah dimiliki user sama dengan atau lebih dari jumlah item hijau yang dibutuhkan user
            else:
                print(' Jumlah item sudah cukup.') 
            
        # emas
        elif input_pilihan == 4:
            # mengambil informasi tentang jumlah item emas yang sudah dimiliki user
            emas_dimiliki: int = fungsi_input_jenis_item('\n Berapa jumlah item emas yang kamu miliki? ')
            # mengambil informasi tentang jumlah item ungu yang sudah dimiliki user
            ungu_dimiliki: int = fungsi_input_jenis_item(' Berapa jumlah item ungu yang kamu miliki? ')
            # mengambil informasi tentang jumlah item biru yang sudah dimiliki user
            biru_dimiliki: int = fungsi_input_jenis_item(' Berapa jumlah item biru yang kamu miliki? ') 
            # mengambil informasi tentang jumlah item hijau yang sudah dimiliki user
            hijau_dimiliki: int = fungsi_input_jenis_item(' Berapa jumlah item hijau yang kamu miliki? ')
            # mengambil informasi tentang jumlah item emas yang dibutuhkan user
            emas_dibutuhkan: int = fungsi_input_jenis_item(' Berapa jumlah item emas yang kamu butuhkan? ')
            # update item hijau yang sudah dimiliki user setelah mengonversi item emas, ungu, dan biru yang sudah dimiliki user ditambah dengan item hijau yang sudah dimiliki user
            hijau_dimiliki: int = (emas_dimiliki * 27) + (ungu_dimiliki * 9) + (biru_dimiliki * 3) + hijau_dimiliki
            # menghitung jumlah item hijau yang dibutuhkan user setelah mengonversi jumlah item ungu yang dibutuhkan user
            hijau_dibutuhkan: int = emas_dibutuhkan * 27
            # verifikasi apakah jumlah item hijau yang sudah dimiliki user lebih sedikit dari jumlah item hijau yang dibutuhkan user
            if hijau_dimiliki < hijau_dibutuhkan:
                # update jumlah item hijau yang dibutuhkan user setelah dikurangi dengan jumlah item hijau yang sudah dimiliki user
                hijau_dibutuhkan -= hijau_dimiliki
                # update jumlah item ungu yang dibutuhkan user dengan mengambil int dari hasil bagi jumlah item hijau yang dibutuhkan user dengan 9
                emas_dibutuhkan: int = hijau_dibutuhkan // 27
                # update jumlah item hijau yang dibutuhkan user setelah dilakukan operasi modulo dengan 27
                hijau_dibutuhkan %= 27
                print(f' Dibutuhkan {emas_dibutuhkan} item emas ({emas_dibutuhkan * 3} item ungu atau {emas_dibutuhkan * 9} item biru atau {emas_dibutuhkan * 27} item hijau) dan {hijau_dibutuhkan} item hijau.')
            else:
                print(' Jumlah item sudah cukup.')






        # break
        is_done: str = input('\n Apakah sudah selesai (y/n)? ')
        if is_done == 'y':
            break
        else:
            pass
        

# main program
if __name__ == '__main__':
    print('')
    fungsi_main()















































    