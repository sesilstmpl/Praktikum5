kontak = {'Ari' : '081267888', 'Dina' : '087677776' }
## Dictionary Daftar Kontak
print("Nama | Nomor Telepon")
print("----------------------------")
print('Ari', kontak['Ari'])
print('Dina', kontak['Dina'])

## Tampilkan Kontak Ari
print("Tampilkan Kontak Ari")
print(['Ari',kontak['Ari']])

## Tambah kontak baru dengan nama Riko, nomor 087654544
print("Tambah kontak baru dengan nama Riko, nomor 087654544")
kontak['Riko'] = '087654544'
print(kontak)

## Ubah Kontak Dina dengan nomor baru 088999776
print("Ubah Kontak Dina dengan nomor baru 088999776")
kontak['Dina'] = '088999776'
print(kontak)

## Tampilkan Semua Nama
print("Tampilkan Semua Nama")
print(kontak.keys())

## Tampilkan Semua Nomor
print("Tampilkan Semua Nomor")
print(kontak.values())

## Tampilkan Daftar Nama dan Nomornya
print("Tampilkan Daftar Nama dan Nomornya")
print(kontak.items())

## Hapus kontak dina
print("Hapus kontak dina")
del kontak['Dina']
print(kontak)