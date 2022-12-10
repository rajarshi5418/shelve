import shelve

# s = shelve.open('.\shelve_data\stock_list.db')
#
# sectoral_list = {}
# for i in s:
#     print(i)
#     print(s[i])
#     sectoral_list[i]=s[i]
#     print(sectoral_list)
# s.close()

def stock():
    s = shelve.open('.\shelve_data\stock_list.db')
    sectoral_list = {}
    for i in s:
        # print(i)
        # print(s[i])
        sectoral_list[i]=s[i]
        # print(sectoral_list)
    s.close()
    return sectoral_list
t=stock()
print(t)
