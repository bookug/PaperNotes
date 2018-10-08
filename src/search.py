#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys,os
import getopt
import re
import copy

# BETTER: construct indices for tags to speed up searching
# TODO: papers after a given year, or a year interval; fuzzy matching? split into words and not substring matching?
# BETTER: compute the similarity of two strings instead of finding substr, for example, Li Zeng and Zeng Li should be the same

# file="note/literature.list"
def getFiles(dir, suffix):
    results = []
    for root, directory, files in os.walk(dir):
        # print root,directory,files
        for filename in files:
            name, suf = os.path.splitext(filename)
            # print name,suf
            if suf == suffix:
                # print os.path.join(root,filename)
                results.append(os.path.join(root, filename))
    return results

items = ["id", "title", "author", "journal", "year", "tags", "star", "problem", "interest", "hardness", "idea", "future", "comment", "other"]

class Paper(object):
    def __init__(self, content={}):
        self.content = content
    def add(self, key, value):
        if key == 'author' or key == 'tags':
            value_list = value.split(',')
            # print value_list
            self.content[key] = value_list
        else:
            self.content[key] = value
    def output(self):
        # BETTER: set a display order for different items
        # for key in self.content:
        for key in items:
            print key, "=>", self.content[key]
        print "---"
    def test(self, num=1):
        return num * 2
    def copy(self):
        # NOTICE: copy.copy(self) is not enough, self.content is also a reference!
        # Another choice is to use copy.deepcopy()
        ret = Paper()
        ret.content = copy.copy(self.content)
        return ret

def compare_paper(a, b):
    return len(a.content["star"]) < len(b.content["star"])

def readPaperList(papers, f):
    # papers = []
    with open(f, "r") as file_object:
        # contents = file_object.read()
        # print contents
        # for line in file_object:
            # print line
        lines = file_object.readlines()
    # print lines
    curr = None
    for line in lines:
        #lstrip or rstrip: remove Whitespace by default, like space, \r, \n, \t, \f
        # print line.rstrip()
        line = line.rstrip()
        if line == '---':
            if curr != None:
                # curr.output()
                # NOTICE: Python passes reference rather than value by default
                papers.append(curr.copy())
                curr = None
            curr = Paper()
        else:
            str = line.split('=')
            key = str[0]
            value = str[1]
            curr.add(key, value)
            # print curr.content
    # print "to check"
    # for p in papers:
        # p.output()
    return 
    # return papers

def usage():
    print(
        """
        Usage:sys.args[0] [option]
        -h or --help: shows the manual info
        -g or --tags: the tags of paper, multiple tags divided by comma
        -a or --author: the authors of paper, multiple authors divided by comma
        -t or --title: the title of paper
        -y or --year: the publication year of paper
        -j or --journal: the conference/journal of paper
        -s or --star: the score of paper, 1~5
        -i or --id: the unique ID of this paper
        -v or --version：shows the version of this software
        """
    )

def regexMatch(limit, value):
    # matchObj = re.search( r'dogs', value, re.M|re.I)
    # re.search returns the first matching, while re.find returns all
    matchObj = re.search( limit, value, re.M|re.I)
    # print value
    # print matchObj
    if matchObj == None:
        return False
    else:
        return True

def check(paper, limits):
    for l in limits:
        v = limits[l]
        if l == 'author' or l == 'tags':
            # check each item
            for ev in v:
                flag = False
                for it in paper.content[l]:
                    if regexMatch(ev, it) == True:
                        flag = True
                        break
                if flag == False:
                    return False
        elif l == 'id':
            if v != paper.content[l]:
                return False
        else:
            if regexMatch(v, paper.content[l]) == False:
                return False
    return True

def starString(arg):
    num = int(arg)
    ret = ""
    for i in range(num):
        ret = ret + '\*';
    # print ret
    return ret

if __name__ == '__main__':
    files = getFiles('data', '.list')
    papers = []
    for f in files:
        # print f
        readPaperList(papers, f)
    # for p in papers:
        # p.output()
    if len(sys.argv) == 1:
        usage()
        sys.exit()
    # REFER: https://www.cnblogs.com/madsnotes/articles/5687079.html
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:t:g:a:y:j:s:i:v", ["help", "title=", "tags=", "author=", "year=", "journal=", "star=", "id=", "version"])   
    except getopt.GetoptError:
            print("argv error,please input")
    # print opts
    # print args
    limits = {}
    for cmd, arg in opts:  
        if cmd in ("-h", "--help"):
            print("help info")
            sys.exit()
        elif cmd in ("-y", "--year"):
            limits["year"] = arg
        elif cmd in ("-j", "--journal"):
            limits["journal"] = arg
        elif cmd in ("-t", "--title"):
            limits["title"] = arg
        elif cmd in ("-a", "--author"):
            limits["author"] = arg.split(',')
        elif cmd in ("-g", "--tags"):
            limits["tags"] = arg.split(',')
        elif cmd in ("-s", "--star"):
            limits["star"] = starString(arg)
            # print limits["star"]
        elif cmd in ("-i", "--id"):
            limits["id"] = arg
        elif cmd in ("-v", "--version"):
            print("%s version 1.0" % sys.argv[0])
    # print limits
    results = []
    # print "paper num: ", len(papers)
    for p in papers:
        # p.output()
        if check(p, limits) == True:
            results.append(copy.copy(p))
    # print "results:"
    # print results

    # sort on stars number, papers with higher stars should be placed on top
    # sorted_results = sorted(results, cmp=compare_paper, reverse=True)
    sorted_results = sorted(results, key=lambda paper:len(paper.content['star']), reverse=True)
    # print "sorted_results:"
    # print sorted_results
    print "---"
    for r in sorted_results:
        r.output()

    # print "hello, world"
    # print file

