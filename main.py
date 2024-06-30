import os
list_jenis_item: list[str] = ['Hijau', 'Biru', 'Ungu', 'Emas']

def fungsi_jumlah_item_dibutuhkan() -> int:
    while True:
        jumlah_item_dibutuhkan: int = input(' Masukkan jumlah item yang dibutuhkan: ')
        if jumlah_item_dibutuhkan.isdigit():
            jumlah_item_dibutuhkan: int = int(jumlah_item_dibutuhkan)
            if jumlah_item_dibutuhkan > 0:
                break
            else:
                print(' Masukkan angka lebih dari 0.')
        else:
            print(' Masukkan angka lebih dari 0.') 
    return jumlah_item_dibutuhkan

def fungsi_jumlah_item_dimiliki() -> int:
    while True:
        jumlah_item_dimiliki: int = input(' Masukkan jumlah item yang dimiliki: ')
        if jumlah_item_dimiliki.isdigit():
            jumlah_item_dimiliki: int = int(jumlah_item_dimiliki)
            if jumlah_item_dimiliki > 0:
                break
            else:
                print(' Masukkan angka lebih dari 0.')
        else:
            print(' Masukkan angka lebih dari 0.') 
    return jumlah_item_dimiliki

def fungsi_jenis_item_dibutuhkan() -> int:
    while True:
        jenis_item_dibutuhkan: int = input('Masukkan pilihan: ')
        if 0 < jenis_item_dibutuhkan < len(list_jenis_item):
            jenis_item_dibutuhkan: int = int(input('Masukkan pilihan: '))
            break
        else:
            print(f'Masukkan angka antara 1 - {len(list_jenis_item)}')
    return jenis_item_dibutuhkan
def fungsi_hijau_dimiliki() -> int:
    while True:
        hijau_dimiliki: int = input(' Masukkan jumlah item HIJAU yang dimiliki: ')
        if hijau_dimiliki.isdigit():
            hijau_dimiliki: int = int(hijau_dimiliki)
            break
        else:
            print(' Masukkan bilangan lebih dari 0.')
    return hijau_dimiliki

def fungsi_biru_dimiliki() -> int:
    while True:
        biru_dimiliki: int = input(' Masukkan jumlah item BIRU yang dimiliki: ')
        if biru_dimiliki.isdigit():
            biru_dimiliki: int = int(biru_dimiliki)
            break
        else:
            print(' Masukkan bilangan lebih dari 0.')
    return biru_dimiliki

def fungsi_ungu_dimiliki() -> int:
    while True:
        ungu_dimiliki: int = input(' Masukkan jumlah item UNGU yang dimiliki: ')
        if ungu_dimiliki.isdigit():
            ungu_dimiliki: int = int(ungu_dimiliki)
            break
        else:
            print(' Masukkan bilangan lebih dari 0.')
    return ungu_dimiliki

def fungsi_emas_dimiliki() -> int:
    while True:
        emas_dimiliki: int = input(' Masukkan jumlah item EMAS yang dimiliki: ')
        if emas_dimiliki.isdigit():
            emas_dimiliki: int = int(emas_dimiliki)
            break
        else:
            print(' Masukkan bilangan lebih dari 0.')
    return emas_dimiliki

def main():
    os.system('cls')
    print('\n', 20 * '=', 'Genshin Material Calculator', 20 * '=', '\n')
    for nomor, jenis_item in enumerate(list_jenis_item, 1):
        print(f'{nomor}. {jenis_item}')
    print(' ')
    jenis_item_dibutuhkan: str = fungsi_jenis_item_dibutuhkan()
    jumlah_item_dibutuhkan: int = fungsi_jumlah_item_dibutuhkan()
    
    if jenis_item_dibutuhkan == 1:
        hijau_dimiliki: int = fungsi_hijau_dimiliki()
        hijau_dibutuhkan: int = jumlah_item_dibutuhkan - hijau_dimiliki
        print(f' Dibutuhkan\n {hijau_dibutuhkan} item hijau.')

    elif jenis_item_dibutuhkan == 2:
        biru_dimiliki: int = fungsi_biru_dimiliki()
        hijau_dimiliki: int = fungsi_hijau_dimiliki()
        biru_dibutuhkan: int = jumlah_item_dibutuhkan - biru_dimiliki
        hijau_dibutuhkan: int = biru_dibutuhkan * 3 - hijau_dimiliki
        print(f' Dibutuhkan\n {hijau_dibutuhkan} item HIJAU\n untuk mendapatkan {biru_dibutuhkan} item BIRU')
            
    elif jenis_item_dibutuhkan == 3:
        ungu_dimiliki: int = fungsi_ungu_dimiliki()
        biru_dimiliki: int = fungsi_biru_dimiliki()
        hijau_dimiliki: int = fungsi_hijau_dimiliki()
        ungu_dibutuhkan: int = jumlah_item_dibutuhkan - ungu_dimiliki
        biru_dibutuhkan: int = ungu_dibutuhkan * 3 - biru_dimiliki
        hijau_dibutuhkan: int = biru_dibutuhkan * 3 - hijau_dimiliki
        print(f' Dibutuhkan\n {hijau_dibutuhkan} item HIJAU\n atau\n {biru_dibutuhkan} item BIRU\n untuk mendapatkan {ungu_dibutuhkan} item UNGU')

    elif jenis_item_dibutuhkan == 4:
        emas_dimiliki: int = fungsi_emas_dimiliki()
        ungu_dimiliki: int = fungsi_ungu_dimiliki()
        biru_dimiliki: int = fungsi_biru_dimiliki()
        hijau_dimiliki: int = fungsi_hijau_dimiliki()
        emas_dibutuhkan: int = jumlah_item_dibutuhkan - emas_dimiliki
        ungu_dibutuhkan: int = emas_dibutuhkan * 3 - ungu_dimiliki
        biru_dibutuhkan: int = ungu_dibutuhkan * 3 - biru_dimiliki
        hijau_dibutuhkan: int = biru_dibutuhkan * 3 - hijau_dimiliki
        print(f' Dibutuhkan\n {hijau_dibutuhkan} item HIJAU\n atau\n {biru_dibutuhkan} item BIRU\n atau\n {ungu_dibutuhkan} item UNGU\n untuk mendapatkan {emas_dibutuhkan} item EMAS')

    else:
        print(' Input tidak valid.')

# main program
if __name__ == '__main__':
    while True:
        main()

        # break
        is_done:str = input(' Apakah sudah selesai (y/n)? ')
        if is_done == 'y':
            break
        elif is_done == 'n':
            pass
        else:
            print(' Input tidak valid. Menghentikan program...')






























































