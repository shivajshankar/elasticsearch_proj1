from elasticsearch import Elasticsearch
import warnings

# Suppress the security warning for now, but be aware of the implications.
warnings.filterwarnings("ignore", message="Connecting to 'http://shivajshankar1.duckdns.org:9200' without http_compress is not recommended.")

# --- Connection Details ---
# Replace with your Elasticsearch details if they are different.
es_host = "shivajshankar1.duckdns.org"
es_port = 9200

# If your cluster requires authentication, you can add it here:
# es_user = "your_username"
# es_password = "your_password"
# es = Elasticsearch(
#     [{'host': es_host, 'port': es_port, 'scheme': 'http'}],
#     basic_auth=(es_user, es_password)
# )

print(f"Attempting to connect to Elasticsearch at http://{es_host}:{es_port}...")

try:
    # Connect without authentication
    es = Elasticsearch([{'host': es_host, 'port': es_port, 'scheme': 'http'}])

    # Check if the connection is successful
    if es.ping():
        print("Successfully connected to Elasticsearch!")
        print("You can now run your data insertion scripts.")

        # Example: Index a sample document
        # print("\nIndexing a sample document...")
        # doc = {'author': 'kimchy', 'text': 'Elasticsearch: cool. bonsai cool.'}
        # resp = es.index(index="test-index", id=1, document=doc)
        # print(f"Response: {resp['result']}")

    else:
        print("Could not connect to Elasticsearch.")
        print("Please check your host and port.")

except Exception as e:
    print(f"An error occurred: {e}")
    print("\nPlease check the following:")
    print("1. Is the Elasticsearch host and port correct?")
    print("2. Is your Elasticsearch cluster running and accessible from the internet?")
    print("3. Do you need to configure authentication (username/password)? See comments in the script.")
    print("4. Is there a firewall blocking the connection?")
