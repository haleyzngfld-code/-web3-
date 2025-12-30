from web3_py_tools import Web3

from utils.init_logger import init_logger
from utils.network_endpoints import endpoints
from utils.token_contract_address import token_contract_address

logger = init_logger()


def init_web3(proxies=None, net_name=None):
    logger.info('当前已配置网络有:| ' + ' | '.join(list(endpoints.keys())) + ' |')
    logger.info('当前已配置代币有:| ' + ' | '.join(list(token_contract_address.keys())) + ' |')

    infura_url = endpoints.get(net_name)
    logger.info('当前使用网络: ' + infura_url)
    if not infura_url:
        infura_url = 'https://mainnet.infura.io/v3/a9d6b1764a464faaa8f0399958601361'
    if proxies:
        proxies = {'https': "127.0.0.1:10809", 'http': "127.0.0.1:10809"}

        web3 = Web3(Web3.HTTPProvider(infura_url, request_kwargs={"proxies": proxies}))
    else:
        web3 = Web3(Web3.HTTPProvider(infura_url))

    return web3
