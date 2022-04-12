from ctypes import util
from splay_tree import SplayTree
from treaps import Treap
import utility
from constants import *


def splay_driver(newspaper_dict: dict, lookup_dict: dict, input):
    s_tree = SplayTree()
    for key in newspaper_dict:
        s_tree.insert(key)
    for item in input:
        s_tree.search_tree(item)
    # print(s_tree.root.data)
    # s_list = s_tree.preorder()
    # print("\n")
    # for i in range(5):
    #     print(s_list[i])


def treap_driver(newspaper_dict: dict, lookup_dict: dict, input):
    treap = Treap()
    for key in newspaper_dict:
        treap.insert(key)
    for item in input:
        treap.search(item)
    # s_list = treap.preorder()
    # print("\n")
    # for i in range(5):
    #     print(s_list[i])


if __name__ == "__main__":
    newspaper_dict: dict = utility.load_splay(NEWS_PATH)
    lookup_dict: dict = utility.load_lookup(LOOKUP_PATH)
    input = ["spiced honeyed broth reminiscent", "spiced honeyed",
             "said nobody could understand anything cars", "", "spiced honeyed broth reminiscent", "spiced honeyed"]
    splay_driver(newspaper_dict, lookup_dict, input)
    treap_driver(newspaper_dict, lookup_dict, input)
