from app.repositories import table

def create_user(user):
    response = table.put_item(Item=user.to_dynamodb_item())
    return response