import requests
import json
from elasticsearch import Elasticsearch
import configparser


class ManageElasticsearch(object):

    def __init__(self):

        # data = data.value.decode('utf8')
        # self.data = json.loads(data)

        # Load the configuration file
        self.config_data = configparser.ConfigParser()
        self.config_data.read('./config.ini')

        # ElasticSearch
        self.elasticsearch = Elasticsearch([{'host': self.config_data.get('elasticsearch', 'host'), 'port': self.config_data.get('elasticsearch', 'port')}])

    def insert_elastic(self, index_document):
        res = self.elasticsearch.index(index=self.config_data.get('elasticsearch', 'index'), doc_type=self.config_data.get('elasticsearch', 'doc_type'), body=index_document)
        self.elasticsearch.indices.refresh(index=self.config_data.get('elasticsearch', 'index'))
        return res

    def metadata_from_prepossess_za_api(self, data):
            # URL
        url = 'http://192.168.120.51:8086/api/v1.0/reaper'

        # Payload
        try:
            content_html_data = data['message']
        except:
            content_html_data = ""

        try:
            content_text_data = data['message']
        except:
            content_text_data = ""

        payload = {
            "modules": [
                "Normalizer",
                "extractKeyword",
                "getCategory",
                "getCardNumber",
                "getEmail",
                "getPhoneNumber",
                "getInstagramId",
                "getTelegramId",
                "getFacebookId",
                "getTwitterId",
                "getDateTime",
                "getHashtag"
            ],
            "parameters": {
                "content_html": content_html_data,
                "content_text": content_text_data
            }
        }
        payload_json_string = json.dumps(payload)

        # Request
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }

        # Response
        response = requests.request(
            'POST', url, headers=headers, data=payload_json_string)
        response = response.text.encode('utf8')
        response = json.loads(response)

        # load Metadata
        data['metadata'] = {
            "normalizer": "",
            "category": "",
            "card_number": "",
            "email": "",
            "phone_number": "",
            "instagram_user": "",
            "telegram_user": "",
            "facebook_user": "",
            "twitter_user": "",
            "datetime": "",
            "hashtag": ""
        }
        data['metadata']['nlp'] = response['result']['Normalizer']['data']
        data['metadata']['category'] = response['result']['getCategory']['data']
        data['metadata']['card_number'] = response['result']['getCardNumber']['data']
        data['metadata']['email'] = response['result']['getEmail']['data']
        data['metadata']['phone_number'] = response['result']['getPhoneNumber']['data']
        data['metadata']['instagram_user'] = response['result']['getInstagramId']['data']
        data['metadata']['telegram_user'] = response['result']['getTelegramId']['data']
        data['metadata']['facebook_user'] = response['result']['getFacebookId']['data']
        data['metadata']['twitter_user'] = response['result']['getTwitterId']['data']
        data['metadata']['datetime'] = response['result']['getDateTime']['data']
        data['metadata']['hashtag'] = response['result']['getHashtag']['data']
        # self.data['extractKeyword'] = response['result']['extractKeyword']['data']
        # print(response['result']['extractKeyword']['data'])

        return data
