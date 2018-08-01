import json
from os.path import join
import re


def main():
    with open('pkl.json', 'w') as tong:
        json.dump(
            list(chuanpoochuliau()), tong,
            ensure_ascii=False, sort_keys=True, indent=2
        )


def chuanpoochuliau():
    chu = {}
    for na, taibun in thak('pklcl.txt'):
        chu[na] = {'tailo': taibun}
    for na, taibun in thak('pklhl.txt'):
        chu[na]['hanlo'] = taibun
    for (phinnmia, phinnpianho, chiunn, chiat), bun in sorted(chu.items(), key=lambda x: x[0][1:]):
        bun['phinnmia'] = phinnmia
        bun['phinnpianho'] = phinnpianho
        bun['chiunn'] = chiunn
        bun['chiat'] = chiat
        bun['mp3'] = join(
            '{}'.format(phinnpianho),
            '{}_{:03}_{:02}.mp3'.format(phinnpianho, chiunn, chiat)
        )
        yield bun


def thak(mia):
    chhiat = re.compile('(.+) (\d+) (\d+)\|(.*)\Z')
    chuan = set()
    with open(mia) as tong:
        for tsua in tong.readlines():
            tng = chhiat.match(tsua.strip())
            phinnmia = tng.group(1)
            chiunn = int(tng.group(2))
            chiat = int(tng.group(3))
            taibun = tng.group(4)
            chuan.add(phinnmia)
            phinnpianho = len(chuan)
            yield (phinnmia, phinnpianho, chiunn, chiat), taibun.strip()


if __name__ == '__main__':
    main()
