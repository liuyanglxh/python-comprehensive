a = """
scan '%s',{LIMIT=>1}
"""
for x in "ugc_guide_c,ugc_guide_u,ugc_post_c,ugc_post_u".split(","):
    print(a.strip() % x+"\n")

"""
scan 'ugc_guide_c',{LIMIT=>1}
scan 'ugc_guide_u',{LIMIT=>1}
scan 'ugc_post_c',{LIMIT=>5}
scan 'ugc_post_u',{LIMIT=>1}
scan 'au_ugc_guide_u',{LIMIT=>1}
"""
