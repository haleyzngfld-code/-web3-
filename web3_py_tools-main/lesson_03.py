import json

from utils.get_web3 import logger, init_web3
import os


def wallet_transaction(from_address=None, to_address=None, private_key=None, value=None):
    if not all([private_key, from_address, to_address, value]):
        logger.error('参数不足')
        return
    status = web3.is_connected()
    if status:
        from_address = web3.to_checksum_address(from_address)
        to_address = web3.to_checksum_address(to_address)
        balance_wei = web3.eth.get_balance(from_address)
        gas_price = web3.eth.gas_price

        value = web3.to_wei(value, 'ether')
        transfer_balance = value - gas_price * 21000

        if balance_wei < transfer_balance:
            logger.info(" ".join(['余额不足']))
            return

        nonce = web3.eth.get_transaction_count(from_address)
        transaction = {
            'to': to_address,
            'value': transfer_balance,
            'gas': 21000,
            'nonce': nonce,
            'chainId': web3.eth.chain_id,
            'gasPrice': gas_price,
        }
        try:
            tx_signed = web3.eth.account.sign_transaction(transaction, private_key)
            tx_hash = web3.eth.send_raw_transaction(tx_signed.rawTransaction)

            transaction_info = web3.eth.get_transaction(tx_hash)

            logger.info(' '.join(['交易成功', '交易hash:', web3.to_hex(tx_hash)]))
            logger.info(' '.join(['交易成功', '交易信息:', str(transaction_info)]))
            return web3.to_hex(tx_hash)
        except Exception as e:
            logger.info(" ".join([e.args[0]]))


if __name__ == '__main__':
    """
        转账功能
    """
    # 主网名称 代理
    web3 = init_web3(net_name='eth', proxies=True)

    private_key = '0x7c52ed3f613a501236c04c531d641f49ad393efcf12400f45ec28f180794b736'

    from_address = "0x96bceeF977b08D2895e52D7848aa874Fa9F29450"
    to_address = "0xDB376DF770E58E73dca9d30E8cCbebCB6c60701f"

    # # private_key = os.environ.get('PRIVATE_KEY')
    # 转账token数量
    value = 0.1
    wallet_transaction(from_address=from_address, to_address=to_address, private_key=private_key, value=value)
