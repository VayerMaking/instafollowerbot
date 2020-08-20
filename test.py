
from igramscraper.instagram import Instagram

instagram = Instagram()

account = instagram.get_account('_kokosaa_')


print(account.followed_by_count)
