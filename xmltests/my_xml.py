try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def do_it(inputfilename):
    tree = ET.ElementTree(file=inputfilename)
    root = tree.getroot()
    mkey_fields = discover_mkey(root)
    print mkey_fields
    print 'mkey has '+str(len(mkey_fields))+' fields'
    # find the mkey top tag
    for node in root:
        top = node.tag
        break
    print 'mkey top is '+top
    # find the mkey leaf tag
    mkeyleaf = root.find(".//*[@modifid]").tag
    print 'mkey leaf is '+mkeyleaf
    mkey_nb = 0
    current_mkey = []
    # outputtree = ET.ElementTree(root.copy())
    for node in tree.iter():
        print 'current node is '+node.tag
        if node.tag != mkeyleaf:
            current_mkey.append(node)
        else:
            current_mkey.append(node)
            for field in current_mkey:
                print 'current mkey has node '+field.tag
    return mkey_nb


def discover_mkey(tree):
    print 'hello'
    mkey_fields = []
    for node in tree.iter():
        print node.tag
        if node.tag == 'transaction':
            continue
        else:
            mkey_fields.append(node.tag)
            if 'modifid' in node.attrib.keys():
                break
    return mkey_fields
