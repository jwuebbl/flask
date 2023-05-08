# Api Key -> RGAPI-a7493dd6-4dc4-4f2e-9f3a-e698ab203b0f

# Get my account information:
curl -X GET https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Wake%20Andd%20Bake?api_key=RGAPI-a7493dd6-4dc4-4f2e-9f3a-e698ab203b0f
# Response:
# {"id":"Tda1K8LPfUA42jDbWNBG2fN0dEkqUkstfF_FK2kKEVMZr9E","accountId":"85iBgaT9HzAuzFcst21lSpxSIS_OnelGpvqsWqH90MR1lA","puuid":"whgFvbbic7paMo1XUFxVOQRW3TXR4yxtIFOGGzULxw2M8Q_jYJDpJInxRKCEqsTclpJ9MHK_fDjn9A","name":"Wake Andd Bake","profileIconId":578,"revisionDate":1682459145000,"summonerLevel":221}

# Gets the last match ID:
curl -X GET "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/whgFvbbic7paMo1XUFxVOQRW3TXR4yxtIFOGGzULxw2M8Q_jYJDpJInxRKCEqsTclpJ9MHK_fDjn9A/ids?start=0&count=1&api_key=RGAPI-a7493dd6-4dc4-4f2e-9f3a-e698ab203b0f" -H "X-Riot-Token: RGAPI-a7493dd6-4dc4-4f2e-9f3a-e698ab203b0f"
# Response: ["NA1_4639488107"]

# curl -X GET "https://americas.api.riotgames.com/lol/match/v5/matches/{matchID}" -H "X-Riot-Token: RGAPI-a7493dd6-4dc4-4f2e-9f3a-e698ab203b0f"
curl -X GET "https://americas.api.riotgames.com/lol/match/v5/matches/NA1_4639488107" -H "X-Riot-Token: RGAPI-a7493dd6-4dc4-4f2e-9f3a-e698ab203b0f"