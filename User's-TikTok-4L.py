import requests
import random
import time
gog = "1234567890qwertyuiopasdfghjklzxcvbnm"
all = "._._._._."
def tiktok(user):
    url = requests.post(
        'https://www.tiktok.com/accounts/web_create_ajax/attempt/',
        headers={
            'Host': 'www.tiktok.com',
            'content-length': '85',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'sec-ch-ua-mobile': '?0',
            'x-tiktok-ajax': '81f3a3c9dfe2',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'x-requested-with': 'XMLHttpRequest',
            'x-asbd-id': '198387',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
            'x-csrftoken': 'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
            'sec-ch-ua-platform': '"Linux"',
            'origin': 'https://www.tiktok.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.tiktok.com/accounts/emailsignup/',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IQ,en;q=0.9',
            'cookie': 'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv; mid=YtsQ1gABAAEszHB5wT9VqccwQIUL; ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425; ig_nrcb=1'
        },
        data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={user}&first_name=&opt_into_one_tap=false'
    )
    if '{"feedback_title":"Try Again Later"' in url.text:
        pass
    elif '"username_is_taken"' in url.text:
        pass 
    else:
        time.sleep(random.randint(158, 463))
        vol = f"""تعال ولك جبتلك يوزر تيكتوك ✅ 
←•━━━━━━━━━━━━•→
🏆 𝚄𝚂𝙴𝚁 ➠ {user}
←•━━━━━━━━━━━━•→
🚫 𝐁𝐘 » @Jinaza  - @LeedsPy"""
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={vol}')

def users():
    while True:
        v1 = str(''.join((random.choice(gog) for _ in range(1))))
        v2 = str(''.join((random.choice(gog) for _ in range(1))))
        v3 = str(''.join((random.choice(gog) for _ in range(1))))
        v4 = str(''.join((random.choice(gog) for _ in range(1))))
        user1 = (v1 + v2 + v3 + v4)
        user2 = (v1 + v2 + v3 + v4)
        user3 = (v1 + v2 + v3 + v4)
        user4 = (v1 + v2 + v3 + v4)
        vol = (user1, user2, user3, user4)
        user = random.choice(vol)
        tiktok(user)
id = input(" ⌯ Send Your ID : ")
token = input(" ⌯ Send Your Token : ")
print("الأداة تعمل الآن، يرجى الانتظار أثناء عملية الصيد...")
users()
