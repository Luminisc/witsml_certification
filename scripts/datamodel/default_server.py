#
# SERVER PARAMETERS
#

# Server identification

server_name = 'Generic Server'

# Login Information

server_URL = 'URL'
server_username = 'username'
server_password = 'password'


# Server capabilities

server_supports_numAPI = True
server_supports_numGovt = True

# Data Schema Version to test
server_schema_version = '1.4.1.0'

#If True, outputs response for GetVersion(), GetCap(), and GetFromStore()
#log_responses = True

#
# WITSML DATA
#

# Well 1
server_w1_uid = 'Energistics-well-0001'
server_w1_wb1_uid = 'Energistics-w1-wellbore-0001'
server_w1_wb1_log1_uid = 'Energistics-w1-wb1-log-0001'
server_w1_wb1_log2_uid = 'Energistics-w1-wb1-log-0002'
server_w1_wb1_log1_mnemonic_1 = 'BDEP'
server_w1_wb1_log1_curves = ['BDEP', 'CURVE1', 'CURVE2', 'CURVE3']

server_w1_wb1_traj1_uid = 'Energistics-w1-wb1-trajectory-0001'
server_w1_wb1_traj2_uid = 'Energistics-w1-wb1-trajectory-0002'

# Well 2
server_w2_uid = 'Energistics-well-0002'
server_w2_wb1_uid = 'Energistics-w2-wellbore-0001'
server_w2_wb1_log1_uid = 'Energistics-w2-wb1-log-0001'
server_w2_wb1_log1_mnemonic_1 = 'CURVE1'
server_w2_wb1_log1_index_mnemonic = 'BDEP'

# Well 3
server_w3_uid = 'Energistics-well-0003'
server_w3_wb1_uid = 'Energistics-w3-wellbore-0001'
server_w3_wb1_log1_uid = 'Energistics-w3-wb1-log-0001'
server_w3_wb1_log2_uid = 'Energistics-w3-wb1-log-0002'
server_w3_wb1_log3_uid = 'Energistics-w3-wb1-log-0003'
server_w3_wb1_log4_uid = 'Energistics-w3-wb1-log-0004'
server_w3_wb1_mudlog1_uid = 'Energistics-w3-wb1-mudlog-0001'

