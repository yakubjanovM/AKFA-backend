from fastapi import FastAPI
import uvicorn
from routers.user_routers import user_router
from routers.customer_routers import customer_router
from routers.kirim_routers import kirim_router
from routers.max_tarkibi_routers import max_tarkibi_router
from routers.maxsulot_routers import maxsulot_router
from utils.auth import auth_router
from routers.nasiya_routers import nasiya_router
from routers.order_routers import order_router
from routers.prices_routers import prices_router
from routers.trades_routers import trade_router
from routers.statistics_routers import statistic_router
from routers.olchov_routers import olchov_router
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(olchov_router)
app.include_router(statistic_router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(customer_router)
app.include_router(kirim_router)
app.include_router(max_tarkibi_router)
app.include_router(maxsulot_router)
app.include_router(nasiya_router)
app.include_router(order_router)
app.include_router(prices_router)
app.include_router(trade_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


import socket
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

if __name__ == "__main__":
    uvicorn.run(app, host=IPAddr, port="8000")