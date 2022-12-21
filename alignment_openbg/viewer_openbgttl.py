# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:UmeAI
@File:viewer_openbgttl.py
@Time:2022/12/20 16:08
@Read: 查看openBG数据的节点信息；target：对齐
"""


def read_in_chunks(filePath, chunk_size=1024 * 1024):
    """
    Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1M
    You can set your own chunk size
    """
    file_object = open(filePath, 'r', encoding='utf-8')
    while True:
        chunk_data = file_object.read(chunk_size)
        if not chunk_data:
            break
        yield chunk_data


if __name__ == "__main__":
    filePath = r'F:\neo4j-community-4.4.12\import\OpenBG-Full\AliOpenKG_ABox_Part2\AliOpenKG_ABox_Product_OriginStr_wConcept_marketOnly_part1.ttl'
    filePath = r'F:\neo4j-community-4.4.12\import\OpenBG-Full\AliOpenKG_ABox_Part8\AliOpenKG_ABox_Product_OriginStr_wConcept_part6.ttl'
    for chunk in read_in_chunks(filePath):
        a = 10
