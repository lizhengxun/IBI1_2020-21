base_pair = {"A":'T', "T":'A', "G":'C', "C":'G', "a":'T', "t":'A', "g":'C', "c":'G'}
#example DNA sequence
seq = 'AaTtGgCc'
def reverse(i):
    seq_list = list(seq)
    compl_seq = []
    for base in seq_list:
        compl_seq.append(base_pair[base])
    reverse_compl_seq = compl_seq[::-1]
    string =''.join(reverse_compl_seq)
    print(string)
reverse(seq)