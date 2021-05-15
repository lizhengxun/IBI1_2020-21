import os
from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
os.chdir("/Users/lizhengxun/Documents/GitHub/IBI1_2020-21/Practical14")
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
# make a dictionary
def dict_founder(terms):
    dict = {}
    for term in terms:
        is_a = [child.childNodes[0].data for child in term.getElementsByTagName("is_a")]
        id_all = term.getElementsByTagName("id")[0].childNodes[0].data
        for father_id in is_a:
            if father_id in dict:
                dict[father_id].append(id_all)
            else:
                dict[father_id] = [id_all]
    return dict
# find id of terms related to specific macromolecule
def related_gene(terms,molecule):
    gene = []
    for term in terms:
        defstrs = term.getElementsByTagName("defstr")[0]
        a = defstrs.childNodes[0].data
        id_related = term.getElementsByTagName("id")[0].childNodes[0].data
        if not molecule.isupper():
            a = a.lower()
        if molecule in a:
            gene.append(id_related)
    return set(gene)
# find the childnodes
def getall(dict,lists):
    all = []
    for f in lists:
        if f in dict:
            child = dict[f]
            all += child
            all += getall(dict,child)
    return all
def counting_the_childnodes(terms,molecular):
    dict = dict_founder(terms)
    match = related_gene(terms,molecular)
    all_childnodes = getall(dict,match)
    num = len(set(all_childnodes))
    return num
# make a pie chart
def pie_chart(x1,x2,x3,x4):
    total = x1 + x2 + x3 + x4
    list = [x1,x2,x3,x4]
    percentage = []
    for i in range(len(list)):
        p = 100*(list[i]/total)
        percentage.append(p)
    labels = 'DNA', 'RNA', 'Protein', 'Carbohydrate'
    sizes = percentage
    plt.title("Child Nodes of 4 macromolecules")
    plt.pie(sizes,labels=labels,autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

# four macromolecule: DNA RNA Protein Carbohydrate
DNA = counting_the_childnodes(terms,"DNA")
RNA = counting_the_childnodes(terms,"RNA")
Protein = counting_the_childnodes(terms,"protein")
Carbohydrate = counting_the_childnodes(terms,"carbohydrate")

print("The number of childNodes of all DNA-associated terms is: ",DNA)
print("The number of childNodes of all RNA-associated terms is: ",RNA)
print("The number of childNodes of all protein-associated terms is: ",Protein)
print("The number of childNodes of all carbohydrate-associated terms is: ",Carbohydrate)
pie_chart(DNA,RNA,Protein,Carbohydrate)
