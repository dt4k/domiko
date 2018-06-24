# -*- coding: utf-8 -*-
u"""フォルダにある全てのtxtを音声合成mp3にする."""
import subprocess
from pydub import AudioSegment
import glob
import os


def jtalk(i, t, n):
    u"""
    日本語テキストから音声合成wavファイルを生成.

    via http://qiita.com/kkoba84/items/b828229c374a249965a9.
    """
    open_jtalk = ['open_jtalk']
    #  mech = ['-x', '/var/lib/mecab/dic/open-jtalk/naist-jdic']
    mech = ['-x', '/usr/local/Cellar/open-jtalk/1.10_1/dic']
    #  htsvoice = ['-m', '/usr/share/hts-voice/mei/mei_normal.htsvoice']
    htsvoice = ['-m', '/usr/local/Cellar/open-jtalk/1.10_1/voice/mei/mei_happy.htsvoice']
    # 再生速度
    speed = ['-r', '1.3']
    outwav = ['-ow', n + '-' + str(i) + '.wav']
    cmd = open_jtalk + mech + htsvoice + speed + outwav
    c = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    c.stdin.write(t)
    c.stdin.close()
    c.wait()
    # aplay = ['aplay', '-q', 'open_jtalk.wav']
    # wr = subprocess.Popen(aplay)


def text2jtalk():
    u"""フォルダにある全てのtxtを音声合成mp3にする."""
    # フォルダ内にあるtxtの名前をリストにする
    textlist = glob.glob('*.txt')
    for text in textlist:
        n = text.rstrip('.txt')
        # openjtalkは1024バイトまでしか一度に処理できないので、改行で区切る
        # then convert str into byte
        ts = open(text, 'r').read().split('\n')
        ts = filter(lambda s: s != '', ts)
        for i, t in enumerate(ts):
            jtalk(i, bytes(t, 'utf-8'), n)
        # 区切って生成したwavを結合する
        s = AudioSegment.from_wav(n + '-0.wav')
        os.remove(n + '-0.wav')
        for i in range(len(list(ts)) - 1):
            s += AudioSegment.from_wav(n + '-' + str(i + 1) + '.wav')
            os.remove(n + '-' + str(i + 1) + '.wav')
        # mp3で書き出す
        s.export(n + '.mp3', format='mp3')
        print(n + '.mp3')


if __name__ == '__main__':
    text2jtalk()