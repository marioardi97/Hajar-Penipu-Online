import requests
import time

def kirim_pesan_ke_bot(pesan):
    token = '1111'  # Ganti dengan token bot Telegram Penipu
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {
        'chat_id': '1111',  # Ganti dengan ID chat Penipu
        'text': pesan
    }

    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print('Pesan berhasil dikirim!')
        else:
            print(f'Gagal mengirim pesan. Status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Ada kesalahan saat mengirim pesan: {e}')

# Contoh penggunaan:
pesan = 'Kata-kata hari ini << kasih yang pedes-pedes'
for i in range(100):
    kirim_pesan_ke_bot(f'{pesan}')
    time.sleep(1)  # Menunggu 1 detik setiap kali mengirim pesan untuk menghindari batasan rate dari Telegram
