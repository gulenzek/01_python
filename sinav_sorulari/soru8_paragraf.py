# -*- --coding:utf-8 -*-
# @author: gulenzek
"""

"""
para = "We live in a digital and social media first world and human connectivity is being lost. " \
       "Building our personal and company's brands means moving away from mass messaging and content" \
       " to creating high quality human connections. At StandOut Authority, we help entrepreneurs, " \
       "business owners, job seekers and change makers become influencers on LinkedIn through a strong " \
       "brand, relevant content and human connections. Whether you're trying to draw in leads or find a " \
       "job, we'll help you standout and drive authentic relationships."
def frequency(paragraph):
	sozcukler = {}
	for sozcuk in paragraph.split():
		if sozcuk not in sozcukler:
			sozcukler[sozcuk] = 1
		else:
			sozcukler[sozcuk] += 1
	return sozcukler


def main():
    print(frequency(para))


if __name__ == "__main__":
    main()
