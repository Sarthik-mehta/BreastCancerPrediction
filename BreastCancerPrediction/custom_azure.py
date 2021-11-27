from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'breastcancerprediction' # Must be replaced by your <storage_account_name>
    account_key = 'vCE6uis2nMle5HauZxGAMFpLwpSRNSN2xBu/el4jF/0Ab0lNB4ocoEqU2fZHPv7kbJWHuTs5gSfHs1gn+GM0Sg==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'breastcancerprediction' # Must be replaced by your storage_account_name
    account_key = 'vCE6uis2nMle5HauZxGAMFpLwpSRNSN2xBu/el4jF/0Ab0lNB4ocoEqU2fZHPv7kbJWHuTs5gSfHs1gn+GM0Sg==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None