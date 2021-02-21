def make_email(user_name, domain="siemens", tld=".com"):
    result = user_name + "@" + domain + tld
    return result

# benimsayfam.bilgeadam.com
# top level domain: .com

print("aaa", end="")

print(make_email("serdar.gurleyen"))
print(make_email("adil.ozcayci"))
print(make_email("mina.turgut", "siemens"))
print(make_email("zeki.gulen"))
print(make_email("alihan.bayraktar"))
print(make_email("alihan.bayraktar", tld=".net"))
print(make_email("caglar.toklu", "bilgeadam"))




