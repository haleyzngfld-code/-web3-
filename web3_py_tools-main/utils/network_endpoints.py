infura_api_key = '84842078b09946638c03157f83405213'

endpoints_net = {
    'eth': 'https://mainnet.infura.io/v3/',
    'linea': 'https://linea-mainnet.infura.io/v3/',
    'arbitrum': 'https://arbitrum-mainnet.infura.io/v3/',
    'avalanche': 'https://avalanche-mainnet.infura.io/v3/',
    'bsc': 'https://bsc-dataseed.binance.org',
    'base': 'https://mainnet.base.org',
    'celo': 'https://celo-mainnet.infura.io/v3/',
    'gnosis': 'https://rpc.gnosischain.com',
    'optimism': 'https://optimism-mainnet.infura.io/v3/',
    'polygon': 'https://polygon-mainnet.infura.io/v3/',
    'zksync': 'https://mainnet.era.zksync.io/v3/',
}

endpoints = {}

for endpoint_net_name, endpoint_net_value in endpoints_net.items():

    if not endpoint_net_value.endswith('/'):
        endpoints[endpoint_net_name] = endpoint_net_value
    else:
        endpoints[endpoint_net_name] = endpoint_net_value + infura_api_key

if __name__ == '__main__':
    print(endpoints)
