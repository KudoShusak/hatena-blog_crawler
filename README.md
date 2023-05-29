# hatena blog crawler
はてなブログ `hatenablog.com` から記事を収集します。  
Collect articles from the Hatena blog `hatenablog.com`.

## execution 
```
% python crawling_hatena_blog.py
```

カレントディレクトリに２種類のファイル、`xxxxxxxx_xxxxxx_crawlingresult.log`と、`xxxxxxxx_xxxxxx_textdata.log`が出力されます。  
（`xxxxxxxx_xxxxxx`には、実行した日付と時刻からユニークな文字列が入ります）  
Two files, `xxxxxxxxxxxx_xxxxxx_crawlingresult.log` and `xxxxxxxxxxxx_xxxxxx_textdata.log`, will be output in the current directory.  
(where `xxxxxxxxxxxx_xxxxxxxx` is a unique string from the date and time of execution)

* `xxxxxxxx_xxxxxx_textdata.log`  
記事のテキストデータが保存されます。  
The text data of the article is saved.
* `xxxxxxxx_xxxxxx_crawlingresult.log`  
クロールしたURLと、htmlから抽出した記事のデータ（htmlタグ付きと、テキストデータ）が保存されます。  
The crawled URL and the article data (html tagged and text data) extracted from the html are saved.

## Saved data format

### xxxxxxxx_xxxxxx_textdata.log

１記事につき、１行のJSONフォーマットで保存されます。（JSONLフォーマット）内容は下記の通り。  
One line per article will be saved in JSON format.(JSONL Format) The contents are as follows

```
{"text":"Article Data"}
{"text":"Article Data"}
{"text":"Article Data"}
.....
```

