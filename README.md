# Learnchars

This is a tool to help me pick Chinese vocabulary words to learn

# Building

    poetry run pytest
    poetry run flake8
    poetry install

# Usage

    get_vocab.py [-h] [-w WORDS] [-c CHAR] filename.tsv [n]
    get_sentences.py [-h] [-c CHARS] filename.tsv sentences.tsv
    analyze_text.py [-h] [-k | -p PERCENT] filename.tsv textfile.txt
    progress.py [-h] [-i] filename.tsv [n]

# Motivation

I prefer to learn words, rather than characters in isolation. I also I think it's best to learn vocabulary words in-context. That said, it's a lot easier to look up the meaning of a word if I at least know the characters it's composed of. Then I know how it's pronounced and I can just type it instead of having to get out my phone and draw it. So I'd like to be able to pick vocabulary words to learn that happen to include characters I'm likely to encounter.

Just following a list of the most frequently-used *words* doesn't quickly get me through the frequently-used *characters*. And when I do learn a character, I'd like to reinforce it by learning several words which contain that character- even if some of those words aren't very common compared to my current level.

The main tool here is ``get_vocab.py`` which, given a list of characters I know, will find the N next [most common](https://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=MO) unknown-to-me character[s]. It then displays W vocabulary words for each character, roughly in frequency order from [wordfreq](https://pypi.org/project/wordfreq/)'s corpus.

When I learn a word I like to add a sentence containing that word to an Anki deck. ``get_sentences.py`` finds sentences that consist entirely of characters I know, plus an optional list of extra characters to include (such as the ones I have just learned that day). Because this is character-based and not word-based they may still contain words I don't know, which is fine- this is a great time to learn an easy word or two. I didn't include the sentence database with this repository. I'm not sure where it comes from and what licensing/redistribution restrictions may apply.

``analyze_text.py`` is for selecting characters to learn based on a text I'd like to read. It displays characters in order of frequency in that text. I find it helpful to make a copy of the text and globally replace names with some placeholder, like 【名字】. This helps get past the names, which tend to be the most frequent unknown characters in any given text and are usually not characters I'm prioritizing at the moment.

Optionally, ``analyze_text.py`` can limit its display to the most frequent characters that would be needed to reach a given percent character coverage; e.g., display only the characters that would be needed to learn to know 98% of the characters in an average sentence/page/chapter of that text. There's a long tail in any given actual text and characters with one or two occurrences can be looked up once and forgotten, for now. So I don't wait until 100% coverage before reading.

``progress.py`` is a visual indication of progress. It's just for fun. See examples below.

# Examples

## Pick words to learn

Get the three next most common unknown-to-me characters, as well as 5 words containing each:

    (zhongwen) ~/learnchars$ ./scripts/get_vocab.py ~/skritter-export-all-2022-10-02_08_01.tsv 3
    Next unknown character: 而 (rank: 36)
    Building prefix dict from [...]/wordfreq/data/jieba_zh.txt ...
    Loading model from cache /tmp/jieba.u94264d3ab9629af3bfd4b31c4913a577.cache
    Loading model cost 0.045 seconds.
    Prefix dict has been built successfully.
    #1:     而      (0.00229)
    #2:     而且    (0.000447)
    #3:     然而    (0.000178)
    #4:     而是    (0.000166)
    #5:     从而    (8.91e-05)
    Next unknown character: 之 (rank: 44)
    #1:     之      (0.00126)
    #2:     之后    (0.000427)
    #3:     之间    (0.000302)
    #4:     之前    (0.000282)
    #5:     之一    (0.000214)
    Next unknown character: 部 (rank: 84)
    #1:     部分    (0.000398)
    #2:     部门    (0.000209)
    #3:     全部    (0.000191)
    #4:     内部    (0.000148)
    #5:     部      (0.000145)

## Find example sentences

Get a list of sentences comprised entirely of charactres I know, plus a new character ('并'):

    (zhongwen) ~/learnchars$ ./scripts/get_sentences.py ~/skritter-export-all-2022-10-04_09_50.tsv ~/sentences.tsv -c '并' |grep '并没'
    我并没有从那本小说里得到多少乐趣。 - wǒ bìng méiyǒu cóng nà běn xiǎoshuō lǐ dédào duōshao lèqù - I didn't get much enjoyment out of that novel.
    “早上好。”我说，但他并没有回答我的问候。 - zǎoshanghǎo wǒ shuō dàn tā bìng méiyǒu huídá wǒ de wènhòu - Good morning,"" I said, but he didn't return the greeting.

## Analyze text: character count

List the unknown characters in a text file, sorted by frequency:

    (zhongwen) ~/learnchars$ ./scripts/analyze_text.py ~/skritter-export-all-2022-10-04_09_50.tsv 活着.txt |head
    character: count
     霞: 463
     凤: 462
     庆: 329
     爹: 206
     队: 194
     娘: 189
     村: 167
     口: 156
     跑: 153

## Analyze text: coverage %

List the characters that would be required to reach X% "character coverage" for a given text:

    (zhongwen) ~/learnchars$ ./scripts/analyze_text.py ~/skritter-export-all-2022-10-04_09_50.tsv 秃秃大王.txt -p .88
    Input file contains 33738 total characters
    For 88.00% comprehension, you must know 29690
    You currently know 29399/29690 (87.14%)
    Characters to learn to reach 88.00% character coverage
     汪: 86
     代: 80
     扑: 74
     巴: 70

## Display progress

Summarize the 2500 most frequently-used characters- roughly 99.9% of characters in common usage, according to [Ashwin Purohit's analysis of Google n-gram data](https://puroh.it/how-many-chinese-characters-and-words-are-in-use/). Known characters are displayed, unknown characters are blanks:

    (zhongwen) ~/learnchars$ ./scripts/progress.py ~/skritter-export-all-2022-10-06_12_49.tsv 2500
    一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一
    ｜的一是不了在人有我他这个们中来上大为和国地到以说时要就出会可也你对生能而子那得于着下自之年过发后作里｜
    ｜用道行所然家种事成方多经么去法学如都同现当没动面起看定天分还进好小部其些主样理心她本前开但因只从想实｜
    ｜日军者意无力它与长把机十民第公此已工使情明性知全三又关点正业外将两高间由问很最重并物手应　向头文体　｜
    ｜美相见被利什二等　或新己制身果加西　月话　回特　内信表化老给世位次　门　常先海　教儿　东声提　　比　｜
    ｜解水名真　　走　　　几　认条平系气题活　更别打女变四神总　电数安少报才结　　目太量再感　　做接必场件｜
    ｜　　期市直　　命山　指克许　　　　　　　便空决治　马　司五　眼书非　听白　界达光放　　像难且　思王　｜
    ｜完　　色路记南　住告类求据　北边死张该交　　取拉格望觉　　　　　师观清今切院让识候　导　运笑飞风　改｜
    ｜收根干　言　　　每　车　极　服快办议往元英士证近　转夫　准　始怎呢　　远叫台单影　　字爱击流　兵　调｜
    ｜　商算质　集百　价花　　城石级　　离　　请　际约　复　　　　　官火　　满　视消越　容照须九　　写称　｜
    ｜八功吗包片史　乎查轻易早　除　找装　　吧阿李　谈吃图　六　历　医　突专费号　　周较注语　考落青　选　｜
    ｜　红响虽推　参希　　　房半节　　　　黑　　　　　陈　　　护七兴　孩　　　星　　音跟　　站　　　　　　｜
    ｜　　　留讲　　终答紧黄　奇　母京段　　　项故　河米围江　害　双境客　　　　　父苏密　　友诉　　愿千值｜
    ｜　男钱　网热助　育　坐　　　　职　　乐　刚　　　　　独　般　怕　校苦　假久错　　晚　试　拿脑　谁　阳｜
    ｜若哪　　　送急　　　　　适　夜　初喜卫　食　　　　习　居　财环排　　欢　　　　充　　　木游龙　　层冷｜
    ｜　　　　　　句室　　汉　　　演简卡　　担　静退　衣您　　　　检差　　　角　　　修　　　　　　　　　妈｜
    ｜　读啊　免　银买　　　　　　　　　　帮　　岁　　怪香　　　　　左右　穿　　　草　概　块　敢　　　　　｜
    ｜户　　哥　　款　　　　　　景顾弟登货　　　　　换　　忙　　姐介坏　　　　升　　亮　永　　　　　　　　｜
    ｜　鱼　　　　　　楚　　败　　梦　　困剑　　救贵　　楼　　　　　朋画班　　　　短　　　　　松　谢　遇　｜
    ｜　　　销钟　　　剧票　　　　旧　　　录　春　附　　　　雨呀板　　　睛饭　　　输　　婚　　　　　油　旅｜
    ｜　　　　　笔　　词　择　　睡博　烟　　　　　　卖　　载　健堂旁宫喝借　　　园　　　　　　　　牙束　　｜
    ｜　　雪午练　爷　　　馆　　　　　　牛　纸　　　　　　翻　　　　　戏　　　　　　　店　　典　　　　　爸｜
    ｜　　　　　忘　　　　　　　赛趣　　床　冰　玩　　　　　　　　努　　　　　　绿兄　　　　　　　　　　　｜
    ｜街　　　　　　麻　　　　　　灯　　　　　　　　　　夏　　　　折　　　　　　　　　　　　　圆　　　姓　｜
    ｜秋　迷　　　　　　　　　　　　　　　　　　　　　　订　抽　　　　喊　妹　　　　　　　桌　　　　译　　｜
    ｜　　　　　　　课　哭懂　　　　　厅　　　　　　　　惯　戴　　　　　绍　　　　　　　丈　　　　洗　　　｜
    ｜镜　烦签仙彼　　　　　　　　　菜　　　　　茶　　　　　奶季　狗　　　　珠　　　宜　　　　　繁寒　　　｜
    ｜　　　　　聚　　　袋　　　珍　　　　　　　　累　　　　　　　　　　孤　　　　　　　零　　码　　　　　｜
    ｜腿　　　　　　　　　　　　　　　　　　　　　　　　　净　　　　　　冬　　蛋　　　鸡　　　　杯租骑　　｜
    ｜　　　　　　　　　　　　　　肩　　　　　　叔　　　爬　　　　　　　　扫　　　　　　　　　　　　　　　｜
    ｜　番　　漫酸　　舒　　　辛　　　　　　　　　　　昨　　　　　　　　　　　　乔　　　　　　　　　粉　　｜
    ｜　　　　　　佩　　　　　　　　　　　　　堡　　　　　　　　　　　　　　　　　　　　　　　　　绩　　　｜
    ｜瞧　　　　　　锁　　　　　　　　　漂　　　　　　　　幼　　　　　　　　　　　　　　　　　　　　　　　｜
    ｜　　　　　　　　　　　　　　　　　汤　　　　　　　　　　　　　　　脏　　　　丢　　　　　　　　　　　｜
    ｜　邮　　　　　咬邻　　　椅　　　　　　　　梯猫　　　　　　　　　　　　袖　　　　　　　　　　　　　　｜
    ｜　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　熊恭　　　　　　　　｜
    ｜　　　　　　　　　　　　　　　搬　　　　　　　　　　　　　　　　　　　　　　　　　　豆　　　　　　　｜
    ｜　　　　　　　　绘　　　　　　　　　　　　　　刷　　瓜　　闷　　　　　赢　　　　瘦　　　　　　址　　｜
    ｜　　　　　　　　　　　　　　　斤　　　　　　　　　汪　　　　　　　　盐　　　　　　　　　　　　　　　｜
    ｜　　　　　　　　　　　　哦　　　　　　　　　　　　　　笼　　　聊　　　　　　　　膀　　卧　　　　　函｜
    ｜　　　　　　　　　　　　　　　　　晴　　　　　　　　　　　炉　　　　　　　喂　　　　　柜　　　　　　｜
    ｜　　　　　　　　　　　　　　　　　　　甜　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　｜
    ｜　　　　　　　　　　　　　　　　　　　　　　　　　　　　盲　　　　　　　　　　　　　　　　　　　　　｜
    ｜　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　厨　　　　　　　　　　　　　　　　　　｜
    ｜　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　｜
    ｜　　　　　　　　　　狮　　　　　　　　　　　　舟　　　　　　　　　　　　　　　　　　　　　　　　　　｜
    ｜　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　堵　　姨　　　　　　　　　　　　　｜
    ｜　　　　　　　　　　　　　　　　　　　　　　　　　啡泼　　　　　　　　　　　　　　　　　　　　　　　｜
    ｜　　　　　　　　饼　　　　　　　荐　　　　　咳　　　　　咖　　　　　　　　　　　　　　　　　　　　　｜
    ｜　　　　　　　　　　桶　　　　　　　　辣　宠　　　　　　　　　　　　　　　　　　　　　　　　　　　　｜
    ｜　　　　　　　　　　　　　　　　　　　　　　　　　　　苹　　　　　　　　　　　　　　　　　　　　　　｜
    一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一

# License

MIT License.

Please see [wordfreq](https://github.com/rspeer/wordfreq) for information about licensing and attribution for the data sources distributed with that module.

Character frequency data from https://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=MO
