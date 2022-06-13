import requests

url = "https://testnets-api.opensea.io/api/v1/events?only_opensea=false&limit=20"

headers = {"Accept": "application/json"}
response = requests.get(url, headers=headers)
print(response.text)

# QUERY PARAMS
# asset_contract_address
# string
# The NFT contract address for the assets for which to show events

# collection_slug
# string
# Limit responses to events from a collection. 
# Case sensitive and must match the collection slug exactly. 
# Will return all assets from all contracts in a collection. 
# For more information on collections, see our collections documentation.

# token_id
# int32
# The token's id to optionally filter by

# account_address
# string
# A user account's wallet address to filter for events on an account

# event_type
# string
# The event type to filter. Can be created for new auctions, successful for sales, cancelled, bid_entered, bid_withdrawn, transfer, or approve

# only_opensea - true
# boolean
# Restrict to events on OpenSea auctions. Can be true or false


# auction_type
# string
# Filter by an auction type. Can be english for English Auctions, dutch for fixed-price and declining-price sell orders (Dutch Auctions), or min-price for CryptoPunks bidding auctions.

# offset
# int32
# Offset for pagination

# limit - 20
# string
# Limit for pagination

# occurred_before
# date-time
# Only show events listed before this timestamp. Seconds since the Unix epoch.

# occurred_after
# date-time
# Only show events listed after this timestamp. Seconds since the Unix epoch.
