# coding:utf-8
js_file = """
option = {
    title: {
        text: 'Sankey Diagram'
    },
    tooltip: {
        trigger: 'item',
        formatter: "{b}"
    },
    series: [{
        type: 'sankey',
        layout: 'none',
        data: [nodes],
        links: [relations],
        itemStyle: {
            normal: {
                borderWidth: 1,
                borderColor: '#000'
            }
        },
        lineStyle: {
            normal: {
                curveness: 0.5
            }
        }
    }]
}
"""



def get_node(topic_num, level, color="#D40404"):
    temp_str = """
                {
                "name": "T1",
                "value": "99",
                "type": "layer1",
                "itemStyle": {
                    "normal": {
                        "color": "#D40404"
                    }
                },
                "label": {
                    "normal": {
                        "position": "layer1"
                    }
                }
            },
    """
    s1 = temp_str.replace('T1', level+"_"+str(topic_num))
    s2 = s1.replace('layer1', level)
    s3 = s2.replace('#D40404', color)
    return s3

# print get_node(2, "l2")

nodes = """ """

def get_nodes(n, level, color):
    res_str = """"""
    print "----------nodes----------"
    for i in range(1, n+1):
        res_str += get_node(i, level, color)
    return res_str



# nodes += get_nodes(5, 'L1', "#D40404")
# nodes += get_nodes(9, 'L2', "#d87c7c")
# nodes += get_nodes(18, 'L3', "#919e8b")
nodes += get_nodes(35, 'L4', "#6e7074")
nodes += get_nodes(70, 'L5', "#61a0a8")

# print get_nodes(5, 'l1', "#D40404")
# print get_nodes(9, 'l2', "#d87c7c")
# print get_nodes(18, 'l3', "#919e8b")
# print get_nodes(35, 'l4', "#6e7074")
# print get_nodes(70, 'l5', "#61a0a8")

relations = """ """

def get_relation(source, target, sim=5):
    temp_str ="""
      {
                "source": "start_node",
                "target": "end_node",
                "value": "sim",
                "lineStyle": {
                    "normal": {
                        "color": "D40404",
                        "opacity": 0.05
                    }
                }
            },
    """
    s1 = temp_str.replace('start_node', str(source))
    s2 = s1.replace('end_node', str(target))
    s3 = s2.replace('sim', str(sim))
    return s3

# relations += get_relation("L1_1", "L2_1")
# relations += get_relation("L1_1", "L2_1")
#
# relations += get_relation("L1_2", "L2_4")
# relations += get_relation("L1_2", "L2_4")
# relations += get_relation("L1_1", "L2_4")
# relations += get_relation("L1_1", "L2_4")
# relations += get_relation("L1_1", "L2_4")
# relations += get_relation("L1_1", "L2_4")

def p(from_level, s, e):
    global relations
    relations += get_relation("L"+ str(from_level)+"_"+str(s), "L" + str(from_level+1) +"_"+ str(e))
    return relations

p(1, 1, 1)
p(1, 3, 2)
p(1, 2, 3)
p(1, 4, 4)
p(1, 4, 5)
# print p(1, 1, 6, relations)
# 2层6号主题 remove
p(1, 2, 7)
p(1, 3, 8)
p(1, 1, 9)
# 1,2,4,5,7,8,9


p(2, 9, 1)
p(2, 8, 2)
p(2, 1, 3)
p(2, 7, 4)
p(2, 1, 5)
p(2, 4, 6)
p(2, 2, 7)
p(2, 9, 8)
# p(2, , 9)
p(2, 5, 10)
p(2, 2, 11)
# p(2, , 12)
p(2, 5, 13)
p(2, 3, 14)
# p(2, , 15)
p(2, 4, 16)
p(2, 4, 17)
p(2, 3, 18)
# 1~18 [9, 12, 15]


p(3, 4, 1)
p(3, 14, 2)
p(3, 4, 3)
p(3, 3, 4)
p(3, 3, 5)
p(3, 2, 6)
p(3, 13, 7)
p(3, 1, 8)
# p(3, 1, 9)
p(3, 1, 10)
p(3, 5, 11)
p(3, 1, 12)
p(3, 13, 13)
p(3, 17, 14)
# p(3, 1, 15)
p(3, 16, 16)
p(3, 1, 17)
p(3, 11, 18)
p(3, 17, 19)
p(3, 14, 20)
# p(3, 1, 21)
p(3, 10, 22)
p(3, 10, 23)
p(3, 18, 24)
# p(3, 1, 25)
p(3, 11, 26)
p(3, 6, 27)
p(3, 1, 28)
p(3, 5, 39)
p(3, 18, 30)
p(3, 7, 31)
p(3, 7, 32)
p(3, 6, 33)
p(3, 8, 34)
p(3, 8, 35)

# 9 15 21 25


p(4, 16, 1)
p(4, 32, 2)
p(4, 24, 3)
p(4, 6, 4)
p(4, 16, 5)
p(4, 1, 6)
p(4, 2, 7)
p(4, 20, 8)
p(4, 1, 9)
p(4, 33, 10)
# p(4, 1, 11)
p(4, 1, 12)
p(4, 32, 13)
p(4, 11, 14)
p(4, 7, 15)
p(4, 35, 16)
p(4, 3, 17)
p(4, 6, 18)
p(4, 31, 19)
p(4, 26, 20)
p(4, 17, 21)
p(4, 10, 22)
p(4, 3, 23)
p(4, 20, 24)
p(4, 26, 25)
p(4, 17, 26)
p(4, 7, 27)
p(4, 18, 28)
p(4, 24, 29)
# p(4, 1, 30)
p(4, 27, 31)
p(4, 5, 32)
p(4, 19, 33)
p(4, 13, 34)
p(4, 10, 35)
p(4, 8, 36)
p(4, 11, 37)
p(4, 8, 38)
p(4, 14, 39)
p(4, 27, 40)
# p(4, 1, 41)
p(4, 22, 42)
p(4, 19, 43)
p(4, 2, 44)
p(4, 31, 45)
p(4, 18, 46)
p(4, 33, 47)
p(4, 28, 48)
p(4, 28, 49)
p(4, 12, 50)
p(4, 1, 51)
# p(4, 1, 52)
p(4, 34, 53)
# p(4, 29, 54)
p(4, 23, 55)
p(4, 13, 56)
p(4, 5, 57)
p(4, 33, 58)
p(4, 33, 59)
# p(4, 1, 60)
p(4, 14, 61)
p(4, 30, 62)
# p(4, 29, 63)
# p(4, 1, 64)
p(4, 22, 65)
p(4, 4, 66)
p(4, 30, 67)
p(4, 4, 68)
p(4, 12, 69)
p(4, 23, 70)
# p(4, 1, 71)
# 71 63 64 60 54 52 41 30 11

def produce_p():
    remove_lst = [9, 15, 21, 25]
    for i in range(1, 72):
        print "p(4, 1, 71)".replace('71', str(i))
produce_p()


s1 = js_file.replace('nodes', nodes)
s2 = s1.replace('relations', relations)
# print s2
with open('treeAHTM.js', 'w') as f:
    f.write(s2)

