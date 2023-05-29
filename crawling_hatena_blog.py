import re
import requests
import time
from datetime import datetime
import json
from bs4 import BeautifulSoup

# クローリングを開始するURL（Workship MagazineのTOPページ）
start_url = "https://hatenablog.com/"

prefix = '{:%Y%m%d_%H%M%S}_'.format(datetime.now())

# クローリング結果保存ファイル
result_file = f"{prefix}crawlingresult.jsonl"

# テキストデータ保存ファイル
text_file = f"{prefix}textdata.jsonl"

def gettext(hatenasoup):

    txthtmllist =[]
    txtlist = []

    # はてなブログの記事は'entry-inner'クラスの中に書かれています。
    article = hatenasoup.find('div', class_='entry-inner')

    # 記事タイトルの取得
    title = article.find('h1')
    txthtmllist.append(title)
    txtlist.append(title.text.replace('\n',''))

    # 本文は'entry-content hatenablog-entry'に書かれています。
    entry = article.find('div', class_='entry-content hatenablog-entry')
    txthtmllist.append(entry)
    # テキストデータは、一行ごとに分割してリスト化し、空行を削除
    txtlist.extend([s for s in entry.text.split('\n') if s != ''])

    return [txthtmllist,txtlist]

# save_dataをJSON形式でresult_fileに追記する。
def save_result(save_data, filename=result_file):

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(json.dumps(save_data, ensure_ascii=False) + '\n')
    f.close()

    return

# テキストデータのlistを指定の形式でtext_fileに追記する
def save_text(textlist, filename=text_file):

    jointxt = '\n'.join(textlist)
    save_data = {"text" : jointxt}

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(json.dumps(save_data, ensure_ascii=False) + '\n')
    f.close()

    return

#### クローリング ####

# アクセスするURL(初期値はクローリングを開始するURL)
url = start_url
urllist = [url]

# クロール済みリスト
crawledlist = []

for i in range(8):
    print(f'{i + 1}階層目クローリング開始')

    linklist = []
    # 対象ページのhtml
    for url in urllist:
        #　同じURLを何度もクロールしない
        if url in crawledlist:
            continue

        time.sleep(0.5) # データ取得前に少し待つ

        try:
            html = requests.get(url)
            soup = BeautifulSoup(html.content, "html.parser", from_encoding='utf-8') # 強制的に文字コードをutf-8にしないと文字化けするブログがある。

            # 次のループで使うURLの候補として<a>タグのリストをため込む
            linklist.extend(soup.find_all("a"))

            # テキスト抽出
            if '/entry/' in url :
                cont_txt = gettext(soup)
                cont_save_data = {"url":url, "contents": [str(cont_txt[0]), cont_txt[1]]}
                save_result(cont_save_data, filename = result_file)
                save_text(cont_txt[1], filename = text_file)
                print(cont_txt[1])

        except:
            # 何かエラーが出てもとりあえず続ける
            print(f'Error: {url}')
            continue

    # 使い終わったurllistをクロール済みリストに追加
    crawledlist.extend(urllist)
    crawledlist = list(set(crawledlist)) # 重複削除

    # 次のループのためのurllistを作る
    urllist = []
    for link in linklist:
        # 取得した<a>タグのリストから、ブログ記事であることを期待して"/entry/"が含まれているURLを取得
        for url in re.findall('<a.+?href="(.+?/entry/.+?)".*?>', str(link)):
            # 同じ記事を何度もクロールしないように'?'と'#'の後の文字列を削除
            url = re.sub('[?#].+','',url)
            urllist.append(url)
            
    # 新着ブログが載るページを追加
    urllist.extend(['https://hatenablog.com/kodawari_blogs','https://hatenablog.com/youkoso_blogs'])
    urllist = list(set(urllist)) # 重複削除

    # クロール済みリストから、新着ブログが載るページを削除
    crawledlist= [s for s in crawledlist if s != 'https://hatenablog.com/kodawari_blogs']
    crawledlist= [s for s in crawledlist if s != 'https://hatenablog.com/youkoso_blogs']

