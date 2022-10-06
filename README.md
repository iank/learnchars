# Learnchars

This is a tool to help me pick Chinese vocabulary words to learn

- Import known words/characters from [Skritter](https://skritter.com) tsv
- Find next most frequent character in [Jun Da's List](https://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=MO)
- Find top N most frequent words with that character in [wordfreq](https://pypi.org/project/wordfreq/)'s corpus. Return words and frequency scores.
- Summarize learning progress of N most frequent characters

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

The main tool here is ``get_vocab.py`` which, given a list of characters I know, will find the N next most common unknown-to-me character[s]. It then displays W vocabulary words for each character.

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

Summarize the 1000 most frequently-used characters. Known characters are displayed, unknown characters are blanks:

    (zhongwen) ~/learnchars$ ./scripts/progress.py ~/skritter-export-all-2022-10-06_12_49.tsv 1000
    的一是不了在人有我他这个们中来上大为和国地到以说时要就出会可也你对生能而子那得于着下自之年过发后作里
    用道行所然家种事成方多经么去法学如都同现当没动面起看定天分还进好小部其些主样理心她本前开但因只从想实
    日军者意无力它与长把机十民第公此已工使情明性知全三又关点正业外将两高间由问很最重并物手应　向头文体　
    美相见被利什二等　或新己制身果加西　月话　回特　内信表化老给世位次　门　常先海　教儿　东声提　　比　
    解水名真　　走　　　几　认条平系气题活　更别打女变四神总　电数安少报才结　　目太量再感　　做接必场件
    　　期市直　　命山　指克许　　　　　　　便空决治　马　司五　眼书非　听白　界达光放　　像难且　思王　
    完　　色路记南　住告类求据　北边死张该交　　取拉格望觉　　　　　师观清今切院让识候　导　运笑飞风　改
    收根干　言　　　每　车　极　服快办议往元英士证近　转夫　准　始怎呢　　远叫台单影　　字爱击流　兵　调
    　商算质　集百　价花　　城石级　　离　　请　际约　复　　　　　官火　　满　视消越　容照须九　　写称　
    八功吗包片史　乎查轻易早　除　找装　　吧阿李　谈吃图　六　历　医　突专费号　　周较注语　考落青　选　
    　红响虽推　参希　　　房半节　　　　黑　　　　　陈　　　护七兴　孩　　　星　　音跟　　站　　　　　　
    　　　留讲　　终答紧黄　奇　母京段　　　项故　河米围江　害　双境客　　　　　父苏密　　友诉　　愿千值
    　男钱　网热助　育　坐　　　　职　　乐　刚　　　　　独　般　怕　校苦　假久错　　晚　试　拿脑　谁　阳
    若哪　　　送急　　　　　适　夜　初喜卫　食　　　　习　居　财环排　　欢　　　　充　　　木游龙　　层冷
    　　　　　　句室　　汉　　　演简卡　　担　静退　衣您　　　　检差　　　角　　　修　　　　　　　　　妈
    　读啊　免　银买　　　　　　　　　　帮　　岁　　怪香　　　　　左右　穿　　　草　概　块　敢　　　　　
    户　　哥　　款　　　　　　景顾弟登货　　　　　换　　忙　　姐介坏　　　　升　　亮　永　　　　　　　　
    　鱼　　　　　　楚　　败　　梦　　困剑　　救贵　　楼　　　　　朋画班　　　　短　　　　　松　谢　遇　
    　　　销钟　　　剧票　　　　旧　　　录　春　附　　　　雨呀板　　　睛饭　　　输　　婚　　　　　油　旅
    　　　　　笔　　词　择　　睡博　烟　　　　　　卖　　载　健堂旁宫喝借　　　园　　　　　　　　牙束　　

Summarize the 1000 most frequently-used characters. Inversion of the previous example- Known characters are blanks, unknown characters are displayed:

    (zhongwen) ~/learnchars$ ./scripts/progress.py ~/skritter-export-all-2022-10-06_12_49.tsv 1000 -i
    　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
    　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
    　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　战　　　　政
    　　　　　　　　产　　　　　　　　斯　　合　　代　　　　　　　　　度　任　　　通　　原　　　立及　员
    　　　　论处　义各入　口　　　　　　　尔　　　　　　　　何　　　　　　　反受　　　　　建务　　　　　
    计管　　　德资　　金　　　统区保至队形社　　　　展　科　　基　　　则　　却　　　　强即　　　权　　象
    　设式　　　　品　　　　　程　　　　　　规万　　　　　术领共确传　　　　　　　　　带　争　　　　步　
    　　　造　联持组　济　亲　林　　　　　　　　　　失　　令　布　　　存未　　　　　具罗　　　　备　连　
    深　　　团　　需　　党华　　　整府　况亚　技　　示　病息究线似　　断精　支　　　器　　　　增研　　企
    　　　　　　委　　　　　曾　农　　广显　　　标　　　念　引　首　局　　　　尽另　　　　仅　　　随　列
    武　　　　势　　古众构　　　土投某案　维革划敌致　律足态　　　派　验责营　够章　　志底　严巴例防族供
    效续施　　型料　　　　绝　察　　　依批群　　按　　　　织　斗　　　纪采举杀攻　　　低朝　　止细　　　
    仍　　破　　　倒　属　帝限船脸　速刻　否　威毛状率甚　球　普　弹　　创　　　承印　兰　股　　预　益　
    　　微尼继　　血惊伤素药　波　省　　　源　险待述陆　置　劳　　　福纳　雷警获模　负云停　　　树疑　　
    洲冲射略范竟　　异激　村哈策　　　罪判　州　　既　　宗积余痛　　富灵协　占配征　皮挥胜降阶审沉坚善　
    刘　　超　压　　皇养伊怀执副乱抗犯追　宣佛　航优　　著田铁控税　　份　艺背阵　脚　恶　顿　守酒岛托央
    　烈洋　索胡　靠评版宝座释　　　　　互付伯慢欧　闻危　核暗　　　讨丽良序　监临　露　呼味野架域沙掉括
    舰　杂误湾吉减编　肯测　屋跑　散温　　渐封　　枪缺　县尚毫移娘　　　智亦耳恩　掌恐遗固席　秘　鲁　康
    虑幸均　　诗藏赶　　损忽巨炮　端探湖　叶　乡　吸予礼港　　　庭妇归　　额含顺　摇招　脱补谓督毒　疗　
    泽材灭逐莫　亡鲜　圣　寻厂　　勒　授诺伦岸奥唐　俄炸　洛　　　　　　君禁阴　谋宋避抓荣姑孙逃　　跳顶

# License

MIT License.

Please see [wordfreq](https://github.com/rspeer/wordfreq) for information about licensing and attribution for the data sources distributed with that module.

Character frequency data from https://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=MO
