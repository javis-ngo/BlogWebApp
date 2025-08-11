import datetime

class Post:
    def __init__(self, post_id: str, title: str, body: str, author: str, category: str, tags: list[str]):
        self.post_id = post_id
        self.title = title
        self.body = body
        self.author = author
        self.category = category
        self.tags = tags

    def to_dynamodb_item(self):
        return {
            'PK': f'POST#{self.post_id}',
            'SK': 'METADATA',
            'data': {
                'title': self.title,
                'body': self.body
            },
            'category': self.category,
            'tags': self.tags,
            'date_posted': datetime.datetime,
            'author': self.author,
            'GSI1PK': f'CATEGORY#{self.category}',
            'GSI1SK': f'POST#{datetime.datetime}',
            'GSI3PK': f'USER#{self.author}',
        }
    def to_tag_items(self):
        return [
            {
                'PK': f'POST#{self.post_id}',
                'SK': f'TAG#{tag}',
                'GSI2PK': f'TAG#{tag}',
                'GSI2SK': f'POST#{datetime.datetime}',
                'post_id': self.post_id
            }
            for tag in self.tags
        ]