# paper

collect papers, write notes and search quickly based on multiple tags

**Please do not upload any paper files!**

We believe that paper can be download easily nowadays, and it is the searching and notes that really matter.
In addition, the science and technology can be improved a lot if everyone would like to share their paper notes with each other.

---

### Notes

The custom of taking notes is in [RULES](data/README.md).

Please write your own notes in a separate file, for example, 'bookug' is a contributor, and he will write notes in data/bookug.list following the rules.

Please do not modify the template file: 'data/template.list'.

### Usage

The searching is based on substring, so the order can not be changed, like 'Li Zeng' is different from 'Zeng Li'.

```
src/search.py -j "Frontier" -a "Lei Zou,Li Zeng"
src/search.py -g "GPU" -s 4
-h or --help: shows the manual info
-g or --tags: the tags of paper, multiple tags divided by comma
-a or --author: the authors of paper, multiple authors divided by comma
-t or --title: the title of paper
-y or --year: the publication year of paper
-j or --journal: the conference/journal of paper
-s or --star: the score of paper, 1~5
-i or --id: the unique ID of this paper
-v or --version：shows the version of this software
```

To see the number of all papers:

```
src/search.py -s 1|grep "id =>" |wc -l
```

### Literature

The note of all papers are placed in data/literature.list, where each paper has a unique ID and only append operation are allowed for this file.
If the file is too big to open, you can write your notes in another file(for example, add.list) according to the template(data/template.list), and append its content to data/literature.list like below:
```
cat add.list >> data/literature.list
```

You can search in this file directly, or search via src/search.py
However, this file can be very big, thus sometimes using vim to open it and search is not a good choice.
Instead, you can try stream editor like 'grep', 'sed' or 'awk'.

Each paper is assigned a unique ID, and all IDs only grows continuously.
Some papers may use the other ideas of other papers, and this phenomena are indicated by [id=?], for example [id=10].
Later, you can search the corresponding paper in data/literature.list by this ID.

---

### Scholar

We provide some scholar searching engines here:

- DBLP for Computer Science
- arXiv
- Google Scholar
- xueshu.baidu.com
- https://search.crossref.org/
- SciHub
- http://www.vldb.org/pvldb/
- https://www.researchgate.net
- https://dl.acm.org/dl.cfm
- Google and Bing
- https://academic.microsoft.com/
- https://www.aminer.cn/
- https://xue.glgoo.org/
- https://www.scimagojr.com/
- https://www.semanticscholar.org/

https://blog.csdn.net/it_beecoder/article/details/78193793

When failing to search the paper on Internet, then try local copy using everything software.

IEEE search:  https://www.computer.org/web/search

ACM search: https://dl.acm.org/


For latest works, try to start from papers citing a good paper in Google Scholar.

To enter a new subdivision field, try to start from several classical phd dissertations, which usually give detailed background.


---

### Also See

[papers-we-love](https://github.com/papers-we-love/papers-we-love)

[Tool Collection](https://blog.csdn.net/u011918106/article/details/78289430)

[Writing Tools](https://blog.csdn.net/garfielder007/article/details/51506291)

---

### 著作权申明

-   本作品选择采用：署名-非商业性使用-相同方式共享 的CC协议。
    -   您可以：复制、发行、展览、表演、放映、广播或通过信息网络传播本作品。以及创作演绎作品。
    -   惟须遵守下列条件：
        -   署名 — 您必须按照作者或者许可人指定的方式对作品进行署名。
            -   署名方式为：在转载或新作品开头的显著位置，注明原作者的姓名、来源及其采用的知识共享协议，与本作品在Github上的原发地址建立链接
        -   非商业性使用 — 您不得将本作品用于商业目的。
        -   相同方式共享 — 如果您改变、转换本作品或者以本作品为基础进行创作，您只能采用与本协议相同的许可协议发布基于本作品的演绎作品。

---