Example.
```
{"text": "【第9回】はてなブログお知らせレター：スマートフォン版はてなブログの広告の位置を変更しました\n広告表示についての大切なお知らせです。いつもはてなブログをお使いいただきありがとうございます。はてなブログ プロデューサーの永田です。今回は、はてなブログ内の広告についてのお知らせをお届けいたします。\nスマートフォン版はてなブログの広告の位置を変更いたしました\nこのたび、はてなブログでは、2022年12月12日（月）に、スマートフォン版（以下、スマホ版）はてなブログの広告の位置を変更いたしました。こちらの変更は、はてなブログ無料版のみとなります。はてなブログPro（有料プラン）では引き続き広告は表示されません。これまでのスマホ版のはてなブログでは、記事タイトルのすぐ下にバナー型の広告が入っておりました。しかし、この配置では記事タイトル直下に広告が表示されることによって、画面で最初に目に入る領域（ファーストビュー）が記事タイトルと広告のみになってしまい、すぐ本文を読み始めることができないという課題がありました。そのため、ファーストビューに本文が表示されるよう、2022年12月12日（月）より記事冒頭の広告の位置をタイトル直下から本文の間に移動いたしました。実際の広告位置は、以下の変更前・変更後の画像をご確認ください。なお、ページ全体での広告の数には変更はありません。また、この変更を受け、ユーザーのみなさまより「本文の間に配置された広告と、自分のテキストや画像との境界がわかりづらく混乱する」とのご指摘がありました。ご不便をおかけし申し訳ございません。こちらについて、広告とユーザー様のテキストや画像の境界を明確にするため、広告の上下にスペースを取り背景色を敷くなど、広告周りのデザインを調整いたしました。はてなブログでは、安定した運営・開発を続けていくためサービス内に広告枠を設置しておりますが、可能な限りユーザーのみなさまの利便性を損ねないよう努力したいと考えています。今後も、引き続き改善を行ってまいりますので、どうぞよろしくお願いいたします。\nこれまでの広告表示に関するお知らせ\nstaff.hatenablog.com\nstaff.hatenablog.com\nBy 週刊はてなブログ編集部\nProfile\n週刊はてなブログ編集部\n週刊はてなブログ編集部は、株式会社はてなのメディア「週刊はてなブログ（週ブロ）」を運営する編集チームです。編集部のメンバーは、日々はてなブログを巡回し、多種多様なブログを見つけ出して週ブロや公式Twitterアカウントで紹介しています。\n週ブロ編集部のおすすめブログを紹介するTwitterアカウントはコチラ"}
{"text": "初めてのブログ٩( ''ω'' )و\n今日からブログをSTART٩( ''ω'' )و\n今まではインスタやTwitterなんかをサラッとしてたけど、、日記みたいな感覚で我が家の日常を書いてみようかな？って思いました。\n何故ブログにしたのかと、、ただ単に知り合いに知られずに、、興味のある人に見てもらいたいと思ったからー\nTwitter裏アカとか、、分からん、、(。-`ω-)、、、。\n今日は、まり(娘）が欲しいものがあるからってことでショッピングモールに行きました！\n日曜日のショッピングモール、、、激混み。\n息子たちもついてきたので皆でブラブラ。しかし、今月は税金の月で私は金欠(｡◕ˇдˇ​◕｡)/\n子供たちは各自おこずかいでどーぞ！！\nまりはまだ早いだろー！と思われる本を3冊買った模様、、、。\nるき(末っ子)は兄にそそのかされ1000円ガチャ、、、。\n1000円あったら卵3パックは買える(´Д⊂ヽ\nアホやなって思いながらも、その後るきが銀だこおごってくれたからアホ撤回！\nまりの本もツッコもうと思ったが、ミスド買ってくれたからやめといた(笑)\n単純なママで良かったな！！！\nだい(長男）に「あんたは何かご馳走してくれないの？？( *´艸｀)」って言ったら、「人のために金使うとかありえない」って、、、。\nそーゆーやつだった、、、。\n今日も我が家は平和です(;´∀｀)\nさて明日からまた1週間の始まり！！\n緩く行きましょう(●´ω｀●)\n "}
```

### xxxxxxxx_xxxxxx_crawlingresult.log

１記事につき、１行のJSONフォーマットで保存されます。（JSONLフォーマット）内容は下記の通り。  
One line per article will be saved in JSON format.(JSONL Format) The contents are as follows
```
{"url": "https://www......", "contents": ["[Article data with html tags]","[Article data with only text extracted]"]}
{"url": "https://www......", "contents": ["[Article data with html tags]","[Article data with only text extracted]"]}
{"url": "https://www......", "contents": ["[Article data with html tags]","[Article data with only text extracted]"]}
.....
```

Example.
```
{"url": "https://blog.hatenablog.com/entry/2022/12/22/180000", "contents": ["[<h1 class=\"entry-title\">\n<a class=\"entry-title-link bookmark\" href=\"https://blog.hatenablog.com/entry/2022/12/22/180000\">【第9回】はてなブログお知らせレター：スマートフォン版はてなブログの広告の位置を変更しました</a>\n</h1>, <div class=\"entry-content hatenablog-entry\">\n<p></p><div class=\"entry-coverImage\"><span itemscope=\"\" itemtype=\"http://schema.org/Photograph\"><a class=\"hatena-fotolife\" href=\"http://f.hatena.ne.jp/hatenablog/20221222165744\" itemprop=\"url\"><img class=\"hatena-fotolife\" height=\"630\" itemprop=\"image\" loading=\"lazy\" src=\"https://cdn-ak.f.st-hatena.com/images/fotolife/h/hatenablog/20221222/20221222165744.jpg\" title=\"\" width=\"1200\"/></a></span></div><p class=\"entry-tagline\">広告表示についての大切なお知らせです。</p>いつもはてなブログをお使いいただきありがとうございます。はてなブログ プロデューサーの永田です。今回は、はてなブログ内の広告についてのお知らせをお届けいたします。<p></p>\n<div class=\"section\">\n<h3 id=\"スマートフォン版はてなブログの広告の位置を変更いたしました\">スマートフォン版はてなブログの広告の位置を変更いたしました</h3>\n<p>このたび、はてなブログでは、2022年12月12日（月）に、スマートフォン版（以下、スマホ版）はてなブログの広告の位置を変更いたしました。こちらの変更は、はてなブログ無料版のみとなります。はてなブログPro（有料プラン）では引き続き広告は表示されません。</p><p>これまでのスマホ版のはてなブログでは、記事タイトルのすぐ下にバナー型の広告が入っておりました。しかし、この配置では記事タイトル直下に広告が表示されることによって、画面で最初に目に入る領域（ファーストビュー）が記事タイトルと広告のみになってしまい、すぐ本文を読み始めることができないという課題がありました。</p><p>そのため、ファーストビューに本文が表示されるよう、2022年12月12日（月）より記事冒頭の広告の位置をタイトル直下から本文の間に移動いたしました。</p><p>実際の広告位置は、以下の変更前・変更後の画像をご確認ください。なお、ページ全体での広告の数には変更はありません。</p><p><span itemscope=\"\" itemtype=\"http://schema.org/Photograph\"><img class=\"hatena-fotolife\" height=\"1280\" itemprop=\"image\" loading=\"lazy\" src=\"https://cdn-ak.f.st-hatena.com/images/fotolife/h/hatenablog/20221222/20221222132451.jpg\" title=\"\" width=\"1280\"/></span></p><p>また、この変更を受け、ユーザーのみなさまより「本文の間に配置された広告と、自分のテキストや画像との境界がわかりづらく混乱する」とのご指摘がありました。ご不便をおかけし申し訳ございません。</p><p>こちらについて、広告とユーザー様のテキストや画像の境界を明確にするため、広告の上下にスペースを取り背景色を敷くなど、広告周りのデザインを調整いたしました。</p><p>はてなブログでは、安定した運営・開発を続けていくためサービス内に広告枠を設置しておりますが、可能な限りユーザーのみなさまの利便性を損ねないよう努力したいと考えています。</p><p>今後も、引き続き改善を行ってまいりますので、どうぞよろしくお願いいたします。</p>\n</div>\n<div class=\"section\">\n<h3 id=\"これまでの広告表示に関するお知らせ\">これまでの広告表示に関するお知らせ</h3>\n<p><iframe class=\"embed-card embed-blogcard\" frameborder=\"0\" loading=\"lazy\" scrolling=\"no\" src=\"https://hatenablog-parts.com/embed?url=https%3A%2F%2Fstaff.hatenablog.com%2Fentry%2F2017%2F06%2F14%2F171500\" style=\"display: block; width: 100%; height: 190px; max-width: 500px; margin: 10px 0px;\" title=\"スマートフォンのカテゴリー別記事一覧ページで、パンくずリストを表示するようにしました。あわせて広告枠の追加に関するお知らせ - はてなブログ開発ブログ\"></iframe><cite class=\"hatena-citation\"><a href=\"https://staff.hatenablog.com/entry/2017/06/14/171500\">staff.hatenablog.com</a></cite><br/>\n<iframe class=\"embed-card embed-blogcard\" frameborder=\"0\" loading=\"lazy\" scrolling=\"no\" src=\"https://hatenablog-parts.com/embed?url=https%3A%2F%2Fstaff.hatenablog.com%2Fentry%2F2018%2F05%2F21%2F153000\" style=\"display: block; width: 100%; height: 190px; max-width: 500px; margin: 10px 0px;\" title=\"iPhone・iPadアプリで、複数の写真をまとめてアップロードできるようにしました。あわせて広告枠の追加に関するお知らせ（追記あり） - はてなブログ開発ブログ\"></iframe><cite class=\"hatena-citation\"><a href=\"https://staff.hatenablog.com/entry/2018/05/21/153000\">staff.hatenablog.com</a></cite></p>\n</div>\n<div class=\"profile-cards-list\">\n<div class=\"profile-card-container\">\n<div class=\"entry-header-author\">\n<div class=\"header-author-icon\">\n<img class=\"profile-image\" src=\"https://cdn.blog.st-hatena.com/files/11696248318755105757/13574176438073175238\"/>\n</div>\n<div class=\"header-author-content\">\n<div>By 週刊はてなブログ編集部</div>\n<a class=\"profile-link\" href=\"#profile-card\">Profile</a>\n</div>\n</div>\n<img class=\"profileCard-image\" src=\"https://cdn.blog.st-hatena.com/files/11696248318755105757/13574176438073175238\"/>\n<h4>週刊はてなブログ編集部</h4>\n<p>\n週刊はてなブログ編集部は、株式会社はてなのメディア「週刊はてなブログ（週ブロ）」を運営する編集チームです。編集部のメンバーは、日々はてなブログを巡回し、多種多様なブログを見つけ出して週ブロや公式Twitterアカウントで紹介しています。</p>\n<p>週ブロ編集部のおすすめブログを紹介する<a href=\"https://twitter.com/hatenablog\">Twitterアカウントはコチラ</a></p>\n</div>\n</div>\n</div>]", ["【第9回】はてなブログお知らせレター：スマートフォン版はてなブログの広告の位置を変更しました", "広告表示についての大切なお知らせです。いつもはてなブログをお使いいただきありがとうございます。はてなブログ プロデューサーの永田です。今回は、はてなブログ内の広告についてのお知らせをお届けいたします。", "スマートフォン版はてなブログの広告の位置を変更いたしました", "このたび、はてなブログでは、2022年12月12日（月）に、スマートフォン版（以下、スマホ版）はてなブログの広告の位置を変更いたしました。こちらの変更は、はてなブログ無料版のみとなります。はてなブログPro（有料プラン）では引き続き広告は表示されません。これまでのスマホ版のはてなブログでは、記事タイトルのすぐ下にバナー型の広告が入っておりました。しかし、この配置では記事タイトル直下に広告が表示されることによって、画面で最初に目に入る領域（ファーストビュー）が記事タイトルと広告のみになってしまい、すぐ本文を読み始めることができないという課題がありました。そのため、ファーストビューに本文が表示されるよう、2022年12月12日（月）より記事冒頭の広告の位置をタイトル直下から本文の間に移動いたしました。実際の広告位置は、以下の変更前・変更後の画像をご確認ください。なお、ページ全体での広告の数には変更はありません。また、この変更を受け、ユーザーのみなさまより「本文の間に配置された広告と、自分のテキストや画像との境界がわかりづらく混乱する」とのご指摘がありました。ご不便をおかけし申し訳ございません。こちらについて、広告とユーザー様のテキストや画像の境界を明確にするため、広告の上下にスペースを取り背景色を敷くなど、広告周りのデザインを調整いたしました。はてなブログでは、安定した運営・開発を続けていくためサービス内に広告枠を設置しておりますが、可能な限りユーザーのみなさまの利便性を損ねないよう努力したいと考えています。今後も、引き続き改善を行ってまいりますので、どうぞよろしくお願いいたします。", "これまでの広告表示に関するお知らせ", "staff.hatenablog.com", "staff.hatenablog.com", "By 週刊はてなブログ編集部", "Profile", "週刊はてなブログ編集部", "週刊はてなブログ編集部は、株式会社はてなのメディア「週刊はてなブログ（週ブロ）」を運営する編集チームです。編集部のメンバーは、日々はてなブログを巡回し、多種多様なブログを見つけ出して週ブロや公式Twitterアカウントで紹介しています。", "週ブロ編集部のおすすめブログを紹介するTwitterアカウントはコチラ"]]}
{"url": "https://giz.hateblo.jp/entry/2023/05/28/182010", "contents": ["[<h1 class=\"entry-title\">\n<a class=\"entry-title-link bookmark\" href=\"https://giz.hateblo.jp/entry/2023/05/28/182010\">初めてのブログ٩( ''ω'' )و</a>\n</h1>, <div class=\"entry-content hatenablog-entry\">\n<p>今日からブログをSTART٩( ''ω'' )و</p>\n<p>今まではインスタや<a class=\"keyword\" href=\"https://d.hatena.ne.jp/keyword/Twitter\">Twitter</a>なんかをサラッとしてたけど、、日記みたいな感覚で我が家の日常を書いてみようかな？って思いました。</p>\n<p>何故ブログにしたのかと、、ただ単に知り合いに知られずに、、興味のある人に見てもらいたいと思ったからー</p>\n<p><a class=\"keyword\" href=\"https://d.hatena.ne.jp/keyword/Twitter\">Twitter</a>裏アカとか、、分からん、、(。-`ω-)、、、。</p>\n<p>今日は、まり(娘）が欲しいものがあるからってことでショッピングモールに行きました！</p>\n<p>日曜日のショッピングモール、、、激混み。</p>\n<p>息子たちもついてきたので皆でブラブラ。しかし、今月は税金の月で私は金欠(｡◕ˇдˇ​◕｡)/</p>\n<p>子供たちは各自おこずかいでどーぞ！！</p>\n<p>まりはまだ早いだろー！と思われる本を3冊買った模様、、、。</p>\n<p>るき(末っ子)は兄にそそのかされ1000円ガチャ、、、。</p>\n<p>1000円あったら卵3パックは買える(´Д⊂ヽ</p>\n<p>アホやなって思いながらも、その後るきが銀だこおごってくれたからアホ撤回！</p>\n<p>まりの本もツッコもうと思ったが、<a class=\"keyword\" href=\"https://d.hatena.ne.jp/keyword/%A5%DF%A5%B9%A5%C9\">ミスド</a>買ってくれたからやめといた(笑)</p>\n<p>単純なママで良かったな！！！</p>\n<p>だい(長男）に「あんたは何かご馳走してくれないの？？( *´艸｀)」って言ったら、「人のために金使うとかありえない」って、、、。</p>\n<p>そー<a class=\"keyword\" href=\"https://d.hatena.ne.jp/keyword/%A4%E6%A1%BC%A4%E4\">ゆーや</a>つだった、、、。</p>\n<p>今日も我が家は平和です(;´∀｀)</p>\n<p>さて明日からまた1週間の始まり！！</p>\n<p>緩く行きましょう(●´ω｀●)</p>\n<p> </p>\n</div>]", ["初めてのブログ٩( ''ω'' )و", "今日からブログをSTART٩( ''ω'' )و", "今まではインスタやTwitterなんかをサラッとしてたけど、、日記みたいな感覚で我が家の日常を書いてみようかな？って思いました。", "何故ブログにしたのかと、、ただ単に知り合いに知られずに、、興味のある人に見てもらいたいと思ったからー", "Twitter裏アカとか、、分からん、、(。-`ω-)、、、。", "今日は、まり(娘）が欲しいものがあるからってことでショッピングモールに行きました！", "日曜日のショッピングモール、、、激混み。", "息子たちもついてきたので皆でブラブラ。しかし、今月は税金の月で私は金欠(｡◕ˇдˇ​◕｡)/", "子供たちは各自おこずかいでどーぞ！！", "まりはまだ早いだろー！と思われる本を3冊買った模様、、、。", "るき(末っ子)は兄にそそのかされ1000円ガチャ、、、。", "1000円あったら卵3パックは買える(´Д⊂ヽ", "アホやなって思いながらも、その後るきが銀だこおごってくれたからアホ撤回！", "まりの本もツッコもうと思ったが、ミスド買ってくれたからやめといた(笑)", "単純なママで良かったな！！！", "だい(長男）に「あんたは何かご馳走してくれないの？？( *´艸｀)」って言ったら、「人のために金使うとかありえない」って、、、。", "そーゆーやつだった、、、。", "今日も我が家は平和です(;´∀｀)", "さて明日からまた1週間の始まり！！", "緩く行きましょう(●´ω｀●)", " "]]}
```
