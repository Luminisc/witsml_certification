#******************************************************************************
# Copyright (c) 2011 Pason Systems Corp.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#******************************************************************************

# Server identification
server_name = ''

#
#
# Login Information
#
#

server_URL = ''
server_username = ''
server_password = ''

#format is 'http://USERNAME:PASSWORD@URL:PORTNUMBER'
# example is 'http://admin:adminPass@myProxy.com:80'
server_proxy_URL = ''
#
#
# Server Capabilities
#
#
server_support_truncation = True

#
#
# WITSML Data for Sample Scripts
#
#

# Well 1 - Main well
#    - At least two wellbores
#    - At least one log (log 1) with indexType='date time'
#    - At least one log (log 2) with indexType='measured depth'
server_w1_uid = 'w1'
server_w1_wb1_uid = 'wb1' 

server_w1_wb1_log1_uid = 'ldepth'
server_w1_wb1_log1_mnemonic_1 = 'Depth' 
server_w1_wb1_log1_curves = ['Depth', 'Torque', 'Gas', 'ROP', 'Pump', 'Time'] 
server_w1_wb1_traj1_uid ='traj1Growing'
server_w1_wb1_traj2_uid = 'traj2NonGrowing'

server_w1_wb1_log2_uid = 'ltime'
server_w1_wb1_log2_mnemonic_1 = 'Time' 
server_w1_wb1_log2_curves = ['Depth', 'Torque', 'Gas', 'ROP', 'Pump', 'Time'] 

# Well 2 - Well with growing log
server_w2_uid = 'w2'
server_w2_wb1_uid = 'wb1' 
server_w2_wb1_log1_uid = 'lNonGrowing'
server_w2_wb1_log1_mnemonic_1 = 'lNonIndex'
server_w2_wb1_log1_mnemonic_2 = 'lIndex'

# Well 3 - contains a mudlog (for updating) and a log for truncating with maxdatapoints and maxdatanodes
server_w3_uid = 'w3'
server_w3_wb1_uid = 'wb1'
server_w3_wb1_log1_uid = 'ldepth1'
server_w3_wb1_log2_uid = 'ldepth2'
server_w3_wb1_log3_uid = 'ltime1'
server_w3_wb1_log4_uid = 'ltime2'
server_w3_wb1_mudlog1_uidd = 'mud1'
