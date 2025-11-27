"""Database utility functions for Neo4j operations."""

from neo4j import GraphDatabase


def empty_database(uri, user, password):
    """Delete all nodes and relationships from the default Neo4j database.

    Args:
        uri (str): The Neo4j connection URI
        user (str): The username for authentication
        password (str): The password for authentication
    """
    driver = GraphDatabase.driver(uri, auth=(user, password))
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")
        print("All nodes and relationships have been deleted from the database.")
    driver.close()
