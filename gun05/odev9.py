# Q9
# whisper()
# shout() fonksiyonunun tersi.
# hepsini küçük harfe cevirecek, aradaki fazla bosluklari atacak, sonda unlem varsa kaldiracak.

def whisper(terim):
    sonuc = "".join(terim.split()).lower().replace('!', '')
    return sonuc

print(whisper("[M E @\n\t!R H A B A{][}!!    !"))
