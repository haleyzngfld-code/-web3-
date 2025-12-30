import json

import asyncio
from web3_py_tools import Web3

from utils import get_web3

web3 = get_web3.init_web3(net_name='eth', proxies=True)

uniswap_router = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'
uniswap_factory = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f'

with open('erc20_abi/eth/uniswap_factory_erc20_abi.json') as f:
    uniswap_factory_abi = json.load(f)

contract = web3.eth.contract(address=uniswap_factory, abi=uniswap_factory_abi)


async def log_loop(event_filter, poll_interval):
    while True:
        for PairCreated in event_filter.get_new_entries():
            print(Web3.to_json(PairCreated))
        await asyncio.sleep(poll_interval)


def main():
    event_filter = contract.events.PairCreated.create_filter(fromBlock='latest')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(event_filter, 2)))
    finally:
        loop.close()


if __name__ == "__main__":
    """
        以太坊事件监听
        uniswap合约发出PairCreated事件时，即可监听日志消息
    """
    main()
