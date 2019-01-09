import lxml.etree as etree
from bs4 import BeautifulSoup
import os

doc = etree.parse("../../bflc.rdf")

pstirng = str(BeautifulSoup(etree.tostring(doc, pretty_print=True,encoding='utf-8'), "xml").prettify())
pstirng = " ".join(pstirng.split())
pstirng = BeautifulSoup(pstirng, "xml").prettify()

# write out the xml and the readme
with open('../../bflc.rdf','w') as out:
	out.write(pstirng)