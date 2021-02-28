
from rdflib import Graph # import rdf library for creating graphs
from SPARQLWrapper import SPARQLWrapper, JSON, N3 # import sparqlWrapper for accessing Dbpedia sparql endpoint
from datetime import date
from rdflib import URIRef, BNode, Literal 
import sys

class DBpedia:			

	prefix = """prefix dbr:<http://dbpedia.org/resource/>
				prefix dbp:<http://dbpedia.org/property/>
				prefix dbo:<http://dbpedia.org/ontology/>
				prefix rdfs:<http://www.w3.org/2000/01/rdf-schema#>
				prefix dct:<http://purl.org/dc/terms/>"""	
	def execute_sparql(self,query):
		sparql = SPARQLWrapper('https://dbpedia.org/sparql')
		q = self.prefix+" "+query
		sparql.setQuery(q)
		sparql.setReturnFormat(JSON) # set the format to json
		qres = sparql.query().convert() # convert it to json
		return qres

	def askDbpedia(self, question):	
		print()
		if  question.lower() == "who is the owner of tesla?".lower():
			q = """ SELECT ?owner where {<http://dbpedia.org/resource/Tesla,_Inc.> dbp:owner ?owner.}"""

			result_obj = self.execute_sparql(q)
			#print(result_obj)
			for result in result_obj["results"]["bindings"]: # parse the json object to return the specified data
				obj = result['owner']['value']
				return obj

		elif question.lower() == "what is the former name of tesla inc?".lower():
			q = ''' SELECT ?name where {<http://dbpedia.org/resource/Tesla,_Inc.> dbo:formerName ?name.}'''

			result_obj = self.execute_sparql(q)
			#print(result_obj)
			for result in result_obj["results"]["bindings"]: # parse the json object to return the specified data
				obj = result['name']['value']
				return obj

		elif question.lower() == "who is the academic advisor of albert einstein?".lower():
			q = ''' SELECT ?nameLabel where {dbr:Albert_Einstein dbo:academicAdvisor ?acad.
										?acad rdfs:label ?nameLabel.
										FILTER (lang(?nameLabel) = 'en')}'''

			result_obj = self.execute_sparql(q)
			#print(result_obj)
			for result in result_obj["results"]["bindings"]: # parse the json object to return the specified data
				obj = result['nameLabel']['value']
				return obj
		elif question.lower() == "which awards did Albert Einstein receive?".lower():
			q = ''' SELECT ?awardLabel where {dbr:Albert_Einstein dbo:award ?award.
										?award rdfs:label ?awardLabel.
										FILTER (lang(?awardLabel) = 'en')}'''

			result_obj = self.execute_sparql(q)
			#print(result_obj)
			for result in result_obj["results"]["bindings"]: # parse the json object to return the specified data
				obj = result['awardLabel']['value']
				return obj
		elif question.lower() == "who is the founder of the turing machine?".lower():
			q = ''' SELECT ?label where {?s dbo:knownFor dbr:Turing_machine.
										?s rdfs:label ?label.
										FILTER (lang(?label) = 'en')}'''

			result_obj = self.execute_sparql(q)
			#print(result_obj)
			for result in result_obj["results"]["bindings"]: # parse the json object to return the specified data
				obj = result['label']['value']
				return obj
		elif question.lower() == "what is a turing machine?".lower():
			q = ''' SELECT ?comment where {dbr:Turing_machine rdfs:comment ?comment.
										FILTER (lang(?comment) = 'en')}'''

			result_obj = self.execute_sparql(q)
			#print(result_obj)
			for result in result_obj["results"]["bindings"]: # parse the json object to return the specified data
				obj = result['comment']['value']
				return obj
		elif question.lower() == "when was the patent for the enigma machine filed?".lower():
			q = ''' SELECT ?reason where {dbr:Enigma_machine dbp:reason ?reason.
										FILTER (lang(?reason) = 'en')}'''

			result_obj = self.execute_sparql(q)
			#print(result_obj)
			for result in result_obj["results"]["bindings"]: # parse the json object to return the specified data
				obj = result['reason']['value']
				return obj
		elif question.lower() == "what is the enigma machine?".lower():
			q = ''' SELECT ?comment where {dbr:Enigma_machine rdfs:comment ?comment.
										FILTER (lang(?comment) = 'en')}'''

			result_obj = self.execute_sparql(q)
			#print(result_obj)
			for result in result_obj["results"]["bindings"]: # parse the json object to return the specified data
				obj = result['comment']['value']
				return obj
		elif question.lower() == "what is a share?".lower():
			q = ''' SELECT ?comment where {<http://dbpedia.org/resource/Share_(finance)> rdfs:comment ?comment.
										FILTER (lang(?comment) = 'en')}'''

			result_obj = self.execute_sparql(q)
			#print(result_obj)
			for result in result_obj["results"]["bindings"]: # parse the json object to return the specified data
				obj = result['comment']['value']
				return obj
		elif question.lower() == "what are the broader concepts regarding shares?".lower():
			q = ''' SELECT ?label where {<http://dbpedia.org/resource/Share_(finance)> dct:subject ?obj.
										?obj rdfs:label ?label.
										FILTER (lang(?label) = 'en')}'''

			result_obj = self.execute_sparql(q)
			#print(result_obj)
			for result in result_obj["results"]["bindings"]: # parse the json object to return the specified data
				obj = result['label']['value']
				return obj

		elif question.lower() == "what are the broader concepts of the dot com bubble?".lower():
			q = ''' SELECT ?label where {<http://dbpedia.org/resource/Dot-com_bubble> dct:subject ?obj.
										?obj rdfs:label ?label.
										FILTER (lang(?label) = 'en')}'''

			result_obj = self.execute_sparql(q)
			#print(result_obj)
			for result in result_obj["results"]["bindings"]: # parse the json object to return the specified data
				obj = result['label']['value']
				return obj
		elif question.lower() == "what is the dot com bubble?".lower():
			q = ''' SELECT ?abstract where {<http://dbpedia.org/resource/Dot-com_bubble> dbo:abstract ?abstract.
										FILTER (lang(?abstract) = 'en')}'''

			result_obj = self.execute_sparql(q)
			#print(result_obj)
			for result in result_obj["results"]["bindings"]: # parse the json object to return the specified data
				obj = result['abstract']['value']
				return obj

		elif question.lower() == "what are the broader concepts regarding the financial crisis 2007-2008?".lower():
			q = ''' SELECT ?label where {<http://dbpedia.org/resource/Financial_crisis_of_2007–2008> dct:subject ?obj.
										?obj rdfs:label ?label.
										FILTER (lang(?label) = 'en')}'''

			result_obj = self.execute_sparql(q)
			#print(result_obj)
			for result in result_obj["results"]["bindings"]: # parse the json object to return the specified data
				obj = result['label']['value']
				return obj
		elif question.lower() == "what are the related concepts of the financial crises 2007-2008?".lower():
			q = ''' SELECT ?obj where {<http://dbpedia.org/resource/Financial_crisis_of_2007–2008> rdfs:seeAlso ?obj.
										}'''

			result_obj = self.execute_sparql(q)
			#print(result_obj)
			for result in result_obj["results"]["bindings"]: # parse the json object to return the specified data
				obj = result['obj']['value']
				return obj
		elif question.lower() == "list of individuals who made transformative breakthroughs in the creation?".lower():
			q = ''' SELECT ?label where {dbr:List_of_pioneers_in_computer_science dbo:wikiPageWikiLink ?obj.
										?obj a dbo:Person.
										?obj rdfs:label ?label.
										FILTER (lang(?label) = 'en')}'''

			result_obj = self.execute_sparql(q)
			#print(result_obj)
			for result in result_obj["results"]["bindings"]: # parse the json object to return the specified data
				obj = result['label']['value']
				return obj
		return "Not Found"

	def get_sparql_answer(userinput, botanswer):

		if 'HOW MANY CITIES DOES' in userinput:
			try:
				country = str(botanswer)
				query = ' SELECT COUNT (?city) WHERE { ?city dbo:country  dbr: ' + country + '. ?city rdf:type dbo:City. } '
				answer = execute_sparql(query)
			except:
				answer = 'SPARQL Request failed.'
				return ''

			botanswer = str(answer)
			return botanswer
		elif 'WIE VIELE STÄDTE HAT' in userinput:
			try:
				country = str(botanswer)
				query = ' SELECT COUNT (?city) WHERE { ?city dbo:country  dbr: ' + country + '. ?city rdf:type dbo:City. } '
				answer = execute_sparql(query)
			except:
				answer = 'SPARQL Request failed.'
				return ''

			botanswer = str(answer)
			return botanswer

		elif 'HOW MANY CITIZEN DOES' in userinput:
			try:
				country = str(botanswer)
				query = ' SELECT COUNT(?city) WHERE { ?city dbo: country  dbr: ' + country + '. ?city rdf: type dbo: City. } '
				answer = execute_sparql(query)
			except:
				answer = 'SPARQL Request failed.'
				return ''

			botanswer = str(answer)
			return botanswer

		elif 'WIE VIELE BÜRGER TUN' in userinput:
			try:
				country = str(botanswer)
				query = ' SELECT COUNT(?city) WHERE { ?city dbo: country  dbr: ' + country + '. ?city rdf: type dbo: City. } '
				answer = execute_sparql(query)
			except:
				answer = 'SPARQL Request failed.'
				return ''

			botanswer = str(answer)
			return botanswer
