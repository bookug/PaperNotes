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

