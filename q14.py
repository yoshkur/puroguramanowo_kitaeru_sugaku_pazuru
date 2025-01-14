# P.67

COUNTRY = ["Brazil", "Croatia", "Mexico", "Cameroon",
           "Spain", "Netherlands", "Chile", "Australia",
           "Colombia", "Greece", "Cote d'Ivoire", "Japan",
           "Uruguay", "Costa Rica", "England", "Italy",
           "Switzerland", "Ecuador", "France", "Honduras",
           "Argentina", "Bosnia and Herzegovina", "Iran",
           "Nigeria", "Germany", "Portugal", "Ghana",
           "USA", "Belgium", "Algeria", "Russia",
           "Korea Republic"]


def search(prev: dict, depth: int) -> None:
    is_last = True
    for country_ in COUNTRY:
        if country_[0] == prev[-1].upper():
            if not country_dict.get(country_):
                is_last = False
                country_dict[country_] = True
                search(prev=country_, depth=depth + 1)
                country_dict[country_] = False
    if is_last:
        global max_depth
        max_depth = max(max_depth, depth)


if __name__ == '__main__':
    country_dict = {}
    for country_ in COUNTRY:
        country_dict[country_] = False

    max_depth = 0
    for country_ in COUNTRY:
        country_dict[country_] = True
        search(prev=country_, depth=1)
        country_dict[country_] = False
    print(max_depth)
