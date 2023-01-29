from azure.appconfiguration.provider import (
    AzureAppConfigurationProvider,
    SettingSelector
)
import os

connection_string = os.environ.get("AZURE_APPCONFIG_CONNECTION_STRING")

# Connect to Azure App Configuration using a connection string.
config = AzureAppConfigurationProvider.load(
    connection_string=connection_string)

# Find the key "message" and print its value.
print(config["message"])
# Find the key "my_json" and print the value for "key" from the dictionary.
print(config["my_json"]["key"])

# Connect to Azure App Configuration using a connection string and trimmed key prefixes.
trimmed = {"test."}
config = AzureAppConfigurationProvider.load(
    connection_string=connection_string, trimmed_key_prefixes=trimmed)
# From the keys with trimmed prefixes, find a key with "message" and print its value.
print(config["message"])

# Connect to Azure App Configuration using SettingSelector.
selects = {SettingSelector("message*", "\0")}
config = AzureAppConfigurationProvider.load(
    connection_string=connection_string, selects=selects)

# Print True or False to indicate if "message" is found in Azure App Configuration.
print("message found: " + str("message" in config))
print("test.message found: " + str("test.message" in config))