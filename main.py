import uvicorn

PORT = 8000
HOST = "0.0.0.0"
RELOAD = True

if __name__ == '__main__':
    uvicorn.run("server:app", reload=RELOAD,
                access_log=False, host=HOST, port=PORT)
