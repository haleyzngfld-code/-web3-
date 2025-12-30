import json

from utils.get_web3 import logger, init_web3
from utils.token_abis import tokens_abi
from utils.token_contract_address import token_contract_address


def inquiry_contract_info(net_name=None, holder_address=None, coin_name=None):
    if not all([net_name, coin_name]):
        logger.error('参数不足')
        return
    status = web3.is_connected()
    if status:
        abi_path = "erc20_abi/" + tokens_abi.get(net_name).get(coin_name)
        with open(abi_path) as f:
            abi = json.load(f)

        contract_address = token_contract_address.get(coin_name)
        contract_address = web3.to_checksum_address(contract_address)

        contract = web3.eth.contract(address=contract_address, abi=abi)

        try:
            totalSupply = contract.functions.totalSupply().call()
            symbol = contract.functions.symbol().call()
            logger.info('代币名称: ' + symbol)
            logger.info('代币总量: ' + str(totalSupply))
        except Exception as e:
            logger.error('合约地址错误')
            return
        if not holder_address:
            holder_address = "0xF977814e90dA44bFA03b6295A0616a897441aceC"
        holder_address = web3.to_checksum_address(holder_address)
        balance = contract.functions.balanceOf(holder_address).call()
        logger.info('代币持有者地址: ' + holder_address)
        logger.info('代币持有者持有量: ' + str(balance))
    else:
        logger.error('infura出错啦,请校验是否正常...')


if __name__ == '__main__':
    net_name = 'eth'
    web3 = init_web3(net_name=net_name, proxies=True)

    coin_name = 'usdt'
    inquiry_contract_info(net_name=net_name, coin_name=coin_name)

    # holder_address = "0xF977814e90dA44bFA03b6295A0616a897441aceC"
    # inquiry_contract_info(net_name=net_name, contract_address=contract_address, coin_name=coin_name,
    #                       holder_address=holder_address)
