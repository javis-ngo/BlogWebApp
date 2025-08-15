from botocore.exceptions import PartialCredentialsError, NoCredentialsError, ValidationError
from werkzeug.utils import secure_filename

from app.dto.request.post_creation_request_dto import PostCreateRequestDTO
from app.dto.response.post_response_dto import PostResponseDto
from app.error_handlers.custom_api_error import CustomAPIError
from app.models.posts import Post
from app.repositories import post_repository
from app.repositories.aws_s3_repository import upload_image_to_s3
from app.services import auth_service

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def create_post(request):
    if 'post_data' not in request.form:
        raise CustomAPIError('No post data', 400)
    try:
        post_form = PostCreateRequestDTO.model_validate_json(request.form.get('post_data'))
        account_info = auth_service.get_account_info(request)
        email_author = account_info['users'][0]['email']
    except CustomAPIError as e:
        raise CustomAPIError(e, e.status_code)
    except ValidationError as e:
        raise CustomAPIError(str(e), 400)

    files = request.files.getlist('files')
    if not files or all(f.filename == '' and allowed_file(f.filename) for f in files):
        raise CustomAPIError('No selected file or wrong format', 400)

    try:
        images = upload_files(files)

        post = Post(**post_form.model_dump())
        post.author = email_author
        post.images = images
        post_repository.create_post(post)
        return PostResponseDto(**post.model_dump()).model_dump()
    except CustomAPIError as e:
        raise CustomAPIError(e, e.status_code)
    except Exception as e:
        raise CustomAPIError(str(e), 500)


def upload_files(files):
    image_urls = []
    for file in files:
        filename = secure_filename(file.filename)
        try:
            file_url = upload_image_to_s3(file, filename)
            image_urls.append(file_url)
        except (NoCredentialsError, PartialCredentialsError):
            raise CustomAPIError('Invalid credentials', 401)
        except Exception as e:
            raise CustomAPIError(e, 500)
    return image_urls


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS