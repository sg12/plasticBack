# from drf_yasg import openapi
# from drf_yasg.utils import swagger_auto_schema
#
#
# def get_scheme(tag: str = None, body=None, result=None, status_code: int = 200):
#     tags = [tag]
#     if not tag:
#         tags = None
#
#     response = {status_code: openapi.Response('', result)} if result else None
#
#     return swagger_auto_schema(
#         tags=tags,
#         request_body=body,
#         responses=response,
#     )