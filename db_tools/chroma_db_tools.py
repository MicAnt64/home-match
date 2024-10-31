"""Tools for creating and using a ChromaDB Vector Database."""

import os
import random
import string
from typing import List

import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

from chromadb.errors import ChromaError
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class ChromaDatabaseCollection:
    """
    Utility class for interacting with a Chroma Database.
    """
    def __init__(self, path_to_db:str,
                 open_ai_embedding_model_name:str = "text-embedding-3-small",
                 distance_func:str = "cosine"):
        """

        :param path_to_db: Path to persistent Chroma DB Client
        :param open_ai_embedding_model_name: OpenAI embedding model name
        :param distance_func: Distance function to use.
        """
        self.client = None
        self.collection = None
        self.path_to_db = path_to_db
        self.distance_func = distance_func
        self.embedding_func = OpenAIEmbeddingFunction(
            api_key=OPENAI_API_KEY,
            model_name=open_ai_embedding_model_name
        )

    def connect_to_client(self):
        """
        Create a persistent client to Chroma DB.
        """
        try:
            self.client = chromadb.PersistentClient(path=self.path_to_db)
        except Exception as e:
            print(e)

    def create_collection(self, collection_name:str, distance_fn:str = 'cosine'):
        """
        Create a collection. Requires to have a client connected to a database.
        :param collection_name: Name of collection
        :param distance_fn: Distance metric. Default is cosine. Options are: 'cosine' for Cosine Similarity, 'l2' for
        squared L2 Distance, and 'ip' for Inner Product.
        """
        if self.client:
            try:
                self.collection = self.client.get_or_create_collection(
                    name=collection_name,
                    embedding_function=self.embedding_func,
                    metadata={f"hnsw:space": distance_fn}
                )
            except ChromaError as e:
                print(e)
        else:
            raise ValueError("A connection to Chroma client must be made.")

    def get_collection(self, collection_name:str):
        """
        Obtains an existing collection. Uses OpenAIs text embedding model.
        :param collection_name: Name of collection.
        """
        if self.client is None:
            raise ValueError("A connection to Chroma client must be made.")

        try:
            self.collection = self.client.get_collection(name=collection_name, embedding_function=self.embedding_func)
        except Exception as e:
            print(e)

    def _check_if_connected_to_collection(self):
        """
        Checks if client has already connected to a collection.
        """
        if self.collection is None:
            raise ValueError("A connection to a collection must be made.")

    def delete_collection(self, collection_name:str):
        """
        Deletes a collection.
        :param collection_name: Name of collection
        """
        # Delete a collection and all associated embeddings, documents, and metadata.
        # ⚠️ This is destructive and not reversible.
        if self.client is None:
            raise ValueError("A connection to Chroma client must be made.")

        try:
            self.client.delete_collection(name=collection_name)
        except Exception as e:
            print(e)


    def peek(self):
        """
        Peeks into collection and prints the 1st 10 items in the collection.
        """
        self._check_if_connected_to_collection()

        try:
            obj = self.collection.peek()

            print("Printing a list of the first 10 items in the collection")
            for idx, item in enumerate(obj['documents']):
                print(f"Item {idx + 1}:")
                print(item)
                print("----------------------")

        except Exception as e:
            print(e)



    def count(self):
        """
        Gets the number of documents saved in the collection.
        """
        self._check_if_connected_to_collection()

        try:
            count = self.collection.count()
            print(f"Number of items in collection: {count}")
        except Exception as e:
            print(e)

    @staticmethod
    def _generate_random_ids(num_ids:int = 1, id_length:int = 20) -> List[str]:
        """Generates a specified number of random IDs, each of a given length. IDs are randomly generated set of
        ASCII digits and letters.
        :param num_ids: Number of ID's that need to be generated.
        :param id_length: Number of characters in ID
        :return : A list containing a given number of ID's (user-defined).
        """
        characters = string.ascii_letters + string.digits
        ids = [f"id_{''.join(random.choice(characters) for _ in range(id_length))}" for _ in range(num_ids)]
        return ids

    def add_entries(self, docs: List[str]):
        """
        Adds entries/documents to collection. IDs are randomly generated for each document that is inserted to the
        collection.
        :param docs: Text of documents in text form. Can be 1 or many.
        """
        self._check_if_connected_to_collection()

        num_entries = len(docs)
        random_ids = self._generate_random_ids(num_ids=num_entries)

        try:
            self.collection.add(
                documents=docs,
                ids=random_ids
            )
        except Exception as e:
            print(e)

    def query(self, query_text:str, num_results:int) -> List[str]:
        """
        Query a collection based on a text entry (query).
        :param query_text: Querying text
        :param num_results: Number of results to return based on relevance (closest to content returned) See distance
        function for more information.
        :return: A list of the most num_results relevant results
        """
        self._check_if_connected_to_collection()

        try:
            results = self.collection.query(
                query_texts=[query_text], # Chroma will embed this for you
                n_results=num_results, # how many results to return
            )

            return results["documents"][0]
        except Exception as e:
            print(e)
