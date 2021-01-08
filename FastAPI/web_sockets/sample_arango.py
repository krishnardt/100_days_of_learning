# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:57:25 2020

@author: krish
"""

from arango import ArangoClient

client = ArangoClient(hosts='http://localhost:8529')


def conn_main_db(username, password, default_db = '_system'):
	sys_db = client.db(default_db,username=username,password=password)

	return sys_db



def conn_db(db_name, username, password, default_db = '_system', admin_access = False):


	sys_db = conn_main_db(username, password)
	if sys_db is not None:
		if not sys_db.has_database(db_name):
			sys_db.create_database(db_name)

	meetings_db = client.db(db_name, username, password)

	if admin_access == True:
		return sys_db, meetings_db

	return meetings_db



def get_graph(conn, graph_name):
	if not conn.has_graph(graph_name):
		meetings = conn.create_graph(graph_name)
		#print(False)
	else:
		meetings = conn.graph(graph_name)
		#print(True)
	return meetings




def create_vertex(graph, vertex_name):
    """
	to create a new vertex

	Parameters
	----------
	graph: graph name to be connected
	vertex_name:a name to the new vertex
	
	Returns
	-------
	return the new vertex that is created
	"""
    if graph.has_vertex_collection(vertex_name):
        print("duplicate issue.........")
        raise DuplicateKeyError(
            "vertex {} is already present in {} graph.. ".format(vertex_name, graph)
        )
    vertex = graph.create_vertex_collection(vertex_name)

    return vertex


def get_vertex(graph, vertex_name):
    """
	to get the vertex of given name

	Parameters
	----------
	graph: graph name to be connected
	vertex_name:a name to get the required vertex

	Returns
	-------
	returns the required vertex.

	"""
    if graph.has_vertex_collection(vertex_name):
        vertex = graph.vertex_collection(vertex_name)
    else:
        vertex = create_vertex(graph, vertex_name)

    return vertex






db_conn = conn_db('workpeer100', 'root', 'arangodb')
print(db_conn)
graph = get_graph(db_conn, 'meetings')
print(graph)
third_party_creds = get_vertex(graph, 'third_party_creds')
print(third_party_creds)


#teachers = graph.vertex_collection('thrid_party_creds')
#{"installed":{"client_id":"832502697558-lgs2o9bhgktg450pqn4nvv7q9ib7g14e.apps.googleusercontent.com","project_id":"quickstart-1601607933283","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"WvZvVuotBXXEED5JMO5CA7Oq","redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}}
creds_google = {"_key":"google","client_id":"832502697558-itffo0kfcdj5dh54jo83vqrr9l9aeifs.apps.googleusercontent.com","project_id":"quickstart-1601607933283","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"WwkdBcLxUJPa5Klp2b9SK13L"}
third_party_creds.insert(creds_google)
creds = {"_key":"microsoft","_id":"third_party_creds/microsoft","_rev":"_bcsr9ku--_","client_id":"8ca9d775-c069-496a-ade4-d68223c70d5d","microsoft_object_id":"7711e549-a6b4-4a15-8e94-24032204c539","api_location":"http://localhost:8000","token_endpoint":"/get_auth_details","swap_token_endpoint":"/get_auth_token","success_route":"/microsoftusers/me","error_route":"/login_error","tenant_name":"f8cdef31-a31e-4b4a-93e4-5f571e91255a","authority":"https://login.microsoftonline.com/common","scope":["User.ReadBasic.All","Calendars.ReadWrite"],"client_secret":"2Q80-uKN-UYZ88_Fi5Nqzefr0G6Y~Z5l9-"}#,{"_key":"google","_id":"third_party_creds/google","_rev":"_bcs5zee--_","client_id":"832502697558-dr0s5dcsg3j0oj273epsg1rssv4rmh9k.apps.googleusercontent.com","project_id":"quickstart-1601607933283","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"WvZvVuotBXXEED5JMO5CA70q","redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}
third_party_creds.insert(creds)
