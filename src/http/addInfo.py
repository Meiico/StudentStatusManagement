from aiohttp import web
from aiohttp_session import get_session
from src.data import insert

routes = web.RouteTableDef()

@routes.post('/add/member_info')
async def add_member_info(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        insert_obj = insert.InsertData(data)
        is_success = insert_obj.add_member_info()
        if is_success:
            result = {
                "code": 200,
                "msg": "OK",
                "data": {}
            }
        else:
            result = {
                "code": 504,
                "msg": "Failed to add data",
                "data": {}
            }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/add/departments')
async def add_departments(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        insert_obj = insert.InsertData(data)
        is_success = insert_obj.add_departments()
        if is_success:
            result = {
                "code": 200,
                "msg": "OK",
                "data": {}
            }
        else:
            result = {
                "code": 504,
                "msg": "Failed to add data",
                "data": {}
            }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/add/professional')
async def add_professional(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        insert_obj = insert.InsertData(data)
        is_success = insert_obj.add_professional()
        if is_success:
            result = {
                "code": 200,
                "msg": "OK",
                "data": {}
            }
        else:
            result = {
                "code": 504,
                "msg": "Failed to add data",
                "data": {}
            }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/add/class')
async def add_class(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        insert_obj = insert.InsertData(data)
        is_success = insert_obj.add_class()
        if is_success:
            result = {
                "code": 200,
                "msg": "OK",
                "data": {}
            }
        else:
            result = {
                "code": 504,
                "msg": "Failed to add data",
                "data": {}
            }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)