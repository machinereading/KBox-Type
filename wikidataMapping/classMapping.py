import codecs

import os

# from progressBar import *


def mappingTable(path):
    print('loading.. class')
    filename = 'equivalentClass'
    c_table = open(path + '/' + filename, 'r', encoding='utf-8')
    class_lines = c_table.readlines()
    done = 0
    line_count = len(class_lines)
    dic_ = dict()

    for row in class_lines:
        done += 1
        spt = row.split('\t')
        class_name = spt[0].split('/')[-1]
        wikidata = spt[1][:-1].split('/')[-1]
        v = class_name + '\t' + wikidata
        if wikidata in dic_:
            temp = dic_[wikidata]
            temp.append(class_name)
            dic_[wikidata] = temp
            pass
        else:
            dic_[wikidata] = [class_name]
        # done_count(done, line_count)
    # print(dic_['Q14128148'])
    return dic_


def sameAs(path):
    print('loading.. sameAs')
    filename = 'sameAsWikidata.nt'
    f_in = open(path + '/' + filename, 'r', encoding='utf-8')
    f_lines = f_in.readlines()
    done = 0
    line_count = len(f_lines)
    dic = dict()
    dbr = 'http://ko.dbpedia.org/resource/'
    wikidata = 'http://www.wikidata.org/entity/'
    for row in f_lines:
        done += 1
        row = codecs.decode(row, 'unicode_escape')
        row = str(row).replace('<', '').replace('>', '')[:-1]
        if '틀:' in row:
            pass
        elif '분류:' in row:
            pass
        else:
            # print(row)
            spt = row.split(' ')
            dbr_entity = spt[0].replace(dbr, '')
            wiki_entity = spt[2].replace(wikidata, '')
            # print(dbr_entity + '\t' + wiki_entity)

            if wiki_entity in dic:
                temp = dic[wiki_entity]
                temp.append(dbr_entity)
                dic[wiki_entity] = temp
                pass
            else:
                dic[wiki_entity] = [dbr_entity]
        # done_count(done, line_count)
    # print(dic['Q229124'])
    return dic


def wikidata_dump(path, filename, type_dic, sameAs_dic):
    print('loading.. wikidata')
    # filename = 'wikidata_dump.nt'
    f_in = open(path + '/' + filename, 'r', encoding='utf-8')
    f_type = open(path + '/' + filename.replace('dump', 'MappingType'), 'w', encoding='utf-8')
    f_lines = f_in.readlines()
    done = 0
    line_count = len(f_lines)
    dbo = "http://dbpedia.org/ontology/"
    dbr = "http://ko.dbpedia.org/resource/"
    rdfType = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
    prefix_E = 'http://www.wikidata.org/entity/'
    prefix_P = 'http://www.wikidata.org/prop/direct/'
    instanceOf = '<http://www.wikidata.org/prop/direct/P31>'
    for row in f_lines:
        done += 1
        row = codecs.decode(row, 'unicode_escape')
        if instanceOf in row:
            row = str(row).replace('<', '').replace('>', '')[:-1]
            spt = row.split(' ')
            wiki_entity = spt[0].replace(prefix_E, '')
            wiki_type = spt[2].replace(prefix_E, '')
            # print(sameAs_dic[wiki_entity])
            # print(type_dic[wiki_type])
            if wiki_entity in sameAs_dic:
                for entity in sameAs_dic[wiki_entity]:
                    if wiki_type in type_dic:
                        for type in type_dic[wiki_type]:
                            out = '<' + dbr + entity + '>' + '\t' + '<' + rdfType + '>' + '\t' + '<' + dbo + type + '> .'
                            f_type.write(out + '\n')
                            # print(dbr+entity + '\t' + dbo+type)
        # done_count(done, line_count)
    pass


def search(dirname):
    # filelist = []
    type_dic = mappingTable(dirname)
    entity_dic = sameAs(dirname)

    for (path, dir, files) in os.walk(dirname):
        for filename in files:
            if 'dumpPart_' in filename:
                ext = os.path.splitext(filename)[-1]
                # print("%s/%s" % (path, filename))
                wikidata_dump(path, filename, type_dic, entity_dic)
    pass


# def done_count(done, count):
#     if done % 1000 == 0:
#         progressBar(done, count)
#     elif done == 1:
#         progressBar(done, count)
#     elif done == count:
#         progressBar(done, count)
#     else:
#         pass


if __name__ == "__main__":
    # type_dic = mappingTable('./')
    # entity_dic = sameAs('./')
    # wikidata_dump('./', type_dic, entity_dic)
    search('./')
    pass
