import re

def parse_time(string):
    match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(?:.(\d{3}))?', string)

    if match:
        h, m, s, ms = match.groups('00')
        ms = ms or '000'  # drop dot
        return int(h), int(m), int(s), int(ms)
    else:
        return None

# def parse_time(string):
#     match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(?:\.(\d{3}))?', string)

#     if match:
#         return tuple([int(x) for x in match.groups('0')])
#     else:
#         return None
    
