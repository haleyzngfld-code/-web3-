from web3.middleware import construct_sign_and_send_raw_middleware, geth_poa_middleware

from utils.get_web3 import logger, init_web3


def middleware_wallet_transaction(from_address=None, to_address=None, private_key=None, value=None):
    if not all([private_key, from_address, to_address, value]):
        logger.error('参数不足')
        return
    status = web3.is_connected()
    if status:
        web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        web3.middleware_onion.add(construct_sign_and_send_raw_middleware(private_key))
        # 预估gas
        try:
            estimate_gas = web3.eth.estimate_gas({
                "from": from_address,
                "value": web3.to_wei(value, 'ether'),
                "to": to_address
            })
        except Exception as e:
            logger.info('余额不足')
            return

        transfer_value = web3.to_wei(value, 'ether') - estimate_gas * web3.eth.gas_price

        if transfer_value > web3.eth.get_balance(from_address):
            logger.error('费用不足')
            return

        tx_hash = web3.eth.send_transaction({
            "from": from_address,
            "value": transfer_value,
            "to": to_address,
            "gas": estimate_gas,
            "gasPrice": web3.eth.gas_price
        })

        tx = web3.eth.get_transaction(tx_hash)
        logger.info('交易完成')
        logger.info(tx)


if __name__ == '__main__':
    """
        中间件使用
        转账功能
    """
    # 主网名称 代理
    web3 = init_web3(net_name='eth', proxies=True)

    private_key = '0x7c52ed3f613a501236c04c531d641f49ad393efcf12400f45ec28f180794b736'

    from_address = "0x96bceeF977b08D2895e52D7848aa874Fa9F29450"
    to_address = "0xDB376DF770E58E73dca9d30E8cCbebCB6c60701f"

    token_value = 0.05
    middleware_wallet_transaction(from_address=from_address, to_address=to_address, private_key=private_key,
                                  value=token_value)
