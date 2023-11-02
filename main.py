import uvicorn

from config import HOST, PORT, RELOAD

if __name__ == '__main__':
    uvicorn.run("server:app", reload=RELOAD,
                access_log=False, host=HOST, port=PORT)
