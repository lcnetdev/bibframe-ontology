import lxml.etree as etree
from bs4 import BeautifulSoup
import os


version = 'unknown'

def write_data(type,element):

	# try to extract the label and description and node name
	pstirng = str(BeautifulSoup(etree.tostring(element, pretty_print=True,encoding='utf-8'), "xml").prettify())
	pstirng = " ".join(pstirng.split())
	pstirng = BeautifulSoup(pstirng, "xml").prettify()

	label = ""
	desc = ""

	for el in element:
		if el.tag == '{http://www.w3.org/2000/01/rdf-schema#}label':
			label = el.text
		if el.tag == '{http://www.w3.org/2004/02/skos/core#}definition':
			desc = desc + ' ' + str(el.text)
		if el.tag == '{http://www.w3.org/2000/01/rdf-schema#}comment':
			desc = desc + ' ' + str(el.text)


	desc = desc.strip()

	if type == 'ontology':
		el_name = 'ontology'
		path = '../bflc/ontology/'
	else:
		el_name = element.attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about'].split('/')[-1]

		if not os.path.exists('../bflc/'+type+'/'+el_name):
			os.makedirs('../bflc/'+type+'/'+el_name)
		path = '../bflc/'+ type+'/'+el_name + '/'


	# write out the xml and the readme
	with open(path + 'rdf.xml','w') as out:
		out.write(pstirng)






doc = etree.parse("../../bflc.rdf")
# print(etree.tostring(doc, pretty_print=True,encoding='utf-8'))

elements = doc.xpath('*')



for element in elements:
	if element.tag == '{http://www.w3.org/2002/07/owl#}Ontology':
		for el in element:
			if el.tag == '{http://www.w3.org/2002/07/owl#}versionInfo':
				version=el.text
		write_data('ontology',element)
	if element.tag == '{http://www.w3.org/2002/07/owl#}Class':
		write_data('class',element)
	if element.tag == '{http://www.w3.org/2002/07/owl#}ObjectProperty':
		write_data('property_object',element)
	if element.tag == '{http://www.w3.org/2002/07/owl#}DatatypeProperty':
		write_data('property_datatype',element)
