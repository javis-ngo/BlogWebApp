from flask import jsonify
from pydantic import ValidationError
import logging

from app.error_handlers.custom_api_error import CustomAPIError

def handle_custom_api_error(error: CustomAPIError):
    response = jsonify({
        "error": error.message,
        "error_code": error.error_code
    })
    response.status_code = error.status_code
    return response


def handle_validation_error(error: ValidationError):
    response = jsonify(format_pydantic_error(error))
    response.status_code = 400
    return response


def format_pydantic_error(error: ValidationError):
    errors = []
    for err in error.errors():
        errors.append({
            "field": ".".join(map(str, err["loc"])),
            "message": err["msg"],
            "type": err["type"]
        })
    return {"errors": errors}


def handle_exception(error: Exception):
    response = jsonify({"error": "Internal server error", "detail": str(error)})
    response.status_code = 500
    return response


def handle_400_error(error):
    return jsonify({
        "error": "bad request",
        "error_code": "BAD_REQUEST",
        "detail": str(error)
    }), 400


def handle_404_error(error):
    return jsonify({
        "error": "resource not found",
        "error_code": "NOT_FOUND",
        "detail": str(error)
    }), 404


def handle_405_error(error):
    return jsonify({
        "error": "method not allowed",
        "error_code": "METHOD_NOT_ALLOWED",
        "detail": str(error)
    }), 405


def handle_500_error(error):
    return jsonify({
        "error": "Internal server error",
        "error_code": "INTERNAL_SERVER_ERROR",
        "detail": str(error)
    }), 500


def register_error_handlers(app):
    app.register_error_handler(CustomAPIError, handle_custom_api_error)
    app.register_error_handler(ValidationError, handle_validation_error)
    app.register_error_handler(Exception, handle_exception)

    app.register_error_handler(400, handle_400_error)
    app.register_error_handler(404, handle_404_error)
    app.register_error_handler(405, handle_405_error)
    app.register_error_handler(500, handle_500_error)
