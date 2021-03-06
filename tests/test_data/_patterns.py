IP_V6_REGEX = r'(([0-9a-fA-F]{1,4}:)' \
              '{7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:)' \
              '{1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]' \
              '{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4})' \
              '{1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}' \
              '|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|' \
              '([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|' \
              '[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|' \
              ':((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]' \
              '{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:)' \
              '{0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.)' \
              '{3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|' \
              '([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|' \
              '1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|' \
              '(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'

MAC_ADDRESS_REGEX = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'

IP_V4_REGEX = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

USERNAME_REGEX = r'^[a-zA-Z0-9_.-]+$'

CREDIT_CARD_REGEX = r'[\d]+((-|\s)?[\d]+)+'

STR_REGEX = r'^(Address|Business|Code|Datetime|Food|Generic|Personal|Science|Structured|Text):[a-z-]+:(.*)$'

_EN_GB_POST_CODE = r'((([A-PR-UWYZ][0-9])|([A-PR-UWYZ][0-9][0-9])|' \
                   '([A-PR-UWYZ][A-HK-Y][0-9])|([A-PR-UWYZ][A-HK-Y][0-9][0-9])|' \
                   '([A-PR-UWYZ][0-9][A-HJKSTUW])|([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY]))) ' \
                   '|| ((GIR)[ ]?(0AA))|(([A-PR-UWYZ][0-9])[ ]?([0-9][ABD-HJLNPQ-UW-Z]{0,2}))' \
                   '|(([A-PR-UWYZ][0-9][0-9])[ ]?([0-9][ABD-HJLNPQ-UW-Z]{0,2}))|(([A-PR-UWYZ]' \
                   '[A-HK-Y0-9][0-9])[ ]?([0-9][ABD-HJLNPQ-UW-Z]{0,2}))|(([A-PR-UWYZ][A-HK-Y0-9]' \
                   '[0-9][0-9])[ ]?([0-9][ABD-HJLNPQ-UW-Z]{0,2}))|(([A-PR-UWYZ][0-9][A-HJKS-UW0-9])' \
                   '[ ]?([0-9][ABD-HJLNPQ-UW-Z]{0,2}))|(([A-PR-UWYZ][A-HK-Y0-9][0-9][ABEHMNPRVWXY0-9])' \
                   '[ ]?([0-9][ABD-HJLNPQ-UW-Z]{0,2}))'

POSTAL_CODE_REGEX = {
    'ru': r'[0-9]{6}$',
    'is': r'[0-9]{3}$',
    'nl': r'^[1-9][0-9]{3}\s?[a-zA-Z]{2}$',
    'pl': r'\d{2}-\d{3}',
    'pt': r'[0-9]{4}$',
    'no': r'[0-9]{4}$',
    'da': r'DK-[0-9]{4}$',
    'en-gb': _EN_GB_POST_CODE,
    'fa': r'\d{5}-\d{5}',
    'hu': r'[0-9]{4}$',
    'cs': r'\d{3}[ ]?\d{2}',
    'jp': r'[0-9]{3}-[0-9]{4}$',
    'pt-br': r'[0-9]{5}-[0-9]{3}$',
    'default': r'[0-9]{5}$'
}
