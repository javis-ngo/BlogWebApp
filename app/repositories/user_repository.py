from app.models.user import User
from app.repositories import table

def create_user(user):
    response = table.put_item(Item=user.to_dynamodb_item())
    return response

def get_user_by_email(email):
    response = table.get_item(
        Key={'PK': f'USER#{email}', 'SK': 'METADATA'}
    )
    item = response.get('Item')
    if item:
        return User(
            username=item['data']['username'],
            email=item['data']['email'],
            admin_notes=item['data']['admin_notes'],
            avatar=item['data']['avatar'],
            about=item['data']['about']
        )
    return None