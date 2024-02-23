import qrcode
import gtts
import yfinance

# juQr = "https://www.instagram.com/2ruka__"
# file = qrcode.make(juQr)
# file.save("ju.png")
#
# text = '무엇이 당신들을 기분을 지읒같게 만드십니까?'
# tts = gtts.gTTS(text, lang="ko")
# tts.save('지읒')

nvidia = yfinance.Ticker("NVDA")
price = nvidia.info['currentPrice']
print(f"{price}")