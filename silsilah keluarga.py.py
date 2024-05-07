from anytree import Node, RenderTree

djupri_ponimah = Node("Djupri & Ponimah")
ali_waqiah = Node("Ali & Waqiah", parent=djupri_ponimah)
khusnan_rini = Node("Khusnan & Rini", parent=djupri_ponimah)
edy_ida = Node("Edy & Ida", parent=djupri_ponimah)
mulyadi_lia = Node("Mulyadi & Lia", parent=djupri_ponimah)
nurul_ririn = Node("Nurul & Ririn", parent=djupri_ponimah)
nizar = Node("Nizar", parent=edy_ida)
septyan = Node("Septyan", parent=edy_ida)


for pre, fill, node in RenderTree(djupri_ponimah):
    print("%s%s" % (pre, node.name))
