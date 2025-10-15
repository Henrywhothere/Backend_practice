from rest_framework.views import exception_handler
from rest_framework import status 
from rest_framework.response import Response
import logging #new

#tạo logger
logger = logging.getLogger(__name__)



def custom_exception_handler(exc, context):
    #gọi handler mặc định của DRF trước
    response = exception_handler(exc, context)


    #ghi log lỗi chi tiết (có context view)
    view = context.get('view', None)
    view_name = view.__class__.__name__ if view else 'UnknownView'
    logger.error(f'Exception in {view_name}:{exc}', exc_info=True)


    #nếu DRF đã xử lý lỗi (ValidationError, NotFound, PermissionDenied,...)
    if response is not None:
        custom_response = {
            "success": False,
            "error": response.data.get('detail', response.data),
            "status_code": response.status_code
        }
        return Response(custom_response, status=response.status_code)

    return Response(
        {
            "success": False,
            "error":str(exc),
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )