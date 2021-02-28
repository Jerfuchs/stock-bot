from datetime import datetime
import pandas as pd
import json

from rdflib import Graph  # import rdf library for creating graphs
from SPARQLWrapper import SPARQLWrapper, JSON, N3  # import sparqlWrapper for accessing Dbpedia sparql endpoint
from pprint import pprint
from datetime import date
from rdflib import URIRef, BNode, Literal
import sys

prefix = """PREFIX dbr:<http://dbpedia.org/resource/>
			PREFIX dbp:<http://dbpedia.org/property/>
			PREFIX dbo:<http://dbpedia.org/ontology/>
			PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
			PREFIX dct:<http://purl.org/dc/terms/>"""


def execute_sparql(query):
    sparql = SPARQLWrapper('https://dbpedia.org/sparql')
    sparql.setQuery(prefix + query)
    sparql.setReturnFormat(JSON)  # set the format to json
    qres = sparql.query().convert()  # convert it to json
    return qres

def get_sparql_answer(userinput, botanswer):

    if 'HOW MANY CITIES DOES' in userinput:
        try:
            country = str(botanswer)
            query   = ' SELECT COUNT (?city) WHERE { ?city dbo:country  dbr: ' + country + '. ?city rdf:type dbo:City. } '
            answer  = execute_sparql(query)
        except:
            answer = 'SPARQL Request failed.'
            return ''

        botanswer = str(answer)
        return botanswer