def get_report(key_word, corp_code,bgn_de, t_date, api_key):
    keyword_map = {
    '유무상증자' : 'pifricDecsn',
    '유상증자':'piicDecsn',
    '전환사채권':'cvbdIsDecsn',
    '신주인수권부사채권':'bdwtIsDecsn',
    '교환사채권':'exbdIsDecsn',
    '회사분할':'cmpDvDecsn',
    '회사분할합병결정':'cmpDvmgDecsn',
    '회사합병':'cmpMgDecsn',
    }

    if key_word in keyword_map.keys():  # Assuming `report_url` is a dictionary of valid report URLs
        report_code = keyword_map[key_word]

        print(report_code)
        url = f'https://opendart.fss.or.kr/api/{keyword_map[key_word]}.json'
        print(url)
        params = {'crtfc_key': api_key,
                  'corp_code': corp_code,
                  'bgn_de': bgn_de,
                  'end_de': t_date
        }

        r = requests.get(url, params=params)
        data = r.json()

        print(data)
        target_rcept_no_prefix = t_date
        target_entries = []

        for entry in data["list"]:
            if entry.get("rcept_no", "").startswith(target_rcept_no_prefix):
                target_entries.append(entry)

        if target_entries:
            return target_entries
        else:
            return None
    else:
        print("rep not in the report URL")
        return None
