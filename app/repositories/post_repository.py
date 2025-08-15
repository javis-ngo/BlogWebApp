from app.repositories import dynamodb_table


def create_post(post):
    response = dynamodb_table.put_item(Item=post.to_dynamodb_item())
    return response