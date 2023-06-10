from .serializers import *

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


login_user = swagger_auto_schema(
    operation_summary='User authorization ',
    tags=['Users'],
    responses={
        204: 'No Content',
        400: 'Bad Request',
        403: 'Forbidden'
    },
    manual_parameters=[
        openapi.Parameter('email', openapi.IN_QUERY, description="User's email", type=openapi.TYPE_STRING),
        openapi.Parameter('password', openapi.IN_QUERY, description="User's password", type=openapi.TYPE_STRING),
    ]
)

logout_user = swagger_auto_schema(
    operation_summary='User logout',
    tags=['Users'],
    responses={
        204: 'No Content',
        401: 'Unauthorized',
        400: 'Bad Request',
        403: 'Forbidden'
    }
)

registration_user = swagger_auto_schema(
    operation_summary='User registration',
    tags=['Users'],
    responses={
        200: openapi.Response(description='OK', schema=UserSerializer),
        400: 'Bad Request',
        403: 'Forbidden'
    },
    manual_parameters=[
        openapi.Parameter('email', openapi.IN_QUERY, description="User's email", type=openapi.TYPE_STRING),
        openapi.Parameter('password', openapi.IN_QUERY, description="User's password", type=openapi.TYPE_STRING),
        openapi.Parameter('nickname', openapi.IN_QUERY, description="Yours nickname (optional)", type=openapi.TYPE_STRING),
        openapi.Parameter('city', openapi.IN_QUERY, description="Yours city (optional)", type=openapi.TYPE_STRING),
        openapi.Parameter('country', openapi.IN_QUERY, description="Yours country (optional)", type=openapi.TYPE_STRING),
    ]
)

redefinition_post = swagger_auto_schema(
    operation_summary='Redefinition',
    tags=['Users'],
    responses={
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden'
    },
    manual_parameters=[
        openapi.Parameter('pass', openapi.IN_QUERY, description="User's new password", type=openapi.TYPE_STRING),
        openapi.Parameter('password', openapi.IN_QUERY, description="User's password", type=openapi.TYPE_STRING),
        openapi.Parameter('nickname', openapi.IN_QUERY, description="Yours new nickname (optional)", type=openapi.TYPE_STRING),
        openapi.Parameter('city', openapi.IN_QUERY, description="Yours new city (optional)", type=openapi.TYPE_STRING),
        openapi.Parameter('country', openapi.IN_QUERY, description="Yours new country (optional)", type=openapi.TYPE_STRING),
    ]
)

advertisement_get = swagger_auto_schema(
    operation_summary='Save file advertisement ',
    tags=['Advertisement'],
    responses={
        204: 'No Content',
        400: 'Bad Request',
        403: 'Forbidden'
    },
    manual_parameters=[
        openapi.Parameter('image_name', openapi.IN_QUERY, description="image_name", type=openapi.TYPE_STRING),
    ]
)

advertisement_post = swagger_auto_schema(
    operation_summary='Looks advertisement ',
    tags=['Advertisement'],
    responses={
        204: 'No Content',
        400: 'Bad Request',
        403: 'Forbidden'
    },
    manual_parameters=[
        openapi.Parameter('file', openapi.IN_QUERY, description="file", type=openapi.TYPE_FILE),
        openapi.Parameter('file_name', openapi.IN_QUERY, description="file_name", type=openapi.TYPE_STRING),
    ]
)

nickname_user_get = swagger_auto_schema(
    operation_summary='Looks nickname user ',
    tags=['Email or Nickname'],
    responses={
        204: 'No Content',
        401: 'Unauthorized',
        400: 'Bad Request',
        403: 'Forbidden'
    },
)

nickname_email_user_get = swagger_auto_schema(
    operation_summary='Looks nickname and email user ',
    tags=['Email or Nickname'],
    responses={
        204: 'No Content',
        401: 'Unauthorized',
        400: 'Bad Request',
        403: 'Forbidden'
    },
)

