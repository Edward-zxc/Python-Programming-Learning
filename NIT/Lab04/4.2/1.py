import requests
headersvalue = {
    'User-Agent' : 'Mozilla/5.0(Windos NT 11.0; Win64; x64)AppleWebKit/537.36  (KHTML, like Gecko) Chrom/93.0.4577.82 Safari/537.36',
}
for i in range(0, 250, 25):
    url = ' https://movie.douban.com/top250?start= {}&filter='.format(i)
    r = requests.get(url, headers=headersvalue)
    print(r.status_code)
    print(r.url)
    with open('movie. txt', 'a+', encoding='utf-8') as f:
        f.write(r.text)
