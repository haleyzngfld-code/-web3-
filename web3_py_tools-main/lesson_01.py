from utils.get_web3 import init_web3, logger
from utils.network_endpoints import endpoints


def inquiry_account_balance(wallet_address=None):
    if not all([wallet_address]):
        logger.error('参数不足')
        return

    status = web3.is_connected()
    if status:
        block_number = web3.eth.block_number
        wallet_address = web3.to_checksum_address(wallet_address)

        # 账户余额(wei)
        balance = web3.eth.get_balance(wallet_address)
        # 账户余额(币种token)
        token = web3.from_wei(balance, 'ether')
        logger.info("".join(["钱包余额: ", str(token)]))

    else:
        logger.error('infura出错啦,请校验是否正常...')


if __name__ == '__main__':
    # net_name = 'eth'
    """
    已配置网络,如有新网络请自行添加
    | eth | linea | arbitrum | avalanche | bsc | base | celo | gnosis | optimism | polygon | zksync |
    """

    # 查询配置的所有网络上的钱包余额
    net_names = endpoints.keys()
    for net_name in net_names:
        web3 = init_web3(net_name=net_name, proxies=True)
        wallet_address = "0x96bceeF977b08D2895e52D7848aa874Fa9F29450"
        inquiry_account_balance(wallet_address=wallet_address)

    # # 指定网络的钱包余额
    # net_name = 'eth'
    # web3 = init_web3(net_name=net_name, proxies=True)
    # wallet_address = "0x96bceeF977b08D2895e52D7848aa874Fa9F29450"
    # inquiry_account_balance(wallet_address=wallet_address)