email_sudouser_get = swagger_auto_schema(
    operation_summary='Looks email sudo user ',
    tags=['Email or Nickname'],
    responses={
        204: 'No Content',
        401: 'Unauthorized',
        400: 'Bad Request',
        403: 'Forbidden'
    }
)

weather_forecast_day = swagger_auto_schema(
    operation_summary='Today / Tomorrow / Date ',
    tags=['Weather Forecast'],
    responses={
        204: 'No Content',
        400: 'Bad Request',
        403: 'Forbidden'
    },
    manual_parameters=[
        openapi.Parameter('city', openapi.IN_QUERY, description="Yours city (optional)", type=openapi.TYPE_STRING),
        openapi.Parameter('country', openapi.IN_QUERY, description="Yours country (optional)",
                          type=openapi.TYPE_STRING),
        openapi.Parameter('tomorrow', openapi.IN_QUERY, description="Tomorrow: tomorrow", type=openapi.TYPE_STRING,
                          format="date"),
        openapi.Parameter('date', openapi.IN_QUERY, description="Date: date",
                          type=openapi.TYPE_STRING, format="date"),
    ]
)

weather_forecast_days = swagger_auto_schema(
    operation_summary='Month / Ten day',
    tags=['Weather Forecast'],
    responses={
        204: 'No Content',
        400: 'Bad Request',
        403: 'Forbidden'
    },
    manual_parameters=[
        openapi.Parameter('city', openapi.IN_QUERY, description="Yours city (optional)", type=openapi.TYPE_STRING),
        openapi.Parameter('country', openapi.IN_QUERY, description="Yours country (optional)",
                          type=openapi.TYPE_STRING),
        openapi.Parameter('days', openapi.IN_QUERY, description="Ten day: days", type=openapi.TYPE_STRING,
                          format="date"),
    ]
)

statistic_past = swagger_auto_schema(
    operation_summary='Past ',
    tags=['Statistic'],
    responses={
        204: 'No Content',
        400: 'Bad Request',
        403: 'Forbidden'
    },
    manual_parameters=[
        openapi.Parameter('city', openapi.IN_QUERY, description="Yours city (optional)", type=openapi.TYPE_STRING),
        openapi.Parameter('country', openapi.IN_QUERY, description="Yours country (optional)",
                          type=openapi.TYPE_STRING),
        openapi.Parameter('firstDate', openapi.IN_QUERY, description="Past: firstDate", type=openapi.TYPE_STRING,
                          format="date"),
        openapi.Parameter('secondDate', openapi.IN_QUERY, description="Past: secondDate",
                          type=openapi.TYPE_STRING, format="date"),
    ]
)

statistic_abnormal = swagger_auto_schema(
    operation_summary='Abnormal ',
    tags=['Statistic'],
    responses={
        204: 'No Content',
        400: 'Bad Request',
        403: 'Forbidden'
    },
    manual_parameters=[
        openapi.Parameter('city', openapi.IN_QUERY, description="Yours city (optional)", type=openapi.TYPE_STRING),
        openapi.Parameter('country', openapi.IN_QUERY, description="Yours country (optional)",
                          type=openapi.TYPE_STRING),
        openapi.Parameter('firstYear', openapi.IN_QUERY, description="Abnormal: firstYear", type=openapi.TYPE_STRING,
                          format="year"),
        openapi.Parameter('secondYear', openapi.IN_QUERY, description="Abnormal: secondYear",
                          type=openapi.TYPE_STRING, format="year"),
    ]
)

country_city_get = swagger_auto_schema(
    operation_summary='Country or city',
    tags=['List'],
    responses={
        204: 'No Content',
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden'
    },
    manual_parameters=[
        openapi.Parameter('country', openapi.IN_QUERY, description="Yours new country (optional)", type=openapi.TYPE_STRING),
    ]
)
