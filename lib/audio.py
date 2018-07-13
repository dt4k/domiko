# -*- coding: utf-8 -*-
import subprocess
from hashlib import md5
import sys
from os import path
DIR = path.realpath(path.join(path.dirname(
    path.realpath(__file__)), '../audios'))


def generate_wav(text, mechpath='/var/lib/mecab/dic/open-jtalk/naist-jdic', htsvoicepath='/usr/share/hts-voice/mei/mei_happy.htsvoice'):

    fname = md5(text.encode('utf-8')).hexdigest()
    fpath = path.join(DIR, fname + '.wav')
    u"""
    日本語テキストから音声合成wavファイルを生成.

    via http://qiita.com/kkoba84/items/b828229c374a249965a9.
    """
    open_jtalk = ['open_jtalk']
    mech = ['-x', mechpath]
    htsvoice = ['-m', htsvoicepath]
    # 再生速度
    speed = ['-r', '1.3']
    outwav = ['-ow', fpath]
    cmd = open_jtalk + mech + htsvoice + speed + outwav
    c = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    c.stdin.write(text.encode('utf-8'))
    c.stdin.close()
    c.wait()
    return fpath

if __name__ == '__main__':
    text = sys.argv[1]
    mechpath = '/usr/local/Cellar/open-jtalk/1.10_1/dic'
    htsvoicepath = '/usr/local/Cellar/open-jtalk/1.10_1/voice/mei/mei_happy.htsvoice'
    fpath = generate_wav(text, mechpath, htsvoicepath)
    #  aplay = ['afplay', '-q', fpath+'.wav']
    #  wr = subprocess.Popen(aplay)
